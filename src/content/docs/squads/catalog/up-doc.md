---
title: "up-doc"
description: "Gera documentos oficiais UP (Relatórios, Manuais, Propostas) com design system validado, pronto para PDF"
---

> Gera documentos oficiais UP (Relatórios, Manuais, Propostas) com design system validado, pronto para PDF


## Agentes

- {'id': 'researcher', 'role': 'Pesquisador', 'persona': 'Especialista em análise de contexto e dados do cliente', 'task': 'Analisar o cliente, período e contexto para estruturar o documento', 'prompt': 'Você é um pesquisador especializado em análise de contexto.\n\nDADOS DO CLIENTE:\n- Nome: {{ client_name }}\n- Tipo de documento: {{ document_type }}\n- Período: {{ period }}\n- Data: {{ document_date }}\n\nSEU OBJETIVO:\n1. Analisar o contexto e público-alvo\n2. Definir tom e estrutura (formal, executivo, técnico)\n3. Identificar KPIs principais\n4. Listar seções necessárias\n\nRESPONDA EM JSON:\n{\n  "analise": "...",\n  "tom": "formal|executivo|técnico",\n  "kpis_principais": ["KPI1", "KPI2", "KPI3", "KPI4"],\n  "secoes": ["Seção 1", "Seção 2", "Seção 3"],\n  "diretrizes": "..."\n}\n'}
- {'id': 'writer', 'role': 'Redator', 'persona': 'Copywriter especializado em relatórios e documentos corporativos UP', 'task': 'Criar conteúdo estruturado seguindo o design system UP', 'depends_on': 'researcher', 'prompt': 'Você é um redator especializado em documentos corporativos da UP Marketing & Comunicação.\n\nANÁLISE ANTERIOR:\n{{ researcher.output }}\n\nDADOS DO CLIENTE:\n- Cliente: {{ client_name }}\n- Tipo: {{ document_type }}\n- Período: {{ period }}\n\nDESIGN SYSTEM UP (IMUTÁVEL):\n- Paleta: Azul (#476FEF), Verde (#46d369), Laranja (#ff8c42), Vermelho (#ff4757)\n- Tipografia: Montserrat (headings), JetBrains Mono (números)\n- Estrutura: 4 páginas A4, KPI cards 2x2, tabelas com cores semânticas\n\nSEU OBJETIVO:\n1. Criar 4 KPI cards com valores fictícios realistas\n2. Estruturar 3-4 seções principais\n3. Gerar insights e recomendações\n4. Manter tom profissional e executivo\n\nRESPONDA EM JSON COM O CONTEÚDO ESTRUTURADO:\n{\n  "kpi_cards": [\n    {"label": "...", "value": "...", "subtext": "..."},\n    ...\n  ],\n  "secoes": [\n    {"titulo": "...", "conteudo": "..."},\n    ...\n  ],\n  "recomendacoes": ["...", "...", "..."],\n  "conclusao": "..."\n}\n'}
- {'id': 'reviewer', 'role': 'Revisor', 'persona': 'Editor especializado em qualidade de conteúdo e conformidade com design system', 'task': 'Revisar conteúdo e garantir conformidade com design system UP', 'depends_on': 'writer', 'prompt': 'Você é um revisor especializado em conteúdo corporativo UP.\n\nCONTEÚDO A REVISAR:\n{{ writer.output }}\n\nCHECKLIST DE CONFORMIDADE:\n✓ Número de KPI cards: 4\n✓ Formatação de números: R$ 1.234,56 | 12,5% | 83.131\n✓ Cores semânticas: Verde (sucesso), Laranja (atenção), Vermelho (crítico)\n✓ Tom: Profissional e executivo\n✓ Sem roxo (usar ciano #22d3ee)\n✓ Seções limpas e organizadas\n✓ Recomendações acionáveis\n\nRETORNE:\n{\n  "status": "APROVADO|PRECISA_REVISÃO",\n  "observacoes": "...",\n  "conteudo_ajustado": {...}\n}\n'}
- {'id': 'exporter', 'role': 'Integrador PDF', 'persona': 'Especialista em integração template + conteúdo e exportação para PDF', 'task': 'Preencher template HTML com conteúdo e gerar PDF', 'depends_on': 'reviewer', 'prompt': 'Você é um integrador especializado em documentos HTML → PDF.\n\nTEMPLATE PATH: {{ template_path }}\nSAÍDA: {{ output_dir }}/Relatorio-{{ client_name }}-{{ date_stamp }}.pdf\n\nDADOS PARA PREENCHER:\n- document_title: {{ document_type }}\n- document_subtitle: Análise e Recomendações\n- client_name: {{ client_name }}\n- period: {{ period }}\n- document_date: {{ document_date }}\n- Conteúdo KPIs e seções: {{ reviewer.output }}\n\nINSTRUÇÕES:\n1. Usar template em: {{ template_path }}\n2. Substituir placeholders {{}} com dados do cliente\n3. Preencher KPI cards, tabelas, seções\n4. Gerar PDF via Chrome headless ou similar\n5. Validar output em: {{ output_dir }}\n\nRETORNE:\n{\n  "status": "COMPLETO|ERRO",\n  "arquivo_pdf": "...",\n  "instrucoes": "Para imprimir: Cmd+P → Print to PDF (margens: nenhuma, A4)"\n}\n'}


