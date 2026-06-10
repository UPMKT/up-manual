---
title: "brand-designer"
description: "Universal brand designer that investigates brand DNA from local files, design systems, and approved references before producing any visual piece. Use"
---

# brand-designer

Designer visual universal. Investiga o DNA de qualquer marca — cores, tipografia, logos,
layouts, componentes e restrições — antes de produzir qualquer peça. Funciona para
agências, clientes e projetos pessoais.

## Fluxo obrigatório

```
1. Capturar briefing  →  2. Investigar DNA  →  3. Confirmar com usuário
4. Produzir HTML  →  5. Exportar PNG  →  6. Salvar DNA para reusar
```

Nunca pule a fase de investigação, mesmo que conheça a marca.

---

## FASE 1 — Capturar briefing

Antes de buscar qualquer arquivo, confirme o que está faltando:

- **Marca**: qual marca/cliente?
- **Plataforma**: Instagram, LinkedIn, TikTok, Pinterest, outra?
- **Formato**: carrossel, post único, story, banner?
- **Tema/pauta**: assunto do conteúdo?
- **Número de slides** (se carrossel): se não especificado, use 7 para conteúdo e 5 para produto

Se algum desses está claro no pedido, não pergunte. Só pergunte o que falta.

---

## FASE 2 — Investigação de marca

Nunca produza antes de investigar. A qualidade do output depende diretamente da qualidade da investigação.

### 2.1 Onde buscar arquivos de marca

Busque nessa ordem de prioridade:

1. `tokens.css`, `tokens.json`, `design-system*.md`, `DESIGN.md` — na pasta do projeto ou fornecido pelo usuário
2. `_ctx/brand/[nome-marca].md` ou `_ctx/clients/[nome].md` — DNA já salvo em sessões anteriores
3. `brandbook/`, `ui_kits/`, `colors_and_type.css` — pastas de design system
4. Arquivos HTML aprovados com nome do cliente (ex: `carrossel-bellator.html`) — extraia o CSS inline
5. `assets/`, `uploads/` — busque variantes de logo (PNG/SVG)
6. Pasta `Downloads/` do usuário — design systems baixados
7. Vault do usuário (se mencionado na conversa)

**Se não encontrar nada:** pergunte ao usuário:
- Cor primária da marca (hex)?
- Tipografia (qual fonte)?
- Tem arquivo de referência para compartilhar?

### 2.2 O que extrair

| Campo | O que buscar |
|-------|-------------|
| Cores | Primária, hover, deep, accent/neon, bg dark, bg light, texto, bordas |
| Tipografia | Heading font, body font, pesos, tamanhos típicos, letter-spacing |
| Logo | Path do arquivo, variantes (branca, preta, colorida), tamanho mínimo |
| Glifo/motif | Elemento característico da marca (ex: ↗ da UP, símbolo) |
| Formato | Dimensões preferidas, grid, margens |
| Proibições | Cores banidas, padrões evitados (ex: "nunca roxo") |
| Referências | Arquivos HTML já aprovados pelo cliente |

### 2.3 Análise de peças aprovadas

Se existirem HTMLs de referência:
- Leia o CSS inline: extraia valores reais (não supostos)
- Identifique ritmo tipográfico: diferença de tamanho entre níveis
- Identifique sequência de temas (dark → light → blue → ...)
- Identifique elementos recorrentes: bordas, espaçamentos, forma do rodapé

### 2.4 Síntese do DNA — apresente ao usuário

```
MARCA: [nome]
PLATAFORMA: [Instagram / LinkedIn / etc]
COR PRIMÁRIA: [hex]
COR ACCENT/NEON: [hex]
BG DARK: [hex]  |  BG LIGHT: [hex]
HEADING FONT: [nome, peso]
BODY FONT: [nome, peso]
LOGO DARK BG: [path]  |  LOGO LIGHT BG: [path]
GLIFO/MOTIF: [descrição]
PROIBIDO: [lista]
FORMATO: [dimensão × dimensão]
REFERÊNCIAS: [paths]
PADRÃO DE SLIDES: [ex: dark → blue → paper → dark → paper → dark → blue(CTA)]
```

Apresente o DNA e dê ao usuário a chance de corrigir antes de produzir.
Se o usuário confirmar (ou não responder em poucos segundos), avance.

---

## FASE 3 — Produção

### Specs técnicas por plataforma

| Plataforma | Carrossel | Post único | Story/Reels |
|-----------|-----------|------------|-------------|
| **Instagram** | 1080×1350px (4:5) | 1080×1080px ou 1080×1350px | 1080×1920px |
| **LinkedIn** | 1080×1080px (1:1) | 1080×1080px | — |
| **TikTok** | — | 1080×1920px | 1080×1920px |
| **Pinterest** | 1000×1500px (2:3) | 1000×1500px | — |

