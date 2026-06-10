#!/usr/bin/env python3
"""
sync.py — Gera páginas do UP Manual a partir das sources reais:
  - ~/.claude/skills/*/SKILL.md
  - ~/squads/*/squad.yaml (ou squad.json)
  - Conteúdo manual para GHL, GSD, referências
"""

import os
import re
import json
import yaml
from pathlib import Path

SKILLS_DIR = Path.home() / ".claude" / "skills"
SQUADS_DIR = Path.home() / "squads"
DOCS_DIR = Path(__file__).parent.parent / "src" / "content" / "docs"

# Mapeamento skill_name -> categoria
SKILL_CATEGORIES = {
    "gsd": "gsd",
    "upscale": "upscale",
    "ghl": "upscale",
    # marketing
    "designer": "marketing",
    "instagram": "marketing",
    "blotato": "marketing",
    "canva": "marketing",
    "brand": "marketing",
    "content": "marketing",
    "copy": "marketing",
    "rafa": "marketing",
    "traffic": "marketing",
    "campanhas": "marketing",
    "storytelling": "marketing",
    "movement": "marketing",
    "carrossel": "marketing",
    "roteiro": "marketing",
    "link-in-bio": "marketing",
    "hooks": "marketing",
    "workflow-producao": "marketing",
    # dev
    "frontend": "dev",
    "test": "dev",
    "tdd": "dev",
    "scalability": "dev",
    "security": "dev",
    "cybersecurity": "dev",
    "n8n": "dev",
    "trigger": "dev",
    "apify": "dev",
    "self-healing": "dev",
    "systematic": "dev",
    "subagent": "dev",
    "epic": "dev",
    "cost": "dev",
    "setup": "dev",
    "git": "dev",
    "scaffold": "dev",
    "migrate": "dev",
    # tools
    "image": "tools",
    "know-me": "tools",
    "researcher": "tools",
    "deep-research": "tools",
    "skillshare": "tools",
    "find-skills": "tools",
    "karpathy": "tools",
    "using": "tools",
    "dispatching": "tools",
    "executing": "tools",
    "finishing": "tools",
    "receiving": "tools",
    "requesting": "tools",
    "verification": "tools",
    "writing": "tools",
    "brainstorming": "tools",
    "caveman": "tools",
    "grill": "tools",
    "handoff": "tools",
    "teach": "tools",
    "diagnose": "tools",
    "prototype": "tools",
    "triage": "tools",
    "zoom-out": "tools",
    "to-issues": "tools",
    "to-prd": "tools",
    "improve-codebase": "tools",
    "write-a-skill": "tools",
    "customer": "tools",
    "opensquad": "tools",
    "squad": "tools",
    "c-level": "tools",
    "advisory": "tools",
    "hormozi": "tools",
    "up-agency": "tools",
    "data-squad": "tools",
    "design-squad": "tools",
    "copy-squad": "tools",
    "copy-master": "tools",
    "onboard": "tools",
    "analise": "marketing",
    "dashboard": "tools",
    "cortes": "marketing",
}

def get_category(skill_name):
    name_lower = skill_name.lower()
    if name_lower.startswith("gsd-"):
        return "gsd"
    if name_lower.startswith("upscale-"):
        return "upscale"
    for prefix, cat in SKILL_CATEGORIES.items():
        if name_lower.startswith(prefix):
            return cat
    return "tools"

def parse_skill_md(path):
    """Extrai frontmatter e conteúdo de SKILL.md"""
    text = path.read_text(errors="replace")

    # Tentar extrair frontmatter YAML
    fm = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
            except Exception:
                pass

    # Extrair título do markdown se não há frontmatter
    title = fm.get("name") or fm.get("title") or ""
    if not title:
        m = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
        if m:
            title = m.group(1).strip()
    if not title:
        title = path.parent.name.replace("-", " ").title()

    # Extrair descrição
    description = fm.get("description") or ""
    if not description:
        lines = [l.strip() for l in body.split("\n") if l.strip() and not l.startswith("#")]
        if lines:
            description = lines[0][:200]

    return title, description, body

def slugify(name):
    return re.sub(r'[^a-z0-9-]', '-', name.lower()).strip('-')

