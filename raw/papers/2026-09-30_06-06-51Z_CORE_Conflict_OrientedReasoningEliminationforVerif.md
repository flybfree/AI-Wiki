---
title: CORE: Conflict-Oriented Reasoning Elimination for Verifiable Language-Model Search
published: 2026-09-30T06:06:51Z
authors: Siyu Song, Rui Xu, Jia Lin, Kai Liu, Weifang Wang
url: http://arxiv.org/abs/2609.39069v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CORE: Conflict-Oriented Reasoning Elimination for Verifiable Language-Model Search

## Abstract
Test-time reasoning systems often respond to failure by restarting or revising the latest step, even when an earlier decision caused the error. We introduce CORE, a search controller that requests a certified conflict core from a verifier, backjumps to the latest decision in that core, and caches the conflict to avoid repeating it. Under sound verification, finite branching and depth, and exhaustive proposals, the uncapped search is complete and never prunes a valid solution. On 2,000 planted graph-coloring instances with matched proposals and an exact verifier, CORE reduces median verifier calls by 39.8% at 30 variables and 35.0% at 36 variables relative to chronological repair; caching further improves on backjumping alone. Across five reasoning tasks, CORE achieves 75.9% mean success with Qwen2.5-7B-Instruct and 84.2% with Qwen3-8B, compared with 72.5% and 81.8% for Tree of Thoughts. It also uses fewer verifier calls and generated tokens on both backbones. These results show the value of using certified failure explanations to direct language-model search.

## Metadata
- **Published**: 2026-09-30T06:06:51Z
- **Authors**: Siyu Song, Rui Xu, Jia Lin, Kai Liu, Weifang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39069v1)