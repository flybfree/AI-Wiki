---
title: Aligned in Form, Not in Meaning: The Comprehension - Containment Decoupling of LLM Safety in Low-Resource Bangla Derogatory Speech
url: http://arxiv.org/abs/2608.02941v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_23-09-19Z_AlignedinForm_NotinMeaning_TheComprehension_Contai.md
generated_at: 2026-08-05 01:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper audits five frontier large language models on native Bangla derogatory speech to test the hypothesis that safety alignment is tied to high‑resource surface forms rather than harmful meaning, showing a comprehension‑containment decoupling. It reports a 7.92 percentage point comprehension deficit in Bangla while token leakage remains identical at 92.83% across languages, and highlights that Chain‑of‑Thought reasoning improves comprehension but harms containment.

## Key Takeaways
- The models show a 7.92 percentage point comprehension deficit for Bangla slurs despite unchanged token leakage, indicating comprehension is impaired while containment appears intact.
- Severity calibration overestimates threat detection on mild slang (+4.00 error) and underestimates it on threats (‑2.00), revealing a focus on surface cues rather than compositional harm.
- Explicit Chain‑of‑Thought reasoning boosts comprehension to 94.72% but systematically reduces containment to 96.23%, showing that reasoning can rescue meaning understanding at the cost of safety filters.

## Context
This research addresses a longstanding challenge in AI safety: aligning models on low‑resource linguistic data where surface forms dominate training data, leading to unsafe behavior. It underscores that current benchmarks calibrated on high‑resource languages may not reliably predict model performance across diverse linguistic contexts.

## Implications
For practitioners, the findings warn against relying solely on token‑level containment strategies and suggest integrating meaning‑grounded evaluation methods. Industry adoption of such approaches could improve fairness and safety for under‑represented language communities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02941v1)
