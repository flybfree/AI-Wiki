---
title: CodeHealth Predicts the Token Cost of Agentic Code Review: A Pre-Registered Study of 465 Agent-Authored Pull Requests
url: http://arxiv.org/abs/2610.21914v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_14-00-33Z_CodeHealthPredictstheTokenCostofAgenticCodeReview_.md
generated_at: 2026-10-15 22:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This pre-registered observational study examines whether a code quality metric called CodeHealth predicts the token cost incurred by multi-agent LLM pipelines performing code review and fix on agent-authored pull requests. Analyzing 465 PRs from 246 repositories using a frozen five-agent pipeline across three different LLMs, the authors find that higher CodeHealth scores are consistently associated with lower token costs, with each CodeHealth point linked to a 3.5% to 6.1% reduction in inference cost. The association is not explained by PR size but appears mediated by file size, suggesting that structural code quality directly influences how much computational effort agentic review pipelines require.

## Key Takeaways
- Across all three LLMs tested, the CodeHealth coefficient in the mixed model was negative with 95% confidence intervals excluding zero, meaning healthier code reliably required fewer tokens to review and fix. Each additional CodeHealth point corresponded to a 3.5% to 6.1% reduction in token cost, a statistically significant but modest per-point effect that nonetheless compounds across large codebases.
- CodeHealth was found to be unrelated to PR footprint, ruling out the confound that larger or more complex pull requests simply score lower on quality metrics. The effect was localized to the review stage, where agents iterated more heavily on unhealthy code without producing proportionally more comments, indicating that poor code structure increases the number of reasoning passes agents must perform.
- Adjusting for the size of the scored files absorbed the CodeHealth–token-cost association, which the authors interpret as mediation by file size. This means the practical lever for reducing agentic review costs is not merely improving a numerical quality score but restructuring code into smaller, more modular files, and two of three registered code smells independently predicted fix cost.

## Context
As organizations increasingly delegate code review to multi-agent LLM pipelines billed per token, understanding what drives inference cost has become a critical operational question. Prior research has established that low code quality increases human maintenance effort, but the parallel question of whether code quality also inflates the computational cost of automated agentic review had not been empirically measured. This paper fills that gap by providing the first pre-registered, stratified observational evidence linking a human-calibrated quality metric to the token expenditure of frozen multi-agent pipelines, bridging software engineering quality research and LLM inference economics.

## Implications
For practitioners deploying agentic code review pipelines, the findings suggest that investing in refactoring and file-size reduction yields a dual benefit: it lowers human maintenance burden and directly reduces per-PR inference costs in token-billed agent systems. The modest per-point effect means organizations should not expect dramatic savings from minor quality tweaks, but the mediation-by-file-size mechanism implies that structural restructuring—splitting large files, reducing coupling—carries a more tangible cost reduction than superficial score improvements. For the broader field, this work establishes a methodological template for pre-registered studies that connect software quality metrics to LLM operational costs, opening a research agenda on how codebase architecture shapes the economics of AI-assisted development workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21914v1)
