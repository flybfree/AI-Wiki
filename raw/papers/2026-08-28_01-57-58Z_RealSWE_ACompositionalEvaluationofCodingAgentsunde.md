---
title: RealSWE: A Compositional Evaluation of Coding Agents under Realistic User Requests
published: 2026-08-28T01:57:58Z
authors: Gyuhyeong Kim, Hyojung Gwon, Jeonghyeon Kim, Kyuhong Shim, Sunjae Lee
url: http://arxiv.org/abs/2608.27831v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RealSWE: A Compositional Evaluation of Coding Agents under Realistic User Requests

## Abstract
Coding agents are now commonly evaluated on the SWE-bench family of benchmarks, whose tasks are built from curated GitHub issues--long, structured, and information-rich. Real user requests, however, are typically far shorter and less structured. To characterize this gap, we define a six-category information taxonomy and four dimensions of linguistic style, and apply them to real user prompts from SWE-chat and problem statements from SWE-bench Verified and Pro. We find that requests carrying only a problem statement, alone or with limited additional context, account for 88% of real prompts but just 7% of benchmark problems. Furthermore, 87% of real prompts are casually written whereas 94% of benchmark problems are formal. Guided by these observations, we introduce sys, 381 multi-variant task families derived from SWE-bench Verified and Pro. Variants within each family share the same underlying task and gold patch while differing only in information composition and linguistic style. Evaluating seven contemporary LLMs with sys, we find that i) realistic inputs reduce resolution rates by 6.4 pp on average and can change model rankings. Controlled analysis further shows that ii) including Desired Behavior and Motivation significantly affects performance, whereas Environment Information and Reproduction Steps merely add tokens without measurable benefit; iii) linguistic style has only small, model-dependent effects. These findings provide actionable guidance for users and agents: explicitly stating the desired behavior and motivation--which most real prompts omit--substantially improves the LLM's software engineering performance.

## Metadata
- **Published**: 2026-08-28T01:57:58Z
- **Authors**: Gyuhyeong Kim, Hyojung Gwon, Jeonghyeon Kim, Kyuhong Shim, Sunjae Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27831v1)