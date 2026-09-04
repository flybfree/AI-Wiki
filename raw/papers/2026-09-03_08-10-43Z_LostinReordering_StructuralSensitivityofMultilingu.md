---
title: Lost in Reordering: Structural Sensitivity of Multilingual LLMs under Semantics-Preserving Perturbations
published: 2026-09-03T08:10:43Z
authors: Karthika Nhayakkat, Rajat Verma, Maharaj Brahma, Vetcha Gnana Mahesh, Maunendra Sankar Desarkar, Ganesh Ramakrishnan, Rohit Saluja
url: http://arxiv.org/abs/2609.03511v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lost in Reordering: Structural Sensitivity of Multilingual LLMs under Semantics-Preserving Perturbations

## Abstract
Large Language Models (LLMs) demonstrate strong multilingual reasoning performance, yet their robustness to semantics-preserving structural variation remains underexplored, particularly for relatively free word-order languages. We investigate the structural sensitivity of multilingual LLMs using two linguistically grounded perturbation settings in Hindi and Malayalam: constrained constituent reordering and active-passive voice transformation. We introduce a benchmark dataset IndicReStruct, with two variants, GSM8K-Reordered and GSM8K-Voice, constructed from GSM8K while preserving semantic meaning. Across six state-of-the-art LLMs and multiple prompting strategies, we observe consistent and significant degradation in mathematical reasoning performance under structurally perturbed inputs. To further understand these failures, we perform qualitative error analysis and mechanistic interpretability experiments using residual-stream activation patching. Our analyses show that reasoning failures frequently arise from disruptions in entity-quantity alignment and that intermediate transformer layers contribute most strongly toward reasoning restoration. Overall, our findings suggest that current multilingual LLMs remain highly sensitive to surface syntactic realization and lack robust compositional invariance under structurally different but semantically equivalent inputs.

## Metadata
- **Published**: 2026-09-03T08:10:43Z
- **Authors**: Karthika Nhayakkat, Rajat Verma, Maharaj Brahma, Vetcha Gnana Mahesh, Maunendra Sankar Desarkar, Ganesh Ramakrishnan, Rohit Saluja
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03511v1)