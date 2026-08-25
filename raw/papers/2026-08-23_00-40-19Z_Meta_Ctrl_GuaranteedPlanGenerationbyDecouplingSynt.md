---
title: Meta-Ctrl: Guaranteed Plan Generation by Decoupling Syntactic and Semantic Constraints
published: 2026-08-23T00:40:19Z
authors: Gwen Yidou-Weng, Edward Sun, Tianyi Ma, Metin Alp Dogan, Benjie Wang, Allen Peng, Guy Van den Broeck, Yuchen Cui
url: http://arxiv.org/abs/2608.22149v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Meta-Ctrl: Guaranteed Plan Generation by Decoupling Syntactic and Semantic Constraints

## Abstract
LLMs generate fluent plans for robots but routinely violate the syntactic and se8mantic constraints they must satisfy to execute, and existing remedies trade formal guarantees against plan quality: soft methods (affordance scoring, grounded decoding) give no guarantee, while symbolic planners (LLM+P) discard the LM's commonsense. We propose \textbf{Meta-Ctrl}, a constrained-decoding framework that guarantees the encoded constraints while preserving the base LM's plan quality. Meta-Ctrl introduces \emph{meta-tokens}---a compact vocabulary of grounded actions---enforcing syntax at the token level and semantics (preconditions, goals, ordering) at the action level, an exact factorization that cuts the memory of constrained decoding from over 107TB to under 2GB. With it, a small open-weight LM becomes competitive where it otherwise sits at the bottom of the leaderboard: on WAH-NL under the LoTa-Bench protocol it reaches the highest reported subgoal success rate, exceeding GPT-4's, with consistent gains across the Embodied Agent Interface. We further demonstrate it on a real tabletop robot, where every generated plan satisfies its preconditions and goals by construction. Project website: https://meta-ctrlg.github.io/.

## Metadata
- **Published**: 2026-08-23T00:40:19Z
- **Authors**: Gwen Yidou-Weng, Edward Sun, Tianyi Ma, Metin Alp Dogan, Benjie Wang, Allen Peng, Guy Van den Broeck, Yuchen Cui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22149v1)