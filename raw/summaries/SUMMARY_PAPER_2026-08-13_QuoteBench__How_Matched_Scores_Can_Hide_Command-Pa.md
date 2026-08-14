---
title: QuoteBench: How Matched Scores Can Hide Command-Path Failures
url: http://arxiv.org/abs/2608.13547v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_17-57-20Z_QuoteBench_HowMatchedScoresCanHideCommand_PathFail.md
generated_at: 2026-08-13 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces QuoteBench to evaluate how matched execution scores can mask command-generation failures in LLM coding agents. It demonstrates that adding a parser between generation and execution degrades success rates dramatically, showing that the failure is not intrinsic but arises from boundary violations. The study shows that models like GPT-5.6-sol hide large gaps by compensating with other configurations.

## Key Takeaways
- Matched scores alone cannot differentiate command-generation errors from failures caused after generation when a parser intervenes.
- Adding an unescaped parser reduces success rates by 55.4 to 73.2 percentage points across eight configurations, indicating that boundary adaptation is key.
- Reported matched gaps such as -3.6 for GPT-5.6-sol correspond to hidden damages of -64.3 and compensations of +60.7, showing scores are misleading.

## Context
LLM coding agents often rely on matched execution scores to gauge performance, but these scores ignore the transport layer between model output and actual command execution. This paper highlights a gap in evaluation methodology that could lead to overestimating model capabilities.

## Implications
For practitioners, reporting only matched scores risks misrepresenting true performance. Future evaluations must include details about generation contract, execution path, operating point, and final-state validator to provide accurate insights into agent reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13547v1)
