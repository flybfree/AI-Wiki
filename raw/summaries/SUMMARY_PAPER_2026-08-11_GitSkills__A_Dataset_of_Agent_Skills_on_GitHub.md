---
title: GitSkills: A Dataset of Agent Skills on GitHub
url: http://arxiv.org/abs/2608.10906v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_13-28-27Z_GitSkills_ADatasetofAgentSkillsonGitHub.md
generated_at: 2026-08-11 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GitSkills, a large‑scale dataset of agent skills stored as SKILL.md files in public GitHub repositories. The collection contains 3.8 million skill files from 282 200 repos, preserving each occurrence with repository metadata and content hashes, and it groups duplicates into 1.9 million distinct contents.

## Key Takeaways
- The dataset captures millions of natural‑language skill definitions that are loaded probabilistically at runtime without a compiler or type checker.
- Skills spread through repositories by copying folders, creating an unstructured ecosystem with no central registry.
- Each file occurrence is stored with its path, repository ID, and hash, enabling precise analysis of reuse and maintenance.

## Context
Agent skills represent a new paradigm for extending language‑model capabilities without code compilation. Their prevalence on GitHub reflects rapid adoption by developers seeking to share specialized function sets, yet existing research lacks systematic data on how these files are created, shared, and maintained.

## Implications
GitSkills provides empirical evidence of skill diffusion patterns that can inform tooling design and security policies for AI‑driven workflows. Practitioners can leverage the dataset to assess reuse risks, optimize skill libraries, and guide best practices in collaborative AI development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10906v1)
