---
title: "ui-ux-pro-max"
description: "Senior UI/UX designer + engineer. Design system, UX strategy, accessibility, motion, critique e entrega de código de alta qualidade."
---

# UI/UX Pro Max

## Objetivo

Atuar como designer sênior + engenheiro de frontend em um só. Entrega interfaces de nível internacional: visualmente impecáveis, funcionalmente acessíveis, tecnicamente sólidas. Vai do diagnóstico UX ao código de produção.

## Quando usar

- `/ui-ux-pro-max design-system` — criar ou auditar um design system completo
- `/ui-ux-pro-max ux-review` — análise de UX com recomendações acionáveis
- `/ui-ux-pro-max component <nome>` — criar componente de nível produção
- `/ui-ux-pro-max motion` — adicionar micro-interações e animações
- `/ui-ux-pro-max audit` — auditoria visual + acessibilidade + performance
- `/ui-ux-pro-max critique` — feedback estruturado sobre UI existente
- `/ui-ux-pro-max figma-to-code` — converter design Figma em código

---

## Processo de execução

### 0. Diagnóstico inicial

Antes de qualquer entrega, responder:
1. Qual é o objetivo de negócio desta tela/componente?
2. Quem é o utilizador? (persona, contexto de uso, dispositivos)
3. Qual stack está em uso? (framework, CSS approach, UI lib)
4. Existe design system ou tokens definidos?
5. Existe Figma ou referência visual?

Se não houver resposta clara, usar `AskUserQuestion` — máximo 3 perguntas de uma vez.

---

## Pilares de qualidade

### 1. Hierarquia visual (Visual Hierarchy)

- **Um único ponto focal** por tela — o olho do utilizador deve saber onde ir primeiro
- Escala tipográfica: `12 → 14 → 16 → 20 → 24 → 32 → 48 → 64` (nunca valores arbitrários)
- Peso para ênfase: `regular (400) → medium (500) → semibold (600) → bold (700)`
- Contraste mínimo WCAG AA: 4.5:1 texto normal, 3:1 texto grande e ícones
- Contraste WCAG AAA preferível: 7:1 para texto de leitura crítica

### 2. Espaçamento e layout

- Sistema de 4px: `4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96`
- Nunca usar valores arbitrários como `margin: 13px` ou `padding: 7px`
- Whitespace generoso = percepção de qualidade
- Container max-width: `640px` (mobile), `768px` (tablet), `1024px` (desktop), `1280px` (wide)
- Breakpoints: `sm: 640px | md: 768px | lg: 1024px | xl: 1280px | 2xl: 1536px`

### 3. Cores e tokens

```
Sistema de tokens obrigatório:
--color-brand-50  ... --color-brand-950  (escala completa)
--color-neutral-50 ... --color-neutral-950
--color-success, --color-warning, --color-error, --color-info
--color-surface-primary, --color-surface-secondary, --color-surface-elevated
--color-text-primary, --color-text-secondary, --color-text-disabled
--color-border, --color-border-strong

Regras:
- Nunca preto puro (#000) — usar #0A0A0A ou similar
- Nunca branco puro (#FFF) — usar #FAFAFA ou #F8F9FA
- Dark mode: inverter a escala, não apenas "escurecer"
- Cores semânticas sempre com tokens (nunca hardcoded)
```

### 4. Tipografia

- Máximo 2 famílias: 1 display/heading + 1 corpo
- Fontes recomendadas: Inter, Geist, Plus Jakarta Sans, DM Sans, Outfit
- `line-height`: 1.2 títulos, 1.5 corpo, 1.7 texto longo
- `letter-spacing`: `-0.02em` a `-0.05em` em headings grandes
- `max-width` em parágrafos: `65ch` (nunca texto full-width em desktop)

### 5. Componentes e estados

Todo componente precisa cobrir **todos** os estados:
```
default → hover → focus → active → disabled → loading → error → success → empty
```

Padrões de componente de alto nível:
- Botões: variantes (primary, secondary, ghost, destructive) × tamanhos (sm, md, lg)
- Inputs: label flutuante ou fixa, helper text, erro inline, ícone leading/trailing
- Cards: header, body, footer — com skeleton loading state
- Modals: trap de foco, dismiss com Esc, backdrop com blur suave
- Toasts: stack automático, auto-dismiss configurável, ação inline

### 6. Acessibilidade (A11y)

**Obrigatório em todo componente:**
- `aria-label` ou `aria-labelledby` em todos os elementos interativos sem texto visível
- `role` semântico correto (não `div` clicável, usar `button`)
- Navegação por teclado funcional: Tab, Shift+Tab, Enter, Space, Esc, setas
- Focus visible: nunca `outline: none` sem substituto visível
- `aria-live` em regiões dinâmicas (notificações, erros, loading)
- Alternativa textual em imagens e ícones
- Form labels associados por `htmlFor`/`id`
- Erro de formulário associado via `aria-describedby`

### 7. Motion e micro-interações

**Filosofia:** movimento serve a intenção, não a estética.

```css
/* Durações por tipo */
--duration-instant:    50ms;   /* hover, focus ring */
--duration-fast:      150ms;   /* toggle, checkbox */
--duration-normal:    250ms;   /* dropdown, tooltip */
--duration-slow:      400ms;   /* modal, sheet, page */
--duration-deliberate: 600ms;  /* onboarding, celebração */

/* Easing */
--ease-out: cubic-bezier(0, 0, 0.2, 1);    /* elementos entrando */
--ease-in:  cubic-bezier(0.4, 0, 1, 1);    /* elementos saindo */
--ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1); /* bounce sutil */
```

Respeitar `prefers-reduced-motion`:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

