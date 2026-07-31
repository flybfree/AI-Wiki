---
title: Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch
published: 2026-07-30T05:08:15Z
authors: Jiazhen Ji, Shouhong Ding
url: http://arxiv.org/abs/2607.27687v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch

## Abstract
Autoresearch improves machine-learning code by proposing changes, running full training jobs, and keeping changes that improve the metric. The efficiency of this loop depends not only on generating ideas, but also on the agent's ability to decide, before spending a training run, whether a proposed modification is likely to work. We study how the reliability of this pre-execution judgment changes over the course of an autoresearch trajectory. In public AutoSOTA logs (Li et al., 2026; Tsinghua FIB Lab, 2026), the fraction of helpful modifications falls from 70% in the first two iterations to 43% by iteration 6+. On 296 same-baseline modification pairs from 39 paper-derived AutoSOTA tasks, each containing one modification that improved the metric and one that did not, with measured outcomes hidden, an LLM judge given candidate rationales but no prior-attempt history reaches 79.5% accuracy on the pairs where strict consensus returns a verdict. On the full 366-pair benchmark, however, this ability weakens substantially late in the loop. As successful changes accumulate, selective accuracy - accuracy conditioned on a strict-consensus verdict - falls from 82.8% to 56.9%, while the judge remains willing to decide. We call this operational pattern the confidence cliff. Rehearse implements the loop change as a lightweight skill for autoresearch loops: propose several ideas, compare them before execution, run the most promising, and judge with a focused memory of similar past attempts and outcomes. This focused outcome memory raises late selective accuracy to 83.5%. Across 4,000 budgeted training runs over three loops, Rehearse improves the endpoint under the same training-run budget on nanochat, image classification, and time-series forecasting.

## Metadata
- **Published**: 2026-07-30T05:08:15Z
- **Authors**: Jiazhen Ji, Shouhong Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27687v1)