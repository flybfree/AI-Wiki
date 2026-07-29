---
title: Entangled by Design: Spurious Intra-Variable Signal Routing in Tabular In-Context Learners
published: 2026-07-28T10:17:59Z
authors: Athanasios Vlontzos, Giorgos Papanastasiou, Bernhard Kainz, Sotirios Tsaftaris
url: http://arxiv.org/abs/2607.25532v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Entangled by Design: Spurious Intra-Variable Signal Routing in Tabular In-Context Learners

## Abstract
Consider a model trained at a single hospital to predict patient recovery, where the measured feature $X$ bundles the patient's true health signal ($C$) with a systematic artefact from that hospital's equipment ($S$). Within that hospital, the artefact correlates with outcomes through unmeasured confounders such as patient demographics; an in-context learner rationally routes predictions through $S$, not $C$, and fails silently when deployed at a new hospital with different equipment. We formalise this as \emph{spurious routing in composite representations}: when a feature $X = [C;\,αS;\,η]$ encodes a causal signal $C$ and a spurious signal $S$ in distinct subspaces, the ICL cannot determine which drives predictions. We prove that under ridge ICL, a linear in-context learner, this routing is unavoidable regardless of context size; TabPFN, a state-of-the-art pretrained tabular ICL model, shows qualitatively consistent behaviour empirically. We derive a closed-form characterisation, $\mathrm{CSR} \propto ρ_S/ρ_C$, confirmed at $r = 0.997$ for linear ICL and $r = 0.979$ for TabPFN. Contrary to intuition, larger context sharpens commitment to the dominant in-context signal, amplifying spurious routing by up to $1.74\times$; in the high-spurious corner, more expressive models show greater vulnerability empirically ($+2.22$ CSR gap at high entanglement). We introduce two lightweight mitigations: environment-stratified context construction and S-swap augmentation, that require only weak environment labels and no knowledge of the causal partition. S-swap reduces spurious routing by $74\%$ for linear ICL and $98.8\%$ for TabPFN, with TabPFN's causal sensitivity increasing $8.4\times$ simultaneously: the model does not become agnostic, it reroutes through the causal signal.

## Metadata
- **Published**: 2026-07-28T10:17:59Z
- **Authors**: Athanasios Vlontzos, Giorgos Papanastasiou, Bernhard Kainz, Sotirios Tsaftaris
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25532v1)