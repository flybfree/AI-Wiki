---
title: Trace-to-Architecture: Capability Bottleneck Diagnosis for Harness Revision
url: http://arxiv.org/abs/2610.16725v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_12-56-13Z_Trace_to_Architecture_CapabilityBottleneckDiagnosi.md
generated_at: 2026-10-14 01:17
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Trace-to-Architecture (T2A), a framework that leverages execution trajectories from both successful and failed agent tasks to diagnose capability bottlenecks and determine which specific harness components to revise. A development agent iteratively diagnoses failures, revises the agent's architecture, and validates changes by confirming that target tasks improve, previously successful tasks remain intact, and edits are actually triggered. Across three benchmark environments—ALFWorld, ScienceWorld, and AppWorld—T2A achieves the highest aggregate scores for all evaluated task agents, surpassing their strongest baselines by 6.2 to 30.3 points, and integrating T2A's procedures into Meta-Harness yields a 21.6-point improvement in mean ScienceWorld score.

## Key Takeaways
- T2A addresses a critical challenge in agent improvement: similar-looking failures may require entirely different fixes, and resolving one bottleneck can expose another. Rather than applying generic patches, the framework uses execution evidence from both successful and failed trajectories to pinpoint exactly which harness component (e.g., planning module, tool-use layer, or memory system) is responsible for a given failure, enabling targeted and precise revisions.
- The framework enforces a rigorous validation loop after every revision: it checks that target tasks improve, that selected previously successful tasks do not regress, and that the applied edits are actually triggered during execution. This prevents the common pitfall of "fixing" one problem while silently breaking another, and the iterative cycle of new execution evidence feeding subsequent diagnosis ensures progressive, safe improvement.
- Empirically, T2A outperforms all evaluated baselines across three distinct agent benchmarks (ALFWorld for household tasks, ScienceWorld for scientific reasoning, and AppWorld for application manipulation), with aggregate improvements ranging from 6.2 to 30.3 points. When integrated into Meta-Harness, the diagnosis and validation procedures alone contribute a 21.6-point gain in ScienceWorld scores from the same starting harness, demonstrating that the diagnostic methodology itself adds substantial value independent of the underlying agent architecture.

## Context
LLM agents are increasingly deployed in complex, multi-step task environments where their performance depends not just on the underlying language model but on the surrounding harness—scaffolding code, tool interfaces, planning strategies, and memory management. Improving these harnesses has traditionally relied on manual engineering or broad hyperparameter sweeps, which are slow, brittle, and often fail to identify the true bottleneck. T2A sits at the intersection of automated program repair, agent evaluation, and meta-learning, offering a principled, evidence-driven alternative that treats agent failure diagnosis as a structured reasoning task rather than trial-and-error tuning.

## Implications
For practitioners building and maintaining LLM agent systems, T2A provides a repeatable, automated workflow for diagnosing and fixing agent failures without requiring deep manual inspection of execution traces, potentially reducing engineering iteration cycles from days to hours. For the broader AI research community, the framework demonstrates that harness-level improvements can yield gains comparable to or exceeding model-level upgrades, suggesting that future agent development should invest as heavily in diagnostic and revision tooling as in model scaling. Industry teams deploying agents in production environments stand to benefit from the built-in regression checks, which guard against the common failure mode where a fix for one task category silently degrades performance on others.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16725v1)
