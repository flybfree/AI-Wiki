---
title: Dude: A Dual-Detection Multi-Agent System for Paper-Code Discrepancy Detection
url: http://arxiv.org/abs/2609.03416v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_06-24-33Z_Dude_ADual_DetectionMulti_AgentSystemforPaper_Code.md
generated_at: 2026-09-03 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Dude, the first Dual‑Detection Multi‑Agent System designed to detect discrepancies between research papers and their code implementations. The authors demonstrate that Dude significantly improves recall and precision over baseline methods, raising F1 scores by up to 18.7% and recall by up to 22.8% on real‑world datasets.

## Key Takeaways
- Granularity asymmetry between paper‑language and code‑language causes agents to misinterpret or over‑report discrepancies, leading to high false positives.  
- The proposed granularity‑aligned negotiation mechanism aligns the fine‑grained understanding of each modality before generating a discrepancy report.  
- A two‑stage salience‑filtering process filters out spurious alerts, thereby boosting recall and precision.

## Context
The rapid growth of research submissions has strained human review capacity, prompting reliance on large language models to automate quality checks. Existing single‑agent LLM approaches suffer from limited context handling and one‑sided detection, resulting in suboptimal performance for discrepancy identification.

## Implications
For researchers, Dude offers a more reliable tool that reduces unnecessary false alarms while preserving genuine issue detection. For industry stakeholders, the system can streamline peer‑review workflows, saving time and improving overall quality control.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03416v1)
