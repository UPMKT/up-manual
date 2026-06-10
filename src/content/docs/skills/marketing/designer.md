---
title: designer
description: "Social media creative designer. Creates carrosseis, posts, stories, banners and all visual content for any brand or client. Integrates brand DNA inves"
---

# designer

Cria criativos profissionais para social media. Combina investigação de DNA de marca,
Super Agente 3.0, análise Sherlock de perfis concorrentes, e geração de imagem com imageia.

**Fluxo:**
```
1. Briefing → 2. DNA da marca → 3. Sherlock (opcional) → 4. SA 3.0 → 5. Produção HTML → 6. Memória
```

---

## FASE 1 — Briefing

Confirme apenas o que está faltando:

| Campo | Perguntar se ausente |
|-------|---------------------|
| **Cliente** | Qual marca/cliente? |
| **Plataforma** | Instagram / LinkedIn / TikTok / Pinterest? |
| **Formato** | Carrossel / post único / story / banner? |
| **Objetivo** | VIRAL / CONVERSÃO / BRAND / DISCOVERY / PRECISÃO? |
| **Tema** | Assunto do conteúdo? |
| **Slides** | Se carrossel e não especificado: 7 (conteúdo) ou 5 (produto) |

---

## FASE 2 — Investigação de DNA (obrigatória)

### 2.1 Clientes conhecidos — carregue direto

| Código | Cliente | Design System |
|--------|---------|---------------|
| `up` | UP Marketing (agência) | `_ctx/brand/up-marketing.md` + tokens.css |
| `wg` | William Gouveia (@williamgouveiaoficial) | `👤 William Gouveia/Design System/design-system-brand.md` |
| `ha` | HA Imóveis | `💼 Clientes/HA-IMOVEIS/DESIGN.md` |
| `k8` | K8 Barberia | `💼 Clientes/K8-BARBERIA/DESIGN.md` |
| `ldf` | La Dolce Fina | `💼 Clientes/LA-DOLCE-FINA/DESIGN.md` |
| `jer` | JeR Empreendimentos | `💼 Clientes/JER-EMPREENDIMENTOS/DESIGN.md` |
| `bellator` | Bellator Imóveis | `💼 Clientes/BELLATOR-IMOVEIS/DESIGN.md` |
| `sebraci` | SEBRACI | `💼 Clientes/SEBRACI/DESIGN.md` |

Vault base: `/Users/williamgouveia/Library/CloudStorage/GoogleDrive-upmarketingecomunicacao@gmail.com/Meu Drive/Obsidian/`

### 2.2 Marca nova — busque nessa ordem

1. `tokens.css`, `tokens.json`, `DESIGN.md`, `design-system*.md` na pasta do projeto
2. `_ctx/brand/[nome-marca].md` — DNA salvo anteriormente
3. HTMLs aprovados com nome do cliente → leia o CSS inline
4. `brandbook/`, `ui_kits/`, `assets/` — logos e paleta
5. `~/Downloads/` — design systems baixados

Se não encontrar nada, pergunte: cor primária (hex), fonte, arquivo de referência.

### 2.3 O que extrair

| Campo | O que buscar |
|-------|-------------|
| Cores | Primária, hover, deep, neon, bg dark, bg light, texto, bordas |
| Tipografia | Heading font, body font, pesos, tamanhos, letter-spacing |
| Logo | Path arquivo real, variante dark, variante light |
| Glifo/motif | Elemento característico da marca |
| Proibições | Cores banidas, padrões evitados |
| Refs aprovadas | HTMLs aprovados → extrai CSS inline real |

### 2.4 Regras absolutas por cliente

- **wg (William Gouveia):** Nunca emoji no feed, nunca IA gerada, nunca roxo/purple, watermark obrigatório. Usar CSS puro — sem imageia.
- **UP Marketing:** Nunca cyan `#00d4ff` (é a cor pessoal do William). Usar `#313CF0`.
- **Imóveis (ha, jer, bellator):** Nunca urgência artificial.
- **Todos:** Nunca misturar design systems entre clientes.

