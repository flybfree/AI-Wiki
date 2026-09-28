---
title: Stealth Apart, Harm Together: Skill Cascading Attacks on Skill-Based Agent Systems
url: http://arxiv.org/abs/2609.30383v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-24_18-00-18Z_StealthApart_HarmTogether_SkillCascadingAttacksonS.md
generated_at: 2026-09-28 01:30
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces skill cascading attacks, a novel threat paradigm where malicious objectives are distributed across multiple modular skills within an agent system, ensuring each modification appears benign in isolation while their combined execution produces harmful outcomes. The authors present SkillCascade, an automated multi-agent red-teaming framework, and release SkillCascade-Bench, a benchmark comprising 213 validated cascading test cases that demonstrate how these attacks reliably induce unsafe behaviors across diverse agents and LLM backbones while evading existing per-skill security scanners.

## Key Takeaways
- Skill cascading attacks exploit the interaction surface of skill-based agent ecosystems by distributing a malicious payload across multiple skills; each skill performs a subtle, seemingly harmless modification that only becomes dangerous when executed in sequence, such as a multi-step pipeline where one skill weakens medication history signals, another downgrades drug interaction severity, and a third suppresses low-priority alerts to silently eliminate critical warnings.
- The authors introduce SkillCascade, an automated red-te

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.30383v1)
