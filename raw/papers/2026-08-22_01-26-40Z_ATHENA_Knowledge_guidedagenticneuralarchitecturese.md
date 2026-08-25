---
title: ATHENA: Knowledge-guided agentic neural architecture search for AutoFormer-based electronic health record modeling
published: 2026-08-22T01:26:40Z
authors: Deyi Li, Qi Xu, Lingyao Li, Tiansheng Wang, Muxuan Liang, Mei Liu
url: http://arxiv.org/abs/2608.21712v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ATHENA: Knowledge-guided agentic neural architecture search for AutoFormer-based electronic health record modeling

## Abstract
Transformer-based models are widely used for clinical prediction from electronic health records (EHRs), yet their architectures still require substantial manual tuning, and the optimal configuration may vary across tasks and hospitals. Neural architecture search (NAS) automates architecture design, but conventional methods are computationally costly for Transformer-based EHR models. Recent large language model (LLM)-guided NAS methods reduce manual search design but typically conduct each search independently, without reusing architecture knowledge across hospitals. In this study, we propose ATHENA (Agentic Transfer across Hospitals for EHR Neural Architecture Search), a knowledge-guided agentic NAS framework for Transformer-based EHR modeling. ATHENA uses a weight-sharing supernet that is pretrained once per hospital, allowing candidate architectures to be instantiated as inherited subnetworks and evaluated through fine-tuning rather than independent pretraining. It also incorporates a two-layer cross-hospital architecture prior. The first layer retrieves high-performing architecture examples from source sites based on task descriptors, while the second estimates the effects of architectural components using SHapley Additive exPlanations (SHAP)-based meta-regression. These priors guide a multi-agent LLM search together with validation feedback from the target hospital. Across six clinical prediction tasks and two independent health systems, ATHENA matches or outperforms four NAS baselines in 9 of 12 hospital-task evaluations at a search budget of 30. It also shows more consistent architecture selection across repeated searches. ATHENA provides a practical approach for reducing manual architecture tuning in Transformer-based EHR modeling. Code is publicly available at https://github.com/GatorAIM/ATHENA.

## Metadata
- **Published**: 2026-08-22T01:26:40Z
- **Authors**: Deyi Li, Qi Xu, Lingyao Li, Tiansheng Wang, Muxuan Liang, Mei Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21712v1)