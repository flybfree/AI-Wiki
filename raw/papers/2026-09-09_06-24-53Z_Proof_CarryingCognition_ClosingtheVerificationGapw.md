---
title: Proof-Carrying Cognition: Closing the Verification Gap with Reality-Settled Reward
published: 2026-09-09T06:24:53Z
authors: Eshwar Reddy M, Sourav Karmakar
url: http://arxiv.org/abs/2609.09776v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Proof-Carrying Cognition: Closing the Verification Gap with Reality-Settled Reward

## Abstract
Frontier gains in language-model reasoning come from reinforcement learning on reasoning traces and are concentrated in domains with a cheap, sound verifier. We argue the field's binding constraint is the verification gap: no scalable, incorruptible reward for reasoning outside formal domains. We make four contributions. (1) Theory: in a joint-Gaussian model of best-of-N selection, verifier-gold correlation rho is the exact exchange rate between test-time compute and capability, and an unsound verifier pays a polynomial penalty N^(1/rho^2); a margin-free copula form predicts realized soundness of real LLM judges to 4% median error. (2) Demonstration: in program-synthesis testbeds with executable ground truth, including a pre-registered scaled replication, unsound verifiers lose Soundness-under-Pressure as optimization grows (0.94 to 0.32 at N=4096) while a sound verifier improves monotonically; reality-anchored settlement beats a frozen verifier under i.i.d. and adversarial pressure, driving the hacking gap from ~0.27 to ~0; soundness scales log-linearly with settled labels, with on-policy settlement ~10x more label-efficient than random labeling. With real LLM judges and unit-test execution as gold, a weak judge loses soundness under best-of-N (p<0.001), a stronger judge is more robust, and selection alone manufactures +0.53 hacking gaps from honest samples. Under real GRPO training, a frozen reward model traces the full overoptimization curve (executed reward collapses 90%) while the same model refit on a 10% settlement stream preserves 6x the executed reward. (3) Paradigm: proof-carrying cognition, where reasoning steps are typed probabilistic claims priced by a self-built world model trained only on held-out reality and settled by proper scoring rules. (4) Benchmark: we specify Soundness-under-Pressure as the headline metric for a reality-settled reasoning benchmark.

## Metadata
- **Published**: 2026-09-09T06:24:53Z
- **Authors**: Eshwar Reddy M, Sourav Karmakar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09776v1)