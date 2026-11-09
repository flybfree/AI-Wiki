---
title: Addition by Subtraction: Toward Mitigating Fragile Safety Alignment in Large Language Models
url: http://arxiv.org/abs/2611.06553v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-04_14-18-05Z_AdditionbySubtraction_TowardMitigatingFragileSafet.md
generated_at: 2026-11-08 21:34
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces "Addition by Subtraction," a finetuning technique designed to reduce the fragility of safety alignment in large language models by gradually removing identified safety-critical neurons and using preference optimization to redistribute safety-aligned behavior across the remaining model components. The authors demonstrate that models trained with this method achieve substantially greater robustness against pruning-based attacks, refusal-direction ablation, and a broad range of black-box jailbreak attacks, with attack success rates reduced by up to 90% across four models from three different vendors.

## Key Takeaways
- Safety alignment in current LLMs is structurally fragile because it depends on a sparse set of safety-critical neurons or a single refusal direction; pruning even a small number of these components can substantially undermine aligned behavior, making models vulnerable to targeted white-box attacks and jailbreaks.
- The Addition by Subtraction method works by iteratively removing identified safety-critical neurons during finetuning while simultaneously applying preference optimization to re-establish safety-aligned behavior through other, non-sparse parts of the model, effectively distributing safety knowledge more broadly across the network.
- The robustness gains generalize well beyond the white-box pruning attacks that motivated the design: the finetuned models show improved resistance to refusal-direction ablation and a wide variety of black-box jailbreak attacks, while also exhibiting improved truthfulness and largely preserving general model capabilities across four models from three different vendors.

## Context
This work addresses a critical structural vulnerability in how safety alignment is implemented in large language models. Prior research has shown that safety behavior in aligned models is often concentrated in a small number of neurons or a single directional vector, creating a single point of failure that attackers can exploit through targeted interventions. By proposing a method that actively redistributes safety behavior away from these sparse components, the paper tackles the problem at its architectural root rather than treating jailbreak attacks as purely adversarial inputs, representing a shift from reactive defense to proactive structural hardening.

## Implications
For practitioners deploying LLMs in safety-critical applications, this approach offers a practical finetuning recipe that can be applied to existing models from multiple vendors to harden their safety guardrails against both white-box and black-box attacks without sacrificing general capabilities. For the broader field, the findings suggest that safety alignment should be designed as a distributed property across model components rather than a localized feature, which has direct consequences for how alignment training pipelines, model pruning strategies, and adversarial robustness evaluations should be conducted in future model development cycles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.06553v1)
