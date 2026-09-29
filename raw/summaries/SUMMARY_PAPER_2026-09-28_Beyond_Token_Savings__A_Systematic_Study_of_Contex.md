---
title: Beyond Token Savings: A Systematic Study of Context Compression in LLM Agents
url: http://arxiv.org/abs/2609.32961v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_21-46-40Z_BeyondTokenSavings_ASystematicStudyofContextCompre.md
generated_at: 2026-09-28 21:56
model: qwen3.6-35b-a3b
---

## Summary
This study systematically investigates the impact of context compression on LLM agents by disentangling decisions regarding what, when, and how much to compress across three open-weight models. Analyzing nearly 35,000 runs on SWE-bench Verified and Terminal-Bench 1.0, the authors reveal that reducing token usage does not inherently improve execution speed or cost; for instance, Qwen-based policies using one-third of the tokens incurred 20-80% longer latencies compared to uncompressed baselines. The research underscores that compression strategies yield divergent results across models and tasks, challenging the efficacy of fixed compression policies in existing agent frameworks.

## Key Takeaways
- Token reduction is not a reliable proxy for efficiency gains: The study demonstrates that aggressive compression can significantly degrade performance metrics beyond token count. Specifically, on Terminal-Bench with Qwen, compressed policies consuming roughly one-third of the tokens required 20-80% more execution time than uncompressed agents, indicating that

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32961v1)
