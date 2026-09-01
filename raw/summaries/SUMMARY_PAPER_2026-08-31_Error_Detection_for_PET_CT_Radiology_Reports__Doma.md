---
title: Error Detection for PET/CT Radiology Reports: Domain-Specific vs Large Language Models
url: http://arxiv.org/abs/2608.30021v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_20-23-01Z_ErrorDetectionforPET_CTRadiologyReports_Domain_Spe.md
generated_at: 2026-08-31 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates language models for detecting clinically meaningful errors in PET/CT oncology reports, comparing compact domain‑specific BERT variants with state‑of‑the‑art open‑weight LLMs. The results show that a 15 million‑parameter domain model achieves 94.4% balanced accuracy, outperforming the best prompted LLM and matching performance after task‑specific adaptation of Llama‑3.3‑70B while retaining higher computational demands.

## Key Takeaways
- A compact 15M‑parameter BERT model reaches 94.4% balanced accuracy with a 5.8% false‑positive rate, demonstrating that domain‑specific training can rival large LLMs on PET/CT error detection.
- The strongest zero‑shot LLM (Qwen3‑32B) scores only 84.0%, highlighting the gap between model scale and task performance without fine‑tuning.
- Task‑specific adaptation of Llama‑3.3‑70B restores the domain model’s accuracy, underscoring that model size alone is less important than appropriate training data.

## Context
Radiology report errors can lead to misdiagnosis and patient harm, yet automated quality assurance tools remain limited by the need for specialized knowledge. This study addresses that gap by applying AI to a challenging PET/CT dataset, showing how domain‑aware models can be both accurate and efficient compared with generic LLMs.

## Implications
Clinicians and radiology departments can adopt lightweight, fine‑tuned language models for automated report checks without the cost of massive compute resources. This approach supports scalable quality assurance pipelines that maintain high detection rates while preserving operational efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30021v1)
