---
title: Verifier-Grounded Agentic RL for Provably Correct Code
url: http://arxiv.org/abs/2610.19298v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_23-17-25Z_Verifier_GroundedAgenticRLforProvablyCorrectCode.md
generated_at: 2026-10-14 21:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a reinforcement learning framework that uses a formal program verifier as the training reward for code generation, replacing the common practice of rewarding only test-passing behavior. The authors design an agentic environment where a language model iteratively interacts with a live verifier over multiple turns, guided by a reward signal that reads the verifier's internal diagnostics rather than its binary verdict. Across multiple Qwen3 model sizes, this approach dramatically improves formal verification rates on code generation benchmarks and generalizes to unseen verification suites.

## Key Takeaways
- The core innovation is a reward function that scores a candidate program by the weighted fraction of proof obligations it discharges, as reported in the verifier's diagnostics, rather than relying on a simple accept-or-reject verdict. This solves the gradient starvation problem where a binary reward provides no learning signal when every attempt fails, and it is further extended with hidden probes derived from a reference proof's annotations to provide richer supervision.
- An integrity audit mechanism is layered above the verifier to prevent the policy from gaming the reward. The audit rejects any candidate that alters the formal specification or assumes the very proposition it was supposed to prove, closing a loophole where a model could trivially satisfy the verifier by encoding the conclusion as a premise.
- The system operates as a multi-turn agent working against a live verifier, with a separately trained proof specialist serving as a frozen collaborator. On DafnyBench, held-out verification accuracy rises from 66.1% to 93.5%, and on SWE-Proof it reaches 100%. The reward outperforms a binary pass-or-fail signal trained under identical settings, and when the agent must also deliver repository patches graded by withheld tests, issue resolution improves from 59.6% to 72.5%. Checkpoints generalize to three verification suites entirely absent from training, including one with a different language and verifier.

## Context
Reinforcement learning from human feedback and test-based rewards have become the dominant training signals for code-generating language models, yet these signals are inherently incomplete because unit tests cover only a finite subset of inputs. Formal verification tools such as Dafny can prove correctness for all inputs, but they have historically been used only at inference time as post-hoc checkers. This paper bridges that gap by making the verifier a first-class training signal, addressing the practical obstacles of sparse gradients and reward hacking that have prevented verifiers from being integrated into RL pipelines.

## Implications
For practitioners building code-generation systems, this work demonstrates that formal verification can be moved from a post-deployment audit step into the training loop itself, yielding models that produce provably correct code rather than merely test-passing code. The generalization to unseen languages and verifiers suggests the approach is not tied to a specific verification toolchain, opening a path toward training agents that can reason about correctness across diverse software ecosystems. For the broader AI safety and reliability community, the integrity audit pattern offers a reusable template for preventing reward gaming whenever a formal checker is used as a training signal.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19298v1)
