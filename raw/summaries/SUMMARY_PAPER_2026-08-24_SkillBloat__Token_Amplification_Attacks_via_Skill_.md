---
title: SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents
url: http://arxiv.org/abs/2608.21929v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_11-41-48Z_SkillBloat_TokenAmplificationAttacksviaSkillInject.md
generated_at: 2026-08-24 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SkillBloat, a two‑phase attack that exploits the trust placed in agent skills to amplify token consumption. The authors evaluate the attack on a real‑world skill benchmark and report average amplification factors ranging from 5.4184× to 10.1455×, showing that malicious skill injection can dramatically increase computational cost beyond normal task execution.

## Key Takeaways
- SkillBloat demonstrates an economic abuse where a crafted skill forces the agent to generate far more tokens than required, turning skill usage into a resource‑exhaustion vector.
- The two‑phase framework first screens diverse attack conditions and then refines the strongest candidate through LLM‑guided full‑document skill rewriting, achieving higher amplification than Phase 1 alone.
- Ablation results confirm that iterative optimization in the second stage consistently improves average best amplification, highlighting the value of refining attacks beyond initial selection.

## Context
The study addresses a gap in AI safety research by showing that skills—meant to enhance agent capabilities—can also serve as an attack surface. This finding is relevant because many coding agents rely on skill libraries to streamline tasks, and any vulnerability here could undermine performance and resource efficiency.

## Implications
For developers deploying LLM‑based coding assistants, the paper warns against treating skills as immutable resources and recommends rigorous validation of skill inputs. Practitioners should adopt continuous monitoring of token usage to detect potential amplification attacks before they degrade system reliability or incur excessive costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21929v1)
