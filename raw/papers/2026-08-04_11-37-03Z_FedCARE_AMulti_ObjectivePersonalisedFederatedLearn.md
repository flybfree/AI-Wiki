---
title: FedCARE: A Multi-Objective Personalised Federated Learning Framework for Smart Healthcare
published: 2026-08-04T11:37:03Z
authors: Rojalini Tripathy, Padmalochan Bera, Shreya Ghosh, Rajkumar Buyya
url: http://arxiv.org/abs/2608.03498v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedCARE: A Multi-Objective Personalised Federated Learning Framework for Smart Healthcare

## Abstract
Federated Learning (FL) enables collaborative model training across distributed healthcare institutions without centralising sensitive patient data. However, real-world healthcare federations are often characterised not only by non-IID data, but also by heterogeneous clinical objectives and partially overlapping feature spaces. Different hospitals may optimise distinct and potentially conflicting objectives, such as mortality risk prediction, readmission reduction, or length-of-stay estimation, while also retaining institution-specific clinical features that cannot be shared with other participants. Existing personalised FL methods mainly address statistical heterogeneity, whereas multi-objective FL approaches typically learn a shared global model without explicit client-level adaptation. To address these limitations, we propose \textbf{FedCARE}, a multi-objective personalised FL framework for smart healthcare services. FedCARE follows a two-stage training strategy. First, it learns a shared global backbone from common clinical features using Pareto-driven multi-objective federated optimisation. Second, each client independently fine-tunes the shared backbone using its private features and local clinical objectives, enabling institution-specific personalisation without additional communication overhead. We implement FedCARE in a cloud-based client-server federated deployment on the Melbourne Research Cloud and evaluate it on two real-world healthcare datasets, MIMIC-III and Diabetes 130-US Hospitals. Experimental results show that FedCARE consistently outperforms standard FL, multi-objective FL, and personalised FL baselines, achieving up to 12.5% AUROC improvement and 32.0% MAE reduction over FedAvg.

## Metadata
- **Published**: 2026-08-04T11:37:03Z
- **Authors**: Rojalini Tripathy, Padmalochan Bera, Shreya Ghosh, Rajkumar Buyya
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03498v1)