---
title: Teaching Agents to Code Reliably
published: 2026-10-02T19:47:19Z
authors: Muhammad Ahmed Mohsin, Myeongsoo Kim, Kangrui Ruan, Shweta Garg, Varun Kumar, Murali Krishna Ramanathan
url: http://arxiv.org/abs/2610.03984v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Teaching Agents to Code Reliably

## Abstract
Autonomous coding agents solve repository issues by reading code, running commands, editing files, and submitting patches. Extra inference-time compute yields gains only when it produces a useful repair and supplies reliable evidence for choosing one. Three behaviors decide both, and we argue they are teachable rather than byproducts of scale, so a policy can carry them instead of a scaffold. Location diversity remains narrow, since attempts return to the same site and extra samples add no coverage. Edit diversity is left unexploited, since methodologies that differ resolve complementary issues no single run reaches. Verification misleads, since a test the agent writes for its own patch accepts many incorrect ones. Directing search by execution feedback and scoring each patch against its own reverted tree resolves 52.8% of SWE-bench Verified using 48.1% of the agent-steps an eight-sample baseline spends. Training moves these behaviors into the policy. On the 270 issues held out from SFT and RL training, weighted supervised fine-tuning raises pass@1 from 31.9% to 35.2% and pass@8 from 46.7% to 51.1%. A reinforcement objective then trains the verifier against gold-labeled repairs and incorrect variants, crediting the assertions that detect them. It raises pass@1 to 43.0% and pass@8 to 60.7%, lifts verifier precision from 26.8% to 41.7%, and more than halves false acceptance. Resolution improves on two of three out-of-distribution suites and verifier precision on all three, and the gains hold at 7B, 14B, and 30B against published coder baselines.

## Metadata
- **Published**: 2026-10-02T19:47:19Z
- **Authors**: Muhammad Ahmed Mohsin, Myeongsoo Kim, Kangrui Ruan, Shweta Garg, Varun Kumar, Murali Krishna Ramanathan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.03984v1)