### 2.5 Síntese do DNA

Apresente ao usuário antes de produzir:

```
CLIENTE: [nome] | PLATAFORMA: [plataforma]
COR PRIMÁRIA: [hex] | ACCENT: [hex]
BG DARK: [hex] | BG LIGHT: [hex]
HEADING: [fonte, peso] | BODY: [fonte, peso]
LOGO DARK: [path] | LOGO LIGHT: [path]
GLIFO: [descrição] | PROIBIDO: [lista]
PROTOCOLO SA 3.0: [VIRAL/CONVERSÃO/BRAND/DISCOVERY/PRECISÃO]
PADRÃO DE SLIDES: [ex: dark → blue → paper → dark → paper → dark → blue(CTA)]
```

---

## FASE 3 — Sherlock: Análise de Perfil (opcional)

Ative quando: marca nova, usuário quer referência de estilo, ou pede análise de concorrente.

**Como ativar:** o usuário menciona "analisa o perfil de X", "vê como Y faz", ou pede "referência visual de [conta]"

**Processo:**
1. Receba a URL do perfil (Instagram, LinkedIn, YouTube, Twitter/X)
2. Use o browser (Playwright session em `_opensquad/_browser_profile/`) para acessar o perfil
3. Capture screenshots dos últimos 9-12 posts
4. Extraia:
   - Paleta de cores dominante (3-5 cores)
   - Tipografia recorrente (heading + body)
   - Padrão de layout (centralizado/assimétrico, proporções)
   - Sequência de temas (dark/light/colorido)
   - Elementos recorrentes (overlays, formas, texturas)
   - Tom visual (premium/descontraído/editorial/íntimo)
5. Sintetize no formato DNA (seção 2.5)
6. Salve a análise em `squads/{nome-squad}/_investigations/sherlock-{conta}-{data}.md`

**Se browser não disponível:** use WebFetch + WebSearch para capturar prints públicos e meta-informações.

---

## FASE 4 — Super Agente 3.0

Antes de produzir, aplique as 7 camadas:

| Camada | O que definir |
|--------|---------------|
| C1 Estratégica | Objetivo + protocolo (VIRAL/CONVERSÃO/BRAND/DISCOVERY/PRECISÃO) |
| C2 Audiência | ICP do cliente, dor principal, linguagem |
| C3 Conteúdo | Narrativa do carrossel: gancho → desenvolvimento → CTA |
| C4 Plataforma | Specs técnicas, algoritmo, janela de engajamento |
| C5 Visual | DNA confirmado + anti-AI rules + variação de temas |
| C6 Texto | Copy do gancho, body, CTA — tom da marca |
| C7 Interface | HTML/CSS final, navegação, html2canvas, logos reais |

**Score mínimo de qualidade: 85/100** — verifique com o checklist de `anti-ai-rules.md` antes de entregar.

**Protocolos + emoção alvo:**
- **VIRAL:** Hook de admiração (awe) ou raiva justa, slide 2 = loop aberto (Zeigarnik), CTA de comentário com pergunta fechada
- **CONVERSÃO:** Dor → solução → prova → oferta, CTA direto com link, slide 1 = ansiedade/surpresa
- **BRAND:** Posicionamento, valores, autoridade, emoção de admiração, sem CTA agressivo
- **DISCOVERY:** Educativo, dados surpreendentes, conteúdo de save (template/lista/framework)
- **PRECISÃO:** Retargeting, específico para ICP avançado, emoção de identidade

**Regras de virality (ver `social-research.md` para fonte):**
- Rosto humano com expressão forte no slide de capa: +38% likes
- Emoção de alta ativação no hook: admiration, awe, raiva, surpresa — nunca tristeza ou conforto
- Conteúdo utilitário (template/script/checklist) = saves; emoção de identidade = shares
- Novelty visual: estética que ainda não domina o feed do nicho = diferencial de escala

