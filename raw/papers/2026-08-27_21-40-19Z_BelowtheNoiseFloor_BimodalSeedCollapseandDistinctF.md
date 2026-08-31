---
title: Below the Noise Floor: Bimodal Seed Collapse and Distinct Failure Modes in Small-Model Knowledge Distillation
published: 2026-08-27T21:40:19Z
authors: Dipto Sumit, Sakib Ul Haque, Farig Sadeque
url: http://arxiv.org/abs/2608.27729v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Below the Noise Floor: Bimodal Seed Collapse and Distinct Failure Modes in Small-Model Knowledge Distillation

## Abstract
Function routing -- selecting the correct API call from a fixed catalog given a natural-language request -- is a deployment problem where small students are attractive but knowledge distillation gains are typically reported single-seed, at scales where seed variance is unknown. On a 740-instance healthcare API routing task with a 1.5B Qwen student and a 20B teacher, we compare eight KD variants against supervised cross-entropy, using three to six seeds for key configurations. We find: (i) per-seed standard deviation ranges from 2.8 to 48.7 percentage points, swallowing every claimed KD gain below five points; (ii) three of seven KD variants exhibit bimodal collapse, with at least one in three to five seeds falling below 55% accuracy while the others train normally, and a fourth showing elevated variance; (iii) collapse has distinct modes -- wrong-function selection for ce_kd and ce_paraphrase, and a previously undocumented output-truncation mode for reasoning_kd, where the model emits reasoning but terminates before producing a function name (0.9% accuracy); (iv) only progressive_kd and rank_kd avoid collapse across observed seeds, with sigma <= 3.9 pp; (v) a naive cross-split +3.78 pp gain from input enrichment reverses to -2.70 pp under controlled within-split multi-seed re-testing. Single-seed evaluation is therefore unable to detect central failure modes in small-model KD.

## Metadata
- **Published**: 2026-08-27T21:40:19Z
- **Authors**: Dipto Sumit, Sakib Ul Haque, Farig Sadeque
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27729v1)