---
name: ai-research-schema
domain: AI/ML Research & Trends
version: 1.0.0
---

# Wiki Schema: AI Research



**Source**: [GitHub Wiki](https://github.com/flybfree/AI-Wiki/wiki)

## Storage Model
- **Canonical user-facing wiki**: GitHub wiki / local wiki working copy at `/home/rich/wiki/ai-research/`
- **Assistant-facing graph mirror**: `/home/rich/logseq-brain/pages/ai-research/` (curated mirror; not a full raw-source dump)
- **PRISM fast-access mirror**: `192.168.3.89/logseq-brain`
- **PRISM wiki mirror**: disabled in the active setup to avoid Logseq collisions
- **Raw source layer**: `raw/articles/`, `raw/papers/`, `raw/summaries/`
- **Curated knowledge layer**: `concepts/`, `entities/article/`, `comparisons/`
- **Navigation layer**: `index.md`, `wiki-topic-index.md`, `wiki-landing-page.md`
- **Operational layer**: `log.md`, `processed_files.log`, `summarized_files.log`, `analyzed_files.log`
## Conventions
- File names: lowercase, hyphens (e.g., `gpt-4o.md`)
- Every page starts with YAML frontmatter
- Use `[[wikilinks]]` for all connections
- Every action must be logged in `log.md`

## Tag Taxonomy
- **Models**: `model`, `architecture`, `benchmark`, `training`
- **Entities**: `company`, `lab`, `person`, `org`
- **Techniques**: `optimization`, `fine-tuning`, `inference`, `alignment`, `multimodal`
- **Meta**: `trend`, `breakthrough`, `controversy`, `paper-summary`

## Page Thresholds
- Create a page only when the source has a material AI/ML connection.
- Acceptable signals include: model releases, research papers, benchmarks, AI products/features, AI infrastructure, safety/governance, policy, or an AI company/lab/person as the primary subject.
- Do not create pages for generic tech, business, aviation, finance, or lifestyle stories unless AI is the main subject or causal factor in the article.
- Do not add "AI-adjacent" framing after the fact just to justify inclusion.
- Update existing pages with new findings.
- Do not create pages for passing mentions.

## Mirror policy
- Mirror the curated layer into Logseq by default.
- Keep raw source captures in the wiki for provenance and auditability.
- Do not mirror raw article/paper bodies into Logseq unless they provide distinct value beyond the summary page.
- Prefer one Logseq node per curated article summary, with a visible link back to the original source.
