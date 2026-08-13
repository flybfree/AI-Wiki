---
title: Cross-Corpus Evaluation of Generalizable Vulnerability Detection in IoT Firmware
url: http://arxiv.org/abs/2608.11492v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_23-05-27Z_Cross_CorpusEvaluationofGeneralizableVulnerability.md
generated_at: 2026-08-12 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper introduces IoTVulBench, a human‑verified benchmark for cross‑corpus firmware vulnerability detection that evaluates models across heterogeneous datasets and architectures. The results show that domain‑matched training with curriculum learning yields higher MCC scores than existing benchmarks such as PrimeVul and D2A.

## Key Takeaways  
- IoTVulBench achieved an MCC of 0.58 on a contamination‑screened target, outperforming PrimeVul (0.44) and D2A (0.39).  
- Staged curriculum learning raised the MCC to 0.69, while a diversity‑optimized ensemble reached 0.73, improving by 0.42 points over the strongest static analyzer at 0.31.  
- At a 0.5% false‑positive rate the model missed only 21% of vulnerabilities compared with 71% for the best comparator.

## Context  
Firmware vulnerability detection is hampered by limited, non‑diverse datasets and models that fail to generalize across real IoT platforms. This work addresses those gaps by providing a benchmark that incorporates human verification and contamination screening, offering a more realistic measure of model robustness.

## Implications  
The findings suggest that curriculum design and data diversity are more critical than raw model scale for reliable vulnerability detection in IoT applications. Practitioners can leverage these insights to build deployment‑ready configurations that balance accuracy with false‑positive rates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11492v1)
