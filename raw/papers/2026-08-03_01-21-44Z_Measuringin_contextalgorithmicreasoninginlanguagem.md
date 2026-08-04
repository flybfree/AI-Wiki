---
title: Measuring in-context algorithmic reasoning in language models against an exact Bayes-optimal standard
published: 2026-08-03T01:21:44Z
authors: Hector Zenil, Luan Ozelim
url: http://arxiv.org/abs/2608.01575v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring in-context algorithmic reasoning in language models against an exact Bayes-optimal standard

## Abstract
Whether large language models perform genuine algorithmic reasoning or mere pattern completion is hard to test, because most benchmarks lack a ground truth for correct inductive inference. We introduce F-ICL, an in-context-learning benchmark that supplies one exactly. Using the Turing-complete machine F, complement-symmetrised into sF to remove output-polarity bias, we exhaustively enumerate all 1.5 billion programs of length $L\le13$ and compute the Bayes-optimal posterior in closed form under a bounded universal (Levin--Solomonoff) prior; models are scored by how closely their served distributions approach it at matched evidence. Each task is paired with its bitwise complement, on which the optimum scores identically, so an original-twin gap isolates the model's inductive bias. Across 105 serving configurations spanning 37 open models (0.8B--675B) and frontier systems from four laboratories, models answer up to 92\% of queries correctly, yet 45 of 46 models yield distributions farther from the optimum than a keystroke reference, and their behaviour is bracketed by low-order prefix statistics fitted only on visible evidence. That reference is itself an algorithmic mixture, induced by a print-only machine with no loops, so the panel's implied measure sits closer to a loop-free mixture than to the loop-bearing optimum, independently of the reference machine. Updating is also non-monotone, which no prior explains: a Bayes-rational solved set can only grow in this realisable, noiseless setting, yet added examples produce $6{,}545$ solved-to-unsolved transitions against $13{,}702$ gains. The gap is not predicted by accuracy (Spearman $ρ=-0.19$, $p=0.21$), does not close with scale or across frontier generations in the serving modes that expose distributions, and is widened by instruction and reasoning post-training. F-ICL is released as an open, reproducible benchmark and toolkit.

## Metadata
- **Published**: 2026-08-03T01:21:44Z
- **Authors**: Hector Zenil, Luan Ozelim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01575v1)