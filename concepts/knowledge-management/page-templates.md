---
title: "Page Templates for the AI Research Wiki"
created: 2026-07-14
updated: 2026-07-14
type: concept
tags: [wiki, logseq, templates, knowledge-management, navigation]
sources: ["https://github.com/flybfree/AI-Wiki/wiki"]
confidence: high
---

# Page Templates for the AI Research Wiki

**Source**: [GitHub Wiki](https://github.com/flybfree/AI-Wiki/wiki)

Use these copy-paste templates when creating or refreshing wiki pages.
They are optimized for:
- fast retrieval by Hermes
- readable reference pages for Rich
- stable syncing into Logseq
- visible source links in rendered content

## General rules

- Keep the top of the page useful within 10 seconds
- Put the visible source link in the body, not only in frontmatter
- Define acronyms on first use
- Include concrete examples for key concepts
- Prefer one canonical page per idea
- Keep navigation pages short and curated

---

## 1) Concept page template

Use for durable ideas, frameworks, systems, and recurring themes.

```markdown
---
title: "<Concept Name>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
tags: [<topic>, <subtopic>, <optional-tags>]
sources: ["<source-url>"]
confidence: high
---

# <Concept Name>

**Source**: [Original Article](<source-url>)

## What it is
One short paragraph that defines the concept in plain English.

## Why it matters
Why this concept is useful, important, or worth tracking.

## Key ideas
- <idea 1>
- <idea 2>
- <idea 3>

## Example
A concrete example or scenario.

## Tradeoffs / caveats
- <tradeoff 1>
- <tradeoff 2>

## Related pages
- [[<related-page-1>]]
- [[<related-page-2>]]
```

## 2) Article summary template

Use for news articles, blog posts, and practical explainers.

```markdown
---
title: "Summary: <Article Title>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: article-summary
tags: [article, <topic>, <source>]
sources: ["<source-url>"]
confidence: high
---

# Summary: <Article Title>

**Source**: [Original Article](<source-url>)

## Summary
Short overview of the article in 2–4 sentences.

## Key takeaways
- <takeaway 1>
- <takeaway 2>
- <takeaway 3>

## Notable details
- <important fact or quote>
- <important fact or quote>

## Why this matters
Why the article matters to the reader or the research area.

## Related pages
- [[<concept-page>]]
- [[<topic-hub>]]
```

## 3) Paper summary template

Use for academic papers and technical reports.

```markdown
---
title: "Summary: <Paper Title>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: paper-summary
tags: [paper, <topic>, <method>]
sources: ["<paper-url>"]
confidence: medium
---

# Summary: <Paper Title>

**Source**: [Original Paper](<paper-url>)

## Summary
Short plain-English summary of the paper.

## Problem
What problem the paper is solving.

## Method
The core technique or approach.

## Results
The main result, benchmark, or finding.

## Limitations
- <limitation 1>
- <limitation 2>

## Why it matters
Why the paper is interesting or important.

## Related pages
- [[<concept-page>]]
- [[<comparison-page>]]
- [[<topic-hub>]]
```

## 4) Tracker page template

Use for fast-moving topics where you want the current state plus history.

```markdown
---
title: "<Tracker Name>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: tracker
tags: [tracker, <topic>, living-page]
sources: ["<source-url-or-list>"]
confidence: high
---

# <Tracker Name>

**Source**: [Primary Source](<source-url>)

## Current snapshot
Short current-state summary.

## What changed recently
- <recent change 1>
- <recent change 2>

## Chronological log
### YYYY-MM-DD
- <dated update>

### YYYY-MM-DD
- <dated update>

## Related pages
- [[<hub-page>]]
- [[<comparison-page>]]
```

## 5) Topic hub template

Use for navigation pages that organize a cluster of related pages.

```markdown
---
title: "<Topic Hub Name>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: hub
tags: [hub, navigation, <topic>]
sources: ["https://github.com/flybfree/AI-Wiki/wiki"]
confidence: high
---

# <Topic Hub Name>

**Source**: [GitHub Wiki](https://github.com/flybfree/AI-Wiki/wiki)

## Start here
- [[<core-page-1>]]
- [[<core-page-2>]]

## Key pages
- [[<page-1>]]
- [[<page-2>]]
- [[<page-3>]]

## Related topics
- [[<related-hub-1>]]
- [[<related-hub-2>]]
```

## 6) Review checklist

Before saving a page, check:

- [ ] Title is unique and descriptive
- [ ] Frontmatter values with special characters are quoted
- [ ] Visible source link exists in the body
- [ ] First-use acronyms are defined
- [ ] At least one concrete example is included
- [ ] Page is linked from an index or hub if it matters
- [ ] Page type is correct
- [ ] Updated date is current

## Suggested usage

- **Concept pages** for durable understanding
- **Article summaries** for current web sources
- **Paper summaries** for research findings
- **Tracker pages** for living topics
- **Hub pages** for navigation and discovery

## Related pages

- [[concepts/knowledge-management/logseq-brain-wiki-operating-model.md|Logseq Brain & Wiki Operating Model]]
- [[SCHEMA.md|Wiki Schema: AI Research]]
- [[wiki-landing-page.md|AI Research Wiki — Landing Page]]
- [[wiki-topic-index.md|AI Research Wiki — Topic Index]]
