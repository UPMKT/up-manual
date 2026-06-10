---
title: Automações — Guia Rápido
description: Como montar e publicar automações no GoHighLevel.
---

## Usar a skill `/upscale-ghl-automacoes`

Esta skill conhece toda a documentação oficial do GHL — gatilhos, actions, condições, templates de jornadas.

### O que ela faz

- Design completo de workflows (lead → agendamento → pós-venda)
- Templates de jornadas prontos (imobiliário, saúde, educação)
- Integração com pagamentos, cursos, Shopify, comunidades
- Escolher o gatilho certo para cada caso
- Montar sequências de SMS/email/WhatsApp

### Limitações da API

Algumas operações só são possíveis via UI — para essas, a skill `/upscale-ghl-playwright` faz automaticamente:

| Operação | API | Playwright |
|----------|-----|-----------|
| Criar workflow | ✓ | ✓ |
| Publicar workflow | ✗ | ✓ |
| Configurar Knowledge Base | ✗ | ✓ |
| Configurar bot mode | ✗ | ✓ |
| Multiple calendários | ✗ | ✓ |
