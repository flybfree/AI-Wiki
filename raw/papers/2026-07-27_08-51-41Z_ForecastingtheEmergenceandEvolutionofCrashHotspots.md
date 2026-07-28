---
title: Forecasting the Emergence and Evolution of Crash Hotspots: A Unified Deep Learning Framework for Proactive Traffic Safety
published: 2026-07-27T08:51:41Z
authors: Jingwen Zhu, Keshu Wu, Pei Li, Steven T. Parker, Bin Ran, David A. Noyce
url: http://arxiv.org/abs/2607.24168v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Forecasting the Emergence and Evolution of Crash Hotspots: A Unified Deep Learning Framework for Proactive Traffic Safety

## Abstract
Road crashes remain among the gravest threats to public safety, and preventing them is a defining task of transportation systems worldwide. Much of that harm concentrates at hotspots, yet a hotspot is less a place than an episode; it emerges quietly at an intersection or along an arterial, intensifies for weeks, then subsides, only to reappear elsewhere. Enforcement guided by maps of past crashes inevitably trails this cycle, patrolling yesterday's hotspots while tomorrow's form unwatched. Breaking that lag requires three capabilities at once: detecting hotspots as they are born, forecasting where they will sit next week, and following each one through its life. We introduce HERALD (Hotspot Emergence, Risk Anticipation, and Life-cycle Dynamics), a unified deep learning framework that provides all three from a single statewide model. HERALD distills each county's recent crash history into weekly risk maps and forecasts the next with a CNN--Transformer, whose mixture-of-experts lets one model serve dense urban cores and sparse rural corridors alike. Each forecast is anchored in the county's long-run crash geography, sharpened by the self-exciting effect of recent crashes, and paired with explicit warnings of where new hotspots are about to appear. Followed over time, every hotspot acquires a legible life story, from birth through growth and stability to decline and death. Across six heterogeneous Wisconsin counties, HERALD forecasts more accurately than five identically trained baselines, locates hotspots most precisely, and flags emerging risks before they take hold. A single adjustable setting trades accuracy for extra sensitivity where deployment demands it. The result shifts hotspot management from mapping the past to anticipating the future.

## Metadata
- **Published**: 2026-07-27T08:51:41Z
- **Authors**: Jingwen Zhu, Keshu Wu, Pei Li, Steven T. Parker, Bin Ran, David A. Noyce
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24168v1)