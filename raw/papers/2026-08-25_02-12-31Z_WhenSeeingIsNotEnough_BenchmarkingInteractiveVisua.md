---
title: When Seeing Is Not Enough: Benchmarking Interactive Visual Grounding in LVLMs
published: 2026-08-25T02:12:31Z
authors: Zhengxiang Wang, Owen Rambow
url: http://arxiv.org/abs/2608.23978v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Seeing Is Not Enough: Benchmarking Interactive Visual Grounding in LVLMs

## Abstract
Visual grounding is typically evaluated as a one-shot mapping from an informative referring expression to a visual target. This formulation misses a central property of real-world reference: target information is often incomplete, ambiguous, and established through interaction. We introduce a controlled evaluation framework for interactive visual grounding in large vision-language models (LVLMs), varying how much target information is provided upfront and how much must be acquired through dialogue. Across four human-grounded visual contexts and four interaction protocols, current LVLMs perform significantly below task-level human baselines. Interaction can help when follow-up questions refine or repair an initial target description. Performance is lowest when no initial description is provided and target information must be acquired through questions, indicating that proactive question-driven grounding remains difficult. LVLMs are also poorly calibrated, often reporting confidence that exceeds their empirical accuracy. Follow-up studies confirm these patterns across varied description sources (human versus AI), reasoning efforts, repeated interactions, description providers, and visual contexts. Overall, interactive visual grounding remains an important challenge, requiring visual matching, information seeking and synthesis.

## Metadata
- **Published**: 2026-08-25T02:12:31Z
- **Authors**: Zhengxiang Wang, Owen Rambow
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23978v1)