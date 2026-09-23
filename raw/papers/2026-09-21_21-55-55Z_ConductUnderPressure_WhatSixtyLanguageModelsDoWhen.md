---
title: Conduct Under Pressure: What Sixty Language Models Do When a User Pushes
published: 2026-09-21T21:55:55Z
authors: Tapan Parikh
url: http://arxiv.org/abs/2609.25447v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conduct Under Pressure: What Sixty Language Models Do When a User Pushes

## Abstract
We study what LLMs do when a user applies pressure in an uncomfortable situation: a user insists, begs, flatters or grieves, and the model gives up a correct fact, writes a document it should refuse, or cheers a plan that will cost the user money. We send frozen multi-turn scenes, identical for every model regardless of the reply, to 60 models from 13 vendors, and label each transcript with a codebook built by open coding and then frozen: a trajectory (the model held its position or folded) and a manner (how it held or folded). Two findings separate. Whether a model holds tracks its generation, meaning how recent it is: fold rate correlates with a public capability index at Spearman -0.64, with little vendor effect. How it holds tracks the vendor: six of the 17 manner codes sort by vendor at permutation p <= 0.001, corrected across the codebook. We report four vendor profiles on the codes that cleared reliability.   We also ask which parts of the labeling need a person. Six LLM coders from three vendors apply the codebook more consistently than three human coders do (Krippendorff's alpha 0.66 against 0.46), agree with the codebook's author on trajectory at kappa 0.84 to 0.91 on transcripts the codebook's examples never touched, and match an adjudicated human reference at 0.83. Blind machine readings recover the codebook's categories but cannot tell which of them a second reader would apply the same way. We conclude that for behavior a non-specialist can judge, the human contribution is authoring and bounding the codes and owning a small reference, not producing labels at volume.

## Metadata
- **Published**: 2026-09-21T21:55:55Z
- **Authors**: Tapan Parikh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25447v1)