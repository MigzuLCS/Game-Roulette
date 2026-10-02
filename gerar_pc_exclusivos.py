import json, re, datetime
from pathlib import Path
import requests
BASE=Path(__file__).resolve().parent
try:
 from config import CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN
except Exception:
 raise SystemExit("Crie config.py a partir de config.example.py e preencha CLIENT_ID e CLIENT_SECRET.")
TOKEN_URL="https://id.twitch.tv/oauth2/token"
API="https://api.igdb.com/v4/games"
RELEASE_API="https://api.igdb.com/v4/release_dates"
def get_token():
 if ACCESS_TOKEN.strip(): return ACCESS_TOKEN.strip()
 r=requests.post(TOKEN_URL,params={"client_id":CLIENT_ID,"client_secret":CLIENT_SECRET,"grant_type":"client_credentials"},timeout=30); r.raise_for_status(); return r.json()["access_token"]
def score(g):
 rc=float(g.get("rating_count") or 0); arc=float(g.get("aggregated_rating_count") or 0); follows=float(g.get("follows") or 0); hypes=float(g.get("hypes") or 0); rating=float(g.get("rating") or 0); agg=float(g.get("aggregated_rating") or 0)
 return (rc**0.65)*0.42+(arc**0.55)*0.12+(follows**0.55)*0.20+(hypes**0.55)*0.06+rating*0.10+agg*0.10
def main():
 token=get_token(); headers={"Client-ID":CLIENT_ID,"Authorization":f"Bearer {token}","Accept":"application/json"}
 # A consulta inicial usa Windows (ID 6) sem exigir exclusividade atual.
 # Depois usamos as datas de lançamento para descobrir se o PRIMEIRO lançamento
 # foi somente no Windows. Assim ports posteriores para consoles continuam válidos.
 fields=("id,name,slug,first_release_date,cover.image_id,rating,rating_count,"
         "aggregated_rating,aggregated_rating_count,follows,hypes,platforms,"
         "release_dates.date,release_dates.platform,version_parent")
 queries=[
   f"fields {fields}; where category = 0 & platforms = 6; sort rating_count desc; limit 500;",
   f"fields {fields}; where platforms = 6; sort rating_count desc; limit 500;",
   f"fields {fields}; where category = 0 & release_dates.platform = 6; sort rating_count desc; limit 500;",
   f"fields {fields}; where release_dates.platform = 6; sort rating_count desc; limit 500;",
 ]
 raw=[]; used_query=None
 print("Buscando candidatos que tiveram lançamento no Windows na IGDB...")
 for qi,qbase in enumerate(queries):
  raw=[]
  for offset in range(0, 10000, 500):
   q=qbase+f" offset {offset};"
   r=requests.post(API,headers=headers,data=q,timeout=60)
   if r.status_code==401: raise SystemExit("401: Client ID/token inválido. Confira config.py.")
   r.raise_for_status(); batch=r.json()
   if not batch: break
   raw.extend(batch)
   if len(batch)<500: break
  if raw:
   used_query=qi+1
   break
 print(f"Candidatos encontrados: {len(raw)} (consulta {used_query or 'nenhuma'})")
 if not raw:
  print("A IGDB não retornou candidatos de Windows. O gerador não altera os catálogos existentes.")
  games=[]
 else:
  print("Verificando em qual plataforma cada jogo foi lançado originalmente...")
  games=[]; seen=set()
  for idx,g in enumerate(raw,1):
   gid=g.get("id")
   if not gid or gid in seen: continue
   if g.get("version_parent") is not None: continue
   releases=g.get("release_dates") or []
   pairs=[]
   for rd in releases:
    if not isinstance(rd,dict): continue
    d=rd.get("date"); plat=rd.get("platform")
    if isinstance(plat,dict): plat=plat.get("id")
    if d is not None and plat is not None: pairs.append((d,plat))
   if not pairs:
    continue
   earliest=min(d for d,_ in pairs)
   first_platforms={plat for d,plat in pairs if d==earliest}
   # Entra se o primeiro lançamento conhecido foi Windows e nenhuma outra
   # plataforma recebeu o jogo na mesma data. Ports posteriores não importam.
   if 6 not in first_platforms: continue
   if any(plat != 6 for plat in first_platforms): continue
   seen.add(gid)
   ts=g.get("first_release_date") or earliest
   year=datetime.datetime.fromtimestamp(ts,datetime.timezone.utc).year if ts else None
   cover=""
   cv=g.get("cover")
   if isinstance(cv,dict) and cv.get("image_id"):
    cover=f"https://images.igdb.com/igdb/image/upload/t_cover_big/{cv['image_id']}.jpg"
   games.append({"id":gid,"name":g.get("name",""),"year":year,"cover":cover,"slug":g.get("slug",''),"_score":score(g)})
  print(f"Verificados {len(raw)} candidatos — exclusivos originalmente de PC: {len(games)}")
  games.sort(key=lambda x:x["_score"],reverse=True)
  games=games[:500]
  for g in games: g.pop("_score",None)
 (BASE/"pc.json").write_text(json.dumps(games,ensure_ascii=False,indent=2),encoding="utf-8")
 gd=BASE/"game_data.js"; txt=gd.read_text(encoding="utf-8"); m=re.search(r'window\.GAME_DATA\s*=\s*(.*);\s*$',txt,re.S)
 if not m: raise SystemExit("game_data.js inválido.")
 data=json.loads(m.group(1)); data["PC"]=games; gd.write_text("window.GAME_DATA = "+json.dumps(data,ensure_ascii=False,separators=(",",":"))+";\n",encoding="utf-8")
 print(f"PC: {len(games)} jogos que FORAM LANÇADOS ORIGINALMENTE COMO EXCLUSIVOS DE PC encontrados.")
 print("Ports posteriores para consoles NÃO eliminam o jogo da lista.")
 print("Atualizado: game_data.js e pc.json")

if __name__=="__main__": main()
