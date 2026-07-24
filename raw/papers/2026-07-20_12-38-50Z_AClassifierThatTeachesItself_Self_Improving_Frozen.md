---
title: A Classifier That Teaches Itself: Self-Improving, Frozen-gate Training (SIFT) for Dynamic Document Classification
published: 2026-07-20T12:38:50Z
authors: Bogdan Raduta, Horia Velicu, Alexandru Preda, Serban Chiricescu
url: http://arxiv.org/abs/2607.18358v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Classifier That Teaches Itself: Self-Improving, Frozen-gate Training (SIFT) for Dynamic Document Classification

## Abstract
Document classification is a solved problem in the laboratory and an unsolved one in the enterprise. The blocker is rarely model architecture; it is the labeling project that must precede a model and the institutional fear of letting a model retrain itself once one exists. We present SIFT (Self-Improving, Frozen-gate Training), a dynamic classifier service, which attacks both. SIFT serves classification from a deliberately cheap, CPU-bound pipeline, a SPLADE sparse encoder feeding a LightGBM head, and escalates only the low-confidence minority of pages to an LLM judge. The judge's verdicts are written back into a labeled corpus, so the expensive model continuously teaches the cheap one: the escalation rate falls, the corpus grows from production traffic rather than from an up-front annotation effort, and accuracy compounds with use. Onboarding a new document family requires only a declarative bundle, label space, anchor phrases, and a judge glossary, not a labeling project. The harder problem is safety: an autonomously retraining classifier can silently regress. SIFT resolves this with a two-part promote gate, a critical-label F1 regression check plus a frozen golden regression set the model is never trained on, either of which vetoes promotion. This turns "retrain monthly without a human" from reckless into routine. We describe the architecture, the self-feeding corpus loop, the frozen-gate promotion mechanism, and an illustrative multi-domain deployment, and we discuss the economics of a classifier whose marginal labeling cost trends toward zero.

## Metadata
- **Published**: 2026-07-20T12:38:50Z
- **Authors**: Bogdan Raduta, Horia Velicu, Alexandru Preda, Serban Chiricescu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18358v1)