---
title: GSD — Git. Ship. Done.
description: Metodologia de desenvolvimento GSD — da ideia ao deploy com agentes e planos estruturados.
---

## O que é o GSD

GSD (Git. Ship. Done.) é a metodologia de desenvolvimento usada na UP. Estrutura o trabalho em fases, planos e execução assistida por agentes.

## Ciclo de vida de um projecto

```
/gsd-new-project → Roadmap + fases
/gsd-plan-phase  → PLAN.md para cada fase
/gsd-execute-phase → Execução com commits atómicos
/gsd-verify-work → Verificação do que foi feito
/gsd-ship        → Deploy final
```

## Skills GSD principais

| Skill | Função |
|-------|--------|
| `/gsd-new-project` | Criar roadmap completo de projecto |
| `/gsd-new-milestone` | Adicionar milestone a projecto existente |
| `/gsd-plan-phase` | Planejar fase com PLAN.md detalhado |
| `/gsd-execute-phase` | Executar plano com agentes paralelos |
| `/gsd-verify-work` | Verificar resultado da fase |
| `/gsd-debug` | Debug científico com checkpoints |
| `/gsd-review` | Code review estruturado |
| `/gsd-ship` | Deploy e entrega |
| `/gsd-pause-work` | Pausa com handoff de contexto |
| `/gsd-resume-work` | Retomar trabalho com contexto restaurado |

## Estrutura de ficheiros GSD

```
.planning/
├── ROADMAP.md          # Visão geral e fases
├── phases/
│   └── 01-nome-fase/
│       ├── PLAN.md     # Plano detalhado
│       └── VERIFY.md   # Resultado verificado
```
