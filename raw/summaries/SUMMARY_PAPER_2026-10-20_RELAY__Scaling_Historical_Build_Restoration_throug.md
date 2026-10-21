---
title: RELAY: Scaling Historical Build Restoration through Rule Reuse and Agentic Repair
url: http://arxiv.org/abs/2610.27784v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_07-49-56Z_RELAY_ScalingHistoricalBuildRestorationthroughRule.md
generated_at: 2026-10-20 22:11
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Relay, a hybrid framework designed to address the critical problem of "environment decay" in historical software build restoration, where external dependencies like base images and packages change independently of source code. Through analysis of 14,159 OSS-Fuzz cases revealing that 69.7% no longer complete reconstruction, the authors demonstrate that most build failures share a small number of recurring symptoms that can be diagnosed once and repaired through reusable deterministic rules. Relay combines LLM-derived repair rules applied at scale with a per-case agent fallback, achieving higher restoration rates at lower cost than either approach used independently.

## Key Takeaways
- Environment decay is pervasive and quantifiable: across 14,159 OSS-Fuzz cases, 69.7% of historical builds no longer complete reconstruction and verification due to drifting external resources such as base images and package repositories. This finding establishes that the problem is not isolated but systemic, affecting the vast majority of historical software benchmarks used in vulnerability research and software engineering studies.
- Recurring failure patterns enable rule-based repair: the authors demonstrate that most build failures share a small number of recurring symptoms, meaning a single diagnosed failure can yield a deterministic repair rule applicable to many other cases. Relay uses an LLM to derive and validate these rules from representative failures, then reuses them without further model calls, dramatically reducing computational cost while matching the restoration rate of per-case agent approaches.
- A hybrid rules-first-then-agent strategy outperforms either approach alone: while reusable rules can restore as many builds as per-case agents with fewer build executions, agents successfully restore cases that rules cannot handle. The hybrid approach applies rules first and escalates only unresolved cases to an agent, yielding higher total restoration than either method independently and at lower cost than using agents alone.

## Context
This work sits at the intersection of AI-assisted software engineering, reproducible research infrastructure, and agentic systems. As vulnerability benchmarks, fuzzing studies, and software engineering experiments increasingly depend on rebuilding historical software snapshots, the fragility of external build environments threatens the reproducibility and scalability of entire research programs. Relay contributes to the broader AI research agenda by demonstrating that LLMs can be used not just for per-instance reasoning but for generating reusable, deterministic artifacts that encode domain knowledge, bridging the gap between expensive agentic reasoning and scalable deterministic automation.

## Implications
For practitioners maintaining large-scale fuzzing infrastructure, CI/CD pipelines, or vulnerability benchmark suites, Relay offers a practical pathway to restore thousands of historical builds without proportionally scaling LLM inference costs, making large-scale regression studies and security audits feasible again. For the AI research community, the paper validates a design pattern—derive rules from representative failures, apply them deterministically at scale, and reserve agentic reasoning for the long tail—that is likely transferable to other domains where recurring failure modes dominate and per-case reasoning is prohibitively expensive.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27784v1)
