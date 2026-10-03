# 🎰 Game Roulette v30

> Uma aplicação web interativa, responsiva e nostálgica projetada para sorteio de plataformas e jogos clássicos através de uma experiência imersiva com animações, efeitos pixelados em tempo real e física suave.

---

## 🎮 Sobre o Projeto

O **Game Roulette** resolve o clássico dilema: *"o que jogar agora?"*. O sistema opera em duas etapas integradas:
1. **Roleta de Plataformas / Consoles**: Escolhe dinamicamente entre dezenas de gerações e sistemas (Nintendo, PlayStation, Xbox, Sega, Atari, PC, etc.).
2. **Roleta de Jogos Dedicada**: Após o sorteio do console, carrega instantaneamente a biblioteca local correspondente e sorteia um jogo daquele acervo, com exibição de capa, ano de lançamento e feedback visual comemorativo.

---

## ✨ Principais Funcionalidades

- **Motor de Renderização em HTML5 Canvas**: Desenho em tempo real das roletas com física angular contínua, desaceleração realista e indicador (*pointer*) interativo com retorno tátil visual.
- **Efeitos Visuais Retrô Procedurais**:
  - Partículas de explosão estilo 8-bit/pixel art geradas diretamente via Canvas sobreposto ao cair no resultado.
  - Badge central comemorativa com tipografia arcade saltando em animação de impacto (*screen pop*).
- **Áudio Sintetizado Nativo**: Efeitos sonoros mecânicos e melodias de vitória usando **Web Audio API** (`OscillatorNode`), sem dependência de arquivos de áudio pesados e com gerenciamento otimizado de memória.
- **Catálogo Offline / Autocontido**: O banco de dados de títulos (`game_data.js`) é carregado localmente, permitindo execução instantânea sem necessidade de servidores ou APIs externas ativas.
- **Interface Responsiva**: Layout modular com suporte a tela cheia, pesquisa instantânea de consoles com debounce e paleta visual futurista dark/cyberpunk.

---

## 🚀 Como Executar

### Opção 1: Diretamente no Navegador (Web)
Basta abrir o arquivo `index.html` em qualquer navegador moderno (Chrome, Firefox, Edge, Safari):
- Dê um duplo clique em `index.html`, ou
- Acesse via GitHub Pages oficial do repositório.

### Opção 2: Executável Desktop
Para Windows, você pode executar diretamente o `Game_Roulette_v30.exe` incluso no repositório.

---

## 🛠️ Tecnologias Utilizadas

- **HTML5** (Semântica estrutural e camadas de Canvas 2D)
- **CSS3 Moderno** (Grid, Flexbox, Glassmorphism, Keyframes e Variáveis CSS)
- **JavaScript Puro (Vanilla JS - ES6+)** (Física da roleta, controle de eventos e manipulação de estado)
- **Web Audio API** (Sintetizador de som procedural)

---

## 📄 Licença

Este projeto é protegido sob os termos de **Licença Proprietária e Direitos Autorais** (*Proprietary License and Copyright Notice*).

```text
Copyright (c) 2026 MigzuLCS. Todos os direitos reservados.
All Rights Reserved.
```

É concedida permissão apenas para uso pessoal, recreativo e visualização através do repositório oficial. É expressamente proibida a cópia não autorizada, redistribuição, exploração comercial ou engenharia reversa sem o consentimento prévio e formal do autor.

Consulte o arquivo [`LICENSE`](./LICENSE) completo para obter todos os detalhes e termos jurídicos.
