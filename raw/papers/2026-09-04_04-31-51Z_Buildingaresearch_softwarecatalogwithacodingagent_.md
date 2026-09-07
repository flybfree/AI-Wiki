---
title: Building a research-software catalog with a coding agent: from hackathon prototype to public deployment
published: 2026-09-04T04:31:51Z
authors: Kazuyoshi Yoshimi, Satoshi Terasaki, Gotai Yamada
url: http://arxiv.org/abs/2609.04711v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Building a research-software catalog with a coding agent: from hackathon prototype to public deployment

## Abstract
Generative AI and coding agents can accelerate research software development, but they also increase the need for efficient software discovery and maintenance. We developed a repository catalog during a three-day hackathon and subsequently examined the engineering required to make it suitable for public deployment, including adversarial review, data-quality checks, browser-level validation, and publication safeguards. We then explored whether the lessons learned from this prototype could be transferred to a much larger, human-curated portal, through a retrieval agent under development for MateriApps that combines curated portal metadata, external documentation, vector search, and local language-model generation. Implementation with coding agents was rapid, but achieving reliable operation required substantial additional engineering: the most consequential problems were not crashes but silent failures that produced plausible yet incomplete or incorrect outputs, arising from incomplete data acquisition, misleading assessments, and retrieval or preprocessing failures. These observations suggest that AI-assisted software portals require explicit validation, monitoring, and repeated review, and that curated metadata and maintained documentation remain essential. The MateriApps work is exploratory and remains under active development, so the observations reported for it are preliminary; a comparable combination of curated metadata, automatically collected documentation, and retrieval-based assistance may nevertheless be useful for extending other research-software portals.

## Metadata
- **Published**: 2026-09-04T04:31:51Z
- **Authors**: Kazuyoshi Yoshimi, Satoshi Terasaki, Gotai Yamada
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04711v1)