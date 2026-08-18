---
title: Writing Style Similarity Reflects Academic Genealogy
url: http://arxiv.org/abs/2608.14843v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_19-35-39Z_WritingStyleSimilarityReflectsAcademicGenealogy.md
generated_at: 2026-08-17 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how the similarity of authorship styles in arXiv papers mirrors the genealogical relationships defined by the Mathematics Genealogy Project. It finds that advisors and academic siblings are significantly more stylistically similar than random peers, causing attribution systems to misclassify these pairs as errors. These findings challenge the assumption that all authorship errors are intentional and highlight the role of mentorship.

## Key Takeaways
- Advisors sit 39.9% closer in cosine distance to their students than a random same‑field author does, indicating strong inherited style.
- Academic siblings, who may never have met, are 30.4% closer across 8,360 pairs despite different institutions, showing shared advisor influence.
- Closed‑set attribution errors occur on the true author's advisors and academic siblings eleven times more often than chance.

## Context
Authorship attribution systems assume each writer’s style is unique, but in academia mentorship transfers stylistic traits. This study uses a large corpus of solo papers to quantify these hidden similarities, revealing that current models may unfairly penalize legitimate collaborative structures. The implications extend beyond academia to any system where stylistic inheritance is common, such as corporate writing teams.

## Implications
For AI researchers building detection tools, ignoring genealogical ties could lead to false accusations against students and siblings. The findings suggest that attribution methods must account for shared mentorship before labeling errors as intentional.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14843v1)