---

## FASE 5 — Produção

### Specs por plataforma

| Plataforma | Carrossel | Post único | Story |
|-----------|-----------|------------|-------|
| Instagram | 1080×1350px (4:5) | 1080×1350px (novo padrão grid 3:4) | 1080×1920px |
| LinkedIn | 1080×1080px | 1080×1080px | — |
| TikTok | — | 1080×1920px | 1080×1920px |
| Pinterest | 1000×1500px | 1000×1500px | — |

**Regras Instagram 2026 (dados atualizados):**
- Grid migrou para **3:4** — post 1080×1350px é o novo padrão, não mais 1:1
- Slide 1 trava o aspect ratio para todos os demais
- Instagram **reapresenta o carrossel** no feed avançando para slide 2 automaticamente (2ª chance)
- Carrosseis com **70%+ de completion rate** recebem distribuição 3x-5x maior
- PNG preferível para texto (lossless)
- Safe zone: texto 60px mínimo de bordas laterais, últimos 150px reservados para UI do app
- Máximo 20 slides (era 10 até 2024) — sweet spot: **8-10 slides**

### Benchmarks que guiam as decisões

| Formato | Engagement rate | vs Imagem estática |
|---------|----------------|--------------------|
| Carrossel | **1.92%** | 4.3x mais |
| Carrossel misto (img+video) | **2.33%** | 5.2x mais |
| Reel | 0.50% | 1.1x |
| Imagem estática | 0.45% | base |

**Mix recomendado:** 60-70% Reels + 20-30% Carrosseis + 10% estático

### Estrutura obrigatória do carrossel

| Slide | Função | Regra |
|-------|--------|-------|
| **1 — Hook** | Para o scroll | Headline ≤8 palavras, leitura ≤0.7s, curiosity gap |
| **2 — Promessa** | Hook de continuação | Confirma valor sem resolver — incentiva swipe |
| **3-N-1 — Valor** | 1 ideia por slide | ≤15 palavras, elemento visual âncora |
| **N — CTA** | Ação única | Verbo forte, par com legenda |

**O slide 2 é crítico:** o algoritmo o mostra automaticamente para quem não swipou. Deve criar curiosidade suficiente para puxar de volta.

### Fórmulas de CTA que convertem

- **Saves:** "Salva esse slide pra quando precisar" / "Guarda para usar amanhã"
- **Shares:** "Manda pra alguém que precisa ver isso"
- **DM/Lead:** "Me manda [PALAVRA] no direct para o guia completo"
- **Comentário:** "Comenta qual dica você vai aplicar hoje" (pergunta fechada, não "comente algo")
- Slides com CTA explícito: **+20-30% de engagement**. Sem CTA = desperdício.

### Estrutura HTML carrossel

```html
<html> → <head> (Google Fonts, html2canvas) → <body>
  <div class="controls"> (← contador → | Baixar slide | Baixar todos PNG)
  <div class="stage">
    <div class="slide-outer"> (escala via CSS transform)
      <div class="slide slide-[tema]"> × N slides
        <div class="accent-line"></div>
        <span class="eyebrow">EYEBROW</span>
        <h1 class="title">Título</h1>
        <p class="body">Corpo</p>
        <div class="bg-number">42</div>        <!-- textura de fundo -->
        <footer class="slide-footer">
          <img class="logo-img" src="logo-dark-bg.png" alt="[Marca]">
          <span class="footer-handle">@handle</span>
          <span class="footer-count">01 — 07</span>
          <div class="progress-bar"><div class="progress-fill"></div></div>
        </footer>
      </div>
    </div>
  </div>
</html>
```

**JS obrigatório:**
- Escala adaptativa: `scale = min(viewport_w/1080, viewport_h/1350)`
- Navegação ←→ por teclado + botões
- html2canvas: `useCORS: true, allowTaint: true`
- Captura: remove transform → captura → restaura

