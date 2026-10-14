---
title: How to Build a Benchmark That Actually Measures Taste
published: 2026-10-10T08:26:28Z
authors: Xiaofan Wu, Xi Zeng, Miaoxia Chen, Peishan Chen, Shuyan Li, Chen Wang, Jiyun Yao, Hanyong Zhong, Jiahao Zhu
url: http://arxiv.org/abs/2610.14707v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How to Build a Benchmark That Actually Measures Taste

## Abstract
Expert-aligned "taste" benchmarks should reward craft judgment, not the ability to game the test. We introduce TasteBench, a pairwise good-vs-bad benchmark across visual, brand, book, and tech items under a frozen rubric with expert-only gold (panel n>=3; percent agreement >=0.60 primary gate; weak engagement labels train/analysis-only), together with a control protocol that separates craft judgment from test-gaming. Applying the protocol to a Round-1 pilot (primary_human_expert; three biological human experts; n=250 pairs) surfaces and quantifies three validity threats: two construction artifacts that inflate the trivial-baseline layer, and a difficulty ceiling that inflates every score. (1) Position: the preferred item is slot A with probability 0.956, so an always_item_a policy scores 0.956 (fair chance 0.5). (2) Lexical leakage: a filename token cue scores 0.912. (3) Difficulty ceiling: craft domains show near-ceiling human agreement (book/brand/tech 1.0), and even under A/B randomization (eval_assignment_seed7; gold_side_A ~0.47) all five VLM cards reach 1.0 on craft, with only visual separating (~0.84-0.91; a post-hoc hard subset, n=107, leaves craft at 1.0). The protocol (expert-only gold, a weak-label firewall, side randomization at construction, filename scrubbing, and hard filters) makes each artifact measurable and, for the two construction artifacts, correctable; we release a reference eval harness and a side-randomization tool, and show the tool removes the position skew (0.916 to 0.495/0.505). The result is a calibrated view of what the benchmark does and does not yet measure: position and leakage are fixable, whereas the craft-domain ceiling is a pair-difficulty limit that Round-2 must address. We do not evaluate engagement, era/circle conditioning, or calibration here, and we claim no general taste SOTA.

## Metadata
- **Published**: 2026-10-10T08:26:28Z
- **Authors**: Xiaofan Wu, Xi Zeng, Miaoxia Chen, Peishan Chen, Shuyan Li, Chen Wang, Jiyun Yao, Hanyong Zhong, Jiahao Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14707v1)