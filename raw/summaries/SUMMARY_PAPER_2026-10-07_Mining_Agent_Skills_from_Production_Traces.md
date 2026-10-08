---
title: Mining Agent Skills from Production Traces
url: http://arxiv.org/abs/2610.05777v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-05_04-21-42Z_MiningAgentSkillsfromProductionTraces.md
generated_at: 2026-10-07 23:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how the availability of success/failure labels in execution traces and the structural form of mined agent skills (workflow plans versus declarative ontologies) affect downstream task performance in enterprise settings. Through a controlled comparison of six mining configurations across two enterprise benchmarks, the authors demonstrate that no single combination of evidence type and skill form universally outperforms others; instead, optimal configurations depend on the specific domain and task structure, motivating a tailored approach to meta-skill mining rather than a one-size-fits-all pipeline.

## Key Takeaways
- On ThinkingBox-Bench, ordered workflow plans outperform declarative ontologies by 1.7 percentage points, and the "Goldilocks" evidence regime (mixing successes and failures with outcome labels) beats success-only evidence by 2.4 percentage points, while blind simulation of skills learned without outcome labels degrades performance by 3.1 percentage points, indicating that outcome information materially shapes skill quality in structured task domains.
- On APEX-Agents, the pattern reverses partially: ontologies show a moderate preference over workflows, and there is no clear advantage among the three evidence regimes, suggesting that in domains with more heterogeneous or exploratory task structures, the presence or absence of outcome labels matters less than the representational form of the skill itself.
- Within each benchmark, task-structure-related constraints produce uneven performance gains from mined skills, meaning that even the best global configuration underperforms on certain task categories, reinforcing the need for domain-aware skill mining rather than a universal pipeline.

## Context
As LLM-based agents are deployed in enterprise workflows, the community has shifted from hand-curated procedural instructions toward automated skill mining from execution traces. However, production environments rarely provide clean success/failure signals, and existing skill-mining pipelines often assume such labels are available. This paper fills a gap by systematically ablating the role of outcome information and skill representation format under realistic production constraints, bridging the divide between controlled research benchmarks and the noisy, label-scarce reality of deployed agent systems.

## Implications
For practitioners building enterprise agent platforms, the findings argue against adopting a single fixed skill-mining recipe and instead call for domain-specific configuration of both evidence sampling strategies and skill representation formats. Industry teams deploying agents in heterogeneous task environments should invest in lightweight outcome-labeling infrastructure where feasible, while also evaluating whether workflow-style or ontology-style skill representations better match their task taxonomy. The results also suggest that future meta-skill research should incorporate task-structure-aware selection mechanisms to avoid the performance cliffs observed within individual benchmark domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.05777v1)
