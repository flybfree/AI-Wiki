---
title: When to Use Extra Context: Evidence-Grounded Terminology Adaptation for Simultaneous Speech Translation
published: 2026-07-20T10:00:46Z
authors: Zeyu Yang, Satoshi Nakamura
url: http://arxiv.org/abs/2607.17766v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When to Use Extra Context: Evidence-Grounded Terminology Adaptation for Simultaneous Speech Translation

## Abstract
Extra context is valuable for simultaneous speech translation of technical talks, but injecting the entire document context into every streaming segment is often too coarse. Through diagnostic experiments, we find that context gains mainly come from paper-specific terminology recovery rather than uniform semantic enhancement. We therefore propose EGTA, an Evidence-Grounded Terminology Adaptation framework that builds a document terminology memory, selects compact candidate terms conditioned on the current streaming state, and adapts ASR/speech-side and decoder-side decision spaces using only the selected terms. EGTA can be instantiated in cascaded, end-to-end, and generation-only SimulST settings without full-model fine-tuning. We evaluate EGTA on an ACL technical-talk SimulST evaluation suite consisting of MCIF-dev and ACL60/60-dev. On MCIF-dev, EGTA-RG improves BLEU by +1.05/+0.59, XCOMET-XL by +0.019/+0.006, named-entity recall by +79\%/+73\% relative, and acronym recall by +0.099/+0.171 on En$\rightarrow$Zh and En$\rightarrow$De. Across MCIF-dev latency settings, EGTA consistently improves XCOMET-XL, named-entity recall, and acronym recall. External validation on ACL60/60-dev further shows consistent terminology-recall gains without additional fine-tuning. Shuffled-memory controls and activation audits provide evidence that the improvements are tied to paper-specific evidence alignment rather than generic context prompting.

## Metadata
- **Published**: 2026-07-20T10:00:46Z
- **Authors**: Zeyu Yang, Satoshi Nakamura
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17766v1)