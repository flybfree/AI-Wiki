---
title: RAG Collapse: LLM Responses Collapse When Retrieved Documents Are Self-Authored
published: 2026-08-22T22:06:44Z
authors: Gregory Druck, Ethan Smith
url: http://arxiv.org/abs/2608.22118v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RAG Collapse: LLM Responses Collapse When Retrieved Documents Are Self-Authored

## Abstract
LLM responses are based on the internet (via training or RAG), and AI is now used to generate a significant amount of content online (Paredes et al., 2026), creating the potential for a self-reinforcing feedback loop. Prior work has shown that when LLMs are recursively trained on their own output, they experience model collapse (Shumailov et al., 2024): responses become less diverse, and eventually no longer resemble the original training data. In this paper, we show that a similar collapse occurs if LLM-based AI systems retrieve references they authored using a search tool. We call this RAG collapse. We conduct extensive experiments with three types of simulations of AI systems retrieving references they generated, using three model families, and 1,019 information-seeking prompts, totaling 1,528 simulations and over one million LLM API calls, and find that 79.6% (1,216/1,528) of simulations end in collapse. Surprisingly, even a single self-authored reference can trigger collapse because the LLM disproportionately cites its own content. This self-bias persists even after controlling for reference quality.

## Metadata
- **Published**: 2026-08-22T22:06:44Z
- **Authors**: Gregory Druck, Ethan Smith
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22118v1)