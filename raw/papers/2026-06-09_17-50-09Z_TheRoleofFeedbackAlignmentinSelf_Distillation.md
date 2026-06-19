---

title: The Role of Feedback Alignment in Self-Distillation
published: "2026-06-09T17:50:09Z"
authors: Semih Kara, Oğuzhan Ersoy
url: http://arxiv.org/abs/2606.11173v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# The Role of Feedback Alignment in Self-Distillation



**Source**: [Original Paper](http://arxiv.org/abs/2606.11173v1)
## Abstract
Conditioning a language model on additional context, such as feedback on a previous attempt, typically improves its response. Self-distillation trains the model to retain this improvement when the context is not present. The method works by matching the model's output distribution under two settings: a student that sees only the question, and a self-teacher that also sees the context. What the model learns therefore depends on what context the self-teacher receives, yet the design of this context remains largely unexplored.   We study context design for self-distillation by training a solver on feedback from a frozen critic. We compare three conditions: (i) a binary reward (GRPO), (ii) the reference solution, and (iii) a step-by-step critique aligned to the solver's reasoning trace.   Step-aligned critique yields the largest gains, outperforming GRPO by 16.11 points and reference-solution-conditioned self-distillation by 5.27 points (Avg@12). Per-token advantage analysis reveals why: step-aligned feedback targets only the tokens where reasoning fails, leaving correct behavior intact. Conditioning on the reference solution, by contrast, pressures the model to change its behavior at every token (even correct steps) because an alternative derivation inevitably differs in phrasing and approach. This suggests that structural alignment between feedback and the solver's reasoning is a key driver of self-distillation effectiveness.

## Metadata
- **Published**: 2026-06-09T17:50:09Z
- **Authors**: Semih Kara, Oğuzhan Ersoy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.11173v1)