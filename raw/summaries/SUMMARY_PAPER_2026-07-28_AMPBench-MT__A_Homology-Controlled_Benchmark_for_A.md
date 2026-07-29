---
title: AMPBench-MT: A Homology-Controlled Benchmark for Antimicrobial Peptide Potency, Spectrum, and Safety Prediction
url: http://arxiv.org/abs/2607.25518v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_10-01-30Z_AMPBench_MT_AHomology_ControlledBenchmarkforAntimi.md
generated_at: 2026-07-28 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper introduces AMPBench-MT, a homology‑controlled benchmark that evaluates antimicrobial peptide (AMP) predictions across binary recognition, species‑conditioned potency regression, spectrum labeling, and safety‑facing endpoints. Experiments across 161 endpoint‑specific model evaluations show that high binary performance does not guarantee correct assay behavior, highlighting the need for endpoint‑aware evaluation.

## Key Takeaways  
- Frozen protein‑language‑model embeddings consistently cluster as the source of pMIC prediction errors, whereas graph and classical regressors perform comparably.  
- Spectrum labels expose PR‑oriented metrics as misleading when observed negatives are scarce, while low toxicity, HC50 hemolysis, and selectivity reveal smaller but more assay‑facing signals.  
- AMP evaluation must shift from recognition leaderboards to endpoint‑aware evidence auditing, as the benchmark demonstrates.

## Context  
Current AMP discovery benchmarks often focus on binary classification or aggregate regression, ignoring how predictions behave under specific experimental conditions such as toxicity or hemolysis. This limits their utility for guiding wet‑lab follow‑up and resource allocation in computational drug design.

## Implications  
For researchers and industry practitioners, AMPBench-MT provides a unified protocol to assess both potency and safety of predicted peptides, reducing false positives that could lead to costly experimental failures. The benchmark encourages the development of models that prioritize endpoint relevance over raw binary accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25518v1)
