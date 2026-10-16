---
title: Human Interventions as Labels: Localizing, Steering, and (Sometimes) Editing the Computations Behind LLM Agent Failures
url: http://arxiv.org/abs/2610.21708v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_11-27-19Z_HumanInterventionsasLabels_Localizing_Steering_and.md
generated_at: 2026-10-15 23:03
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes treating human interventions in LLM agent systems not as discarded corrections or training data, but as measurement labels that pinpoint the specific internal computation responsible for a failure. Focusing on one concrete failure mode—agents asking clarifying questions when a request is already unambiguous—the authors demonstrate across five open-weight model families that the ask-versus-act decision is causally localizable within the residual stream, can be steered away using directions learned from intervention labels, and can sometimes be consolidated into model weights, though the method that works varies unpredictably across families.

## Key Takeaways
- The ask-vs-act decision is causally localizable in every eligible model family (Qwen2.5-3B, Gemma-2-2B, OLMo-3-7B, Mistral-Nemo-12B, Phi-4): a single direction learned from intervention labels flips 72–100% of held-out over-asks at a definite residual-stream depth, while random directions under the same procedure flip at most one episode, establishing that the failure is not diffuse but concentrated at a specific computational site.
- Over-asking exhibits two distinct mechanistic signatures: in four of five families the model demonstrably encodes the belief that the request is unambiguous (the belief is decodable, causally inert, and orthogonal to the decision), yet still asks; in the fifth family, rare over-asks track genuinely different world-representations, indicating the failure mode is not monolithic across architectures.
- Steering gated on a probe readout removes most of the simulated oversight burden while preserving legitimate clarifying questions (bootstrap 95% confidence intervals exclude zero), whereas a simple prompt instruction makes the problem worse; consolidating the fix into weights yields a map rather than a universal rule—LoRA confined to the causal band passes all criteria on one model while behavior cloning on identical data breaks retention, and the reverse holds on three other families, with the fifth crossing the boundary across random seeds.

## Context
Interpretability research has increasingly sought to localize specific behaviors within transformer computations, but most work targets static classification or generation tasks. This paper extends mechanistic interpretability to interactive agent settings where failures are dynamic, multi-step, and typically corrected by human overseers whose interventions are treated as operational overhead rather than scientific signal. By reframing those interventions as labels that index a precise internal computation, the authors bridge the gap between interpretability tooling and practical agent supervision pipelines, and they deliberately report negative results (a geometric rule that failed on out-of-family tests) rather than fitting a replacement, signaling methodological honesty in a field prone to overfitting narratives.

## Implications
For practitioners deploying LLM agents in production, this work suggests that targeted, low-cost interventions from human supervisors can be harvested as precise diagnostic labels to identify and correct specific failure circuits without full retraining, potentially reducing oversight costs while preserving legitimate agent behaviors. For the interpretability community, the finding that no single consolidation method (LoRA versus behavior cloning) generalizes across model families warns against assuming a universal recipe for editing agent behavior and underscores the need for per-family mechanistic auditing before committing to a fix strategy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21708v1)
