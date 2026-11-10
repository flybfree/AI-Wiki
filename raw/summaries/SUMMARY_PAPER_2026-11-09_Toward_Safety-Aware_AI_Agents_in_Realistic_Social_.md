---
title: Toward Safety-Aware AI Agents in Realistic Social Engineering Attack Scenarios
url: http://arxiv.org/abs/2611.10037v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-05_17-11-44Z_TowardSafety_AwareAIAgentsinRealisticSocialEnginee.md
generated_at: 2026-11-09 21:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces SEA (Social Engineering Attack Benchmark), the first interactive evaluation environment designed to assess the intrinsic security capabilities of personal AI agents when confronted with social engineering attacks in realistic daily-life scenarios. The authors evaluate 11 frontier open-source and closed-source models across 320 tasks spanning Chinese and English cultural settings, revealing that every model is vulnerable to varying degrees of social engineering manipulation, with proactive verification rates universally below 32%. They further propose META-SEA, a co-evolutionary training framework that enables smaller open-source models like Qwen3-8B to achieve defense performance comparable to closed-source models.

## Key Takeaways
- SEA represents the first systematic interactive benchmark for social engineering attacks on AI agents, covering 8 daily-life domains, 30+ simulated applications, a 4-level difficulty gradient, and a 5-dimensional evaluation framework, with tasks co-designed alongside anti-fraud specialists to ensure ecological validity across two culturally distinct linguistic settings.
- Evaluation across 11 frontier models demonstrates that all models are breached to varying degrees, with Chinese-language attack success rates ranging from 16.9% to 84.3%, and critically, proactive verification rates universally remain below 32%, indicating a systemic failure across the entire model landscape to independently verify suspicious requests before acting.
- The META-SEA co-evolutionary framework enables Qwen3-8B, a relatively small open-source model, to achieve defense performance on par with closed-source frontier models while simultaneously reducing ungrounded action claims, suggesting that targeted adversarial training can close the security gap without requiring proprietary model access.

## Context
As personal AI agents are increasingly deployed on user devices to execute actions involving real money transfers, sensitive personal data, and consequential decisions, their vulnerability to social engineering manipulation—such as phishing, pretexting, and urgency-based pressure—has remained largely unexamined in a systematic, interactive setting. Prior safety evaluations have focused on static prompt injection or adversarial robustness in text generation, but the operational reality of agents that autonomously act on behalf of users demands evaluation in dynamic, multi-step interaction environments that mirror real fraud and manipulation scenarios.

## Implications
For industry practitioners deploying AI agents in financial services, healthcare, and consumer applications, the finding that even frontier models fail to proactively verify suspicious actions highlights an urgent need for built-in verification protocols and human-in-the-loop safeguards before agents execute irreversible transactions. The META-SEA framework offers a practical pathway for organizations using open-source models to harden agent defenses through co-evolutionary adversarial training, potentially reducing dependence on expensive closed-source APIs while maintaining robust security posture against culturally and linguistically diverse social engineering threats.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.10037v1)
