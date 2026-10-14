---
title: Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents
url: http://arxiv.org/abs/2610.18784v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_17-35-27Z_PackLight_CarryOn_BuildingObject_OrientedContextfo.md
generated_at: 2026-10-14 02:06
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CarryOn is an object-oriented context runtime designed for long-horizon agents that reorganizes how agents manage their working context across extended task sequences. Rather than relying on compressed interaction histories or reconstructed accounts of progress, CarryOn structures continuation around reusable task objects called "continuation carriers," achieving performance gains of 5.8% on OSWorld 2.0 and 7.0% on BrowseComp-Plus while simultaneously reducing total token usage by 51.9% and 22.9%, respectively.

## Key Takeaways
- CarryOn reframes long-horizon agent context management around reusable progress objects rather than the interaction histories that produced that progress. The system builds a context view from three components: continuation carriers (reusable task state), complementary execution context, and a live tail of recent interactions, shifting the paradigm from history replay to progress reuse.
- A central technical challenge addressed is maintaining the validity of reusable task objects after their surrounding interaction history is retired or "folded." CarryOn solves this by maintaining carrier records across folds, revising only affected records against bound evidence and applicable environment checks, while carrying forward unaffected records and jointly updating execution context—avoiding the costly need to reconstruct the full representation at every fold.
- The experimental results demonstrate that this object-oriented approach yields substantial dual benefits: improved task performance on both OSWorld 2.0 (5.8% gain) and BrowseComp-Plus (7.0% gain) while simultaneously cutting token consumption by 51.9% and 22.9%, showing that better context organization can improve both quality and efficiency.

## Context
This work sits at the intersection of agent memory management, context window optimization, and long-horizon task planning—areas that have become critical bottlenecks as AI agents are deployed in increasingly complex, multi-step environments. Current approaches to long-horizon agent context typically rely on summarization, compression, or sliding-window strategies that treat interaction history as the primary substrate for continuation. CarryOn challenges this assumption by proposing that progress itself, rather than the narrative of how progress was achieved, should be the organizing principle for agent context, aligning with broader trends in object-oriented software design and state-based planning.

## Implications
For practitioners building autonomous agents that must operate over dozens or hundreds of steps—such as software engineering agents, web-browsing assistants, or robotic task planners—CarryOn offers a concrete architectural pattern that can reduce operational costs by over 50% while improving task success rates. The carrier-based revision mechanism, which updates only affected records against bound evidence rather than reconstructing entire context representations, provides a scalable path toward agents that maintain coherent task state across arbitrarily long horizons without proportional increases in token budgets or computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18784v1)
