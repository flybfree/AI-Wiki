---
title: A Cloud-Edge System for Multimodal Clinical Screening in Resource-Constrained Rural Settings
published: 2026-08-13T02:45:40Z
authors: Hei Ting,  Chan, Chenwei Wu, Xueshen Liu, Zesen Zhao, Boyuan Zheng, Luis Filipe Nakayama, Michael G. Morley, Liyue Shen, Jiasi Chen, Z. Morley Mao
url: http://arxiv.org/abs/2608.12745v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Cloud-Edge System for Multimodal Clinical Screening in Resource-Constrained Rural Settings

## Abstract
Medical AI has demonstrated specialist-level diagnostic accuracy, yet these capabilities remain largely inaccessible in resource-constrained rural settings where bandwidth is scarce, compute is limited, and clinical decision-making requires integrating heterogeneous modalities. We introduce a cloud--edge collaborative architecture that addresses these constraints: lightweight, domain-specific models on the edge transform raw medical data into compact structured outputs, while a cloud LLM synthesizes these outputs into clinical summaries. An LLM-based orchestrator dynamically selects diagnostic tools based on patient context, promoting comprehensive modality coverage without processing irrelevant inputs. We evaluate on 20 multimodal clinical cases spanning cardiac, obstetric, trauma, and screening scenarios under three simulated network profiles (500,kbps--5,Mbps). The hybrid system achieves 98--99% diagnostic tool recall with 92--96% precision, matches or exceeds cloud-only baselines on clinical accuracy, and maintains bandwidth-invariant latency (25--35,s) at 4--15x lower token cost. These results highlight the role of architectural design in enabling efficient multimodal integration and improving factual grounding compared to cloud-only approaches under deployment constraints.

## Metadata
- **Published**: 2026-08-13T02:45:40Z
- **Authors**: Hei Ting,  Chan, Chenwei Wu, Xueshen Liu, Zesen Zhao, Boyuan Zheng, Luis Filipe Nakayama, Michael G. Morley, Liyue Shen, Jiasi Chen, Z. Morley Mao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12745v1)