# 🎯 UP Document Generator Squad

Gera documentos oficiais UP (Relatórios, Manuais, Propostas) com design system validado e pronto para PDF.

## 🚀 Como Usar

### Opção 1: Script Bash Rápido (Mais Prático)

```bash
# Modo interativo (melhor para primeira vez)
up-doc

# Modo com argumentos
up-doc --type "Relatório" --cliente "HA Imóveis" --periodo "13 a 19 março"

# Com todos os parâmetros
up-doc --type "Relatório" --cliente "HA Imóveis" --periodo "13 a 19 março" \
       --date "28 de março de 2026" --subtitle "Performance Meta Ads"
```

**O que ele faz:**
1. ✅ Pergunta tipo de documento, cliente, período, data
2. ✅ Copia o template HTML
3. ✅ Substitui placeholders {{}} automaticamente
4. ✅ Abre no navegador para edição
5. ✅ Mostra passo-a-passo para exportar PDF

**Tempo total:** 2 minutos (do comando até PDF pronto)

---

### Opção 2: Opensquad Squad (Automação Completa)

```bash
# No terminal do projeto
/opensquad run up-doc
```

**Pipeline de agentes:**
1. 🔍 **Pesquisador** — Analisa contexto do cliente
2. ✍️ **Redator** — Cria conteúdo estruturado
3. ✅ **Revisor** — Valida conformidade com design system
4. 📄 **Exportador** — Gera PDF final

**Tempo total:** 3-5 minutos (automático, sem intervenção)

---

## 📋 Fluxo Completo

```
┌─────────────────────────────────────────────────┐
│  up-doc (ou /opensquad run up-doc)              │
├─────────────────────────────────────────────────┤
│ 1. Coletar dados do cliente                     │
│    • Tipo (Relatório/Manual/Proposta)           │
│    • Nome do cliente                            │
│    • Período                                    │
│    • Data                                       │
├─────────────────────────────────────────────────┤
│ 2. Copiar template de document-template-up.html │
│    • Substitui placeholders {{}}                │
│    • Mantém design system imutável              │
├─────────────────────────────────────────────────┤
│ 3. Abrir no navegador para edição               │
│    • Preenchre KPI cards                        │
│    • Adiciona tabelas/seções                    │
│    • Customiza conteúdo por cliente             │
├─────────────────────────────────────────────────┤
│ 4. Exportar para PDF                            │
│    • Cmd+P → Print to PDF                       │
│    • Margens: nenhuma, A4                       │
│    • Elementos gráficos: ATIVADO                │
├─────────────────────────────────────────────────┤
│ 5. Arquivo salvo em:                            │
│    ~/Documents/UP-Documentos/Relatorio-*.pdf    │
└─────────────────────────────────────────────────┘
```

