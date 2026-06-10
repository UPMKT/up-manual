---
title: UP Portal Ops
description: "Squad de engenharia do PortalclienteUP — implementa features, corrige bugs, audita código e mantém o portal operacional 24/7."
---

> Squad de engenharia do PortalclienteUP — implementa features, corrige bugs, audita código e mantém o portal operacional 24/7.


## Agentes

- PO
- Frontend
- Supabase
- QA
- Docs


# UP Agency — Mega Marketing Squad

> Agência de marketing digital autônoma que pesquisa, planeja, cria, edita e revisa conteúdo multi-plataforma.

---

## Visão Geral

O UP Agency é um squad de 5 agentes de IA que opera de forma totalmente autônoma, sem necessidade de intervenção humana durante a execução. O pipeline processa pesquisa de mercado, estratégia, criação de conteúdo, edição técnica e revisão de qualidade — entregando conteúdo pronto para publicação em 8 plataformas.

**Versão:** 1.0.0
**Modo:** Autônomo (0 checkpoints)
**Performance:** Econômico (haiku + sonnet)
**Criado em:** 17 de março de 2026

---

## Agentes

| Agente | Persona | Modelo | Especialidade |
|--------|---------|--------|---------------|
| Alex | Researcher | haiku | Pesquisa de mercado, concorrentes, BI, benchmarks |
| Sophie | Strategist | sonnet | Estratégia, funis de venda, tráfego pago, calendário editorial |
| Max | Creator | sonnet | Conteúdo multi-plataforma, copywriting, roteiros de vídeo |
| Luna | Editor | haiku | Edição multi-formato, specs técnicos, design, acessibilidade |
| Quinn | Reviewer | haiku | Qualidade (7 dimensões), aprovação autônoma, gate de qualidade |

---

## Plataformas Cobertas

| Plataforma | Formatos |
|------------|----------|
| Instagram | Carrossel, Reels, Stories, Feed |
| YouTube | Long-form, Shorts |
| TikTok | Vídeos verticais 9:16 |
| LinkedIn | Posts, Carousels, Artigos |
| Facebook | Feed, Stories |
| WhatsApp Business | Mensagens, Broadcast |
| Newsletter (Substack) | Email marketing |
| Community | Engajamento e gestão |

---

## Funções do Sistema

| Função | Agente Responsável |
|--------|-------------------|
| market-research | Alex |
| competitor-monitoring | Alex |
| business-intelligence | Alex |
| strategy | Sophie |
| sales-funnel | Sophie |
| traffic-management | Sophie |
| social-media | Max |
| video-scripting | Max |
| design | Max + Luna |
| quality-review | Quinn |

---

## Pipeline

O pipeline executa em 5 steps sequenciais:

```
Step 1: Alex (Research)     → weekly-research.md
Step 2: Sophie (Strategy)   → weekly-strategy.md
Step 3: Max (Create)        → daily-content.md
Step 4: Luna (Edit)         → edited-content.md
Step 5: Quinn (Review)      → approved-content.md
```

### Cadência
- **Research + Strategy:** Semanal (toda segunda-feira)
- **Create + Edit + Review:** Diário

### Fluxo de Rejeição
Se Quinn rejeitar uma peça (score < 7.0):
1. Conteúdo volta para Max (Step 3)
2. Máximo de 2 ciclos de revisão
3. Se falhar após 2 ciclos: salvo em `output/drafts/` para revisão manual

---

## Estrutura de Arquivos

