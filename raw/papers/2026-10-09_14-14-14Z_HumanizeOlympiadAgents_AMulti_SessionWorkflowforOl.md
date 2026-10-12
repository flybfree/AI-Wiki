---
title: Humanize Olympiad Agents: A Multi-Session Workflow for Olympiad Problem Solving with Solve, Review, Wiki, Verify
published: 2026-10-09T14:14:14Z
authors: Zhengyang Zhang, Jing Xiong, Hongzhou Lin, Juihui Chung, Zijian Zhang, Song Han, Sihao Liu, Ligeng Zhu
url: http://arxiv.org/abs/2610.13632v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Humanize Olympiad Agents: A Multi-Session Workflow for Olympiad Problem Solving with Solve, Review, Wiki, Verify

## Abstract
Large language model (LLM) agents are rapidly improving on long-horizon scientific and olympiad tasks. Recent systems have produced a Lean-formalized resolution of the Navier--Stokes problem and autonomous solutions to four open questions in the Erdős Conjectures database. Yet neither system releases both its underlying model and complete inference stack. More broadly, a single agent session remains brittle on difficult problems: early errors can propagate, missing domain knowledge can stall progress, and apparent success can mask a misinterpretation or weakening of the original task. We introduce HOA (Humanize Olympiads Agent), an open, flow-level framework that coordinates multiple agent sessions through three complementary feedback channels. First, an independent reviewer evaluates each candidate and provides actionable feedback. Second, a structured wiki supplies task-specific knowledge that may be missing or unreliable in model pretraining. Third, a verifier checks generated Lean proofs against trusted challenge statements. With GPT-5.6 Sol, HOA achieves perfect scores on the IMO, IPhO, and IOI 2026, near-full marks on the IChO 2026 problem set, and solves all 672 problems (100%) on PutnamBench. On the Lean-Eval leaderboard, HOA ranks first, solving 251 of 304 problems (82.6%). We further evaluate HOA with open models. Using Kimi-K3, HOA achieves full scores on the IMO, IPhO, and IOI, and a gold-level score of 97.1% on the IChO. These results closely match the closed-source GPT-5.6 Sol + /Goal baseline on the IMO and IPhO, while exceeding it on the IChO and IOI, demonstrating that systematic feedback can help bridge substantial differences in base-model capability.

## Metadata
- **Published**: 2026-10-09T14:14:14Z
- **Authors**: Zhengyang Zhang, Jing Xiong, Hongzhou Lin, Juihui Chung, Zijian Zhang, Song Han, Sihao Liu, Ligeng Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13632v1)