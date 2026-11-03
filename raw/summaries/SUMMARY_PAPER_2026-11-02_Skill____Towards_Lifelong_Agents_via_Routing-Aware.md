---
title: Skill++: Towards Lifelong Agents via Routing-Aware Skill Refinement
url: http://arxiv.org/abs/2611.00544v1
type: paper-summary
date: 2026-11-02
source_paper: 2026-10-31_01-58-58Z_Skill___TowardsLifelongAgentsviaRouting_AwareSkill.md
generated_at: 2026-11-02 21:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses the problem of routing interference in LLM agent skill libraries, where newly added skills with similar metadata can displace previously correct routing decisions, breaking agent functionality as libraries grow. The authors propose Skill++, a method that rewrites only the name and description of each incoming skill to explicitly state what the body supports, how it differs from its closest predecessor, and what related work it excludes—without requiring router retraining or labeled data. In experiments spanning 731 skills across ten sessions, Skill++ achieves 76.3% correct skill selection versus 36.4% under original metadata, outperforming all compared baselines across three benchmarks and five LLM routers.

## Key Takeaways
- Routing interference is a fundamental failure mode in progressive-disclosure skill architectures: because the router selects skills solely by name and description metadata, a newly added skill with similar phrasing can silently displace an earlier, still-valid skill, even though neither the original skill body nor the router weights have changed. This problem is aggravated for publicly shared skills whose descriptions may not faithfully match their bodies.
- Skill++ reframes the challenge as a class-incremental continual learning problem and solves it through targeted metadata rewriting rather than model retraining. Each incoming skill's description is rewritten to include three explicit components: what the body supports, how the skill differs from its closest predecessor, and what related work it excludes. This approach avoids catastrophic forgetting inherent in router retraining and avoids the per-skill feedback requirements of prior rewriting methods.
- The method demonstrates strong generalization: performance gains hold across three distinct benchmarks, five different LLM routers, and transfer to the Codex CLI agent harness, indicating the approach is router-agnostic and practical for real-world agent deployment rather than confined to controlled benchmarks.

## Context
As LLM agents increasingly rely on modular skill libraries to extend capabilities, the scalability and reliability of skill routing become critical infrastructure concerns. This paper sits at the intersection of continual learning, retrieval-augmented generation, and agentic AI systems, addressing a gap where existing methods either risk catastrophic forgetting through router retraining or fail to handle semantically similar skills. The formulation of skill routing as class-incremental continual learning provides a principled framework that connects agent engineering to established machine learning theory, enabling the community to apply proven continual-learning insights to practical agent deployment challenges.

## Implications
For practitioners building agent platforms with growing skill libraries, Skill++ offers a training-free, data-free intervention that can be applied at skill ingestion time, dramatically reducing the operational cost of maintaining routing accuracy as libraries scale. For the broader AI field, the work highlights that metadata quality—not just model capability—is a bottleneck in agentic systems, suggesting that future agent frameworks should treat skill descriptions as first-class, versioned artifacts subject to automated refinement pipelines. Industry deployments such as Codex CLI and similar agent harnesses stand to benefit immediately, since the method requires no access to router weights or labeled training data, making it deployable in closed-source or API-only environments where retraining is infeasible.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.00544v1)
