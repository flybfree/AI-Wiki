---
title: HANIA: Planner-Guided Multimodal Graph Evidence Selection for Grounded Question Answering
published: 2026-08-29T06:38:21Z
authors: Zafar Ali, Asad Khan, Nimbeshaho Thierry, Nabila Amir, Adam A. Q. Mohammed, Pavlos Kefalas
url: http://arxiv.org/abs/2608.29088v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HANIA: Planner-Guided Multimodal Graph Evidence Selection for Grounded Question Answering

## Abstract
Multimodal question answering remains sensitive to noisy, incomplete, and weakly grounded evidence. Long unstructured contexts can introduce redundancy and encourage unsupported generation, while flat retrieval may overlook relations needed for multi-step reasoning. We present HANIA, a planner-guided multimodal graph framework for evidence-grounded question answering. HANIA processes the supplied image and text using a frozen vision-language model to extract concise question-relevant visual evidence with explicit abstention. It then constructs an input-grounded multimodal graph and applies a two-group finite-state planner to coordinate descriptive and relational evidence. Coverage-aware pruning retains a compact evidence set based on relevance, graph confidence, concept coverage, and modality diversity. The selected passages, visual statements, and graph triples are provided to a frozen instruction-tuned decoder. We evaluate HANIA on ScienceQA using answer accuracy, evidence-filtering quality, evidence-budget sensitivity, and efficiency. The results show that structured evidence planning and compact graph-guided retrieval can support competitive multimodal question answering without target-dataset fine-tuning or iterative retrieval. The code is available at https://github.com/Zafar-southeast/HANIA.

## Metadata
- **Published**: 2026-08-29T06:38:21Z
- **Authors**: Zafar Ali, Asad Khan, Nimbeshaho Thierry, Nabila Amir, Adam A. Q. Mohammed, Pavlos Kefalas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29088v1)