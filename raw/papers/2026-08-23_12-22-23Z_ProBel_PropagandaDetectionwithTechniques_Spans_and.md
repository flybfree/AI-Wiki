---
title: ProBel: Propaganda Detection with Techniques, Spans, and Explanations
published: 2026-08-23T12:22:23Z
authors: Mohamed Bayan Kmainasi, Ali Ezzat Shahroor, Elisa Sartori, Giovanni Da San Martino, Firoj Alam
url: http://arxiv.org/abs/2608.22388v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ProBel: Propaganda Detection with Techniques, Spans, and Explanations

## Abstract
Propaganda detection includes several related prediction levels, ranging from sentence-level decisions to technique classification and span identification. However, it remains unclear how supervision at these levels interacts when learned jointly across Arabic and English. We present ProBel, an Arabic and English resource that aligns binary labels, multi-label annotations over 23 propaganda techniques grouped into six coarse categories, technique-labeled spans, and reference explanations for the same news sentences. It includes a substantially larger English collection and supports matched binary, coarse-grained, multi-label, and span-level tasks in both languages. We evaluate zero-shot prompting, task-specific fine-tuning, and joint training under a shared setup. A single bilingual multi-task model achieves the best overall performance and remains competitive across tasks and languages. Cross-task analysis shows that transfer depends on the supervision level. Joint classification training preserves binary performance, whereas span-only training can weaken sentence-level prediction. Joint bilingual training yields the most stable results, while monolingual fine-tuning can reduce transfer to the other language. We will release the data, code, and evaluation scripts.

## Metadata
- **Published**: 2026-08-23T12:22:23Z
- **Authors**: Mohamed Bayan Kmainasi, Ali Ezzat Shahroor, Elisa Sartori, Giovanni Da San Martino, Firoj Alam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22388v1)