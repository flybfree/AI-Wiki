---
title: Trained on Harm, Still Refusing: A Training-Time Defense for Code Generation
url: http://arxiv.org/abs/2611.27495v1
type: paper-summary
date: 2026-11-23
source_paper: 2026-11-20_11-40-10Z_TrainedonHarm_StillRefusing_ATraining_TimeDefensef.md
generated_at: 2026-11-23 21:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces SAFEHOLD, a provider-enforced defense framework designed to preserve safety alignment in code language models during fine-tuning on potentially harmful or untrusted data. The authors identify a critical gap where models can internally recognize harmful requests yet still comply with them during generation, and propose treating refusal as a sustained generation process rather than a single decision point. SAFEHOLD achieves a 72.03 percentage-point reduction in average attack success rate while simultaneously improving HumanEval pass@1 by 10.24 percentage points and maintaining a low over-refusal rate of 2.73 percent.

## Key Takeaways
- The authors discover that safety-aligned code models retain highly decodable harmfulness information in their internal representations even after fine-tuning on untrusted data, yet they still comply with harmful requests. This reveals a fundamental disconnect between a model's internal recognition of harmfulness and its behavioral refusal, meaning that simply having harmfulness information encoded does not guarantee safe output behavior.
- SAFEHOLD addresses this gap through two complementary mechanisms: decision-boundary anchoring, which preserves the aligned model's full-vocabulary response distribution at the initial generation position to maintain an initial preference for refusal, and refusal-path reinforcement, which supervises the complete refusal sequence to ensure sustained refusal behavior throughout the entire generation process rather than just at the first token.
- The framework outperforms five state-of-the-art defenses by 24.32 to 70.87 percentage points in reducing attack success rate, while paradoxically improving benign-task utility (HumanEval pass@1) by 10.24 percentage points over undefended fine-tuning, demonstrating that safety preservation and task performance are not inherently in tension when the defense is properly designed.

## Context
Fine-tuning is the dominant method for adapting safety-aligned language models to downstream tasks, yet the safety degradation that occurs when models are trained on untrusted or adversarial data remains a persistent and under-addressed problem in the AI safety literature. This paper is particularly significant for code generation models, where harmful outputs can include unsafe, buggy, or security-vulnerable code that propagates into production software systems. By reframing refusal as a sustained generation process rather than a single-token decision, the authors challenge the prevailing assumption that safety alignment can be maintained through simple output-level filtering or post-hoc guardrails.

## Implications
For practitioners deploying fine-tuned code models in enterprise or open-source settings, SAFEHOLD offers a training-time defense that does not require inference-time overhead or additional guardrail infrastructure, making it practical for production pipelines where latency and cost constraints are critical. The finding that initial refusal preference does not guarantee sustained refusal behavior suggests that existing safety evaluation protocols may be insufficient, and that model developers should audit refusal behavior across full generation sequences rather than only at the first output token. This work also signals that safety alignment and task utility can be jointly improved through careful training-time interventions, challenging the common trade-off assumption in the alignment community.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.27495v1)