```
squads/up-agency/
├── squad.yaml                    # Configuração principal do squad
├── squad-party.csv               # Roster dos agentes (CSV)
├── README.md                     # Este arquivo
│
├── agents/                       # Definições dos agentes (.agent.md)
│   ├── researcher.agent.md       # Alex — Researcher
│   ├── strategist.agent.md       # Sophie — Strategist
│   ├── creator.agent.md          # Max — Creator
│   ├── editor.agent.md           # Luna — Editor
│   └── reviewer.agent.md         # Quinn — Reviewer
│
├── pipeline/                     # Pipeline de execução
│   ├── pipeline.yaml             # Definição do pipeline
│   ├── steps/                    # Steps individuais
│   │   ├── 01-research.md
│   │   ├── 02-strategy.md
│   │   ├── 03-create.md
│   │   ├── 04-edit.md
│   │   └── 05-review.md
│   └── data/                     # Dados de pesquisa e outputs intermediários
│       ├── research-brief.md     # Base de pesquisa (15 frameworks, 5 domínios)
│       ├── weekly-research.md    # Output do Alex (semanal)
│       ├── weekly-strategy.md    # Output da Sophie (semanal)
│       ├── daily-content.md      # Output do Max (diário)
│       └── edited-content.md     # Output da Luna (diário)
│
├── output/                       # Outputs finais
│   ├── DOCUMENTACAO-COMPLETA.md  # Documentação do sistema (1.247 linhas)
│   ├── DASHBOARD-ARCHITECTURE.md # Blueprint do dashboard (1.862 linhas)
│   ├── MAPEAMENTO-AGENTES-DASHBOARD.md  # Mapeamento agentes × módulos
│   ├── HOME-KANBAN.md            # Módulo HOME — Dashboard Kanban
│   ├── MULTI-CONTA-ONBOARDING.md # Multi-conta e onboarding automático
│   ├── BRIEFING-UPLOAD-SISTEMA.md # Upload de briefing com IA
│   ├── CHAT-AGENTES.md           # Chat com agentes individuais
│   ├── GESTAO-AGENTES.md         # Cadastro e gestão de agentes
│   ├── FUNIS-PRODUTOS.md         # 15 funis de venda e produtos
│   ├── TRAFEGO-PAGO.md           # Tráfego pago e otimização
│   ├── VENDAS-FATURAMENTO.md     # Vendas e faturamento
│   ├── CRM-PIPELINE.md           # CRM e pipeline de leads
│   ├── SUPORTE-WHATSAPP.md       # Suporte via WhatsApp (Iris)
│   ├── BIBLIOTECA-REPOSITORIO.md # Repositório de arquivos
│   ├── MEMORIA-GRAFO.md          # Grafo de conhecimento
│   ├── CRONS-AGENDAMENTO.md      # Cron jobs e agendamento
│   ├── SKILLS-SUPERPODERES.md    # Skills plugáveis dos agentes
│   ├── DEBUG-MONITORAMENTO.md    # Diagnóstico e monitoramento
│   └── {run-id}/                 # Pasta da run
│       └── v{n}/
│           └── approved-content.md  # Conteúdo aprovado por Quinn
│
├── _memory/                      # Memória persistente do squad
│   └── memories.md               # Learnings, padrões, logs
│
├── _investigations/              # Investigações Sherlock (análise de perfis)
│
└── state.json                    # Estado do pipeline em tempo real
```

---

## Módulos do Dashboard (Opensquad Control Tower)

O squad alimenta um dashboard web com 22 módulos documentados:

| # | Módulo | Agente(s) | Documento | Status |
|---|--------|-----------|-----------|--------|
| 1 | HOME — Dashboard Kanban | Sistema + Todos | `HOME-KANBAN.md` | Documentado |
| 2 | Squad Command Center | Sistema (state.json) | `DASHBOARD-ARCHITECTURE.md` | Documentado |
| 3 | Content Factory (Kanban) | Alex, Max, Luna, Quinn | `DASHBOARD-ARCHITECTURE.md` | Documentado |
| 4 | Traffic Command — Tráfego Pago | Sophie, Alex, Quinn | `TRAFEGO-PAGO.md` | Documentado |
| 5 | Funnel Builder — Funis & Produtos | Max, Sophie, Luna, Quinn | `FUNIS-PRODUTOS.md` | Documentado |
| 6 | Performance Dashboard | Alex, Sophie | `DASHBOARD-ARCHITECTURE.md` | Documentado |
| 7 | Vendas — Faturamento | Alex, Sophie | `VENDAS-FATURAMENTO.md` | Documentado |
| 8 | CRM — Pipeline de Leads | Sophie, Alex, Max | `CRM-PIPELINE.md` | Documentado |
| 9 | Calendar & Scheduling — Crons | Sophie, Sistema | `CRONS-AGENDAMENTO.md` | Documentado |
| 10 | Research & Intelligence | Alex | `DASHBOARD-ARCHITECTURE.md` | Documentado |
| 11 | Memory & Learning — Grafo | Quinn, Alex | `MEMORIA-GRAFO.md` | Documentado |
| 12 | Multi-Conta & Onboarding | Todos | `MULTI-CONTA-ONBOARDING.md` | Documentado |
| 13 | Briefing Upload (IA) | Alex + Sistema | `BRIEFING-UPLOAD-SISTEMA.md` | Documentado |
| 14 | CHAT — Comunicação com Agentes | Todos | `CHAT-AGENTES.md` | Documentado |
| 15 | AGENTES — Cadastro e Gestão | Sistema | `GESTAO-AGENTES.md` | Documentado |
| 16 | Biblioteca — Repositório | Sistema + Todos | `BIBLIOTECA-REPOSITORIO.md` | Documentado |
| 17 | Suporte — WhatsApp | Iris (6º agente) | `SUPORTE-WHATSAPP.md` | Documentado |
| 18 | Skills — Super Poderes | Todos | `SKILLS-SUPERPODERES.md` | Documentado |
| 19 | Debug — Monitoramento | Sistema | `DEBUG-MONITORAMENTO.md` | Documentado |

Documentação completa: `output/DASHBOARD-ARCHITECTURE.md`
Mapeamento agentes × módulos: `output/MAPEAMENTO-AGENTES-DASHBOARD.md`

---

## Como Executar

### Via Opensquad CLI
```bash
# Na raiz do projeto
/opensquad run up-agency
```

