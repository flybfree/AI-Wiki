---
title: RESKILL: Explicit Failure Attribution and Structured Repair for Interactive Language Agents
url: http://arxiv.org/abs/2609.15684v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-14_14-55-13Z_RESKILL_ExplicitFailureAttributionandStructuredRep.md
generated_at: 2026-09-15 01:23
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
The paper introduces RESKILL, a structured repair framework designed to enhance how interactive language agents handle post-failure skill updates. Unlike traditional opaque one-shot reflection methods, RESKILL maintains an explicit repair state across multiple rounds by linking failure hypotheses to candidate patches and using retest outcomes to guide iterative improvements. Evaluated on ALFWorld and TextCraft under fixed repair budgets, the framework consistently outperforms direct and hypothesis-conditioned repair baselines, demonstrating that integrating explicit attribution with persistent retest-driven updates yields more durable performance gains.

## Key Takeaways
- RESKILL replaces opaque one-shot reflection with a structured, multi-round repair process that explicitly tracks how failure explanations relate to candidate skill patches and carries unsuccessful retest outcomes into subsequent editing rounds.
- The framework employs coverage-based attribution to select local repairs, allowing the language model to supply structured factors while the system compares patches against active failure hypotheses to determine which edits are most likely to succeed in the environment.
- Across six benchmark-model settings on ALFWorld and TextCraft, RESKILL achieved the highest final success rates, improving average performance by 3.7 percentage points over direct repair and 3.3 points over hypothesis-conditioned repair, highlighting that explicit attribution must be paired with iterative retest feedback for lasting improvement.

## Context
As language agents increasingly depend on reusable skills to navigate complex interactive environments, the ability to systematically recover from failures has become a critical bottleneck in agent reliability and scalability. Traditional repair mechanisms often lack transparency and fail to leverage historical failure data effectively, limiting their capacity for sustained learning. This work addresses that gap by formalizing a structured repair loop that aligns with modern research emphasizing explainable, iterative agent refinement and empirical validation.

## Implications
The findings suggest that practitioners building interactive language agents should move beyond single-step error correction and adopt multi-round, attribution-driven repair pipelines to maximize long-term task success. By making failure hypotheses explicit and conditioning future edits on empirical retest results, developers can create more robust systems capable of self-correcting in dynamic environments. This approach also provides a clearer framework for evaluating agent resilience, potentially influencing how reliability benchmarks are designed and optimized in future AI research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15684v1)
