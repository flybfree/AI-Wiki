---
title: Fetch-then-Explore: Decoupling Selection from Extraction over a Persistent Workspace for Search Agents
url: http://arxiv.org/abs/2608.02097v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_11-58-21Z_Fetch_then_Explore_DecouplingSelectionfromExtracti.md
generated_at: 2026-08-03 23:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Fetch‑then‑Explore, a method that separates page selection from evidence extraction for search agents and stores selected pages in a persistent workspace. Experiments on BrowseComp and WideSearch show it matches or exceeds existing baselines, especially when agents revisit the same page later.

## Key Takeaways
- The workspace records all selected pages for a question rather than discarding them after each interaction, allowing evidence to be reused across multiple turns.
- Extraction is deferred until the agent knows what specific fact to look for, enabling repeated pulls without re‑fetching the whole page.
- This decoupling makes selection nearly free and enables agents to recover missed information when they return to a previously visited page.

## Context
Current search agents rely on either immediate read‑in or transient browsing, both of which limit memory and cause repeated fetching. The persistent workspace addresses this by treating pages as durable artifacts linked to a question’s trajectory.

## Implications
For practitioners, Fetch‑then‑Explore suggests that long‑term evidence accumulation can be more effective than short‑term in‑memory handling. It may improve system design for agents that need deep reasoning over many steps without costly re‑queries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02097v1)
