---
title: Unfolding Scientific Papers into Multi-Turn Generation Trajectories for Continued Pre-Training
published: 2026-08-26T14:06:29Z
authors: Qiankai Xu, Qiguang Chen, Zixin Su, Wenhao Huang, Yue Gao, Jiaheng Liu, Ge Zhang
url: http://arxiv.org/abs/2608.25826v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unfolding Scientific Papers into Multi-Turn Generation Trajectories for Continued Pre-Training

## Abstract
A recent line of synthetic-data work reconstructs the thinking behind existing text rather than rewriting the text itself, but it operates on short web passages, recovers only local thoughts, and leaves the structure of whole documents untouched. Scientific papers are written to a clear and largely uniform structure and make a natural substrate for lifting this paradigm to the document level. We present a pipeline that unfolds each paper into a multi-turn generation trajectory in which a teacher model reconstructs the writing process of the whole paper: a writing request, a global plan, and pre-writing deliberation for each section. All section texts and the abstract are kept verbatim from the source paper. We apply the pipeline to quality-filtered arXiv papers and obtain a corpus for continued pre-training (CPT) that is roughly twice the size of the source text. The same reverse construction extends to instruction data and evaluation. Treating real paper text as the answer yields an SFT dataset. Anchoring tasks in held-out papers yields PAW-Bench, an academic-writing benchmark whose tasks carry their own rubrics and checklists. In controlled experiments CPT on our corpus followed by supervised fine-tuning on public datasets improves writing benchmarks broadly while preserving general reasoning and improving long-document reading. The writing gain persists even when every model is fine-tuned on a dedicated writing SFT dataset. Mixing our SFT data into that recipe lifts academic writing further.

## Metadata
- **Published**: 2026-08-26T14:06:29Z
- **Authors**: Qiankai Xu, Qiguang Chen, Zixin Su, Wenhao Huang, Yue Gao, Jiaheng Liu, Ge Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25826v1)