def safe_yaml_str(s):
    """Escapa string para uso seguro em frontmatter YAML"""
    if not s:
        return '""'
    # Remover newlines e truncar
    s = s.replace('\n', ' ').replace('\r', '').strip()[:200]
    # Se contém caracteres especiais YAML, usar aspas
    if any(c in s for c in [':', '#', '{', '}', '[', ']', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', '"', "'"]):
        s = s.replace('"', "'")
        return f'"{s}"'
    return s or '""'

def generate_skills():
    print("Gerando skills...")

    all_skills = []

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_name = skill_dir.name
        skill_md = skill_dir / "SKILL.md"

        if not skill_md.exists():
            continue

        category = get_category(skill_name)
        title, description, body = parse_skill_md(skill_md)

        # Gerar página da skill
        out_dir = DOCS_DIR / "skills" / category
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{skill_name}.md"

        safe_title = safe_yaml_str(title)
        safe_desc = safe_yaml_str(description[:150] if description else f"Skill {skill_name}")
        content = f"""---
title: {safe_title}
description: {safe_desc}
---

{body}
"""
        out_path.write_text(content)
        all_skills.append((skill_name, category, title, description))

    print(f"  {len(all_skills)} skills geradas")
    return all_skills

def generate_skills_index(all_skills):
    """Gera página de catálogo com todas as skills"""
    categories = {}
    for name, cat, title, desc in all_skills:
        categories.setdefault(cat, []).append((name, title, desc))

    cat_labels = {
        "gsd": "GSD — Metodologia",
        "upscale": "Upscale & GHL",
        "marketing": "Marketing & Conteúdo",
        "dev": "Desenvolvimento",
        "tools": "Ferramentas & Workflow",
    }

    lines = ["""---
title: Catálogo de Skills
description: Todas as skills disponíveis no Claude Code — 144+ comandos organizados por categoria.
---

import { CardGrid, Card } from '@astrojs/starlight/components';

"""]

    for cat_key in ["gsd", "upscale", "marketing", "dev", "tools"]:
        skills_in_cat = categories.get(cat_key, [])
        if not skills_in_cat:
            continue
        label = cat_labels.get(cat_key, cat_key)
        lines.append(f"\n## {label} ({len(skills_in_cat)})\n")
        lines.append("\n| Skill | Descrição |\n|-------|----------|\n")
        for name, title, desc in sorted(skills_in_cat, key=lambda x: x[0]):
            short_desc = (desc or "")[:100].replace("|", "–")
            lines.append(f"| [`/{name}`](/skills/{cat_key}/{name}) | {short_desc} |\n")

    out = DOCS_DIR / "skills" / "index.mdx"
    out.write_text("".join(lines))
    print(f"  Índice de skills gerado")

def generate_squads():
    print("Gerando squads...")
    if not SQUADS_DIR.exists():
        print("  ~/squads/ não encontrado")
        return

    all_squads = []

    for squad_dir in sorted(SQUADS_DIR.iterdir()):
        if not squad_dir.is_dir():
            continue

        squad_name = squad_dir.name

        # Tentar ler squad.yaml ou squad.json
        config = {}
        for fname in ["squad.yaml", "squad.yml", "squad.json"]:
            fpath = squad_dir / fname
            if fpath.exists():
                try:
                    text = fpath.read_text(errors="replace")
                    if fname.endswith(".json"):
                        config = json.loads(text)
                    else:
                        config = yaml.safe_load(text) or {}
                    break
                except Exception:
                    pass

        # README ou descrição
        readme = ""
        for fname in ["README.md", "readme.md", "DESCRIPTION.md"]:
            rpath = squad_dir / fname
            if rpath.exists():
                readme = rpath.read_text(errors="replace")
                break

        title = config.get("name") or config.get("title") or squad_name.replace("-", " ").title()
        description = config.get("description") or ""
        agents = config.get("agents", [])

        # Gerar página
        out_dir = DOCS_DIR / "squads" / "catalog"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{squad_name}.md"

        agents_section = ""
        if agents:
            if isinstance(agents, list):
                agent_list = "\n".join(f"- {a.get('name', a) if isinstance(a, dict) else a}" for a in agents)
                agents_section = f"\n## Agentes\n\n{agent_list}\n"

        safe_title = safe_yaml_str(title)
        safe_desc = safe_yaml_str(description[:150] if description else f"Squad {squad_name}")
        content = f"""---
title: {safe_title}
description: {safe_desc}
---

{f"> {description}" if description else ""}

{agents_section}

{readme if readme else ""}
""".strip() + "\n"

        out_path.write_text(content)
        all_squads.append((squad_name, title, description, len(agents) if isinstance(agents, list) else 0))

    print(f"  {len(all_squads)} squads gerados")
    return all_squads

def generate_squads_index(all_squads):
    lines = ["""---
title: Squads
description: Todos os squads disponíveis no Opensquad — equipas de agentes especializados.
---

"""]

    lines.append("| Squad | Comando | Agentes | Descrição |\n")
    lines.append("|-------|---------|---------|----------|\n")
    for name, title, desc, n_agents in sorted(all_squads or [], key=lambda x: x[0]):
        short_desc = (desc or "")[:80].replace("|", "–")
        agents_str = str(n_agents) if n_agents else "—"
        lines.append(f"| [{title}](/squads/catalog/{name}) | `/{name}` | {agents_str} | {short_desc} |\n")

    out = DOCS_DIR / "squads" / "index.md"
    out.write_text("".join(lines))

def generate_ghl_docs():
    print("Gerando docs GHL...")

    pages = {
        "index.md": {
            "title": "GHL & Upscale",
            "description": "Ecossistema GoHighLevel da UP Marketing — automações, bots, CRM e gestão de leads.",
            "body": """
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
"""
        },
        "locations.md": {
            "title": "Locations & Tokens",
            "description": "Mapa de locations GHL e tokens PIT activos.",
            "body": """
:::caution[Segurança]
Esta página não contém os tokens reais. Os tokens PIT estão em `Obsidian/_ctx/ghl.md` e na memória do Claude.
:::

## Locations activas

| Location | Location ID | Uso |
|----------|------------|-----|
| UP Marketing — Comercial | `JsLAteS4y7Ptxxj0rJ8n` | Leads, pipeline comercial |
| UP Marketing — Criação | `JsLAteS4y7Ptxxj0rJ8n` | Conteúdo, gestão criativa |
| Bellator Hospedagem | `1mFej8GZat3TDYde7B86` | Cliente Bellator |
| Firmino Assessoria | `0YLJzXsqFPY8CbWw7Iif` | Cliente Firmino |
| Sarah Kelly | `ybAbNQBZrx0zfWWbboG5` | Cliente Sarah Kelly |
| Paulo Tavares Dantas | `oRIAZAp6reaywd9Lvf6B` | Cliente PTD |

## Renovar token expirado

1. Entrar no GHL da location
2. Settings → API Keys → Personal Integration Token
3. Gerar novo token
4. Actualizar em `Obsidian/_ctx/ghl.md`
5. Informar Claude Code do novo token
"""
        },
        "automacoes.md": {
            "title": "Automações — Guia Rápido",
            "description": "Como montar e publicar automações no GoHighLevel.",
            "body": """
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
"""
        },
        "bot-builder.md": {
            "title": "Bot Builder",
            "description": "Criar e configurar bots Conversation AI no GoHighLevel.",
            "body": """
## Skill `/upscale-bot-builder`

Cria e configura bots Conversation AI completos no GHL via API + UI quando necessário.

### O que configura

- Persona do bot (nome, tom, instruções)
- Knowledge Base (KB) com documentos da empresa
- Flow Builder — fluxos condicionais
- Modo Suggestive vs Auto-Pilot
- Handoff para humano
- Calendário para agendamento automático

### Fluxo padrão

```
1. Definir persona e objectivo
2. Criar bot via API
3. Adicionar KB (Playwright — UI only)
4. Configurar Flow Builder (Playwright)
5. Testar no WhatsApp/SMS
6. Activar Auto-Pilot
```

### Pricing (snapshot Upscale)

| Plano | Bot | KB | Conversas/mês |
|-------|-----|----|---------------|
| Starter | 1 | 1 | 500 |
| Growth | 3 | 5 | 2.000 |
| Pro | Ilimitado | Ilimitado | Ilimitado |
"""
        },
    }

    ghl_dir = DOCS_DIR / "ghl"
    ghl_dir.mkdir(parents=True, exist_ok=True)

    for fname, data in pages.items():
        content = f"""---
title: {data['title']}
description: {data['description']}
---

{data['body'].strip()}
"""
        (ghl_dir / fname).write_text(content)

    print(f"  {len(pages)} páginas GHL geradas")

def generate_gsd_docs():
    print("Gerando docs GSD...")

    gsd_dir = DOCS_DIR / "gsd"
    gsd_dir.mkdir(parents=True, exist_ok=True)

    pages = {
        "index.md": {
            "title": "GSD — Git. Ship. Done.",
            "description": "Metodologia de desenvolvimento GSD — da ideia ao deploy com agentes e planos estruturados.",
            "body": """
## O que é o GSD

GSD (Git. Ship. Done.) é a metodologia de desenvolvimento usada na UP. Estrutura o trabalho em fases, planos e execução assistida por agentes.

## Ciclo de vida de um projecto

```
/gsd-new-project → Roadmap + fases
/gsd-plan-phase  → PLAN.md para cada fase
/gsd-execute-phase → Execução com commits atómicos
/gsd-verify-work → Verificação do que foi feito
/gsd-ship        → Deploy final
```

## Skills GSD principais

| Skill | Função |
|-------|--------|
| `/gsd-new-project` | Criar roadmap completo de projecto |
| `/gsd-new-milestone` | Adicionar milestone a projecto existente |
| `/gsd-plan-phase` | Planejar fase com PLAN.md detalhado |
| `/gsd-execute-phase` | Executar plano com agentes paralelos |
| `/gsd-verify-work` | Verificar resultado da fase |
| `/gsd-debug` | Debug científico com checkpoints |
| `/gsd-review` | Code review estruturado |
| `/gsd-ship` | Deploy e entrega |
| `/gsd-pause-work` | Pausa com handoff de contexto |
| `/gsd-resume-work` | Retomar trabalho com contexto restaurado |

## Estrutura de ficheiros GSD

```
.planning/
├── ROADMAP.md          # Visão geral e fases
├── phases/
│   └── 01-nome-fase/
│       ├── PLAN.md     # Plano detalhado
│       └── VERIFY.md   # Resultado verificado
```
"""
        },
        "fases.md": {
            "title": "Fases e Planos",
            "description": "Como usar as skills de planeamento e execução de fases GSD.",
            "body": """
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
"""
        },
    }

    for fname, data in pages.items():
        content = f"""---
title: {data['title']}
description: {data['description']}
---

{data['body'].strip()}
"""
        (gsd_dir / fname).write_text(content)

    print(f"  {len(pages)} páginas GSD geradas")

def generate_home():
    content = """---
title: UP Manual
description: Manual operacional da UP Marketing & Comunicação — skills, squads, workflows e sistemas.
template: splash
hero:
  tagline: Base de conhecimento operacional da UP Marketing — skills, squads, automações e metodologia.
  actions:
    - text: Ver Skills
      link: /skills/index
      icon: right-arrow
      variant: primary
    - text: Ver Squads
      link: /squads/index
      icon: right-arrow
---

import { CardGrid, Card } from '@astrojs/starlight/components';

## O que está aqui

<CardGrid>
  <Card title="144+ Skills" icon="puzzle">
    Todos os comandos `/skill` disponíveis no Claude Code, organizados por categoria.
  </Card>
  <Card title="Squads" icon="group">
    Equipas de agentes Opensquad — do copy à análise de dados.
  </Card>
  <Card title="GHL & Upscale" icon="setting">
    Automações GoHighLevel, bots, tokens e fluxos de leads.
  </Card>
  <Card title="GSD Metodologia" icon="rocket">
    Git. Ship. Done. — framework de desenvolvimento com agentes.
  </Card>
</CardGrid>
"""
    (DOCS_DIR / "index.mdx").write_text(content)
    print("  Home gerada")

def generate_reference():
    ref_dir = DOCS_DIR / "reference"
    ref_dir.mkdir(parents=True, exist_ok=True)

    content = """---
title: Stack Técnica
description: Stack e ferramentas da UP Marketing.
---

## Desenvolvimento

| Ferramenta | Uso |
|-----------|-----|
| Next.js | Frontend / Full-stack |
| Supabase | Base de dados + Auth |
| Tailwind CSS | Estilos |
| TypeScript | Linguagem |
| Vercel | Deploy |

## Agentes & IA

| Ferramenta | Uso |
|-----------|-----|
| Claude Code | Desenvolvimento assistido |
| Opensquad | Orquestração de squads |
| GSD | Metodologia de projecto |
| GoHighLevel | CRM + Automação |

## MCPs activos

- Supabase
- Vercel
- Playwright (Opensquad)
- Hostinger
- Gmail / Google Calendar / Google Drive
- Notion
- Meta Ads
- Figma
- Canva

## Integrações

| Sistema | Propósito |
|---------|-----------|
| GoHighLevel | CRM, automações, bots |
| Google Workspace | Email, Calendar, Drive |
| Meta Ads | Campanhas Facebook/Instagram |
| Obsidian | Vault de conhecimento |
"""
    (ref_dir / "stack.md").write_text(content)
    print("  Referências geradas")

if __name__ == "__main__":
    print("=== Sync UP Manual ===\n")

    try:
        import yaml
    except ImportError:
        print("Instalar PyYAML: pip install pyyaml")
        import sys; sys.exit(1)

    generate_home()
    all_skills = generate_skills()
    generate_skills_index(all_skills)
    all_squads = generate_squads()
    generate_squads_index(all_squads)
    generate_ghl_docs()
    generate_gsd_docs()
    generate_reference()

    print(f"\n=== Concluído ===")
    print(f"Skills: {len(all_skills)}")
    print(f"Squads: {len(all_squads) if all_squads else 0}")
    print("\nCorrer: cd ~/up-manual && npm run build")
