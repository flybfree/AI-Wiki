---
title: Wrong Design Intent Is Worse Than None: A Derangement-Control Diagnosis of Header Conditioning in CAD Program Completion
published: 2026-07-25T13:11:23Z
authors: Yang Xiao
url: http://arxiv.org/abs/2607.23191v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Wrong Design Intent Is Worse Than None: A Derangement-Control Diagnosis of Header Conditioning in CAD Program Completion

## Abstract
Fine-tuned code LLMs can be conditioned on a lightweight design-intent header to steer parametric CAD generation, but whether the model actually reads the header's content has not been tested under a metric independent of the conditioning itself, nor with a causal control. We study CADCON, a five-feature design-intent header prepended to CadQuery-style sketch-extrude programs during LoRA fine-tuning of Qwen2.5-Coder-1.5B, re-scored by executable geometric assertions on the produced B-rep solid, sharing no code with the header-defining regex extractor. Across three seeds and a pre-registered {0%, 40%}-prefix $\times$ {correct, wrong, masked}-header matrix we find: (i) in conditional completion (40% prefix), a semantically wrong header degrades adherence below the no-header baseline (0.43 $\to$ 0.30/0.21 text/token) on design intents the model can render unconditioned -- polygonal and thin geometries; circle and tall intents sit at a baseline generation floor for this checkpoint ($\approx$0 in both compared arms) and are uninformative for this contrast; (ii) a derangement control -- retrained with shuffled ground-truth headers, identical header marginal but destroyed content correlation -- remains competent yet is immune to wrong headers, while the standard model is not (text headers; interaction significant on 3/3 seeds, p $\leq$ $4.2\times10^{-3}$): the harm requires the learned header$\to$program mapping, excluding the marginal/mechanical distribution-shift confound; (iii) the independent metric deflates the apparent benefit of a correct header (token: +0.21 regex $\to$ +0.02 geometry), quantifying metric circularity; (iv) the harm is regime-specific -- at 0% prefix the unconditioned baseline cannot generate valid CAD at all. Wrong intent is not noise: it actively misdirects generation.

## Metadata
- **Published**: 2026-07-25T13:11:23Z
- **Authors**: Yang Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23191v1)