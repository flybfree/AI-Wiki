---
title: TsuGO: Probing Search Efficiency in LLM Reasoning via Go Life-and-Death Problems
url: http://arxiv.org/abs/2608.13221v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_13-24-47Z_TsuGO_ProbingSearchEfficiencyinLLMReasoningviaGoLi.md
generated_at: 2026-08-13 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TsuGO, a benchmark that measures search efficiency in large language model reasoning by using Go life-and-death problems. It shows that current LLMs often perform poorly at selecting promising candidate moves and backtracking, indicating weak organization of their internal search process. The results highlight that longer outputs or higher token usage do not guarantee better solving ability.

## Key Takeaways
- Stronger models succeed by finding the correct candidate earlier and sustaining effort on productive branches.
- Most models behave closer to unguided search algorithms than to neural-guided KataGo, suggesting poor search organization.
- Longer CoT or higher Token Efficiency does not necessarily imply better search efficiency.

## Context
LLM evaluation has shifted from final accuracy to process-level metrics that capture how models plan and allocate reasoning resources. This paper fills a gap by providing a structured benchmark that isolates domain knowledge from search mechanics, enabling clearer measurement of search organization.

## Implications
For researchers, TsuGO offers a concrete way to assess whether improvements in token efficiency translate into effective search strategies. For industry practitioners, it underscores the need for models to develop robust internal planning mechanisms rather than relying solely on output length.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13221v1)