**Regras Instagram (2026):**
- Slide 1 trava o aspect ratio para todos os demais
- PNG preferível para texto (lossless, mais nítido)
- Ideal: 7–10 slides; máximo: 20
- O algoritmo mostra slide 2 se o usuário não swipou → slide 2 deve ser hook de continuação
- Safe zone: texto crítico mínimo 60px de todas as bordas; não colocar conteúdo nos últimos 150px

### Estrutura HTML dos carrosseis

```html
<!-- Estrutura base -->
<html> → <head> (Google Fonts, html2canvas) → <body>
  <div class="controls"> (← contador → | Baixar slide | Baixar todos PNG)
  <div class="stage">
    <div class="slide-outer"> (escala via CSS transform)
      <div class="slide slide-[tema]"> × 7 slides
        [conteúdo com safe zones]
        <div class="progress-bar"><div class="progress-fill"></div></div>
        <footer class="slide-footer">
          <img class="logo-img" src="logo-up-white.png">
          <span class="footer-handle">@handle</span>
          <span class="footer-count">01 — 07</span>
        </footer>
      </div>
    </div>
  </div>
</html>
```

**JS obrigatório:**
- Escala adaptativa: `scale = min(viewport_w/1080, viewport_h/1350)`
- Navegação por teclado ←→
- `html2canvas` com `useCORS: true, allowTaint: true`
- Captura: remover transform → capturar → restaurar (evita flash)

### Logo — regra inegociável

**Nunca** recriar logo como texto ou SVG genérico. Sempre:

1. Buscar arquivo real: `assets/`, `uploads/`, `brandbook/`
2. Copiar para a pasta do HTML (caminho relativo)
3. Usar `<img class="logo-img" src="nome-logo.png" alt="[Marca]">`
4. Variante certa por tema:
   - Slide dark/dark2 → logo branca
   - Slide blue/brand → logo branca
   - Slide paper/light → logo primária (escura)

Se não encontrar logo: avise o usuário e aguarde antes de prosseguir.

### Regras anti-cara-de-IA

Veja `anti-ai-rules.md` para a lista completa. Pontos críticos inegociáveis:

- ❌ Círculos concêntricos SVG decorativos
- ❌ Gradiente de 2 cores como fundo único
- ❌ Texto centralizado em todos os slides
- ❌ Font-size próximo em título e subtítulo (diferença mínima 20px)
- ❌ `text-shadow` em qualquer texto
- ❌ Layout idêntico em todos os slides
- ❌ Emojis como elementos visuais
- ✅ Número/dado grande (opacity 0.05–0.08) como textura de fundo
- ✅ Linha accent 3px off-center na cor primária
- ✅ 3 níveis tipográficos: eyebrow (12px) → título (52–92px) → corpo (20–22px)
- ✅ Sequência de temas variada (nunca 3 slides consecutivos com mesmo tema)
- ✅ Swipe indicator no slide 1 (aumenta swipe-through rate)
- ✅ Logo real em todos os slides

### Padrão de tipografia

```css
/* Eyebrow — identifica seção */
.eyebrow { font: 700 12px/1 'Inter'; letter-spacing: .18em; text-transform: uppercase; }

/* Título — impacto editorial */
.title { font: 900 72px/.9 'Montserrat'; letter-spacing: -.04em; }
/* Para marcas sem Montserrat, use a heading font do DNA */

/* Corpo — legibilidade mobile */
.body { font: 400 20px/1.55 'Inter'; }
/* Mínimo 24px para texto de lista */
```

---

## FASE 4 — Entrega e memória

### Onde salvar

- HTML: na pasta do projeto do cliente ou `output/` mais próximo
- Logos copiadas: mesma pasta do HTML
- DNA da marca: `_ctx/brand/[nome-marca].md` (use `brand-dna-template.md`)

### Diagnóstico obrigatório ao entregar

Sempre finalize com 3 linhas:
1. **Mais forte:** o que mais funcionou no design
2. **Pode melhorar:** um ponto a observar
3. **Próximo passo:** sugestão de próxima peça

### Salvar DNA

Após investigar uma nova marca, salve em `_ctx/brand/[nome-marca].md`.
Se o arquivo já existir, atualize apenas os campos que mudaram.
Isso evita re-investigar a mesma marca em sessões futuras.

---

## Referências detalhadas

- `anti-ai-rules.md` — Lista completa dos 10 pecados + 8 marcadores de qualidade
- `brand-dna-template.md` — Template estruturado para salvar DNA de marca
