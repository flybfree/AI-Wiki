---
title: Temporal Leakage in Financial News NLP: A Multi-Architecture Audit with a Regime-Specific M&A Signal
published: 2026-08-18T00:23:25Z
authors: Chenhao Xue, Raslen Guesmi, Siwei Feng, Yucheng Gong, Jacob Xavier Sundram, Jordan Pang, Lan Wang, Julian Kaljuvee
url: http://arxiv.org/abs/2608.17223v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Temporal Leakage in Financial News NLP: A Multi-Architecture Audit with a Regime-Specific M&A Signal

## Abstract
Financial-news direction prediction has become a popular NLP benchmark, yet reported gains depend critically on whether the train-test split is chronological or random, i.e., on temporal leakage. We audit this dependence on a 49,799-article corpus across 16 feature-model combinations spanning TF-IDF, MiniLM, FinBERT, and fine-tuned RoBERTa-large / DeBERTa-v3-large, plus separate zero/few-shot and LoRA probes of Llama-3 and Qwen2.5 LLMs: random splits inflate MCC by $1.1\times$ to $6.5\times$, tracking model capacity and feature richness, and end-to-end FinBERT fine-tuning re-amplifies rather than closes the gap (size-matched ratio $1.75\times$). Conditioning on event type, mergers and acquisitions (M&A) is the only audited category with a positive locked-test signal under near-temporal chronological evaluation (TF-IDF MCC $= 0.138$ train-only, $0.068$ under train$\cup$val refit; 10,000-permutation $p < 10^{-3}$); the signal does not transfer to FNSPID's 2009-2020 U.S. corpus, localising the headline to our 2024-2025 European-tilted M&A semantics rather than a universal predictor. Three independent role labellers converge on acquirer-tagged articles as the signal locus, a power-limited qualitative convergence rather than a hypothesis-tested asymmetry. Chronological splitting plays for financial NLP the role characteristics-purging plays for asset pricing: it strips the predictable, stale component of news and leaves a residual that is small, event-localized, and lexically shallow. We advocate leakage audits as a required disclosure for financial-NLP benchmarks.

## Metadata
- **Published**: 2026-08-18T00:23:25Z
- **Authors**: Chenhao Xue, Raslen Guesmi, Siwei Feng, Yucheng Gong, Jacob Xavier Sundram, Jordan Pang, Lan Wang, Julian Kaljuvee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17223v1)