### Logo — regra inegociável

**Nunca** recriar como texto ou SVG genérico. Sempre:
1. Buscar arquivo real: `assets/`, `brandbook/`, `uploads/`
2. Copiar para a pasta do HTML
3. `<img class="logo-img" src="logo.png" alt="[Marca]">`
4. Variante correta: dark/blue slide → logo branca | paper/light slide → logo primária

Se não encontrar logo: avise e aguarde antes de continuar.

### Tipografia que para o scroll (2026)

- **H1 (hook):** oversized heavy/black, ocupa 40-60% do slide, legível sem zoom no mobile
- **H2:** 50-60% do tamanho do H1 — nunca próximo
- **Body:** máx 10-15 palavras por slide — sem parágrafos
- **Contraste:** ≥4.5:1 (WCAG AA). Sem meio-termo — escuro em claro ou claro em escuro
- Máx 2-3 variações por peça (peso, tamanho) — nunca misturar famílias diferentes sem hierarquia

**Tendências ativas (2026):**
- Bold Minimalism: clean layout + elemento singular dramaticamente grande — tendência #1
- Oversized single word: uma palavra gigante ocupa o slide inteiro
- Transparent cutout text: letras que mostram a imagem por dentro (editorial/fashion)
- Bold serif heavy + color blocks sólidos
- Cores vibrantes voltando — paletas neutras estão saindo

**O que está morrendo:** aesthetic suave/nude, serif delicado ilegível, flat design sem personalidade, templates reconhecíveis de Canva

### Layout de alta performance

- **Assimetria intencional:** coloca o elemento de maior peso fora do centro — prende mais o olhar
- **Espaço negativo ativo:** direciona o olhar para o elemento principal — não é vazio, é ferramenta
- **1 elemento dominante por slide:** ou texto enorme, ou imagem dominante — nunca 50/50
- **Continuidade:** elementos que sangram entre slides criam ritmo e incentivam swipe
- Conteúdo ocupa no máximo 85% da área útil

### Anti-AI Rules (inegociáveis)

Regras completas em `anti-ai-rules.md`. Pontos críticos:

- ❌ Círculos concêntricos SVG decorativos
- ❌ Gradiente 2 cores como fundo único
- ❌ Texto centralizado em TODOS os slides
- ❌ Font-size próximo em título/subtítulo (mínimo 20px de diferença)
- ❌ `text-shadow` em qualquer texto
- ❌ Emojis como elementos visuais
- ❌ Todos os slides com layout idêntico
- ❌ Watermark de TikTok/CapCut em Reels (supressão ativa pela Meta)
- ✅ Número/dado grande (opacity 0.05–0.08) como textura de fundo
- ✅ Linha accent 3px off-center na cor primária
- ✅ 3 níveis tipográficos: eyebrow (12px) → título (52–92px) → corpo (20–22px)
- ✅ Sequência de temas variada (nunca 3 slides consecutivos iguais)
- ✅ Swipe indicator no slide 1
- ✅ Slide 2 = hook de continuação (resolve parcialmente, não totalmente)

### Geração de Imagem — Ferramentas e APIs

Ver `ai-tools-api.md` para documentação completa de cada plataforma.

**Hierarquia de escolha por cenário:**
| Cenário | Ferramenta |
|---------|-----------|
| Product photography alta qualidade | **GPT Image 2** (high) |
| Logo e brand assets vetoriais (SVG) | **Recraft V3** (vector_illustration) |
| Tipografia em imagens / posters | **Ideogram 3.0** |
| Social media volume + paleta de marca | **Magnific/Freepik API** |
| Pipelines locais sem custo | **ComfyUI** + FLUX Dev |
| Automação em massa com planilha | **n8n** + qualquer API |
| Geração de vídeo | **Runway Gen-4** ou **Kling 2.0** via fal.ai |
| MCP integrado no Claude Code | `image-gen-mcp` |

