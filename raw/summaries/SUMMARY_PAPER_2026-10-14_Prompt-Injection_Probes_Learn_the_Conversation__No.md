---
title: Prompt-Injection Probes Learn the Conversation, Not Just the Injection
url: http://arxiv.org/abs/2610.18408v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_13-51-06Z_Prompt_InjectionProbesLearntheConversation_NotJust.md
generated_at: 2026-10-14 00:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper demonstrates that linear probes trained to detect indirect prompt injection in LLM agent pipelines are largely learning superficial features like conversation position and text length rather than genuine injection signals, achieving 0.91–0.98 AUROC even without access to the model's hidden states. By augmenting training data with matched negatives—identical conversations without injections and harmless text formatted to resemble injections—the authors dramatically reduce false alarm rates across six open models while maintaining high detection sensitivity for true attacks.

## Key Takeaways
- Standard prompt-injection probe evaluations are fundamentally flawed: conversation position and text-length features alone can achieve 0.91–0.98 AUROC, meaning a probe can "pass" evaluation without ever learning what an injection actually looks like in hidden-state space. This exposes a critical blind spot in how the community benchmarks these monitors.
- Adding matched negatives to training data—specifically, the same conversation stripped of its injection and harmless text deliberately formatted to mimic injection structure—cuts false alarms on injection-free conversations from 41–80% down to 4–27%, and on harmless look-alikes from 92–98% down to 3–16%, across six open models and both in-distribution and out-of-distribution applications.
- Despite the large reduction in false positives, detection performance is preserved: with a threshold calibrated on normal traffic, the improved probe still catches a median 95% of attacks that successfully fooled the agent (compared to 91% without the augmented data), confirming that the matched negatives sharpen the decision boundary rather than simply suppressing all signals.

## Context
Indirect prompt injection is one of the most pressing security threats to autonomous LLM agents that read tool outputs, search results, or user-supplied documents. The community has increasingly relied on lightweight linear probes over hidden states as a first-pass filter to flag suspicious inputs before escalating to more expensive verification. This paper reveals that the standard evaluation protocols for such probes are insufficiently adversarial, allowing models to exploit trivial structural cues rather than learning robust injection semantics. The finding parallels broader concerns in ML evaluation where benchmark shortcuts inflate apparent performance.

## Implications
For practitioners deploying agent pipelines, this work provides a concrete, low-cost recipe—augmenting probe training data with matched negatives—that can be applied to any open model to make injection monitors far more reliable in production, reducing the costly false-alarm escalations that currently plague agent safety pipelines. For the research community, it signals that existing injection-detection benchmarks need to be redesigned to include position-matched and format-matched negatives, otherwise reported AUROC numbers will continue to overstate real-world robustness. The transferability of the technique to text-only filters further suggests that the underlying principle—forcing classifiers to distinguish content from structure—applies broadly beyond hidden-state probing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18408v1)
