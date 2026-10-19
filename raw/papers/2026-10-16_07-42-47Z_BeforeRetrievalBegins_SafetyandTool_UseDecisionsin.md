---
title: Before Retrieval Begins: Safety and Tool-Use Decisions in LLM Agents
published: 2026-10-16T07:42:47Z
authors: Aditya Nawal, Manit Baser, Mohan Gurusamy
url: http://arxiv.org/abs/2610.23071v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Before Retrieval Begins: Safety and Tool-Use Decisions in LLM Agents

## Abstract
Large language models increasingly act as agents that call external tools, yet most tool-safety research examines only what follows a tool call. The prior decision of whether to call the tool remains largely unexamined and can influence downstream safety. Across the seven open-weight models, the unweighted model-average harm rate after admitted harmful requests is 74.5%. To identify what governs this decision, we apply a factorial intervention to the input request. Within our generated construction, neutralizing the requested-operation component produces the largest admission contrast (19 pp). A linear direction estimated from this contrast influences held-out admission in four of seven models; effects on operation-neutralized requests in some models show that it is not an operation-specific mechanism. We then test whether written refusal is behaviorally and representationally coupled to the same decision. Written refusal accompanies 33.6% of admitted harmful calls. Plain-text refusal training reduces unsafe admission in models that retain benign tool use, showing that response-level safety training can transfer to the call decision. Together, these results establish a partial, model-dependent relation between written refusal and tool admission. They motivate direct evaluation and supervision of tool admission rather than treating text refusal as its proxy.

## Metadata
- **Published**: 2026-10-16T07:42:47Z
- **Authors**: Aditya Nawal, Manit Baser, Mohan Gurusamy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.23071v1)