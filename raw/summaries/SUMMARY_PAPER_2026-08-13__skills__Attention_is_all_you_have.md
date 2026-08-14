---
title: @skills: Attention is all you have
url: http://arxiv.org/abs/2608.12610v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_21-49-00Z_skills_Attentionisallyouhave.md
generated_at: 2026-08-13 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces @skills as an open protocol that decouples the three functions of a skill — content, persistence, and automatic triggering — so that only the last function consumes prompt slots. By treating skills as ordinary directories with a single .gitignore‑style line, the system lets agents read any skill without installing it or making it resident in the system prompt. The protocol is additive, installable via a package, and enables teams to use many skills simultaneously.

## Key Takeaways
- Installation bundles three separable functions (content, persistence, automatic triggering) but only the last requires prompt residency, leaving the long tail of skills unused.
- @skills provides a path‑addressed interface that reads any skill directly from a Git‑tracked tree, eliminating the need for installation or manifest files.
- The protocol is optional; local paths and gh: identifiers work without the hub, while indexed GitHub skills retain their identities.

## Context
The rapid growth of public agent skills has created a bottleneck in prompt usage, limiting how many can be active at once. This paper addresses that bottleneck by proposing a lightweight, file‑based protocol that aligns with existing workflows and reduces cognitive load for developers.

## Implications
For practitioners, @skills means they can deploy dozens of agents without exhausting prompt slots, improving system reliability and scalability. For the industry, it democratizes skill sharing across teams and projects, fostering modularity in AI agent ecosystems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12610v1)
