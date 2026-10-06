---
title: Programmatic Search Agents: Extending Agentic Search Beyond Query Reformulation
url: http://arxiv.org/abs/2610.06689v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-05_16-52-57Z_ProgrammaticSearchAgents_ExtendingAgenticSearchBey.md
generated_at: 2026-10-05 22:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the Programmatic Search Agent (PSA), a framework that extends agentic search control beyond query reformulation to encompass the processing and presentation of retrieved evidence. The authors demonstrate that current search agents, despite adapting their queries, lack direct control over candidate processing and evidence delivery, leading to inefficiencies where relevant passages are retrieved but never surfaced to the agent. PSA addresses this gap by making local executable computation over retrieved candidates the fundamental unit of a search action, yielding significant improvements in task success and token efficiency across multiple benchmarks.

## Key Takeaways
- The authors identify a critical failure mode in existing search agents: supporting passages can be successfully retrieved from the search substrate yet never delivered to the agent for inspection. A same-page oracle intervention experiment confirms that changing the returned evidence directly reduces the number of subsequent search steps, proving that evidence presentation is a bottleneck independent of query quality.
- PSA introduces a persistent candidate workspace where the agent incrementally generates program cells that reuse previously retrieved candidates, execute dependent operations, and selectively determine what evidence the agent inspects next. The runtime resolves data dependencies within each cell, while the agent retains adaptive control over its search strategy across cells as new evidence arrives, unifying flexible primitive composition with selective evidence presentation.
- Evaluated on InfoSeek-Eval and BrowseComp-Plus using five policy backbones without any task-specific training, PSA improves macro-averaged task success by 4.00 and 7.56 percentage points over a Query-based Agent baseline. Notably, the Tool-based Agent shares PSA's primitives and persistent workspace, yet PSA still outperforms it, indicating that the programmatic composition and selective presentation mechanism provides advantages beyond simply having access to the same tools. Within-backbone reductions in final-step tokens average 28.3% and 33.9%, demonstrating substantial efficiency gains.

## Context
This work sits at the intersection of agentic retrieval-augmented generation and tool-use planning, a rapidly growing area where large language models are deployed as autonomous agents that iteratively search, reason, and synthesize information. Most existing agentic search systems treat the search interface as a fixed black box, limiting the agent's agency to reformulating queries. By showing that the agent's inability to control how retrieved candidates are processed and presented constitutes a distinct failure mode, this paper challenges a foundational design assumption in the field and proposes a principled architectural extension.

## Implications
For practitioners building search-augmented agents in production, PSA suggests that investing in programmable evidence-processing layers—rather than solely optimizing query strategies—can yield meaningful gains in both accuracy and token efficiency without requiring task-specific fine-tuning. For the broader AI research community, the finding that a same-page oracle intervention reduces search steps implies that future agent architectures should treat evidence selection and candidate manipulation as first-class agent actions, potentially reshaping how search tool interfaces are designed for autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06689v1)