### Primeira Execução (resultados)
- **Run ID:** 2026-03-17-174634
- **Score médio:** 8.53/10
- **Peças aprovadas:** 3/3 (Carrossel IG 8.75, TikTok 8.40, LinkedIn 8.45)
- **Peças rejeitadas:** 0

---

## Configurações

| Parâmetro | Valor |
|-----------|-------|
| auto_approve | true |
| max_revision_cycles | 2 |
| output_dir | output/ |
| memory_dir | _memory/ |
| checkpoints | none |

---

## Documentação

| Documento | Linhas | Conteúdo |
|-----------|--------|----------|
| `DOCUMENTACAO-COMPLETA.md` | 1.247 | Arquitetura, agentes, pipeline, plataformas, decisões |
| `DASHBOARD-ARCHITECTURE.md` | 1.862 | Blueprint completo: tech stack, módulos, wireframes, APIs, fases, custos |
| `MAPEAMENTO-AGENTES-DASHBOARD.md` | 308 | Mapeamento de cada módulo para seus agentes responsáveis |
| `HOME-KANBAN.md` | ~350 | Módulo HOME: Kanban de operação diária |
| `MULTI-CONTA-ONBOARDING.md` | ~500 | Multi-conta, onboarding automático, selector |
| `BRIEFING-UPLOAD-SISTEMA.md` | ~600 | Upload de briefing, processamento IA, revisão |
| `CHAT-AGENTES.md` | ~350 | Chat individual com agentes, ações rápidas |
| `GESTAO-AGENTES.md` | ~400 | Cadastro, edição, troca de modelo, métricas |
| `FUNIS-PRODUTOS.md` | ~600 | 15 funis de venda, geração de assets, métricas |
| `TRAFEGO-PAGO.md` | 1.676 | Campanhas, otimização automática, ranking criativos, 5 tabelas SQL |
| `VENDAS-FATURAMENTO.md` | ~590 | KPIs, breakdown por origem, checkout integrations |
| `CRM-PIPELINE.md` | 1.328 | Kanban 6 estágios, lead scoring BANT, fluxo completo de lead |
| `SUPORTE-WHATSAPP.md` | 1.525 | WhatsApp API, FAQ, auto-respostas, agente Iris |
| `BIBLIOTECA-REPOSITORIO.md` | ~240 | Repositório de arquivos, categorias, busca full-text |
| `MEMORIA-GRAFO.md` | ~400 | Grafo de conhecimento, 7 categorias de nós, auto-extração |
| `CRONS-AGENDAMENTO.md` | ~500 | 18 cron jobs, anti-conflito, calendário 24h |
| `SKILLS-SUPERPODERES.md` | 1.445 | Skills plugáveis, catálogo, 20 skills recomendadas, custos |
| `DEBUG-MONITORAMENTO.md` | ~500 | Doctor, métricas, logs, console, desbloqueio visual |
| `PRD-OPENSQUAD-CONTROL-TOWER.md` | 912 | PRD executivo consolidado: 19 módulos, custos, roadmap, riscos |
| `README.md` | ~300 | Este arquivo |

---

## Métricas de Qualidade (Quinn)

### 7 Dimensões de Avaliação
| Dimensão | Peso |
|----------|------|
| Hook Strength | 20% |
| Value Delivery | 20% |
| Brand Alignment | 15% |
| Platform Fit | 15% |
| CTA Clarity | 10% |
| Accuracy | 10% |
| Engagement Potential | 10% |

### Regras de Aprovação
- Score geral >= 7.0: APROVADO
- Nenhuma dimensão individual < 4.0
- Máximo 2 ciclos de revisão antes de escalação

---

## Tech Stack do Dashboard (planejado)

| Camada | Tecnologia |
|--------|-----------|
| Frontend | Next.js 15 + Tailwind CSS + shadcn/ui |
| Backend | tRPC + Supabase |
| Banco | PostgreSQL (Supabase) |
| Auth | Magic Link (Supabase Auth) |
| Realtime | WebSocket + Supabase Realtime |
| Charts | Recharts |
| Kanban | DnD Kit |
| Cron | node-cron (Vercel) |
| Deploy | Vercel |
| APIs | Meta Marketing v21, Google Ads v17, TikTok Business v1.3 |

---

## Equipe — UP Marketing & Comunicação

| Nome | Papel | Responsabilidade no Sistema |
|------|-------|---------------------------|
| William Gouveia | CEO e Guardião da Marca | Estratégia geral, aprovação final, LinkedIn, gravação TikTok, tom de voz |
| Patrícia | Social Media Manager | Publicação, monitoramento, engajamento |
| Sara | Content Producer | Produção, agendamento, métricas diárias |

---

*UP Agency Squad v1.0.0 — Opensquad Framework*
*UP Marketing & Comunicação — William Gouveia, CEO e Guardião da Marca*
*Criado em 17 de março de 2026*
