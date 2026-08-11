---
title: ColluSkill: Adversarial Cross-Skill Composition for Evading Agent Skill Scanners
url: http://arxiv.org/abs/2608.09732v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_15-32-44Z_ColluSkill_AdversarialCross_SkillCompositionforEva.md
generated_at: 2026-08-10 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ColluSkill, a framework that composes seemingly benign individual skills into a harmful workflow, and ChainGuard, a scanner that checks skill chains. Experiments show ColluSkill succeeds 96% of the time while single-skill defenses fail, and ChainGuard cuts success to 22.5% with minimal false positives.

## Key Takeaways
- Current skill scanners only examine individual skills, missing risks from combined actions.
- The attack exploits contextual dependencies between skills, passing artifacts to create a hidden payload.
- ChainGuard reconstructs cross-skill flows to detect chain-level threats without sacrificing benign workflow detection.

## Context
The rise of LLM-based agents has expanded the attack surface beyond single functions to complex skill chains. Traditional security tools lack holistic analysis, leaving vulnerabilities that could enable coordinated malicious behavior.

## Implications
Organizations must shift from isolated skill inspection to evaluating entire execution pipelines. This paper underscores the need for chain-aware defenses in emerging agent ecosystems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09732v1)
