---
title: Multi-agent discussion gains less when dissent is withheld
url: http://arxiv.org/abs/2609.38324v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-29_18-00-14Z_Multi_agentdiscussiongainslesswhendissentiswithhel.md
generated_at: 2026-09-30 20:52
model: qwen3.6-35b-a3b
---

## Summary
This paper addresses conflicting reports on whether multi-agent LLM discussions improve accuracy or lead to incorrect consensus by introducing a parsimonious model grounded in four observed agent behaviors: withholding dissent, internalizing answers, reconsidering after hearing dissent, and correcting toward the correct answer. The analysis demonstrates that discussion enhances majority voting only when the rate of withheld dissent falls below a critical threshold determined by the net correction rate and the internalization rate. Empirical validation across multiple benchmarks confirms that reducing withholding increases gains, while disabling reasoning can paradoxically improve outcomes by lowering internalization and promoting reconsideration of minority views.

## Key Takeaways
- Discussion improves accuracy only when the dissent withholding rate $c$ is below a critical threshold $c^* = \gamma/(\gamma + a)$, where $\gamma$ represents the net correction rate and $a$ represents the internalization rate; if agents withhold too frequently, the group cannot overturn incorrect initial majorities.
- The performance gain from discussion shrinks as withholding rises across different LLMs and benchmarks like HiddenBench and MedEInst, but explicitly instructing agents not to withhold dissent significantly boosts accuracy by ensuring valid minority opinions are voiced and evaluated.
- Turning reasoning off can increase the gain from discussion because complex reasoning raises the internalization rate $a$, causing agents to rigidly adhere to their initial answers and ignore reconsideration of minority positions, whereas reduced reasoning fosters better correction dynamics

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38324v1)
