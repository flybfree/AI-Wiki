---
title: Proof-Carrying Cognition: Closing the Verification Gap with Reality-Settled Reward
url: http://arxiv.org/abs/2609.09776v1
type: paper-summary
date: 2026-09-11
source_paper: 2026-09-09_06-24-53Z_Proof_CarryingCognition_ClosingtheVerificationGapw.md
generated_at: 2026-09-11 10:06
model: qwen3.6-35b-a3b
---

## Summary
The paper addresses the "verification gap" in language model reasoning, arguing that scalable, incorruptible rewards are missing outside formal domains. It introduces "proof-carrying cognition," a paradigm where reasoning steps are probabilistic claims priced by a world model trained on held-out reality and settled via proper scoring rules. Empirical results demonstrate that reality-anchored settlement significantly improves soundness under pressure compared to frozen verifiers, effectively closing the hacking gap while maintaining reward fidelity during reinforcement learning.

## Key Takeaways
- Theory establishes that verifier-gold correlation ($\rho$) acts as the exact exchange rate between test-time compute and capability; unsound verifiers incur a polynomial penalty scaling with $N^{(1/\rho^2)}$, while a margin-free copula form accurately predicts realized soundness of real LLM judges with 4% median error.
- Demonstrations in program-synthesis testbeds show that unsound verifiers suffer severe degradation in Soundness-under-Pressure as optimization increases, whereas sound verifiers improve monotonically; reality-anchored settlement reduces the hacking gap to near zero and preserves executed reward six times better than frozen models under GRPO training.
- The authors propose "proof-carrying cognition" as a new paradigm where reasoning steps are typed probabilistic claims priced by a self-built world model trained exclusively on held-out reality and settled using proper scoring rules, accompanied by the specification of Soundness-under-Pressure as the headline metric for future reality-settled reasoning benchmarks.

## Context
As frontier language models increasingly rely on reinforcement learning for complex reasoning, the field faces a critical bottleneck in verifying non-formal outputs without expensive human annotation or corruptible automated judges. This work situates itself at the intersection of scalable verification and reward modeling, challenging the reliance on frozen reward signals that degrade under distribution shift and adversarial pressure during

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09776v1)
