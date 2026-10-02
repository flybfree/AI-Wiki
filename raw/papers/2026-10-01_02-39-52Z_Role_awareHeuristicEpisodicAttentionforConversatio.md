---
title: Role-aware Heuristic Episodic Attention for Conversational LLMs
published: 2026-10-01T02:39:52Z
authors: Wanyang Hong, Zhaoning Zhang, Yi Chen, Libo Zhang, Baihui Liu, Linbo Qiao, Zhiliang Tian, Dongsheng Li
url: http://arxiv.org/abs/2610.00958v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Role-aware Heuristic Episodic Attention for Conversational LLMs

## Abstract
Large language models often lose track of persistent instructions and relevant information as multi-turn conversations grow. We study this cumulative contextual decay through three related failure modes: attention pollution, dilution, and drift. We propose REA (Role-aware Heuristic Episodic Attention), a context-management framework that assigns different persistence and representation policies to instructions and episodic interactions. Instructional Memory retains identified global constraints in a dedicated prefix. Episodic Memory preserves user inputs and compresses model replies, while heuristic retrieval selects raw text, compressed representations, or omission for each historical turn. On Long-MT-Bench+, REA improves the judge score from 6.32 to 7.36 on a 10-point scale, a 16.5% relative gain over the Vanilla baseline, and reduces average latency by 2.91$\times$. Additional evaluations show aggregate gains on three backbones spanning 1.7B-7B parameters and on Chinese and English role-playing tasks. These results support role-aware context management as a practical approach to maintaining conversational continuity and instruction adherence.

## Metadata
- **Published**: 2026-10-01T02:39:52Z
- **Authors**: Wanyang Hong, Zhaoning Zhang, Yi Chen, Libo Zhang, Baihui Liu, Linbo Qiao, Zhiliang Tian, Dongsheng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00958v1)