<!-- generated-by: gsd-doc-writer -->
# Getting Started — UP Manual

## Prerequisites

Antes de começar, assegura que tens as seguintes ferramentas instaladas:

| Ferramenta | Versão mínima | Para quê |
|------------|---------------|----------|
| `Node.js` | >= 22 | Compilar e servir o site Astro |
| `npm` | >= 10 | Gerir dependências |
| `Python 3` | >= 3.8 | Executar `scripts/sync.py` para actualizar conteúdo |
| `PyYAML` | qualquer | Parser YAML usado pelo script de sync |

Instalar PyYAML se ainda não estiver disponível:

```bash
pip install pyyaml
```

## Installation steps

1. Clonar o repositório:

```bash
git clone https://github.com/UPMKT/up-manual
cd up-manual
```

2. Instalar dependências Node:

```bash
npm install
```

## First run

Iniciar o servidor de desenvolvimento:

```bash
npm run dev
```

O site estará disponível em `http://localhost:4321`.

## Common setup issues

**Erro `Cannot find module` ou falha no `astro dev`**
Confirma que estás a usar Node.js 22+:
```bash
node -v   # deve retornar v22.x.x
```
Se a versão for inferior, actualiza o Node.js (recomendado via `nvm use 22`).

**`sync.py` falha com `ModuleNotFoundError: No module named 'yaml'`**
PyYAML não está instalado no ambiente Python activo:
```bash
pip install pyyaml
```
Se usares `python3` explicitamente, garante que o pip correcto é invocado:
```bash
python3 -m pip install pyyaml
```

**Conteúdo do site desactualizado após editar skills ou squads**
O repositório não contém as fontes directamente. É preciso correr o script de sync:
```bash
python3 scripts/sync.py
```
O script lê `~/.claude/skills/` e `~/squads/` e regenera os ficheiros em `src/content/docs/`. Depois, faz `git push` para disparar o deploy automático na Vercel.

**Porta 4321 já em uso**
Astro escolhe a próxima porta disponível automaticamente, ou podes especificar:
```bash
npm run dev -- --port 4322
```

## Next steps

- **ARCHITECTURE.md** — Estrutura do projecto, pipeline de sync e organização de conteúdo.
- **CONFIGURATION.md** — Ficheiros de configuração do Astro, Vercel e estilos de marca.
