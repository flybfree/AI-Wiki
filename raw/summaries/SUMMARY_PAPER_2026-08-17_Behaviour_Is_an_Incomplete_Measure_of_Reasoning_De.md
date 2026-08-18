---
title: Behaviour Is an Incomplete Measure of Reasoning Development: Cross-surface pre-arrival accessibility and the limits of developmental inference in a recurrent-depth reasoner
url: http://arxiv.org/abs/2608.16085v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_04-30-25Z_BehaviourIsanIncompleteMeasureofReasoningDevelopme.md
generated_at: 2026-08-17 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how reasoning development is measured in a recurrent-depth relational reasoner and shows that behavioural thresholds do not fully capture internal progress. It finds that three-hop competence required many more symbolic epochs than verbal epochs, while four-hop never exceeded 3/40 on held-out behaviour and ended at 0/40 after a long grind. Internal accessibility probes reveal early predictive signals before any behavioural change.

## Key Takeaways
- Three‑hop competence cost 186.5‑fold more logical epochs on the symbolic surface versus the verbal surface, yet four‑hop never exceeded 3/40 on held‑out behaviour and ended at 0/40 after a long grind.
- Linear probes detected future‑answer identity on the verbal surface before behavioural arrival, with p = 0.012987, indicating internal accessibility precedes observable competence.
- Probe eligibility is defined by behavioural arrival, so measuring population changes confounds the measurand and training‑time development.

## Context
The study highlights a gap between external behaviour and internal state in AI reasoning models, where progress may be invisible to downstream tasks. This disconnect challenges current practices that rely solely on behavioural checkpoints as proxies for capability growth.

## Implications
Researchers should move beyond behavioural thresholds toward probing internal states to understand true learning. Practitioners can design experiments that separate training‑time and inference‑time axes, ensuring causal insights rather than correlational artefacts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16085v1)
