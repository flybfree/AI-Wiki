---
title: Jagged Judges: Epistemic Stability Under Silence, Pressure, and Persistence
published: 2026-08-12T23:14:05Z
authors: Justin Zhao, Himaghna Bhattacharjee, Hannah Korevaar, Bhaktipriya Radharapu, Khalid El-Arini
url: http://arxiv.org/abs/2608.12645v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Jagged Judges: Epistemic Stability Under Silence, Pressure, and Persistence

## Abstract
LLM judges have become central infrastructure for model evaluations, online grading, and reward modeling. Judges are typically validated by accuracy on golden data, but accuracy says little about whether they are stable under re-prompting, challenge, or sustained pushback. We introduce the \emph{Wiggle Framework}, a unified stress test for epistemic stability in LLM judges. The framework decomposes judge robustness along three dimensions: Mechanical Consistency (stability under re-prompting and reframing), Single-turn Conviction (stability under a single challenge), and Multi-turn Persistence (stability under sustained or adaptive pressure). We use the framework to study 9 frontier models across 14 judging tasks spanning safety, toxicity, AI writing detection, and political-response evaluation. Every model exhibits substantial wiggle as a judge --- flipping verdicts 25--71\% of the time under static pushback, and 62--91\% with an adversarial LLM persuader. Critically, we find that pressure that succeeds in changing a judge's verdict is almost always net-corrupting with respect to ground truth. Beyond the framework itself, we identify baseline jury majority strength as the most effective single-shot signal for anticipating which items wiggle. Taken together, this is the first apples-to-apples cross-dataset comparison of mechanical, conformity, and persuadability tests in a judging context.

## Metadata
- **Published**: 2026-08-12T23:14:05Z
- **Authors**: Justin Zhao, Himaghna Bhattacharjee, Hannah Korevaar, Bhaktipriya Radharapu, Khalid El-Arini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12645v1)