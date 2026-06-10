---
title: "Skill: upscale-ghl-playwright"
description: Scripts Python com Playwright para automatizar operações do GHL que NÃO estão disponíveis na API V2. Usa sessão persistente para manter login entre ex
---

# Skill: upscale-ghl-playwright

## O que essa skill faz
Scripts Python com Playwright para automatizar operações do GHL que NÃO estão disponíveis na API V2. Usa sessão persistente para manter login entre execuções.

## Quando usar
Apenas quando a operação NÃO puder ser feita via API. Exemplos:
- Criar/editar Knowledge Base
- Configurar Flow Builder (respostas personalizadas do bot)
- Configurar ação transferBot no Conversation AI
- Configurar múltiplos calendários em appointmentBooking
- Executar Bot Trial (verificação visual)

## Scripts Disponíveis

| Script | O que faz | Uso |
|--------|-----------|-----|
| `ghl_lib.py` | Biblioteca compartilhada (login, navegação, screenshots) | Importado pelos outros |
| `ghl_login.py` | Login inicial e salvamento de sessão | `python ghl_login.py <subdominio>` |
| `ghl_attach_transferbot.py` | Configura ação transferBot no bot | `python ghl_attach_transferbot.py <bot_id> <location_id>` |
| `ghl_multi_cal_appointment.py` | Configura múltiplos calendários em appointmentBooking | `python ghl_multi_cal_appointment.py <bot_id> <cal_id1> <cal_id2>` |
| `ghl_bot_trial_runner.py` | Executa 10 cenários do Bot Trial automaticamente | `python ghl_bot_trial_runner.py <location_id> <bot_id>` |

## Sessão Persistente
- Sessão salva em: `~/.claude/scripts/ghl-playwright/session/`
- Login único necessário por subdomínio
- Após login, todos os scripts reutilizam a sessão

## Pré-requisitos
```bash
pip install playwright
playwright install chromium
```

## Fluxo Típico
```bash
# 1. Login inicial (apenas uma vez por cliente)
python ~/.claude/scripts/ghl-playwright/ghl_login.py hub.triadeflow.ai

# 2. Depois, scripts específicos reutilizam a sessão
python ~/.claude/scripts/ghl-playwright/ghl_attach_transferbot.py BOT_ID LOCATION_ID
```

## Gotchas
- GHL usa JS pesado — sempre usar `wait_for_load_state("networkidle")`
- Seletores mudam com updates do GHL — preferir seletores por texto (`get_by_text`) quando possível
- Screenshots em erro são salvas em `~/.claude/scripts/ghl-playwright/screenshots/`
- Nunca rodar headless em produção — GHL detecta e pode bloquear

