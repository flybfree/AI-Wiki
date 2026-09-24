---
title: Fine-Tuning LLMs for Translation: General Forgetting Mitigation Does Not Preserve MT-Specific Instruction Following
published: 2026-09-23T17:02:59Z
authors: Niklas Scholz, David Thulke, Abdallah Nasir, Will Allred, Evgeny Matusov, Hermann Ney
url: http://arxiv.org/abs/2609.28395v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fine-Tuning LLMs for Translation: General Forgetting Mitigation Does Not Preserve MT-Specific Instruction Following

## Abstract
Fine-tuning large language models on parallel data improves translation quality but can cause catastrophic forgetting. Mitigation methods are generally evaluated by retention on general benchmarks. We ask whether these findings transfer to machine translation (MT) fine-tuning and to MT-specific instruction following (MT-IF): instructions that modify a translation, such as formality, grammatical gender, and length control. We compare methods anchored to auxiliary data, to model outputs, and to the base model parameters, first in a screening study with Llama 3.2 1B Instruct, then on Llama 3.1 8B Instruct fine-tuned on bidirectional Arabic-English or Spanish-English data. Elastic Weight Consolidation preserves general capabilities best in both stages; on the 8B Spanish model the average score on general benchmarks drops 1.7 points versus 11.0 for standard fine-tuning, yet its scores for formality and grammatical gender control remain close to standard fine-tuning. Only data mixing with control-task examples preserves these controls, but its gains do not transfer to unseen prompts for the same task.

## Metadata
- **Published**: 2026-09-23T17:02:59Z
- **Authors**: Niklas Scholz, David Thulke, Abdallah Nasir, Will Allred, Evgeny Matusov, Hermann Ney
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28395v1)