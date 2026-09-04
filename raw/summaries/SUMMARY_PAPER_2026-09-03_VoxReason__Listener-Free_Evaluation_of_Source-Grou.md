---
title: VoxReason: Listener-Free Evaluation of Source-Grounded Speech Planning Before Synthesis
url: http://arxiv.org/abs/2609.03203v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-02_22-35-02Z_VoxReason_Listener_FreeEvaluationofSource_Grounded.md
generated_at: 2026-09-03 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
VoxReason introduces a listener‑free evaluation method that checks whether the hidden planning decisions of expressive speech systems are grounded in cited source records before any waveform is generated. The deterministic verifier evaluates citation legality, slot agreement, unsupported state, schema validity, and one‑cue counterfactual locality on 1440 checked cases. Results show that slot accuracy can be high even when citations are missing due to shortcut controls.

## Key Takeaways
- Shortcut controls demonstrate that a key‑lookup oracle reaches plan‑slot accuracy of 1.000 on seen keys while an emotion prior still achieves only 0.958 slot accuracy on source‑key‑disjoint cases without citing intensity or identity.
- In a separate 100‑case learned source‑key‑disjoint comparison, locality SFT+CF repair improves plan‑slot accuracy/locality from 0.684/0.141 to 0.919/1.000.
- Removing source records lowers citation‑required grounded score by 0.488.

## Context
This work tackles a longstanding problem in expressive TTS where planning decisions are not verified against the source material, potentially causing misalignment between intended meaning and audio output. By providing an objective, listener‑free verification pipeline, VoxReason supplies a metric for evaluating plan quality independent of downstream waveform quality.

## Implications
Practitioners can integrate VoxReason into training pipelines to enforce citation‑aware planning, thereby improving slot accuracy and preventing hallucinated or inconsistent utterances. The method also underscores the necessity of robust locality regularization in large language models handling source‑grounded generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03203v1)