Framer Motion patterns preferidos:
```tsx
// Entrada suave
{ initial: { opacity: 0, y: 8 }, animate: { opacity: 1, y: 0 }, transition: { duration: 0.25 } }

// Exit com layout shift mínimo
<AnimatePresence mode="wait">
  <motion.div key={id} exit={{ opacity: 0, scale: 0.95 }} />
</AnimatePresence>
```

---

## Stack tecnológica padrão

| Camada | Escolha recomendada | Alternativa |
|--------|--------------------|-----------:|
| Framework | Next.js 15 (App Router) | Remix, Astro |
| Styling | Tailwind CSS v4 | CSS Modules |
| Componentes base | shadcn/ui + Radix UI | Headless UI |
| Ícones | Lucide React | Phosphor Icons |
| Motion | Framer Motion | Motion One |
| Forms | React Hook Form + Zod | Conform |
| Tabelas | TanStack Table | — |
| Gráficos | Recharts | Tremor |
| Datas | date-fns | dayjs |

---

## UX Review — framework de análise

Ao fazer `/ui-ux-pro-max ux-review`, avaliar cada dimensão com nota 1-4:

| Dimensão | 1 (Crítico) | 2 (Fraco) | 3 (Bom) | 4 (Excelente) |
|----------|------------|----------|---------|--------------|
| **Hierarquia visual** | Sem foco claro | Hierarquia confusa | Hierarquia funcional | Guia intuitivamente |
| **Consistência** | Caótico | Padrões inconsistentes | Maioria consistente | Sistema coerente |
| **Feedback** | Nenhum | Inconsistente | Feedback básico | Rico e contextual |
| **Acessibilidade** | Falha crítica | WCAG A incompleto | WCAG AA | WCAG AAA |
| **Responsividade** | Quebra em mobile | Adaptação básica | Mobile-first | Adaptativo fluido |
| **Performance percebida** | Bloqueante | Lento | Aceitável | Imediato |

Saída obrigatória do review:
```markdown
## UI/UX Review — [Nome da tela/componente]

### Pontuação geral: X/24

| Dimensão | Nota | Evidência |
|----------|------|-----------|
...

### Top 3 problemas críticos
1. [problema] → [impacto] → [solução específica]

### Quick wins (< 1h de implementação)
- ...

### Melhorias estratégicas
- ...

### Código de referência para os fixes
```[código]```
```

---

## Design System — estrutura completa

Ao criar ou auditar um design system, entregar:

```
design-system/
├── tokens/
│   ├── colors.css       # variáveis CSS de cor
│   ├── typography.css   # escala tipográfica
│   ├── spacing.css      # escala de espaço
│   ├── shadows.css      # sistema de sombras
│   ├── radius.css       # border-radius tokens
│   └── animation.css    # timing e easing
├── components/
│   ├── Button/
│   ├── Input/
│   ├── Card/
│   ├── Modal/
│   ├── Toast/
│   └── ...
├── layouts/
│   ├── Container.tsx
│   ├── Grid.tsx
│   └── Stack.tsx
└── docs/
    └── DESIGN-SYSTEM.md
```

Sombras por nível de elevação:
```css
--shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.05);
--shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
--shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
--shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
--shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
```

---

## Critique estruturado

Ao fazer critique de UI, estruturar assim:

### O que está funcionando (manter)
- [aspecto positivo + porquê funciona]

### O que está fraco (melhorar)
- [problema] → [impacto no utilizador] → [sugestão concreta]

### O que está errado (corrigir urgente)
- [problema crítico] → [como corrigir]

### Referências visuais
- [inspirações ou patterns de referência relevantes]

---

## Figma-to-Code workflow

1. Receber link ou contexto do Figma
2. Usar `mcp__claude_ai_Figma__get_design_context` para extrair tokens e componentes
3. Usar `mcp__claude_ai_Figma__get_screenshot` para referência visual
4. Mapear tokens Figma → tokens CSS/Tailwind
5. Implementar componente respeitando espaçamento pixel-perfect
6. Verificar responsividade nos breakpoints
7. Adicionar estados faltantes (hover, focus, etc.)
8. Testar acessibilidade com keyboard navigation

---

## Output esperado (padrão de entrega)

Todo componente entregue deve incluir:

```tsx
// 1. Tipos TypeScript completos
interface ComponentProps {
  variant: 'primary' | 'secondary' | 'ghost'
  size?: 'sm' | 'md' | 'lg'
  disabled?: boolean
  loading?: boolean
  children: React.ReactNode
}

// 2. Componente com variantes por cva() ou clsx()
// 3. Estados: default, hover, focus, active, disabled, loading
// 4. aria-* attributes corretos
// 5. Animações com Framer Motion ou CSS transitions
// 6. Dark mode com Tailwind dark:
// 7. Responsivo mobile-first
```

---

## Anti-patterns — nunca fazer

- `div` clicável sem `role="button"` e `tabIndex={0}`
- `outline: none` sem focus ring alternativo visível
- Cores hardcoded no JSX (usar tokens/variáveis)
- `!important` em CSS (sinal de problema arquitetural)
- Animações sem `prefers-reduced-motion`
- Texto sobre imagem sem overlay de contraste verificado
- Placeholder como substituto de label
- Múltiplos H1 numa mesma página
- `z-index` arbitrários sem sistema (usar escala: 0, 10, 20, 30, 40, 50)
- Mobile como afterthought — sempre mobile-first

---

## Referências e padrões de nível mundial

- **Design systems de referência:** Vercel (Geist), Linear, Stripe, Notion, Radix
- **Padrão de qualidade:** "Parece que saiu de uma empresa de produto de SF"
- **Critério de aprovação:** O utilizador sabe o que fazer sem precisar ler
