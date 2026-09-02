---
title: SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems
url: http://arxiv.org/abs/2609.00595v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_02-34-44Z_SoK_WhenSafeAgentsFailTogether_TheSecurityofMultiA.md
generated_at: 2026-09-01 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper argues that safe agents can fail together in multi‑agent LLM systems because failures propagate across principal boundaries and are not caught by local checks. It introduces an A‑I‑R framework to analyze 197 works, covering six interfaces, four adversary positions, seven risks, and eight attack paths. The authors audit 44 evaluation studies and propose a five‑part contract for defenses.

## Key Takeaways
- Safe agents can fail together across boundaries, producing system‑wide failures that local checks cannot detect.
- The A‑I‑R framework unifies attacks by adversary position, interaction interface, and resulting risk, revealing eight recurring attack paths.
- Defenses must close execution paths and support recovery, highlighting path closure and recovery as key challenges.

## Context
Multi‑agent LLM systems are increasingly deployed for complex tasks where multiple autonomous agents share state and authority. Traditional security models assume isolated components, which can mask coordinated failures. This paper addresses the gap by providing an end‑to‑end view of how attacks propagate through interaction interfaces.

## Implications
For practitioners, the findings stress the need to design contracts that enforce path closure and recovery rather than relying on per‑agent safeguards. The framework offers a reusable toolkit for evaluating MAS security across diverse designs, guiding research toward robust, observable defenses.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00595v1)
