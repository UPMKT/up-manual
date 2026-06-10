<!-- generated-by: gsd-doc-writer -->
# Architecture — UP Manual

## System overview

UP Manual é um site de documentação estático gerado com Astro Starlight. A entrada de dados vem de duas fontes externas ao repositório — ficheiros `SKILL.md` em `~/.claude/skills/` e ficheiros `squad.yaml` em `~/squads/` — que o script `scripts/sync.py` lê e transforma em páginas Markdown dentro de `src/content/docs/`. O Astro compila esse conteúdo para HTML estático em `dist/`, que é servido via Vercel. Não há base de dados nem runtime no servidor.

## Component diagram

```
Fontes externas               Pipeline de sync              Site gerado
─────────────────             ────────────────              ────────────
~/.claude/skills/             scripts/sync.py               src/content/docs/
  */SKILL.md        ──────►   parse_skill_md()    ──────►     skills/{gsd,upscale,
                              get_category()                   marketing,dev,tools}/
~/squads/                     generate_squads()   ──────►     squads/catalog/
  */squad.yaml     ──────►   generate_skills_index()  ►       skills/index.mdx
  */squad.json                generate_ghl_docs() ──────►     ghl/
                              generate_gsd_docs() ──────►     gsd/
                              generate_reference() ────►      reference/

src/content/docs/             Astro + Starlight              Deploy
─────────────────             ─────────────────              ──────
*.md / *.mdx       ──────►   astro build          ──────►   dist/
astro.config.mjs              docsLoader()                   Vercel (vercel.json)
src/styles/custom.css         docsSchema()
src/content.config.ts
```

## Data flow

1. O developer corre `python scripts/sync.py` a partir da raiz do repositório.
2. O script lê `~/.claude/skills/*/SKILL.md`, extrai frontmatter YAML e corpo Markdown, determina a categoria (via `get_category()` e o dicionário `SKILL_CATEGORIES`), e escreve `src/content/docs/skills/{categoria}/{skill-name}.md`.
3. Para squads, lê `~/squads/*/squad.yaml` (ou `.json`), extrai nome, descrição e lista de agentes, e escreve `src/content/docs/squads/catalog/{squad-name}.md`.
4. O script gera ainda páginas estáticas para as secções GHL, GSD e referências directamente a partir de conteúdo hardcoded em Python.
5. Após o sync, `npm run build` invoca `astro build`: o `docsLoader()` lê todos os ficheiros em `src/content/docs/`, o `docsSchema()` valida o frontmatter, e o Starlight gera HTML com sidebar automática.
6. O output em `dist/` é publicado na Vercel via deploy normal (`buildCommand: npm run build`, `outputDirectory: dist`).

## Key abstractions

| Abstracção | Ficheiro | Descrição |
|-----------|---------|-----------|
| `generate_skills()` | `scripts/sync.py:167` | Itera `~/.claude/skills/`, classifica e escreve páginas de skills |
| `get_category()` | `scripts/sync.py:107` | Mapeia nome de skill para categoria (gsd/upscale/marketing/dev/tools) |
| `parse_skill_md()` | `scripts/sync.py:118` | Extrai frontmatter YAML e título/descrição de um `SKILL.md` |
| `generate_squads()` | `scripts/sync.py:243` | Lê `squad.yaml`/`squad.json` e gera páginas de squads |
| `safe_yaml_str()` | `scripts/sync.py:155` | Sanitiza strings para uso seguro em frontmatter YAML |
| Colecção `docs` | `src/content.config.ts` | Define a colecção Astro com `docsLoader` + `docsSchema` do Starlight |
| Sidebar config | `astro.config.mjs:11` | Combina items explícitos com `autogenerate` por directório |
| Custom theme | `src/styles/custom.css` | Sobrepõe variáveis CSS do Starlight (paleta índigo UP) |

## Directory structure rationale

```
up-manual/
├── astro.config.mjs          # Configuração Astro + Starlight (sidebar, tema, metadados)
├── src/
│   ├── content.config.ts     # Regista a colecção "docs" com loader/schema do Starlight
│   ├── content/
│   │   └── docs/             # Todo o conteúdo do site — cada subdirectório é uma secção
│   │       ├── ghl/          # Páginas GHL & Upscale (geradas pelo sync.py)
│   │       ├── gsd/          # Páginas GSD metodologia (geradas pelo sync.py)
│   │       ├── guides/       # Guias manuais (conteúdo editado à mão)
│   │       ├── reference/    # Stack técnica e referências (gerada pelo sync.py)
│   │       ├── skills/       # Skills por categoria (geradas pelo sync.py a partir de ~/.claude/skills/)
│   │       │   ├── dev/
│   │       │   ├── gsd/
│   │       │   ├── marketing/
│   │       │   ├── tools/
│   │       │   └── upscale/
│   │       └── squads/       # Squads Opensquad (gerados pelo sync.py a partir de ~/squads/)
│   │           └── catalog/
│   └── styles/
│       └── custom.css        # Variáveis CSS — paleta de cores da UP (índigo)
├── scripts/
│   └── sync.py               # Gerador de conteúdo — lê sources externas e escreve Markdown
├── docs/                     # Documentação do próprio projecto (ARCHITECTURE.md, etc.)
├── public/                   # Assets estáticos servidos directamente
├── dist/                     # Output do build (gitignored, publicado na Vercel)
├── vercel.json               # Configuração de deploy Vercel
└── package.json              # Dependências: astro, @astrojs/starlight, sharp
```

A separação entre `src/content/docs/` (conteúdo gerado/editado) e `scripts/` (gerador) é deliberada: permite correr o sync de forma independente do build, e permite editar páginas manualmente sem quebrar o pipeline automatizado. As secções `ghl/`, `gsd/` e `reference/` são geradas mas podem ser sobrepostas com edições manuais porque o sync não apaga ficheiros existentes — apenas sobrescreve os que correspondem a fontes encontradas.
