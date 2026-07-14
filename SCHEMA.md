---
name: ai-research-schema
domain: AI/ML Research & Trends
version: 1.0.0
---

# Wiki Schema: AI Research



**Source**: [GitHub Wiki](https://github.com/flybfree/AI-Wiki/wiki)

## Storage Model

- **Canonical user-facing wiki**: GitHub wiki / local clone at `/home/rich/wiki/ai-research/`
- **Assistant-facing mirror**: `/home/rich/logseq-brain/pages/ai-research/`
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
- Create a page if an entity/concept is central to a new source.
- Update existing pages with new findings.
- Do not create pages for passing mentions.
