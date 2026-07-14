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

## Opinionated defaults

Use these defaults unless a page has a strong reason to differ:

- **Concept pages** should be learning-first and explanation-heavy
- **Article and paper summaries** should be retrieval-first and concise
- **Tracker pages** should surface current state before history
- **Hub pages** should be navigation-only, not explanatory essays
- **Summary pages** should always use `Summary:` in both frontmatter title and H1
- **All pages** should prefer explicit, clickable source links in the rendered body

## 0) Learning-first concept page template

Use this when the goal is understanding, teaching, or building intuition.

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

## In one sentence
Plain-English definition.

## What it is
Explain the idea carefully but without jargon.

## Why it matters
Explain the practical importance.

## Key terms
- **Term 1**: definition
- **Term 2**: definition

## Example
Concrete example or scenario.

## Common misconceptions
- <misconception 1>
- <misconception 2>

## Related pages
- [[<related-page-1>]]
- [[<related-page-2>]]
```

## 0b) Assistant-optimized retrieval concept template

Use this when the page should answer questions quickly for Hermes.

```markdown
---
title: "<Concept Name>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
tags: [<topic>, <subtopic>, retrieval]
sources: ["<source-url>"]
confidence: high
---

# <Concept Name>

**Source**: [Original Article](<source-url>)

## Short answer
One to three sentences that directly answer “what is this?”

## Key facts
- <fact 1>
- <fact 2>
- <fact 3>

## When to use it
- <use case 1>
- <use case 2>

## When not to use it
- <non-use case 1>
- <non-use case 2>

## Related pages
- [[<related-page-1>]]
- [[<related-page-2>]]
```

## 1) Article summary template

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

## 2) Paper summary template

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

## 3) Tracker page template

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

## 4) Topic hub template

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

## 5) Logseq-safe summary template

Use this for any summary page that must not collide with the source title in Logseq.

```markdown
---
title: "Summary: <Source Title>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: summary
tags: [summary, <topic>, <source>]
sources: ["<source-url>"]
confidence: high
---

# Summary: <Source Title>

**Source**: [Original Article](<source-url>)

## Summary
Short overview in plain English.

## Key takeaways
- <takeaway 1>
- <takeaway 2>

## Why it matters
Short explanation of significance.

## Related pages
- [[<concept-page>]]
- [[<topic-hub>]]
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

- **Learning-first concept pages** for teaching and intuition
- **Assistant-optimized concept pages** for fast question answering
- **Article summaries** for current web sources
- **Paper summaries** for research findings
- **Tracker pages** for living topics
- **Hub pages** for navigation and discovery
- **Logseq-safe summaries** for avoiding title collisions

## Related pages

- [[concepts/knowledge-management/logseq-brain-wiki-operating-model.md|Logseq Brain & Wiki Operating Model]]
- [[SCHEMA.md|Wiki Schema: AI Research]]
- [[wiki-landing-page.md|AI Research Wiki — Landing Page]]
- [[wiki-topic-index.md|AI Research Wiki — Topic Index]]
