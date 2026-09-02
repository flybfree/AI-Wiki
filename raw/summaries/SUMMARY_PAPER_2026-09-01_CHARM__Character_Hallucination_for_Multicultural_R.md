---
title: CHARM: Character Hallucination for Multicultural Role Play Benchmark
url: http://arxiv.org/abs/2609.01352v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-57-14Z_CHARM_CharacterHallucinationforMulticulturalRolePl.md
generated_at: 2026-09-01 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CHARM, a multicultural benchmark designed to evaluate whether large language models correctly recognize and respect character knowledge boundaries during role‑playing tasks. The results show that most hallucinations stem from compliance failures—models acknowledge a query is out of scope yet still answer factually with in‑character information.

## Key Takeaways
- Models often detect that a question lies outside a character’s temporal or cross‑universe boundary but continue to generate answers, indicating a failure to suppress the stored fact.  
- The benchmark reveals systematic cultural variation in these failures, suggesting imbalances in how characters from different regions are represented within model knowledge.  
- Re‑posing the same questions to the target character confirms that many out‑of‑character responses are parametric overrides rather than genuine boundary violations.

## Context
Character role‑playing is a key application of LLMs where fidelity to a character’s identity and temporal limits matters. Prior evaluations have not distinguished between boundary awareness and compliance, leaving a gap in understanding why models err in specific ways across diverse cultural contexts.

## Implications
Accurate boundary detection is essential for applications such as educational tools, entertainment agents, and multilingual customer service bots that must respect character constraints. Addressing these failures can improve model reliability and reduce the risk of generating misleading or culturally insensitive responses.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01352v1)
