---
title: Crossing the Margin Cliff: Toward Relearn-Robust LLM Unlearning via Margin Calibration
published: 2026-07-30T08:15:58Z
authors: Xiangyu Yin, Jiaxu Liu, Zhen Chen, Chih-Hong Cheng
url: http://arxiv.org/abs/2607.27836v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Crossing the Margin Cliff: Toward Relearn-Robust LLM Unlearning via Margin Calibration

## Abstract
Large language model unlearning is consistently fragile under relearn attacks. On TOFU, fine-tuning on twenty forget examples substantially recovers held-out forget-set ROUGE for every method we evaluate, and we trace this fragility to optimization geometry. The per-token answer margin of fourteen post-hoc methods spanning gradient, preference, and distillation families converges into a narrow band above the retain reference in 41 of 42 method--size cells, a regularity we call the margin cliff. We prove that this cliff follows whenever the retain coupling holds the diagnostic log-odds of forget content above a floor, a condition that token-saturating losses induce at stationarity and that we verify directly on 34 of 42 cells. Margin Calibration (\textsc{MC}) is a plug-in polish adding a non-saturating margin hinge anchored at the reference's per-token margin plus a KL probe on a disjoint instruction corpus, restoring forget-side pressure where the native loss saturates. Under a stated gradient-dominance condition, whose on-trajectory gradient signature we measure by instrumenting the polish, its stationary set lies on the cliff-crossing side, yielding an attack-budget upper bound on the relearn margin lift. Across TOFU (three Llama-3 sizes, three forget tiers), MUSE-News on Llama-2-7B-hf, and a Phi-3.5 panel, a single frozen configuration wins all 14 head-to-head forget aggregates and all populated relearn cells (panel-mean post-attack ROUGE-L $0.41$ to $0.18$) and lowers raw membership AUC on 13/14, with reduced retain-side utility as the main cost. A deployment variant matches these gains without a retain-trained reference.

## Metadata
- **Published**: 2026-07-30T08:15:58Z
- **Authors**: Xiangyu Yin, Jiaxu Liu, Zhen Chen, Chih-Hong Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27836v1)