---

## 🎨 Componentes Disponíveis

### KPI Cards (2x2 Grid)
```html
<div class="kpi-card primary">
  <div class="kpi-label">Investimento Total</div>
  <div class="kpi-value">R$ 5.432,00</div>
  <div class="kpi-subtext">7 dias</div>
</div>
```

**Classes de cor:**
- `.primary` — Azul UP (#476FEF)
- `.success` — Verde (#46d369)
- `.warning` — Laranja (#ff8c42)
- `.danger` — Vermelho (#ff4757)

### Data Cards
```html
<div class="card success">
  <div class="card-title">Título</div>
  <div class="card-text">Conteúdo aqui...</div>
</div>
```

**Tipos:** `.info` (ciano) | `.success` (verde) | `.warning` (laranja) | `.danger` (vermelho)

### Tabelas
```html
<table class="table striped">
  <thead>
    <tr>
      <th>Campanha</th>
      <th style="text-align: right;">Investimento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cadastro - Premium</td>
      <td style="text-align: right;"><span class="success">R$ 15,40</span></td>
    </tr>
  </tbody>
</table>
```

### Badges
```html
<span class="badge blue">OBJETIVO</span>
<span class="badge green">SUCESSO</span>
<span class="badge orange">ATENÇÃO</span>
<span class="badge red">CRÍTICO</span>
```

---

## 📚 Estrutura de 4 Páginas

| Página | Nome | Conteúdo |
|--------|------|----------|
| 1 | **Capa** | Logo + Título + Cliente + Período + Footer |
| 2 | **Introdução** | Objetivo + 2 Cards info |
| 3 | **Métricas** | KPI Cards 2x2 + Dados principais |
| 4 | **Análise** | Seções + Tabelas + Conclusão + Footer |

---

## 🎯 Placeholders Customizáveis

| Placeholder | Exemplo | Onde |
|-------------|---------|------|
| `{{document_title}}` | "Relatório de Performance" | Capa + Header |
| `{{document_subtitle}}` | "Análise de Campanhas" | Capa |
| `{{client_name}}` | "HA Imóveis" | Capa + Footer |
| `{{period}}` | "13 a 19 de março" | Capa |
| `{{document_date}}` | "28 de março de 2026" | Capa |

---

## ✅ Checklist de Uso

- [ ] Executar `up-doc` ou `/opensquad run up-doc`
- [ ] Preencher dados do cliente (nome, período, tipo)
- [ ] Editar conteúdo no navegador:
  - [ ] KPI cards com valores reais
  - [ ] Tabelas com dados
  - [ ] Seções customizadas
  - [ ] Recomendações
- [ ] Validar que NÃO há roxo (usar ciano #22d3ee)
- [ ] Exportar para PDF: Cmd+P → Print to PDF
- [ ] Validar margens (nenhuma) e tamanho (A4)
- [ ] Salvar em `~/Documents/UP-Documentos/`

---

## 🔧 Troubleshooting

**Logo não aparece?**
→ Verificar caminho: `/Users/williamgouveia/up-marketing-ds/public/images/logos/logo-white.png`

**Cores diferentes ao imprimir?**
→ Ativar "Elementos gráficos de fundo" em Cmd+P → Mais configurações

**Fonte estranha?**
→ Google Fonts carrega automaticamente — verificar conexão internet

**Quebras de página incorretas?**
→ CSS @page e @media print estão configurados — não mexer na estrutura

---

## 📞 Referência Design System

**Arquivo de referência:** `report-design-system.md`

**Cores (Imutáveis):**
- Azul UP: `#476FEF`
- Verde (Sucesso): `#46d369`
- Laranja (Atenção): `#ff8c42`
- Vermelho (Crítico): `#ff4757`
- Ciano (Info): `#22d3ee`

**Tipografia:**
- Headings: Montserrat 700-800
- Body: Montserrat 400-500
- Números: JetBrains Mono 600

---

**Status:** ✅ Pronto para Produção
**Última atualização:** 28/03/2026
**Template Version:** 1.0 — UP Document Generator
