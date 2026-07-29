---
title: Rethinking CD: A Reproducibility Study and Extension on the Ineffectiveness of Contrastive Decoding at Mitigating Object Hallucinations in MLLMs
url: http://arxiv.org/abs/2607.25196v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_01-55-58Z_RethinkingCD_AReproducibilityStudyandExtensiononth.md
generated_at: 2026-07-28 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper reproduces and extends the study of contrastive decoding (CD) in multimodal large language models, showing that CD’s reported gains on hallucination benchmarks are often spurious. Experiments across MME, POPE, and CHAIR with LLaVA and Qwen reveal that CD does not consistently improve visual grounding and may even shift output distributions unidirectionally.

## Key Takeaways
- CD induces a unidirectional output distribution shift in discriminative datasets, suggesting the improvements are not genuine.  
- The adaptive plausibility constraint (APC) reduces sampling to greedy search on both discriminative and generative benchmarks.  
- Hallucination signals propagate through each layer of expert and amateur models, indicating no robust mitigation.

## Context
Contrastive decoding has become a popular training‑free technique for reducing object hallucinations in multimodal LLMs, yet its effectiveness remains debated due to limited reproducibility across datasets. This study provides the first systematic replication and broader evaluation beyond the original benchmark.

## Implications
The findings challenge practitioners relying on CD as a reliable solution for visual grounding, urging research into more consistent and dataset‑agnostic methods. For industry users, it highlights the need to validate model improvements with rigorous cross‑dataset testing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25196v1)
