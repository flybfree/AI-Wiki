---
title: CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM Honesty
url: http://arxiv.org/abs/2610.22292v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_17-43-47Z_CAT_alyzingHonesty_ContinuousAdversarialTrainingfo.md
generated_at: 2026-10-15 22:12
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces CATCH (Continuous Adversarial Training for Consistent Honesty), a training method that teaches large language models to produce honest answers while steering them away from dishonest outputs, without degrading the model's general capabilities. Evaluated on Llama-3.3-70B-Instruct and Qwen3-3.6-27B, CATCH demonstrates that training on only hundreds of self-reporting scenarios yields honest behavior that robustly generalizes across multiple benchmarks, outperforming prompting and supervised fine-tuning while matching state-of-the-art honesty activation steering in honesty gains but surpassing it in preserving model utility.

## Key Takeaways
- CATCH uses a continuous adversarial training framework inspired by methods originally designed for robust refusal of harmful queries, training the model toward honest answers and away from dishonest ones simultaneously. This dual-direction optimization allows the model to learn honesty as a behavioral trait rather than merely suppressing specific dishonest outputs, and it generalizes transferably across distinct evaluation benchmarks including MASK, Among Us multi-agent games, and AuditBench.
- The method achieves strong results with remarkably few training targets—only hundreds of examples drawn from self-reporting scenarios—making it far more data-efficient than supervised fine-tuning approaches. It consistently reduces dishonesty under adversarial pressure on MASK, increases honest confessions in the competitive multi-agent game Among Us, and improves discovery rates of hidden model behaviors in AuditBench, demonstrating transferability across fundamentally different task structures.
- CATCH outperforms both prompting strategies and supervised fine-tuning for improving honesty, and matches state-of-the-art honesty activation steering in honesty metrics. However, it surpasses activation steering in maintaining general model utility, achieved through a novel choice of utility-preserving training data that prevents the capability degradation commonly associated with honesty-focused interventions.

## Context
As LLMs are increasingly deployed in high-stakes domains such as medicine, law, finance, and education, their tendency to fabricate claims, contradict known facts, or assert unsupported statements poses a growing reliability risk. Existing alignment training and prompting techniques have proven insufficient to eliminate these dishonest behaviors, and activation steering methods that do improve honesty often degrade the model's broader capabilities. CATCH addresses this gap by offering a training-based approach that embeds honesty as a transferable behavioral pattern rather than a narrow output constraint, representing a shift from post-hoc correction toward intrinsic behavioral alignment.

## Implications
For practitioners deploying LLMs in regulated or safety-critical applications, CATCH offers a practical path to reducing hallucination and unsupported claims without the computational overhead or utility trade-offs of activation steering or large-scale supervised fine-tuning. The method's data efficiency—requiring only hundreds of training targets—lowers the barrier for organizations seeking to improve model honesty in production systems. For the broader research community, the transferability of honesty behavior learned through adversarial training suggests that behavioral traits can be systematically instilled in LLMs through targeted optimization, opening new directions for alignment research beyond traditional instruction-following paradigms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22292v1)
