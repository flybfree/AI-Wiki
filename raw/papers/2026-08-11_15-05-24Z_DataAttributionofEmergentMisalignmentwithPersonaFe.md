---
title: Data Attribution of Emergent Misalignment with Persona Features
published: 2026-08-11T15:05:24Z
authors: Clemens Vetter, David Kaczér, Lucie Flek, Florian Mai
url: http://arxiv.org/abs/2608.11025v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Data Attribution of Emergent Misalignment with Persona Features

## Abstract
Emergent misalignment (EM) is the phenomenon where fine-tuning a language model on a narrow task leads to harmful behavior in unrelated domains. A leading mechanistic account attributes EM to persona features: latent directions acquired during pre-training that misaligned fine-tuning amplifies. We ask where these features come from: which pre-training documents activate them, and whether naturally occurring human-written text suffices to induce EM. Using Sparse Autoencoder (SAE) based model diffing across four open-weight models, we find that features related to jailbreak personas, sarcasm, deception, and manipulation are amplified by misalignment fine-tuning, while safety-relevant and assistant-identity features are suppressed. Steering individual features controls EM in both directions: it induces misalignment rates of up to 62% in aligned models -- exceeding the 35% reached by misalignment fine-tuning itself -- and re-aligns misaligned models to near-baseline misalignment rates. Attributing the causal features to a corpus of one million pre-training web documents retrieves semantically relevant narratives about villainous characters, domination, and harmful agency. However, fine-tuning on these human-written documents does not reliably induce EM, even after reformatting into assistant-style responses, whereas synthetic instruction-response pairs derived from the same content do -- and transfer across model families. Semantic relevance alone is therefore not sufficient: response structure or model-generated phrasing plays an important role in inducing EM.

## Metadata
- **Published**: 2026-08-11T15:05:24Z
- **Authors**: Clemens Vetter, David Kaczér, Lucie Flek, Florian Mai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11025v1)