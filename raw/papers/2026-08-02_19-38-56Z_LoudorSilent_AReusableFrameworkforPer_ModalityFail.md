---
title: Loud or Silent? A Reusable Framework for Per-Modality Failure Analysis in Multimodal Clinical AI
published: 2026-08-02T19:38:56Z
authors: Quang Bui, Shlok Jaiswal, Samuel Paik-Heintz, Kevin Zhou, Kaushik Madapati, Krittaphas Chaisutyakorn, Noah Dane Hebdon, Dimitrios Proios, Sebastián Andrés Cajas Ordóñez, Kacper Dobek, Boya Zhang, Aly Dhedhi, Ahram Han, Kushul Reddy Palakala, Rahul Gorijavolu, Jacques Kpodonu, Leo Anthony Celi
url: http://arxiv.org/abs/2608.01462v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Loud or Silent? A Reusable Framework for Per-Modality Failure Analysis in Multimodal Clinical AI

## Abstract
Multimodal clinical models are usually judged on accuracy with every modality present, but deployment removes modalities; an echocardiogram is often unavailable where an ECG is routine. Two questions then matter beyond the size of the accuracy loss: which modality was responsible, and whether the model fails loudly or silently once that modality is dropped. The distinction is per-example and modality-level, and is separate from post-hoc feature attribution (e.g. SHAP). Models are replaced often; the evaluation that answers these questions is reused. We present a model-agnostic modality-failure framework: given N modality embeddings, any mask-aware probe, and labels, it returns a per-example failure taxonomy, a per-modality complementarity matrix that attributes error to modalities, and a loud-vs-silent dropout profile separating monitorable failures from those that pass unflagged far from the decision boundary, using only deployment-observable signals. We release it as a small, unit-tested harness and validate it against planted ground truth. Across seeds it recovers that planted modality dominance and complementary subset, reports per-modality loud-vs-silent rates, and scales to a three-modality complementarity matrix; because the planted structure is known by construction, this validates recovery of per-example attribution rather than clinical performance. We then instantiate the framework on frozen EchoJEPA and HuBERT-ECG embeddings for LVEF and the EF <= 40% HFrEF gate over a paired MIMIC-IV cohort, where on the held-out test split (n = 245) dropping echo nearly doubles error. The narrow echo-to-ECG overlap that bounds cohort size is itself a deployment finding for cardiac foundation models. All of our work can be found at https://github.com/criticaldata/PRIMED-AI.

## Metadata
- **Published**: 2026-08-02T19:38:56Z
- **Authors**: Quang Bui, Shlok Jaiswal, Samuel Paik-Heintz, Kevin Zhou, Kaushik Madapati, Krittaphas Chaisutyakorn, Noah Dane Hebdon, Dimitrios Proios, Sebastián Andrés Cajas Ordóñez, Kacper Dobek, Boya Zhang, Aly Dhedhi, Ahram Han, Kushul Reddy Palakala, Rahul Gorijavolu, Jacques Kpodonu, Leo Anthony Celi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01462v1)