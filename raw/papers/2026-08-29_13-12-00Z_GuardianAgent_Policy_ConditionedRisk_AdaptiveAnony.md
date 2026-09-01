---
title: GuardianAgent: Policy-Conditioned Risk-Adaptive Anonymization with Verified Adversarial Escalation
published: 2026-08-29T13:12:00Z
authors: Ruiyi Yang, Gayathri Lihinikaduarachchi, Rahat Masood, Flora D. Salim, Salil S. Kanhere
url: http://arxiv.org/abs/2608.29251v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GuardianAgent: Policy-Conditioned Risk-Adaptive Anonymization with Verified Adversarial Escalation

## Abstract
Privacy protection for live web traffic requires more than detecting private spans. Agent-based privacy protection systems must determine whether an outgoing action complies with the destination site's privacy policy, then apply only the level of rewriting or sanitisation justified by the residual disclosure risk. We present GuardianAgent, a policy-conditioned anonymization framework that couples structured risk assessment with verified adaptive rewriting. GuardianAgent computes risk through AMRSF (Adaptive Multi-factor Risk Scoring Formula), an explicit controller that combines policy-violation likelihood with data sensitivity, recipient transmission, purpose legitimacy, contextual basis, and policy transparency, rather than relying on an LLM to assign risk directly. This risk score determines both the allow/transform/deny decision and the initial anonymization level. For efficiency, GuardianAgent uses an evidential fast path for low-uncertainty policy matches and invokes an LLM slow path only for uncertain cases. For rewriting, it applies a five-level hierarchy driven by a verified adversarial guesser: guesses trigger escalation only when supported by the original text, preventing hallucinated attacker confidence from causing unnecessary over-anonymization. Experiments across three benchmarks spanning legal text (TAB), Reddit posts (SynthPAI), and multi-format synthetic PII records (PII-Masking-300k) show that GuardianAgent achieves the strongest privacy-utility trade-off among published baselines and is the only method to reach more than 0.90 privacy in all three domains, remaining robust under a backbone switch. Action-context stress tests further show that the same outgoing text receives different decisions and anonymization strengths under different recipients, purposes, action bases, and policy-transparency conditions.

## Metadata
- **Published**: 2026-08-29T13:12:00Z
- **Authors**: Ruiyi Yang, Gayathri Lihinikaduarachchi, Rahat Masood, Flora D. Salim, Salil S. Kanhere
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29251v1)