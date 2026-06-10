<!-- generated-by: gsd-doc-writer -->
# DEPLOYMENT.md — UP Manual

## Deployment Targets

O UP Manual é um site estático Astro/Starlight, deployado exclusivamente na Vercel via integração GitHub.

| Plataforma | Config | Trigger |
|-----------|--------|---------|
| Vercel | `vercel.json` | Push para `main` |

`vercel.json`:
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "installCommand": "npm install",
  "framework": "astro"
}
```

Repositório: `https://github.com/UPMKT/up-manual`  
<!-- VERIFY: Team name no Vercel: "UP Marketing e Comunicacao's projects" -->

## Build Pipeline

Não existe workflow CI/CD configurado no repositório (sem `.github/workflows/`). O pipeline é inteiramente gerido pela Vercel.

**Sequência automática após `git push main`:**

1. Vercel webhook detecta o push
2. `npm install` — instala dependências (`@astrojs/starlight`, `astro`, `sharp`)
3. `npm run build` → `astro build` — compila o site para `dist/`
4. `dist/` é deployado como site estático

Não há variáveis de ambiente necessárias — o site é completamente estático.

## Content Update Cycle

Para actualizar o conteúdo das skills e squads (o caso de uso mais comum):

```bash
# 1. Sincronizar conteúdo das sources locais para src/content/docs/
python3 scripts/sync.py

# 2. Stagiar e commitar
git add -A
git commit -m "sync: actualizar skills e squads"

# 3. Push → Vercel faz deploy automaticamente
git push
```

O `scripts/sync.py` lê de:
- `~/.claude/skills/*/SKILL.md` — todas as skills do Claude Code
- `~/squads/*/squad.yaml` (ou `squad.json`) — squads do Opensquad

E escreve em `src/content/docs/` nas pastas `skills/`, `squads/`, `ghl/`, `gsd/`, `reference/`.

## Environment Setup

Nenhuma variável de ambiente é necessária. O projecto é totalmente estático — sem backend, sem autenticação, sem secrets.

Pré-requisitos locais para o ciclo de actualização de conteúdo:
- Node.js (ver `docs/GETTING-STARTED.md` para versão)
- Python 3 com PyYAML (`pip install pyyaml`)
- Vercel CLI (opcional, só para deploy manual): `npm install -g vercel`

## Manual Deploy

Para fazer deploy manualmente sem `git push`:

```bash
# Requer autenticação Vercel CLI prévia
npx vercel --prod
```

<!-- VERIFY: URL do projecto no dashboard Vercel para UP Manual -->

## Rollback Procedure

Como não há pipeline CI/CD personalizado, o rollback é feito pelo dashboard da Vercel:

1. Abrir o dashboard do projecto no Vercel
2. Ir a **Deployments**
3. Localizar o deployment anterior estável
4. Clicar em **...** → **Promote to Production**

Alternativamente, reverter o commit no Git e fazer push:

```bash
git revert HEAD
git push
```

## Domain Configuration

<!-- VERIFY: Domínio personalizado configurado no dashboard Vercel para este projecto -->

O domínio é configurado em **Vercel → Project Settings → Domains**. Enquanto não configurado, o site está acessível pelo URL auto-gerado pela Vercel (`up-manual-*.vercel.app`).

## Monitoring

Não há monitorização de erros configurada no repositório (sem Sentry, Datadog ou OpenTelemetry detectados em `package.json`).

<!-- VERIFY: Se existe alerta de build failure configurado no Vercel (email/Slack) -->

O Vercel fornece logs de build e analytics básicos nativamente no dashboard do projecto.
