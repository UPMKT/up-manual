<!-- generated-by: gsd-doc-writer -->
# UP Manual

Base de conhecimento operacional da UP Marketing & Comunicação — 134+ skills do Claude Code, 21 squads Opensquad, guias GHL/Upscale e metodologia GSD. Site estático gerado com Astro Starlight e publicado automaticamente no Vercel.

## Instalação

```bash
git clone https://github.com/UPMKT/up-manual
cd up-manual
npm install
```

## Quick Start

1. Gerar o conteúdo a partir das skills e squads locais:

```bash
python3 scripts/sync.py
```

2. Iniciar o servidor de desenvolvimento:

```bash
npm run dev
```

O site fica disponível em `http://localhost:4321`.

## Comandos

| Comando | Descrição |
|---------|-----------|
| `npm run dev` | Servidor local com hot-reload |
| `npm run build` | Build estático para `dist/` |
| `npm run preview` | Pré-visualizar o build local |
| `python3 scripts/sync.py` | Regenerar todo o conteúdo (skills, squads, GHL, GSD) |

## Estrutura de Conteúdo

O conteúdo em `src/content/docs/` é gerido pelo `scripts/sync.py` — não editar manualmente os ficheiros gerados.

```
src/content/docs/
├── skills/          # 134+ skills por categoria (gsd, upscale, marketing, dev, tools)
├── squads/          # 21 squads Opensquad
├── ghl/             # Guias GoHighLevel & Upscale
├── gsd/             # Documentação da metodologia GSD
└── reference/       # Referências técnicas
```

## Deploy

O deploy é feito automaticamente no Vercel a cada push para o repositório. A configuração está em `vercel.json` — build command `npm run build`, output directory `dist`.

## Licença

Uso interno — UP Marketing & Comunicação.
