---
title: Whose turn is it? Context-guided model routing for stateful agents
published: 2026-10-13T23:13:37Z
authors: Anikesh Parashar, Avik Dutta, Vashu Chauhan, Sumit Gulwani, Priyanshu Gupta, Hosein Hasanbeig, Vu Le, Ashish Tiwari, Jack Williams
url: http://arxiv.org/abs/2610.19292v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Whose turn is it? Context-guided model routing for stateful agents

## Abstract
Model routing can reduce the cost of LLM applications by assigning simpler requests to cheaper models without sacrificing the quality of the response. However, most routers treat requests as independent. Stateful agents do not operate under this assumption: a user turn may require multiple model and tool calls, its difficulty depends on the state produced by earlier turns, and changing models can sacrifice reuse of the conversational prompt cache. We study zero-shot, cost-aware routing at the user-turn boundary, systematically varying the routing rule, access to session history, candidate models that differ in size, reasoning effort, or model provider, and prompt-cache behavior. We evaluate on multi-turn versions of SheetCopilot and SpreadsheetBench 2, where persistent workbooks and cross-turn dependencies make isolated routing decisions especially brittle. At a matched offloading rate, giving the router session history improves task pass rate over the same router without history, with gains for every model pair; history-aware routing remains within one point of always using the expensive model. We also found that cost depends on execution dynamics rather than token prices alone: the cheaper model's per-task cost advantage narrows from 6.8x to 3.2x on longer sessions. A closed form cache analysis further shows that downward switches (expensive to cheap) recover their cache cost within two LLM calls, whereas upward switches do not break even under the evaluated conditions. Together, these results show that agent routing is a sequential decision problem: effective policies must account for what happened earlier in the session and for the asymmetric cost of switching models.

## Metadata
- **Published**: 2026-10-13T23:13:37Z
- **Authors**: Anikesh Parashar, Avik Dutta, Vashu Chauhan, Sumit Gulwani, Priyanshu Gupta, Hosein Hasanbeig, Vu Le, Ashish Tiwari, Jack Williams
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19292v1)