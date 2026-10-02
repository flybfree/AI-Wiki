---
title: Agents Are Systems, Not Models: Rethinking Agentic Evaluation
url: http://arxiv.org/abs/2610.01618v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_12-55-07Z_AgentsAreSystems_NotModels_RethinkingAgenticEvalua.md
generated_at: 2026-10-01 21:58
model: qwen3.6-35b-a3b
---

## Summary
This paper argues that agent evaluations should treat agents as configurable systems rather than fixed entities, revealing that configuration choices significantly impact performance, cost, and consistency. Using a new benchmark of scientific coding tasks, the authors demonstrate that task information has the largest effect on outcomes, surpassing model size and time budget, while run-to-run variability accounts for over half of the outcome variance. The study concludes that desired behaviors are often better implemented through system design than prompting and releases a comprehensive benchmark with thousands of trajectories to support this shift in evaluation methodology.

## Key Takeaways
- Configuration choices drive significant performance differences, with task information proving more influential on outcomes than both time budget and backbone model size, while also reducing costs and improving calibration; additionally, approximately 54% of outcome variance stems from run-to-run repetition within the same configuration rather than changes to the configuration itself.
- Agent behaviors exhibit complex interactions where factors like time budget only provide benefits when paired with sufficient information or a capable model, and behavioral analysis shows that providing a dedicated verification tool substantially alters agent behavior compared to merely prompting for self-verification, suggesting system-level implementations are more effective than prompt-based requests.
- The research advocates for a fundamental rethinking of agentic evaluation by treating agents

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.01618v1)
