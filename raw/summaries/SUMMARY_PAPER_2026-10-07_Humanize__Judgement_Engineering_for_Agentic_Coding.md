---
title: Humanize: Judgement Engineering for Agentic Coding
url: http://arxiv.org/abs/2610.08900v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-06_17-54-42Z_Humanize_JudgementEngineeringforAgenticCoding.md
generated_at: 2026-10-07 22:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary

Humanize presents a multi-agent orchestration workflow for agentic coding that addresses the fundamental problem that the agent writing code is a poor judge of whether the task is complete. By introducing explicit, mechanically enforced decision gates between planning, implementation, review, and learning phases, the system uses deterministic hooks and a cross-vendor reviewer agent to ensure reliability. The paper validates this approach through 118 public postmortems, 68 versions over 108 days, and applications spanning software engineering, competitive programming, and mathematical proof tasks.

## Key Takeaways

- The core architectural insight is that alternating builder and reviewer agents drawn from two different model vendors creates a Markov chain over repository states where a defect survives only if both models independently miss it. This cross-vendor sampling, combined with 72 mechanical gates enforced by deterministic hooks rather than model judgment, provides a structural guarantee that no single model's blind spots can silently propagate through the workflow.

- Empirical evidence from 118 public postmortems reveals that independent review successfully catches unsupported builder claims, but stopping remains a critical weakness: two-thirds of rounds occurred after implementation was already accepted. This suggests that while the review mechanism is effective at catching errors, the system struggles with knowing when to terminate, highlighting that completion judgment is harder than error detection.

- The system's practical impact is demonstrated across diverse domains: a 567-file gem5 build-system migration under upstream review, top-three finishes in all three Full-Agent tracks of the MLSys 2026 FlashInfer contest via Kernel Design Agents, full scores in IOI 2026, IMO 2026, IPhO 2026, and IBO 2024, a gold-medal-level 418.5/437 in IChO 2026, a perfect 672/672 on PutnamBench, and a first-place ranking of 251/303 on Lean-Eval's leaderboard competing against professional mathematicians.

## Context

This paper sits at the intersection of agentic AI systems, software engineering automation, and multi-agent orchestration, addressing a widely recognized bottleneck in the field: as code generation becomes cheap and fast, the harder problem shifts from producing code to reliably determining when work is actually finished. The work contributes to the growing body of research on judgement engineering and verification in AI agents, offering a concrete, deployable workflow rather than a purely theoretical framework, validated through both observational deployment data and competitive benchmarks.

## Implications

For practitioners building agentic coding pipelines, Humanize demonstrates that mechanical enforcement of decision boundaries and cross-vendor review can substantially improve reliability without requiring a single monolithic model to self-assess its own output. For the broader AI research community, the finding that stopping remains a key weakness even with robust review mechanisms points to an open problem in agent design: how to define and detect task completion in open-ended coding tasks. The competitive results across programming, mathematics, and science olympiads suggest that judgement-engineered multi-agent workflows may generalize well beyond software engineering into domains requiring rigorous verification.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.08900v1)
