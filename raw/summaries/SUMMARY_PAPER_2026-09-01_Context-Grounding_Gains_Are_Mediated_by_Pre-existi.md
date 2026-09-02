---
title: Context-Grounding Gains Are Mediated by Pre-existing Machinery: Auditing GRPO, SFT, and DPO
url: http://arxiv.org/abs/2609.00925v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_08-49-01Z_Context_GroundingGainsAreMediatedbyPre_existingMac.md
generated_at: 2026-09-01 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper investigates whether improvements in grounding—how well language models follow prompt evidence that conflicts with memorized knowledge—require new training machinery or merely strengthen existing ones. By comparing nine post‑training variants of GRPO, SFT, and DPO from a single checkpoint, the authors find that grounding gains are modest for most GRPO methods but significant for conflict‑SFT and nearly ceiling‑reaching for DPO when matched to the starting model’s distribution.

## Key Takeaways  
- Grounding gains in GRPO variants are small and not statistically significant across seeds.  
- Conflict‑SFT improves grounding moderately, while DPO drives grounding close to its maximum possible value on the same distribution.  
- Both SFT and DPO rely heavily on the causal attention heads already present in the starting model; removing that direction suppresses gains, while restoring it recovers about 35 % of DPO’s improvement.

## Context  
The study addresses a long‑standing question in AI research: whether post‑training fine‑tuning can unlock new capabilities or merely amplify those already encoded in a model. Understanding the role of existing architectural features helps clarify how to design efficient, safe training pipelines that avoid unintended side effects.

## Implications  
For practitioners, the findings suggest that leveraging pre‑existing mechanisms—such as causal attention heads—can yield substantial grounding improvements without introducing new hardware or complex algorithms. This insight can guide resource allocation and model selection in real‑world deployment scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00925v1)
