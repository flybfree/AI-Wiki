---
title: HALO: Heterogeneous Admission through Localized Obligations for Safe Agentic Execution
published: 2026-07-30T03:46:31Z
authors: Taewoo Park, Kyeonghyun Yoo, Kiseok Kim, Seunghyun Yoo, Hwangnam Kim
url: http://arxiv.org/abs/2607.27636v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HALO: Heterogeneous Admission through Localized Obligations for Safe Agentic Execution

## Abstract
Recent agentic AI systems may return a heterogeneous response containing notices, requests, handoffs, and actions. Conditions can change before external use, so components from the same response need not remain supported together. Rejecting the whole response discards useful components, whereas checking components independently can leave a dependent without its prerequisite. We present Heterogeneous Admission with Localized Obligations (HALO), a runtime protocol that preserves supported components whose declared prerequisites also remain supported, rechecks each exact action before dispatch, and allows blocked actions to be replaced only by fresh candidates. HALO matched all 96 admission expectations and passed all 20 protocol tests. In structured-response replay, it retained 248/248 supported components, including 128/128 unaffected by unrelated changes, while a whole-response policy retained 0/248. Across ten cold-start PX4/Gazebo sessions, HALO blocked every tested stale route, observed no matching stale setpoint, and completed all fresh recoveries.

## Metadata
- **Published**: 2026-07-30T03:46:31Z
- **Authors**: Taewoo Park, Kyeonghyun Yoo, Kiseok Kim, Seunghyun Yoo, Hwangnam Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27636v1)