---
title: Perturbation-based Regional Interpretability through Subtraction Mapping (PRISM): naming-error dissociations in language models and post-stroke aphasia
published: 2026-08-13T02:02:05Z
authors: Xiang Guan, Roger D. Newman-Norlund, Yong Yang, Saeed Ahmadi, Regan Willis, Nadra Salman, Kalil Warren, Srihari Nelakuditi, Chris Rorden, Leonardo Bonilha, Julius Fridriksson
url: http://arxiv.org/abs/2608.12717v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Perturbation-based Regional Interpretability through Subtraction Mapping (PRISM): naming-error dissociations in language models and post-stroke aphasia

## Abstract
Mechanistic interpretability of large language models lacks spatially resolved, falsifiable tools for testing whether internal components are specialized for distinct cognitive operations. We adapt subtraction analysis, the standard framework of human neuroimaging, from biological brains to perturbed transformers, and apply the same logic to both substrates in parallel. Building on the Brain-LLM Unified Model (BLUM), which showed that layer-perturbed LLaVA-1.6-Vicuna-13B error profiles match the lesion patterns of aphasic patients, we develop PRISM (Perturbation-based Regional Interpretability through Subtraction Mapping). PRISM maps the seven clinical Philadelphia Naming Test categories, subtracts error classes pairwise, and treats each perturbation seed as a subject in a group analysis with threshold-free cluster enhancement along the layer axis. We run a structurally matched analysis on 213 chronic post-stroke aphasia patients using correlation-difference lesion-symptom mapping, and replicate both sides on held-out splits. The designs match in subject dimension (seeds, patients), spatial dimension (layers, atlas-parcellated cortex) and thresholding, but the contrast operator differs: a within-subject error-proportion difference for the LLM, a between-subject correlation difference for the cortex. Both substrates recover a robust phonemic-favoring dissociation, a deep layer cluster and a frontal-perisylvian cortical cluster, both replicating; the semantic-favoring direction is a consistently signed but non-significant trend on both. PRISM thus gives a falsifiable, spatially resolved test of functional-specialization claims in transformer language models. A confirmatory ROI-level intervention (PRISM Stage 3) licensing the strongest causal-mechanism claim is left to subsequent work.

## Metadata
- **Published**: 2026-08-13T02:02:05Z
- **Authors**: Xiang Guan, Roger D. Newman-Norlund, Yong Yang, Saeed Ahmadi, Regan Willis, Nadra Salman, Kalil Warren, Srihari Nelakuditi, Chris Rorden, Leonardo Bonilha, Julius Fridriksson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12717v1)