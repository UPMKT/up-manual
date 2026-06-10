<!-- generated-by: gsd-doc-writer -->
# Development — UP Manual

## Local setup

Requisitos: Node.js `v22` (ver `.nvmrc`), Python 3 com `pyyaml` instalado.

```bash
git clone <repo-url>
cd up-manual
npm install
```

Para sincronizar o conteúdo gerado (skills e squads) antes de arrancar:

```bash
pip install pyyaml   # apenas na primeira vez
python scripts/sync.py
```

Arrancar o servidor de desenvolvimento com hot reload:

```bash
npm run dev
# Site disponível em http://localhost:4321
```

Não há variáveis de ambiente necessárias para desenvolvimento local — o Astro não precisa de `.env`.

## Build commands

| Comando | Descrição |
|---------|-----------|
| `npm run dev` | Servidor de desenvolvimento com hot reload em `localhost:4321` |
| `npm run build` | Build de produção — gera HTML estático em `dist/` |
| `npm run preview` | Serve o `dist/` localmente para pré-visualizar o build |
| `python scripts/sync.py` | Sincroniza skills (`~/.claude/skills/`) e squads (`~/squads/`) para `src/content/docs/` |

Não existem scripts de lint ou format configurados em `package.json`.

## Adicionar conteúdo

### Nova página manual

Criar um ficheiro `.md` (ou `.mdx` para componentes Starlight) no subdirectório correcto de `src/content/docs/`. O frontmatter `title` e `description` são obrigatórios:

```md
---
title: Título da Página
description: Descrição curta da página.
---

Conteúdo em Markdown.
```

A sidebar `autogenerate` em `astro.config.mjs` apanha automaticamente todos os `.md` do directório, por ordem alfabética. Para páginas com componentes (`CardGrid`, `Card`), usar extensão `.mdx`.

### Actualizar catálogo de skills ou squads

Após adicionar, remover ou editar skills em `~/.claude/skills/` ou squads em `~/squads/`, correr:

```bash
python scripts/sync.py
```

O script lê `~/.claude/skills/*/SKILL.md` e `~/squads/*/squad.yaml` (ou `.json`), classifica cada skill por categoria (via `SKILL_CATEGORIES` em `scripts/sync.py`) e regera as páginas correspondentes em `src/content/docs/skills/` e `src/content/docs/squads/catalog/`.

## Estrutura do sidebar

O sidebar é definido em `astro.config.mjs`. Cada secção usa `autogenerate` (apanha todos os `.md` de um directório) ou items explícitos com `slug`. Para adicionar uma nova secção:

1. Criar o subdirectório em `src/content/docs/`.
2. Adicionar uma entrada ao array `sidebar` em `astro.config.mjs`:

```js
{
  label: 'Nova Secção',
  items: [{ autogenerate: { directory: 'nova-seccao' } }],
},
```

## Personalização de tema

O tema visual é definido em `src/styles/custom.css` usando variáveis CSS do Starlight. Para alterar a paleta de cores, editar as variáveis `:root` e `[data-theme='dark']`:

```css
:root {
  --sl-color-accent: #4f46e5;      /* cor principal (índigo) */
  --sl-color-accent-high: #818cf8; /* destaque claro */
}
```

## Code style

Não existe configuração de ESLint, Prettier ou Biome neste repositório. O TypeScript está configurado em `tsconfig.json` mas só é usado pelo Astro internamente — não há código TypeScript a editar directamente. Para ficheiros Python (`scripts/sync.py`), sem linter configurado.

## Branch conventions

Nenhuma convenção documentada no repositório.

## PR process

Nenhum template de PR em `.github/`. Processo padrão:

- Branch a partir de `main`
- Correr `python scripts/sync.py` e `npm run build` para verificar que o conteúdo compila sem erros
- Abrir PR para `main`
