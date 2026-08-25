---
title: SDoH-Aware Narrative Anchoring Bias in Medical LLMs for Trustworthy Clinical Decision Support
published: 2026-08-24T04:58:32Z
authors: Ahnaf Atef Choudhury, Ramkrishna Saha
url: http://arxiv.org/abs/2608.22802v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SDoH-Aware Narrative Anchoring Bias in Medical LLMs for Trustworthy Clinical Decision Support

## Abstract
Medical large language models are often judged by how many clinical questions they answer correctly. That view is useful, but it misses a practical risk. A model may know the right answer and still change its response when the same case is written in a different patient voice. This paper evaluates that risk as SDoH aware narrative anchoring bias. We use NarrativeShield SDoH MedQA, a counterfactual medical question answering dataset in which each case appears in persona based narratives while the answer key remains fixed. The dataset is reshaped from wide format into case grouped persona rows. We evaluate three open source instruction tuned LLMs from the Qwen2.5 family: 1.5B, 3B, and 7B. The final experiment uses 300 clinical cases and produces 8,100 model responses across three prompting conditions. We report persona level accuracy, counterfactual consistency, correct consistency, and narrative sensitivity error. Qwen2.5 7B achieves the best accuracy at 56.33 percent and the best correct consistency at 40.33 percent. Paired McNemar exact tests show significant accuracy gains for 7B over 3B in all prompt settings. Even so, narrative sensitivity remains, with the lowest error still at 31.67 percent. These results suggest that trustworthy clinical decision support should be evaluated by both average correctness and stability across medically equivalent patient narratives.

## Metadata
- **Published**: 2026-08-24T04:58:32Z
- **Authors**: Ahnaf Atef Choudhury, Ramkrishna Saha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22802v1)