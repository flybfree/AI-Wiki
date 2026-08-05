---
title: Relational Priors as Convergence Pressure in LLM-Based Multi-Agent Systems
published: 2026-08-04T07:11:28Z
authors: Ming Shen, Chao Shang, Sadat Shahriar, Devang Kulshreshtha, Yi Zhang, Sandesh Swamy, Yanjun Qi
url: http://arxiv.org/abs/2608.03239v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Relational Priors as Convergence Pressure in LLM-Based Multi-Agent Systems

## Abstract
Large language model-based multi-agent systems (LLM-MAS) are designed through roles, debate protocols, and aggregation rules. These choices create implicit social expectations: agents may be expected to trust, challenge, defer to, or collaborate with peers. We study the effects of making inter-agent relation semantics explicit. We use a minimal signed-network formulation of relational priors and inject natural-language renderings into agent system prompts while holding the task protocol fixed. Across a commons-governance simulation and multi-agent debate, relational priors primarily act as convergence pressure: increasing relational positivity tends to make agents coordinate or agree more readily. This pressure can help when utility rewards behavioral alignment, as in sustainable resource governance and subjective consensus. It does not, however, reliably improve accuracy. In objective QA debates, higher positivity can increase agreement even when correctness-conditioned agreement does not improve and may decline in some settings. Effects vary by model backbone, relation type, and topology; explicit neutrality is not equivalent to omitting relational framing. We argue that relational priors should not be a default add-on for LLM-MAS. Their safer use is diagnostic and task-specific: compare against a no-prior baseline, monitor correctness-conditioned metrics when truth matters, and omit the relational layer when validation does not justify it.

## Metadata
- **Published**: 2026-08-04T07:11:28Z
- **Authors**: Ming Shen, Chao Shang, Sadat Shahriar, Devang Kulshreshtha, Yi Zhang, Sandesh Swamy, Yanjun Qi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03239v1)