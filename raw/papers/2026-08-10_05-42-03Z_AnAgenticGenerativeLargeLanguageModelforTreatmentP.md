---
title: An Agentic Generative Large Language Model for Treatment Planning of Colorectal Cancer
published: 2026-08-10T05:42:03Z
authors: Mengxian Lyu, Cheng Peng, Tim Jang, Ang Li, Mengyuan Zhang, Ziyi Chen, Leighton Elliott, Tianshi Liu, Lidice Galindo, Chiranjeevi Sainatham, Oscar F. Borja-Montes, Kaleb E. Smith, Ying Zhang, Lichao Sun, Jiang Bian, Gloria Lipori, Duane A. Mitchell, Elizabeth A. Shenkman, Yi Guo, Thomas J. George, Yonghui Wu
url: http://arxiv.org/abs/2608.09142v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Agentic Generative Large Language Model for Treatment Planning of Colorectal Cancer

## Abstract
Treatment planning in precision oncology requires synthesizing heterogeneous patient information with rapidly evolving clinical guidelines to ensure guideline-concordant care. While large language models (LLMs) show promise in many diagnostic tasks, their adoption for high-stakes treatment planning is hindered by complex reasoning, adherence to timely clinical guidelines, and safety concerns. In this study, we present GatorOnco, an agentic LLM for colorectal cancer (CRC) treatment planning. GatorOnco is developed using a total of 282 billion tokens of biomedical text, including healthcare system-scale clinical text comprising 166 billion tokens from UF Health. We implemented a domain-adaptation method that integrates pre-training, model merging, a two-stage post-training approach, and agent-based reinforcement learning. An agentic retrieval-augmented generation (RAG) approach dynamically integrates time-sensitive clinical guidelines into the reasoning process. In a blind, randomized clinical evaluation conducted by five UF Health oncologists, GatorOnco significantly outperformed open-source LLMs (P < 0.01) and achieved expert-level performance comparable to UF Health oncologists. Compared with expert oncologists, GatorOnco received significantly higher ratings for readability (4.46 vs. 4.19, P < 0.01) and completeness (3.91 vs. 3.52, P < 0.01), while showing statistically comparable performance in correctness (4.09 vs. 4.11, P = 0.921), currency (4.04 vs. 3.98, P = 0.478), and safety (4.22 vs. 4.22, P = 0.999). These findings demonstrate that integrating agentic reasoning with large-scale domain adaptation can help bridge the gap for generative AI in high-stakes cancer treatment planning.

## Metadata
- **Published**: 2026-08-10T05:42:03Z
- **Authors**: Mengxian Lyu, Cheng Peng, Tim Jang, Ang Li, Mengyuan Zhang, Ziyi Chen, Leighton Elliott, Tianshi Liu, Lidice Galindo, Chiranjeevi Sainatham, Oscar F. Borja-Montes, Kaleb E. Smith, Ying Zhang, Lichao Sun, Jiang Bian, Gloria Lipori, Duane A. Mitchell, Elizabeth A. Shenkman, Yi Guo, Thomas J. George, Yonghui Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09142v1)