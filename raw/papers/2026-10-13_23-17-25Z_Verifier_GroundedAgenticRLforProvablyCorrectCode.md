---
title: Verifier-Grounded Agentic RL for Provably Correct Code
published: 2026-10-13T23:17:25Z
authors: George Ma, Yuhao Zhang, Bing He, Zeren Shui, Ferhat Erata, Murali Krishna Ramanathan, Somayeh Sojoudi, Hao Zhou
url: http://arxiv.org/abs/2610.19298v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Verifier-Grounded Agentic RL for Provably Correct Code

## Abstract
Reinforcement learning for code usually rewards passing tests, which a model can do while remaining wrong on the inputs the tests do not cover. A program verifier instead decides whether a program satisfies a formal specification for all inputs. Language models are almost always paired with verifiers at inference time only, and turning a verifier into a reward raises two difficulties. It reports only acceptance or rejection, which gives no gradient when every attempt fails, and a policy can cheat it, most simply by telling it to assume what the proof was supposed to establish. We build an agentic environment and reward that address both. The reward reads the verifier's diagnostics rather than its verdict, scoring a candidate by the weighted fraction of proof obligations it discharges, extended with hidden probes from a reference proof's annotations. An integrity audit outranks the verifier, rejecting any candidate that alters the specification or assumes what it was meant to prove. The model works as an agent against a live verifier over many turns, with a separately trained proof specialist as a frozen collaborator. Across Qwen3 models from 1.7B to 14B and a 35B Qwen3.6 mixture-of-experts model, held-out verification on code generation rises from 66.1% to 93.5% on DafnyBench and from 56.3% to 100% on SWE-Proof. This reward leads every other training signal we compare, including a binary pass-or-fail reward trained under otherwise identical settings, with the widest margin on code generation. When the agent must also deliver the repository patch, graded by each project's withheld tests, the fraction of held-out issues it resolves rises from 59.6% to 72.5%. Evaluated unchanged on three verification suites withheld from training, the checkpoints improve on all of them, including one whose language and verifier are absent from training.

## Metadata
- **Published**: 2026-10-13T23:17:25Z
- **Authors**: George Ma, Yuhao Zhang, Bing He, Zeren Shui, Ferhat Erata, Murali Krishna Ramanathan, Somayeh Sojoudi, Hao Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19298v1)