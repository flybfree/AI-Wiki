---
title: Repo2Skill-Evo: Repository Skills Go Stale in Silence
url: http://arxiv.org/abs/2608.21964v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_14-07-51Z_Repo2Skill_Evo_RepositorySkillsGoStaleinSilence.md
generated_at: 2026-08-24 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether LLM agents can keep repository-specific procedural knowledge current across software release transitions; it finds that most transitions invalidate parts of the skill set and frontier agents still perform poorly. Across 57 real-world repositories and 105 selected release transitions, every transition invalidated part of the V1 skill set, yet six frontier agents achieved only an average macro F1 of 29.9% to 69.7% under a patch-grounded removal metric that balances stale-content recall against over‑editing precision.

## Key Takeaways
- The version specificity that makes a skill useful also creates fragility: after a release, the skill becomes stale without any explicit signal.
- Every evaluated transition invalidated part of the V1 skill set, meaning outdated guidance persists silently in the agent’s knowledge base.
- Frontier agents still achieved only an average macro F1 of 29.9% to 69.7%, indicating that even state‑of‑the‑art systems cannot reliably maintain repository skills.

## Context
LLM agents rely on externalized procedural knowledge such as API calls and script conventions, which are encoded in skill sets; when these become outdated after a release, the agent continues to use them without detection. This paper addresses the durability of that knowledge transfer across version boundaries, highlighting a silent decay problem.

## Implications
For practitioners, this means that deploying LLM agents on evolving codebases requires proactive mechanisms to detect and refresh stale skill content; otherwise performance deteriorates unnoticed. Industry adoption must incorporate continuous skill maintenance pipelines to preserve reliability in dynamic software ecosystems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21964v1)
