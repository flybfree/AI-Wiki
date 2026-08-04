---
title: DeBERTa-Sentinel: Toward Transparent and Trustworthy Detection of AI-Generated Text
published: 2026-08-02T07:08:20Z
authors: Muhammad Yousaf Rehman, Muhammad Islam
url: http://arxiv.org/abs/2608.01046v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeBERTa-Sentinel: Toward Transparent and Trustworthy Detection of AI-Generated Text

## Abstract
The rapid spread of large language models (LLMs) across the web raises concerns about misinformation, academic integrity, automated content manipulation, and risks to vulnerable online communities. Existing transformer-based detectors, such as GPT-Sentinel, show promise but struggle to generalize to diverse model outputs and paraphrasing attacks, limiting their role in building trustworthy web ecosystems. This work introduces DeBERTa-Sentinel, a responsible AI-generated text detection framework leveraging DeBERTa-v3's disentangled attention to capture subtle structural irregularities in synthetic content. A central design principle is transparency: unlike black-box commercial detectors, DeBERTa-Sentinel exposes token-level explanations of its decisions, enabling affected stakeholders journalists, educators, and platform trust and safety teams to audit, challenge, and contextualize detection outcomes. Using the GLC-AIText dataset of 28,057 human and LLM-generated samples (GPT, LLaMA, and Claude) with a 60-20-20 split, DeBERTa-Sentinel achieves 98.21\% validation accuracy and surpasses the RoBERTa-Sentinel baseline from NeurIPS 2025, achieving 97.53\% test accuracy, 95.89\% precision, 99.33\% recall, and 99.53\% ROC-AUC, and maintaining a 0.665\% false negative rate. The model's interpretability reveals linguistic markers such as academic phrasing and formal transitions associated with synthetic text, directly supporting stakeholder needs for verifiable, auditable content-authenticity decisions. By advancing responsible detection methods that reduce bias and enhance explainability, DeBERTa-Sentinel promotes trustworthy, ethical, and human-centric AI systems. Code and data are available at https://github.com/Galileo-Galili/HUMAN-VS-AI-TEXT-DETECTION.

## Metadata
- **Published**: 2026-08-02T07:08:20Z
- **Authors**: Muhammad Yousaf Rehman, Muhammad Islam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01046v1)