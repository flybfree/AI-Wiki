---
title: Stratum: Repository Memory for Coding Agents Beyond the Context Window
url: http://arxiv.org/abs/2610.36153v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_18-53-45Z_Stratum_RepositoryMemoryforCodingAgentsBeyondtheCo.md
generated_at: 2026-10-27 20:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes Stratum, a tiered persistent memory architecture that lives alongside a code repository and serves coding agents across multiple sessions, addressing the fundamental problem that coding agents lack memory of past work despite context windows growing a thousand-fold. The authors demonstrate through empirical measurements on real repositories that the bottleneck for coding agents is not context capacity but knowledge selection and persistence, and show that a memory-augmented agent identifies root-cause files in 21 of 24 trials versus 6 of 24 for a retrieval-only baseline, at 4.5x lower median token cost.

## Key Takeaways
- Mid-size projects already exceed the largest production context windows, and storing knowledge inside the model's key-value cache costs 10,000 to 100,000 times more bytes than storing it as indexed text, making persistent external memory architectures essential rather than optional for practical coding agents.
- Analysis of 752 real bug-fix commits reveals that the median fix edits only two files, and those files plus their direct imports constitute less than 10% of the repository, proving that the critical challenge is selecting the right knowledge rather than having enough capacity to hold everything.
- Even with transitive import reachability and test links, 47% of co-edited file pairs remain structurally disconnected, meaning the knowledge needed for effective file selection must be mined from historical experience and session history rather than inferred from static code structure alone.
- Retrieval over a store of one million nodes takes 1.7 ms at the median, demonstrating that the memory layer introduces negligible latency overhead while providing substantial gains in multi-session task success and token efficiency.

## Context
This work sits at the intersection of AI coding agents, retrieval-augmented generation, and software engineering tooling. While the field has focused heavily on scaling context windows and improving single-session reasoning, this paper reframes the problem as a memory-architecture challenge, arguing that persistent, experience-aware knowledge stores are the missing infrastructure for autonomous coding agents to operate effectively across long-running development workflows.

## Implications
For practitioners building coding agents, this research suggests that investing in persistent repository memory systems will yield dramatically higher success rates and lower token costs than simply expanding context windows or improving retrieval pipelines. For the broader AI industry, the findings point toward a future where coding agents accumulate institutional knowledge about specific codebases over time, enabling them to avoid repeating failed approaches and to build on prior diagnostic reasoning, fundamentally changing how software maintenance and debugging are automated.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36153v1)
