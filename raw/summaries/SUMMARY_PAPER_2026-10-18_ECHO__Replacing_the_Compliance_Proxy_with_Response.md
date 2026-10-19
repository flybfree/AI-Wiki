---
title: ECHO: Replacing the Compliance Proxy with Response Harmfulness in Optimization-Based Jailbreak Attack
url: http://arxiv.org/abs/2610.23030v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_07-07-08Z_ECHO_ReplacingtheComplianceProxywithResponseHarmfu.md
generated_at: 2026-10-18 20:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ECHO (Evaluation-Conditioned Harmfulness Optimization) is a novel optimization-based jailbreak attack framework that replaces the traditional token-level compliance proxy—such as the likelihood of an affirmative prefix—with response-level, continuous harmfulness scores derived from HarmSig, a 1.7B regressor grounded in actual harmful capability. By evaluating what the model actually says rather than what it might say, ECHO achieves up to 0.898 StrongREJECT mean score and 89.23% HarmBench success rate across five open-weight victim models on AdvBench, significantly outperforming prior optimization-based jailbreak methods.

## Key Takeaways
- The fundamental flaw in existing optimization-based jailbreak attacks is their reliance on a token-level compliance proxy computed on the prompt rather than the decoded reply. This proxy cannot distinguish a cautious hedge (e.g., "I cannot answer that") from a fully actionable harmful answer, leaving the search process blind to the model's actual output and limiting attack effectiveness.
- ECHO introduces HarmSig, a 1.7B regressor that produces continuous, response-level harmfulness scores grounded in actual harmful capability. This shifts the optimization objective from predicting whether a model will comply to measuring how harmful the generated response truly is, enabling the search to target genuinely dangerous outputs rather than superficially affirmative ones.
- The method couples HarmSig with five word-level perturbation operators and a Keyword-Anchored Beam Search algorithm with global top-m memory, all operating under a strict black-box threat model. This combination achieved 0.898 StrongREJECT mean score and 89.23% HarmBench success across five open-weight victims on AdvBench, demonstrating that response-grounded optimization substantially outperforms prompt-proxy-based approaches.

## Context
This paper addresses a critical and persistent vulnerability in large language model safety: despite extensive alignment training, models remain susceptible to jailbreak attacks that bypass safety guardrails. The broader field of adversarial robustness for LLMs has largely relied on optimization methods that optimize for proxy signals on the input side, creating a fundamental gap between what the attack optimizes for and what the model actually produces. ECHO represents a paradigm shift by grounding the optimization loop in the model's actual generated output, aligning the attack objective with the true safety evaluation metric.

## Implications
For practitioners deploying safety-aligned LLMs, ECHO demonstrates that current jailbreak defenses are more fragile than previously measured, since attacks that evaluate actual response harmfulness can uncover vulnerabilities invisible to compliance-proxy-based methods. This raises urgency for model developers to stress-test safety alignment using response-grounded adversarial evaluation rather than relying solely on prompt-level compliance metrics. The publicly available code and the black-box threat model assumption make ECHO immediately applicable for red-teaming teams and safety auditors seeking stronger, more realistic adversarial probes against production language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23030v1)
