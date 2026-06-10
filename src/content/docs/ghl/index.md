---
title: GHL & Upscale
description: Ecossistema GoHighLevel da UP Marketing — automações, bots, CRM e gestão de leads.
---

## Skills disponíveis

| Skill | Quando usar |
|-------|------------|
| `/upscale-ghl-automacoes` | Design de workflows, jornadas de lead, templates |
| `/upscale-bot-builder` | Criar/configurar bot Conversation AI |
| `/upscale-ghl-gatilhos` | Referência de triggers e actions |
| `/upscale-ghl-playwright` | Operações UI que a API não cobre |

## Fluxo entre agentes

```
Lead/Captação → /upscale-ghl-automacoes → (se bot) /upscale-bot-builder
Bot a configurar → /upscale-bot-builder → (se UI) /upscale-ghl-playwright
Dúvida trigger/action → /upscale-ghl-gatilhos
Workflow completo → /upscale-ghl-automacoes orquestra os outros
```

## Regras críticas

- **NUNCA enviar WhatsApp directo** — sempre SMS via GHL (`type: 'SMS'`)
- **Conversation AI (bot config, KB, mode)** = UI-only, sem API
- **Publicar workflows** = UI-only
- **401 num token** → expirado → pedir novo token imediatamente
