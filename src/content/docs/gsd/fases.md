---
title: Fases e Planos
description: Como usar as skills de planeamento e execução de fases GSD.
---

## /gsd-plan-phase

Cria um `PLAN.md` detalhado para uma fase com:
- Análise de requisitos
- Breakdown de tarefas com dependências
- Estratégia de verificação
- Threat model (para fases de segurança)

## /gsd-execute-phase

Executa o PLAN.md com:
- Wave-based parallelization (tarefas independentes em paralelo)
- Commits atómicos por tarefa
- Checkpoint protocol em caso de desvio
- State management entre tasks

## /gsd-verify-work

Verifica se a fase atingiu o objectivo:
- Análise goal-backward (não só "tasks completed")
- Testa flows de utilizador
- Cria VERIFICATION.md

## Comandos de gestão

| Skill | Uso |
|-------|-----|
| `/gsd-progress` | Estado actual do projecto |
| `/gsd-health` | Saúde geral do projecto |
| `/gsd-stats` | Métricas e estatísticas |
| `/gsd-update` | Actualizar estado de tarefas |
| `/gsd-inbox` | Processar backlog de ideias |
| `/gsd-capture` | Capturar ideia/bug rapidamente |
