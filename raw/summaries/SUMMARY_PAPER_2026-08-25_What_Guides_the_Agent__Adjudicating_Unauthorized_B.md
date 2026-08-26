---
title: What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions
url: http://arxiv.org/abs/2608.24022v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_03-24-53Z_WhatGuidestheAgent_AdjudicatingUnauthorizedBehavio.md
generated_at: 2026-08-25 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Attnlocate, a runtime framework that detects behavior‑guiding instruction spans within LLM attention matrices to stop unauthorized tool calls. It treats the problem as an object detection task and achieves high precision with low false positives across multiple models.

## Key Takeaways
- The framework casts context localization into an object detection problem using token‑level features from multi‑head attention.
- A 1‑D U‑Net with anchor‑free heads detects behavior‑guiding spans with mean IoU of 0.743 and AUROC 0.956.
- Attnlocate adapts to authority policies without retraining, enabling dynamic adjudication of malicious invocations.

## Context
Current LLM agents rely on a single natural‑language channel, making them susceptible to injection attacks that hijack tool calls during inference. Existing defenses treat malicious content as static input or output artifacts, which cannot capture dynamic instruction manipulation.

## Implications
For developers and security researchers, Attnlocate offers a proactive method to monitor and block unauthorized behavior without altering model weights. This strengthens trust in autonomous agents across diverse LLM families and supports policy‑driven governance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24022v1)
