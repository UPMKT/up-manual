<!-- generated-by: gsd-doc-writer -->
# Configuration

UP Manual é um site estático — não usa variáveis de ambiente. Toda a configuração está nos ficheiros abaixo.

## Ficheiros de configuração

| Ficheiro | Propósito |
|----------|-----------|
| `astro.config.mjs` | Configuração principal do Astro + Starlight (título, sidebar, CSS) |
| `vercel.json` | Configuração de deploy na Vercel |
| `tsconfig.json` | Configuração TypeScript (estende `astro/tsconfigs/strict`) |
| `src/styles/custom.css` | Variáveis de cor e estilos de marca |
| `scripts/sync.py` | Script de sincronização de conteúdo (sem configuração necessária) |

## Environment variables

Não existem variáveis de ambiente. O projecto é totalmente estático — sem base de dados, sem API keys, sem runtime config.

## astro.config.mjs

Configuração principal da Starlight. Os campos relevantes a editar:

```js
starlight({
  title: 'UP Manual',                         // título no header do site
  description: '...',                          // meta description
  customCss: ['./src/styles/custom.css'],      // CSS de marca
  sidebar: [ /* grupos de navegação */ ],
})
```

### Estrutura da sidebar

A sidebar é declarada como array de grupos. Cada grupo tem um `label` e `items`. Os items podem ser:

- **Slug fixo:** `{ label: 'Nome', slug: 'caminho/pagina' }`
- **Auto-gerado:** `{ autogenerate: { directory: 'nome-dir' } }` — inclui automaticamente todos os ficheiros `.md`/`.mdx` dentro de `src/content/docs/{nome-dir}/`

Grupos actuais:

| Label | Tipo | Diretório / Slug |
|-------|------|-----------------|
| Início | slug fixo | `home` |
| Skills — Catálogo Completo | slug fixo | `skills/catalog` |
| Skills — GSD Metodologia | autogenerate | `skills/gsd` |
| Skills — Upscale & GHL | autogenerate | `skills/upscale` |
| Skills — Marketing & Conteúdo | autogenerate | `skills/marketing` |
| Skills — Desenvolvimento | autogenerate | `skills/dev` |
| Skills — Ferramentas | autogenerate | `skills/tools` |
| Squads — Todos os Squads | slug fixo | `squads/overview` |
| Squads — Catálogo | autogenerate | `squads/catalog` |
| GHL & Upscale | autogenerate | `ghl` |
| GSD Metodologia | autogenerate | `gsd` |
| Referências | autogenerate | `reference` |

Para adicionar uma nova secção à sidebar, acrescentar um bloco ao array `sidebar` em `astro.config.mjs` e criar os ficheiros correspondentes em `src/content/docs/`.

## vercel.json

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "installCommand": "npm install",
  "framework": "astro"
}
```

Estes valores são suficientes para deploy automático na Vercel. Nenhum ajuste manual é necessário.

## src/styles/custom.css

Define as cores de marca sobre as variáveis CSS da Starlight.

### Modo claro

| Variável | Valor | Uso |
|----------|-------|-----|
| `--sl-color-accent-low` | `#1a1a3e` | fundo de badges/hover subtil |
| `--sl-color-accent` | `#4f46e5` | cor de destaque principal (indigo) |
| `--sl-color-accent-high` | `#818cf8` | texto sobre fundo escuro |
| `--sl-color-white` | `#ffffff` | branco base |
| `--sl-color-gray-1` | `#f1f5f9` | cinzento muito claro |
| `--sl-color-gray-2` | `#e2e8f0` | cinzento claro |
| `--sl-color-gray-6` | `#1e293b` | cinzento escuro |
| `--sl-color-black` | `#0f172a` | preto base (fundo dark) |

### Modo escuro (`[data-theme='dark']`)

| Variável | Valor |
|----------|-------|
| `--sl-color-accent-low` | `#312e81` |
| `--sl-color-accent` | `#6366f1` |
| `--sl-color-accent-high` | `#a5b4fc` |

Para alterar a cor de destaque, substituir os valores de `--sl-color-accent` em ambos os blocos (`:root` e `[data-theme='dark']`).

## tsconfig.json

Estende `astro/tsconfigs/strict` sem alterações. Inclui todos os ficheiros do projecto, excluindo `dist/`.

Não requer modificação em circunstâncias normais.

## scripts/sync.py

Script Python que gera as páginas do site a partir das fontes locais. Não tem ficheiro de configuração — os caminhos são hardcoded:

| Variável | Caminho |
|----------|---------|
| `SKILLS_DIR` | `~/.claude/skills/` |
| `SQUADS_DIR` | `~/squads/` |
| `DOCS_DIR` | `src/content/docs/` (relativo ao script) |

### Dependências

Requer PyYAML. Instalar com:

```bash
pip install pyyaml
```

### Categorias de skills

O mapeamento `skill_name → categoria` é definido no dict `SKILL_CATEGORIES` dentro do script. Prefixos `gsd-` e `upscale-` têm prioridade automática. Para adicionar uma nova skill a uma categoria, acrescentar uma entrada ao dict.

### Execução

```bash
python scripts/sync.py
```

O script não aceita argumentos. Regenera todo o conteúdo em `src/content/docs/` (skills, squads, GHL, GSD, referências, home).
