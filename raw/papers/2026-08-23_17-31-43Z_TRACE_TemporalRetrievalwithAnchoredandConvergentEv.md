---
title: TRACE: Temporal Retrieval with Anchored and Convergent Evidence for Long-Horizon Video Understanding
published: 2026-08-23T17:31:43Z
authors: Pengyiang Liu, Junbo Niu, Xiaoyang Hu, Zhongyue Shi, Zitian Wang, Linjiang Huang, Si Liu
url: http://arxiv.org/abs/2608.22516v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACE: Temporal Retrieval with Anchored and Convergent Evidence for Long-Horizon Video Understanding

## Abstract
A long-video answer is evidence-supported only when the frames decoded from the video cover every event the answer depends on. Existing evaluations score final-answer correctness or predicted evidence intervals, but the frames a method decodes before answering are rarely audited, so correct answers can still rest on incomplete observation. We introduce VES-Bench, a 600-question benchmark of Temporal Ordering and Event Counting items over 348 public long videos. Each item carries a jointly necessary set of evidence intervals, letting us audit at three strictness levels whether a method's decoded frames cover every one of them. We also propose TRACE, a training-free agent that grounds answers in raw visual clips, builds an evidence bundle round by round, and stops only when the answer stabilises as the bundle grows and a final pass over the same clips returns the same answer. Under a same-backbone audit, TRACE answers 50.7% of questions correctly with at least two decoded frames inside every evidence interval, at 98.7 frames per question: over 10 points above uniform decoding at 128 frames (40.2%), and within 2.6 points of uniform decoding at 256 frames at 0.39x its frame cost, while reaching the highest answer accuracy in the audit (63.5%). TRACE also stays competitive on Video-MME (86.1), LVBench (75.6), and LongVideoBench (75.1).

## Metadata
- **Published**: 2026-08-23T17:31:43Z
- **Authors**: Pengyiang Liu, Junbo Niu, Xiaoyang Hu, Zhongyue Shi, Zitian Wang, Linjiang Huang, Si Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22516v1)