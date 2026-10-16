---
title: When Reasoning Is Not Enough: Proactive Inquiry for Cross-Modal Safety in Multimodal Large Language Models
url: http://arxiv.org/abs/2610.22068v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_15-28-47Z_WhenReasoningIsNotEnough_ProactiveInquiryforCross_.md
generated_at: 2026-10-15 23:02
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses a critical safety gap in multimodal large language models (MLLMs): the phenomenon where individually benign images and text inputs, when interpreted jointly, produce unsafe outputs. The authors distinguish between implicit reasoning risk (where reasoning drifts toward harm) and a newly identified intent-level risk, where cross-modal ambiguity silently commits the model to a hazardous premise that path-level optimization alone cannot correct. They propose SAFE-PRO, a framework that uses a Risk-Conditioned Uncertainty signal to decide when to ask safety-grounded clarifying questions versus when to apply path optimization, demonstrating consistent safety improvements across seven benchmarks and two base MLLMs.

## Key Takeaways
- The paper introduces the concept of intent-level risk as distinct from implicit reasoning risk. Intent-level risk occurs when cross-modal ambiguity causes the model to silently commit to a hazardous premise before any reasoning path is generated, meaning that path-level optimization techniques (such as those used in SRPO) cannot correct the error because the flawed premise is already baked into the model's interpretation. This reframes multimodal safety as a problem that requires intervention before reasoning begins, not just during or after it.
- SAFE-PRO operates by combining predictive entropy with a learned cross-modal risk score to form a Risk-Conditioned Uncertainty (RCU) signal. This signal determines two decisions: when the model should ask safety-grounded clarifying questions to resolve ambiguity, and where path optimization should be applied. The reward function explicitly prioritizes safety while penalizing over-refusal, preventing the model from simply refusing to answer as a safety shortcut. The authors also provide theoretical analysis of gradient variance and unsafe-completion risk under RCU.
- The authors construct SSUI-Dialog, a multimodal multi-turn dataset with dual-intent supervision, to train and evaluate the framework. Empirically, SAFE-PRO consistently improves safety over SRPO across seven benchmarks and two base MLLMs, roughly halves over-refusal rates, and surpasses GPT-4o and Claude-3.5-Sonnet in average single-turn safety, suggesting that proactive inquiry mechanisms can outperform much larger commercial models on safety metrics.

## Context
As MLLMs are increasingly deployed in consumer-facing applications such as image captioning, visual question answering, and content moderation, the risk of unsafe outputs arising from the interaction between visual and textual modalities has become a pressing concern. Prior safety work has largely focused on text-only models or on post-hoc filtering of outputs. This paper matters because it identifies a failure mode specific to multimodal systems—silent commitment to hazardous premises through cross-modal ambiguity—and proposes a mechanism (proactive inquiry) that intervenes before reasoning begins. The introduction of dual-intent supervision in SSUI-Dialog also signals a shift in how multimodal safety datasets are constructed, moving beyond single-turn harmful-output detection toward multi-turn dialogic safety evaluation.

## Implications
For practitioners deploying MLLMs in production, this work suggests that safety cannot be achieved solely through output filtering or reasoning-path optimization; systems need mechanisms to detect when cross-modal interpretation is ambiguous and to proactively seek clarification from the user before generating a response. The finding that a smaller, purpose-built framework can surpass GPT-4o and Claude-3.5-Sonnet on safety benchmarks while reducing over-refusal has direct commercial relevance, indicating that safety engineering does not require scaling model size. For the research community, the theoretical analysis of gradient variance under RCU and the dual-intent supervision paradigm in SSUI-Dialog provide new tools and evaluation standards that could shape future multimodal safety benchmarks and training methodologies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22068v1)
