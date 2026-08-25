---
title: Where Cognition Lives: Dissecting Emergent from Computed Function in a Minimal Complete Cognitive Architecture
url: http://arxiv.org/abs/2608.22347v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_10-27-13Z_WhereCognitionLives_DissectingEmergentfromComputed.md
generated_at: 2026-08-24 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether cognitive functions in a minimal complete architecture emerge from gradient descent or are explicitly computed, and it shows that competence and halting appear to be emergent rather than pre‑programmed. The authors demonstrate that value decisions are not captured by the system’s own allocator but must be computed separately.

## Key Takeaways
- Competence emerges as a function of adaptive halting where payoff rises from 0.467 under uniform difficulty to 0.921 after posterior self‑observation, indicating that stopping is weighted more than any fixed rule.
- Value does not emerge in the system; explicit couplings capture only zero of the payoff while an allocator captures +0.151 and routing correlation rises to +0.79, showing second‑order decisions are computed rather than learned.
- The frozen LLM actuator shows self‑consistency voting as a bound (+0.0236) with inter‑sample agreement near zero, revealing that stopping signals concentrate on wrong answers.

## Context
This work contributes to the debate over emergent versus engineered intelligence in AI systems by providing empirical evidence from a minimal architecture where halting and value decisions are not pre‑specified but arise during training. It highlights how gradient‑based optimization can produce behaviors that resemble higher‑order cognition without explicit computation of those functions.

## Implications
For practitioners, the findings suggest that designing architectures with emergent decision mechanisms may yield more robust systems than those relying solely on hard‑coded rules. The research also underscores the need for rigorous testing of self‑consistency signals to avoid reliance on misleading stopping cues in real‑world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22347v1)
