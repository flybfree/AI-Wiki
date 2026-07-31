---
title: SpecCal: Ambiguity-Aware Candidate Calibration for Infrared Spectrum-Based Molecular Structure Reconstruction
published: 2026-07-30T07:21:55Z
authors: Yixuan Chen, Bo Liu, Yusen Tan, Guokun Yang, Wenjie Du, Jun Xia
url: http://arxiv.org/abs/2607.27788v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SpecCal: Ambiguity-Aware Candidate Calibration for Infrared Spectrum-Based Molecular Structure Reconstruction

## Abstract
Inferring molecular structures from infrared (IR) spectra is a fundamental yet challenging problem. A key difficulty is that an IR spectrum provides limited structural information: different molecules may share similar functional groups and local vibrational patterns, leading to highly similar spectral responses. Thus, even when an observed spectrum has a unique underlying structure, reconstructing it from the spectrum remains ambiguous. Existing IR-to-molecule models usually generate a ranked set of candidate molecules, but this set is largely determined by the model's learned generation preference and may not fully capture the structures that best satisfy the observed spectral constraints. To address this limitation, we propose SpecCal, a training-free candidate calibration framework for IR-to-molecule prediction. SpecCal operates on the candidate outputs of existing base models and improves the prediction set by re-ranking current candidates while introducing additional structurally plausible alternatives guided by spectral consistency. The framework is plug-and-play and model-agnostic, requiring no parameter updates for integration with diverse base models. Experiments on multiple benchmarks show that SpecCal consistently improves top-k reconstruction at both SMILES and scaffold levels across different base models. Further analyses demonstrate that calibrating candidate sets under spectral ambiguity provides a practical way to improve molecular reconstruction from IR spectra. The code is available at: https://anonymous.4open.science/r/SpecCal-B18A.

## Metadata
- **Published**: 2026-07-30T07:21:55Z
- **Authors**: Yixuan Chen, Bo Liu, Yusen Tan, Guokun Yang, Wenjie Du, Jun Xia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27788v1)