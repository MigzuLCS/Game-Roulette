# 🎮 Game Roulette — Consoles & Jogos

Sorteador interativo de consoles e jogos retrô clássicos com roleta dupla, física mecânica de rotação suave, efeitos de rascunho (*line-boil*), filtro pixelizado e catálogo local com 39 consoles e centenas de jogos.

---

## 🚀 Como Hospedar no GitHub Pages

Este repositório já está 100% configurado para funcionar diretamente no **GitHub Pages**:

1. Crie um novo repositório no seu GitHub (exemplo: `game-roulette`).
2. Faça o upload ou envie os arquivos deste projeto via Git:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Game Roulette v30"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   git push -u origin main
   ```
3. No seu repositório no GitHub, clique na aba **Settings** (Configurações).
4. No menu lateral esquerdo, clique em **Pages**.
5. Na seção **Build and deployment** > **Branch**:
   - Selecione a branch `main` (ou `master`).
   - Mantenha a pasta `/ (root)`.
   - Clique em **Save**.
6. Em cerca de 1 minuto, o link do seu site estará disponível no topo da página:
   `https://SEU_USUARIO.github.io/SEU_REPOSITORIO/`

---

## 🕹️ Execução Local

Você também pode utilizar o aplicativo offline no seu computador sem precisar de internet ou servidor:

- **Opção 1 (Navegador):** Dê um duplo clique no arquivo `index.html`.
- **Opção 2 (Executável Windows):** Dê um duplo clique em `Game_Roulette_v30.exe` para abrir a roleta em janela dedicada.

---

## ✨ Recursos

- **Roleta Dupla Sincronizada:** Sorteia primeiro o console e carrega imediatamente o catálogo de jogos correspondente para o segundo sorteio.
- **Seleção Personalizada de Consoles:** Caixas de seleção individuais para escolher exatamente quais plataformas participam da roleta, com persistência automática no cache do navegador (`localStorage`).
- **Alta Performance:** Sistema de *Sprite Caching* que mantém 60–144 FPS contínuos mesmo em roletas com mais de 100 jogos.
- **Física Mecânica Calibrada:** Desaceleração suave e orgânica com suspense no último segundo.
- **Filtro Pixelizado & Efeito Orgânico Wobble:** Alternáveis em tempo real por botões dedicados com ícones vetoriais em SVG.
- **100% Offline-First:** Toda a base de dados reside localmente em `game_data.js` via API IGDB.
