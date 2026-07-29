---
title: AMPBench-MT: A Homology-Controlled Benchmark for Antimicrobial Peptide Potency, Spectrum, and Safety Prediction
published: 2026-07-28T10:01:30Z
authors: Ziheng Zhou, Huiyu Luo, Xiaohu Zhu, Nan Wang, Xuebiao Qin, Chaoyan Zhang, Jun Yan
url: http://arxiv.org/abs/2607.25518v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AMPBench-MT: A Homology-Controlled Benchmark for Antimicrobial Peptide Potency, Spectrum, and Safety Prediction

## Abstract
Computational AMP discovery is often evaluated through AMP/non-AMP recognition, yet follow-up decisions depend on assay-derived evidence such as target-species potency, hemolysis, toxicity, and selectivity. Existing AMP and peptide benchmarks cover binary recognition, multilabel annotation, assay regression, or broader peptide-model comparison, but they do not jointly place AMP recognition, species-conditioned potency, spectrum, safety-facing proxy endpoints, and cross-endpoint behavior within one sequence-homology-controlled protocol. To address this problem, we introduce AMPBench-MT, a provenance-preserving benchmark that standardizes canonical peptide records and organizes them into binary recognition, species-conditioned pMIC regression, and endpoint-specific potency and safety-facing readouts. Across 161 endpoint-specific model evaluations, high binary performance does not reliably indicate assay-endpoint behavior. Frozen protein-language-model embeddings form the leading pMIC error cluster, while graph and classical regressors remain close. Spectrum labels further reveal that PR-oriented metrics can be misleading under scarce observed negatives, whereas low-toxicity, HC50 hemolysis, and selectivity expose smaller but more assay-facing signals. AMPBench-MT shows that AMP evaluation should move beyond recognition leaderboards toward endpoint-aware evidence auditing. Our proposed benchmark is available at https://huggingface.co/datasets/ZihengZhou06/AMPBench-MT.

## Metadata
- **Published**: 2026-07-28T10:01:30Z
- **Authors**: Ziheng Zhou, Huiyu Luo, Xiaohu Zhu, Nan Wang, Xuebiao Qin, Chaoyan Zhang, Jun Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25518v1)