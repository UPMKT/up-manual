---
title: "upscale-ghl-automacoes"
description: "---"
---

---
name: upscale-ghl-automacoes
description: Skill mestre de automações GHL Upscale. Didáctica para iniciantes e completa para avançados. Explica o conceito de automação (trigger→condition→action), cobre 94+ gatilhos e 107+ ações, inclui 21 templates prontos por vertical (estética, imobiliário, consultoria, ecommerce), erros comuns e como evitá-los, checklist antes de publicar, vocabulário explicado. Integra com Conversation AI (upscale-bot-builder) e UI automation (upscale-ghl-playwright). Acionar quando: alguém quer montar automação no GHL pela primeira ou centésima vez, escolher gatilho certo, adaptar template a cliente, debugar workflow com problema, integrar bot+workflow, automatizar jornada lead→agendamento→follow-up→pós-venda.
---

# upscale-ghl-automacoes

Skill de automações GHL Upscale — **para quem nunca fez automação e para quem já fez centenas**.

---

## Por onde começar?

**Nunca fiz automação no GHL:**
→ Leia primeiro `guia-iniciante.md` — explica o conceito completo em linguagem simples

**Já sei o básico, quero montar um workflow:**
→ Vá directo a `templates.md` — 21 workflows prontos por vertical, adapte ao cliente

**Sei o que quero fazer, preciso do trigger/action certo:**
→ `gatilhos-completo.md` (94+ gatilhos) ou `acoes-completo.md` (107+ ações)

**Algo não está a funcionar:**
→ `erros-comuns.md` — os 8 erros mais frequentes com solução directa

**Pronto para publicar:**
→ `checklist.md` — 15 pontos antes de activar em produção

---

## Mapa de ficheiros

| Ficheiro | Para quem | Conteúdo |
|----------|-----------|----------|
| `guia-iniciante.md` | Iniciantes | Conceito de automação, vocabulário, primeiros passos, exemplos reais |
| `templates.md` | Todos | 21 workflows prontos (estética, imob, consultoria, ecommerce, bot) |
| `gatilhos-completo.md` | Intermédio/Avançado | 94+ gatilhos — nome, quando usar, campos, gotchas |
| `acoes-completo.md` | Intermédio/Avançado | 107+ ações — payload JSON, variáveis, notas |
| `erros-comuns.md` | Todos | 8 erros frequentes + solução |
| `checklist.md` | Todos | 15 pontos antes de publicar |
| `integracao-bot.md` | Avançado | Padrões workflow ↔ Conversation AI |
| `oficial-ghl.md` | Avançado | Features avançadas da doc oficial (Scheduler, Custom Code, Arrays, Company workflows) |

---

## Skills irmãs (chamar quando necessário)

| Skill | Quando |
|-------|--------|
| `/upscale-bot-builder` | Criar ou configurar bot Conversation AI |
| `/upscale-ghl-gatilhos` | Referência rápida de trigger ou action |
| `/upscale-ghl-playwright` | Operações UI: KB, Flow Builder, transferBot |

---

---

## Como este agente ajuda a equipa (modo cooperativo)

Este agente é um **especialista paciente**. A equipa não precisa saber de automações — basta descrever o que quer que aconteça no negócio. O agente traduz isso em workflow.

### Quando alguém pede ajuda para criar uma automação

**Passo 1 — Entender o objectivo em linguagem simples**

Perguntar (máximo 3 perguntas, uma de cada vez):
1. "Quando deve disparar a automação? O que acontece no negócio nesse momento?"
2. "O que deve acontecer a seguir? (mensagem, notificação, mover pipeline, criar tarefa...)"
3. "Há alguma condição? (ex: só se não respondeu, só em horário comercial, só para leads de X origem)"

Não usar jargão técnico nas perguntas. Se a pessoa disser "quero avisar a equipa quando um lead marca consulta", o agente percebe que isso é `Trigger: Appointment Created → Action: Send Internal Notification`.

**Passo 2 — Propor o workflow visualmente antes de construir**

Mostrar a lógica do workflow de forma clara antes de qualquer configuração:

```
EXEMPLO DE COMO MOSTRAR:

Quando: Lead preenche formulário
   ↓ (imediato)
Faz: Envia SMS "Olá! Recebemos o teu pedido."
   ↓ (espera 2 minutos)
Faz: Cria oportunidade no pipeline "Novo Lead"
   ↓ (espera 2 minutos)
Faz: Notifica a equipa via Slack/SMS interno
   ↓ (espera 24 horas)
Verifica: Respondeu à mensagem?
  → SIM: Notifica equipa "Lead respondeu!"
  → NÃO: Envia email de follow-up
```

Perguntar: "Faz sentido este fluxo? Há algo a mudar?"

**Passo 3 — Explicar cada passo antes de avançar**

Para cada acção do workflow, explicar de forma simples:
- O que faz
- Porquê está ali
- O que acontece se correr mal

Exemplo: "A espera de 2 minutos antes do email é para não parecer que foi enviado por um robô — dá um toque mais humano."

**Passo 4 — Dar o código/configuração exacta**

Quando a equipa aprovar o design, dar:
- Nome sugerido para o workflow
- Qual gatilho escolher e com que filtros
- Cada acção com texto pronto (SMS, email, etc.)
- Configurações do workflow (re-entry, stop on response, time window)

**Passo 5 — Guiar o teste**

Antes de publicar, guiar passo a passo:
1. "Cria um contacto de teste com o teu número e email"
2. "Clica em Test Workflow e selecciona esse contacto"
3. "Verifica: chegou o SMS? O email? O pipeline moveu?"
4. Se algo não correu bem: diagnosticar juntos com base no `erros-comuns.md`

**Passo 6 — Checklist antes de publicar**

Percorrer os pontos do `checklist.md` com a equipa antes de activar.

---

### Princípios de comunicação com a equipa

- **Nunca assumir que a pessoa sabe termos técnicos.** Trigger = "o que dispara", Action = "o que acontece", Branch = "caminho separado".
- **Sempre mostrar o workflow visualmente** (diagrama de texto com setas) antes de entrar em configurações.
- **Validar a cada passo** — não avançar sem confirmação da equipa.
- **Explicar o porquê** de cada decisão, não só o quê.
- **Se houver erro**, não culpar — diagnosticar juntos com perguntas simples.
- **Propor o mais simples primeiro** — só adicionar complexidade se a equipa pedir.

---

## Regras de ouro das automações GHL

1. **Testar sempre** com contato real antes de activar em produção
2. **Nomear bem:** `[Categoria] - [Objectivo] - [Trigger]`
3. **Um workflow, um objectivo** — não criar monsters com 50 branches
4. **Respeitar horários** — SMS fora do expediente vai para spam
5. **Ter saída** — todo workflow precisa de uma forma de o contato sair
6. **Sem loops** — dois workflows que se chamam mutuamente travam o sistema

**Versão:** 2026-06-08 — Fontes: Guia Magnetic Flows 2026 + help.gohighlevel.com
**Ecossistema:** Upscale / UP Marketing