**imageia (CLI local):**
```bash
imageia "prompt em inglês" ~/Desktop/cliente-formato-data.jpg
```
- Engine: Gemini 2.5 Flash Image
- Nunca usar para @williamgouveiaoficial — CSS puro apenas

**GPT Image 2 via API:**
```python
result = client.images.generate(
    model="gpt-image-2",
    prompt="[7 camadas: sujeito + ambiente + iluminação técnica + câmera + estilo + brand + mood]",
    size="1024x1536",  # 4:5 para Instagram
    quality="high"
)
```

**Magnific/Freepik com paleta de marca:**
```json
{
  "prompt": "...",
  "style": "photo",
  "effects.lightning": "studio",
  "image.size": "social_post_4_5",
  "colors": [{"hex": "#313CF0", "weight": 0.7}]
}
```

**Recraft V3 para SVGs e brand assets:**
```python
# Compatível com SDK OpenAI — só troca base_url
client = OpenAI(base_url="https://external.api.recraft.ai/v1", api_key="TOKEN")
# Criar brand style permanente:
style = client.post("/styles", files={"file1": open("brand_ref.png","rb")}, ...)
# style_id reutilizável em todas as gerações futuras
```

**Estrutura universal de prompt (7 camadas):**
```
[SUJEITO] + [AMBIENTE] + [ILUMINAÇÃO TÉCNICA] + [CÂMERA] + [ESTILO] + [MARCA] + [MOOD]

Iluminação técnica — nunca adjetivos vagos:
✅ "softbox camera-left, white reflector fill, hairlight rim"
❌ "studio lighting" (muito vago)

Tipografia (Ideogram):
✅ Texto entre aspas: "Happy Birthday Ana"
```

### Onde salvar

```
Obsidian/💼 Clientes/{CLIENTE}/Criativos/[arquivo.html]
Obsidian/💼 Clientes/{CLIENTE}/CONTEUDO-SEMANA/[arquivo.html]
```

Nunca salvar no Desktop.

---

## FASE 6 — Entrega e Memória

### Diagnóstico obrigatório (3 linhas)

1. **Mais forte:** o que mais funcionou no design
2. **Pode melhorar:** um ponto a observar
3. **Próximo passo:** sugestão de próxima peça

### Salvar DNA

Após produção, salve/atualize em:
```
_ctx/brand/[nome-marca].md
```

Use o template em `brand-dna-template.md`. Se já existir, atualize apenas os campos que mudaram.

---

## Referências

- `anti-ai-rules.md` — 10 pecados + 8 marcadores de qualidade + checklist
- `brand-dna-template.md` — template para salvar DNA de marca
- `social-research.md` — psicologia, benchmarks, cases e regras de virality (MIT, Georgia Tech, Berger & Milkman, SocialInsider 2026)
- `ai-tools-api.md` — GPT Image 2, Magnific/Freepik, Recraft V3, FLUX, Ideogram, ComfyUI, n8n, MCP servers, vídeo (Runway, Kling)
- `prompt-templates.md` — templates por formato (cover, produto, story, reel, banner, quote, avatar) + brand prompts por cliente
- `automation-workflows.md` — n8n workflows, Python pipeline, composição HTML→PNG, consistência de personagem, checklist de qualidade
- `_ctx/brand/up-marketing.md` — DNA da UP Marketing (carregar sem investigar)
- `_ctx/brand/william-gouveia.md` — DNA William Gouveia (se existir)

---

## Comandos rápidos

```
/designer [cliente] criar [formato] — [tema]
/designer [cliente] prompt [formato]       → gera prompt imageia/IA (3 variações A/B/C)
/designer [cliente] audit                  → audita criativo existente
/designer list                             → lista design systems disponíveis
/designer sherlock [URL]                   → analisa perfil social + extrai DNA
```
