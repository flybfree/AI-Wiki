---
title: Beyond Consensus: Downward Bias and Role Asymmetry in Multi-Agent LLM Judges for Subjective Evaluation
published: 2026-08-31T07:28:55Z
authors: Minsoo Song, Chanwoo Kim, Sugyeong Eo, Chanjun Park
url: http://arxiv.org/abs/2608.30373v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Consensus: Downward Bias and Role Asymmetry in Multi-Agent LLM Judges for Subjective Evaluation

## Abstract
Multi-Agent Debate (MAD) has been widely adopted to improve LLM-based evaluation by prompting multiple agents to negotiate and reach a consensus. However, for subjective rubric-based scoring, inter-agent agreement does not guarantee alignment with human judgments. In this paper, we compare a single-judge baseline against a consensus-based MAD protocol on subjective evaluation tasks and design three ablations to isolate the impact of role prompting, multi-round interaction, and explicit score sharing. Evaluations across six LLMs show that the single-judge baseline achieves the strongest human alignment on average across six judge models, whereas MAD shows degradation in human alignment on both tasks. Our ablations demonstrate that this performance drop stems primarily from asymmetric role prompting rather than the interaction itself. Specifically, assigning a strict judge role introduces a systematic downward bias that the consensus process fails to correct. The central finding is that this bias reflects strict-stance dominance beyond averaging: the consensus score falls well beyond the arithmetic midpoint of the standalone strict and lenient conditions, rather than averaging them out. Removing role asymmetry (Symmetric MAD) largely recovers baseline performance, while masking peer scores widens inter-agent disagreement on average and worsens average human alignment. These findings demonstrate that multi-agent consensus can enforce artificial agreement at the expense of true human alignment, revealing a structural limitation in consensus-style, role-specialized MAD protocols for subjective scoring.

## Metadata
- **Published**: 2026-08-31T07:28:55Z
- **Authors**: Minsoo Song, Chanwoo Kim, Sugyeong Eo, Chanjun Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30373v1)