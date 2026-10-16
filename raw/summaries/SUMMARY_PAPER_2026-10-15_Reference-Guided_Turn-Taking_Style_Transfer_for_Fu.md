---
title: Reference-Guided Turn-Taking Style Transfer for Full-Duplex Spoken Language Models
url: http://arxiv.org/abs/2610.20763v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-14_18-12-58Z_Reference_GuidedTurn_TakingStyleTransferforFull_Du.md
generated_at: 2026-10-15 22:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies a single late-layer residual-stream direction, termed the "initiative vector," within full-duplex spoken language models that governs the model's turn-taking behavior—specifically, how much it speaks versus how much it listens. The authors demonstrate that this vector can be extracted from the model's own conversations without any training or annotation, and that scaling it during generation dramatically shifts the speech ratio from 6–12% to 42–61%, effectively transferring a human speaker's conversational personality into the model using only a short reference recording.

## Key Takeaways
- The initiative vector is a single direction in the late-layer residual stream that encodes the model's decision to take the floor. It can be extracted purely from the model's own conversational outputs with no supervised training or human annotation, and it anticipates speech onsets up to 800 milliseconds before they occur, meaning it reads the turn-taking decision before the model actually speaks.
- Steering along this vector produces large, consistent shifts in speech ratio across different conversations, model weights, and training corpora. Without any steering, models produce 21–30% speech ratio; with the initiative vector scaled, the ratio moves to 42–61%, while suppressing it drops the ratio to 6–12%. This shows the vector is a genuine causal control knob rather than a correlational artifact.
- Turn-taking style transfer is reference-specific: providing a short recording of a particular human speaker calibrates the model to match that speaker's conversational rhythm. Swapping in a different speaker's reference worsens the match in 93–98% of cases, and the best uniform steering dose is statistically indistinguishable from no steering at all, confirming that per-person calibration is essential and that the style is not a fixed property of the weights.

## Context
Full-duplex spoken language models, which process audio continuously and decide frame-by-frame whether to speak or listen, represent a frontier in conversational AI. Prior work on controlling model behavior has relied on external prompts, system instructions, or post-hoc filtering, none of which identified the internal quantity that actually determines how much a model speaks. This paper fills that gap by locating a single interpretable direction inside the model's own computation, bridging the gap between mechanistic interpretability and practical conversational control, and showing that personality-like traits in language models are not monolithic weight properties but separable, steerable vectors.

## Implications
For practitioners building voice assistants, virtual companions, or interactive agents, this finding means turn-taking personality can be calibrated per user with a brief reference recording rather than retraining or fine-tuning the entire model, dramatically lowering the cost of personalization. For the broader AI safety and alignment community, it demonstrates that behavioral traits in large models are decomposable and controllable at the representation level, opening a path toward auditing and steering specific conversational dispositions without opaque external scaffolding. Industry deployments of real-time voice AI could leverage this technique to match a target speaker's rhythm, interrupt frequency, and verbosity, making synthetic voices feel more natural and individually tailored.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20763v1)
