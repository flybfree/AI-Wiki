---
title: Build or Adopt? Custom-Built vs. General-Purpose LLM Agent Harnesses for Automotive GUI Testing
url: http://arxiv.org/abs/2610.33636v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-24_12-32-16Z_BuildorAdopt_Custom_Builtvs_General_PurposeLLMAgen.md
generated_at: 2026-10-26 21:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the "build vs. adopt" decision for LLM agent harnesses in the context of automotive GUI testing at Volvo Group, comparing a production custom-built harness against general-purpose alternatives (Claude Code and OpenCode) while holding tools and models constant. The study finds that general-purpose harnesses match custom-built ones on structured IVI test tasks but incur significantly higher inference costs, yet yield lower total monthly costs when engineering effort is factored in, and outperform custom-built harnesses on open-ended tasks due to superior error recovery.

## Key Takeaways
- On Volvo's stepwise IVI regression tests, general-purpose harnesses achieve comparable success rates to the custom-built harness but exhibit greater run-to-run variability, while their per-task inference cost is 2.6 to 10.7 times higher. However, when accounting for the engineering effort saved by not maintaining a bespoke agent loop, the total monthly cost for a nightly IVI regression suite is 3 to 66 percent lower with general-purpose harnesses, making adoption economically favorable despite higher token consumption.
- On open-ended tasks in public applications such as Google Maps and Booking.com, general-purpose harnesses succeed more often than the custom-built harness, primarily because they recover more effectively from incorrect actions. This suggests that the iterative reasoning and self-correction capabilities built into mature general-purpose harnesses provide a practical advantage for exploratory or unstructured testing scenarios.
- Interviews with ten practitioners (developers, a product owner, and testers) reveal that external advances in general-purpose harnesses can silently convert an in-house harness into technical debt even when it has not deteriorated in absolute terms. Adopting a general-purpose harness shifts maintenance burden from the agent loop itself to tools and instructions, but reduces the team's control over what the model receives. Regardless of harness choice, testers consistently want to inspect the agent's actions and verify adherence to prescribed test scenarios.

## Context
As LLM agent frameworks mature rapidly, organizations across industries face a recurring strategic question: whether to continue investing in bespoke agent infrastructure or to adopt externally maintained general-purpose harnesses. This paper contributes a rare controlled comparison in a real industrial setting—automotive in-vehicle infotainment testing—where the same tools accessed via the Model Context Protocol and the same underlying models are used across harnesses, isolating the harness as the sole variable. This methodological rigor makes the findings directly transferable to other domains where teams maintain custom agent pipelines.

## Implications
For industry practitioners, the findings challenge the common assumption that custom-built agent harnesses are inherently superior for domain-specific tasks, showing instead that the engineering cost of maintaining bespoke agent loops can outweigh any marginal performance advantage. Organizations should reassess their in-house harness investments periodically, as external progress can erode their value without any degradation in the custom system itself. For the broader AI research community, the paper highlights the importance of transparency and inspectability in agent-based testing workflows, underscoring that practitioners' trust depends on visibility into agent actions regardless of which harness is deployed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33636v1)
