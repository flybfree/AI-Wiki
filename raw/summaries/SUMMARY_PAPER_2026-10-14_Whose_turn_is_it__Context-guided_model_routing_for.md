---
title: Whose turn is it? Context-guided model routing for stateful agents
url: http://arxiv.org/abs/2610.19292v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_23-13-37Z_Whoseturnisit_Context_guidedmodelroutingforstatefu.md
generated_at: 2026-10-14 21:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates cost-aware model routing at the user-turn boundary for stateful LLM agents, arguing that treating each request as independent is fundamentally flawed when agents maintain persistent state across multi-turn sessions. By evaluating routing strategies on multi-turn spreadsheet tasks (SheetCopilot and SpreadsheetBench 2), the authors demonstrate that history-aware routing significantly outperforms history-blind routing while remaining nearly as accurate as always using the most expensive model, and they reveal that model-switching costs are asymmetric and depend heavily on execution dynamics rather than token prices alone.

## Key Takeaways
- Session history is critical for effective routing: at a matched offloading rate, providing the router with access to prior turns improves task pass rate over the same router without history, with measurable gains across every tested model pair. History-aware routing stays within one percentage point of always using the expensive model, showing that informed routing can nearly match the quality ceiling while reducing cost.
- Cost savings from cheaper models erode over longer sessions: the per-task cost advantage of the cheaper model narrows from 6.8x to 3.2x as sessions grow, because execution dynamics (multiple tool calls, reasoning steps, and state management) dominate total cost rather than per-token pricing. This means naive token-price-based routing underestimates the true cost of offloading in stateful agent workflows.
- Model switching carries asymmetric cache penalties: a closed-form analysis shows that switching from an expensive model to a cheaper one recovers its prompt-cache cost within two LLM calls, but switching upward (cheap to expensive) never breaks even under the evaluated conditions. This asymmetry means routing policies must treat model transitions as sequential decisions with persistent state consequences, not isolated per-request choices.

## Context
LLM model routing has emerged as a practical strategy for reducing inference costs in production systems, but existing routers overwhelmingly assume requests are independent and stateless. Stateful agents—those that maintain workbooks, code contexts, or multi-step tool-use plans across turns—violate this assumption, making routing a sequential decision problem intertwined with prompt-cache management and cross-turn dependencies. This paper fills a gap by systematically studying how session history, model heterogeneity (size, reasoning effort, provider), and cache behavior interact in realistic multi-turn agent settings, moving the field beyond single-turn benchmarks.

## Implications
For practitioners deploying multi-turn agents in production, this work signals that routing policies must be redesigned as sequential controllers that track session state and cache economics rather than as per-request classifiers. The asymmetric switching costs and the erosion of cost savings in longer sessions suggest that naive offloading strategies will underperform in real agent workloads, and that infrastructure teams need to account for execution dynamics when estimating savings. For the research community, the findings establish a benchmark and methodology for evaluating agent-aware routing, pushing the field toward stateful, cache-aware routing frameworks that reflect how agents actually operate.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19292v1)
