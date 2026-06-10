<!-- generated-by: gsd-doc-writer -->
# Testing — UP Manual

## Overview

UP Manual não tem suite de testes automatizados (sem Jest, Vitest nem framework equivalente). A validação é feita através do próprio processo de build do Astro, que detecta erros de conteúdo em tempo de compilação, e por revisão manual via `npm run preview`.

## Build-time validation

O comando `npm run build` é a principal ferramenta de verificação. O Astro executa as seguintes validações automaticamente:

- **Frontmatter schema** — Todos os ficheiros `.md` em `src/content/docs/` são validados contra o schema definido em `src/content.config.ts`. Campos obrigatórios em falta (`title`, `description`) causam falha imediata do build.
- **Slug conflicts** — Slugs duplicados na sidebar de `astro.config.mjs` são detectados e reportados.
- **`autogenerate` em directório vazio** — Se um grupo `autogenerate` apontar para um directório sem ficheiros `.md`, o Astro pode gerar erro ou sidebar vazia.

```bash
npm run build
```

Build bem-sucedido produz output em `dist/` sem erros no terminal. Qualquer erro de frontmatter ou configuração interrompe o build com mensagem detalhada.

## Verificação manual após sync

Após correr `python3 scripts/sync.py`, executar este checklist antes de fazer commit:

1. **Build sem erros**
   ```bash
   npm run build
   ```
   Confirmar que termina sem erros. Erros de frontmatter mostram o ficheiro e linha exacta.

2. **Preview local**
   ```bash
   npm run preview
   ```
   Abre o site em `http://localhost:4321` (porta por defeito). Verificar:
   - Sidebar renderiza todos os grupos esperados
   - Páginas geradas pelo `sync.py` abrem sem erro 404
   - Search index está disponível (caixa de pesquisa funcional)

3. **Sidebar items** — Confirmar que os grupos com `autogenerate` (ex: `skills/gsd`, `skills/upscale`, `squads/catalog`) têm entradas. Um grupo vazio indica que o directório correspondente em `src/content/docs/` está vazio ou não foi gerado.

4. **Search index** — O Starlight gera o índice de pesquisa no build. Verificar no preview que a pesquisa retorna resultados para termos esperados (ex: "bot builder", "workflow").

## O que causa falha de build

| Problema | Causa | Solução |
|----------|-------|---------|
| `Missing required field "title"` | Ficheiro `.md` gerado sem frontmatter `title` | Verificar templates em `sync.py` |
| `Missing required field "description"` | Frontmatter sem campo `description` | Adicionar `description` ao template do `sync.py` |
| `Duplicate slug` | Dois ficheiros com o mesmo slug na sidebar | Renomear ficheiro ou ajustar slug em `astro.config.mjs` |
| `autogenerate` sem conteúdo | Directório alvo está vazio | Garantir que `sync.py` gerou ficheiros antes do build |
| YAML frontmatter inválido | Caracteres especiais sem aspas no `title` ou `description` | Colocar o valor entre aspas duplas no frontmatter |

## Fluxo de trabalho recomendado

```bash
# 1. Sincronizar conteúdo das sources externas
python3 scripts/sync.py

# 2. Validar build
npm run build

# 3. Confirmar visualmente
npm run preview

# 4. Commit se tudo OK
git add src/content/docs/
git commit -m "docs: sync conteúdo via sync.py"
```

## Sem CI configurado

Não existe workflow de CI que corra `npm run build` automaticamente em pull requests. A validação é inteiramente manual e responsabilidade do operador antes de cada deploy.
