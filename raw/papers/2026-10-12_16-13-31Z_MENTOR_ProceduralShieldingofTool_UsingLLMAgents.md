---
title: MENTOR: Procedural Shielding of Tool-Using LLM Agents
published: 2026-10-12T16:13:31Z
authors: Ashwani Anand, Ivi Chatzi, Ritam Raha, Anne-Kathrin Schmuck
url: http://arxiv.org/abs/2610.17039v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MENTOR: Procedural Shielding of Tool-Using LLM Agents

## Abstract
Tool-using LLM agents are increasingly used to automate workflows governed by procedural manuals, such as company rules for booking travel or procuring hardware. These manuals are written in natural language for humans and describe general requirements over such complex workflows. Ensuring compliance of LLM agents with these manuals is difficult, and state-of-the-art techniques use either LLM judges or manually written rules to forbid problematic tool-calls locally at runtime. This is insufficient because (i) only blocking tool calls keeps the agent clueless about how to make correct progress towards fulfilling its task, and (ii) can lead to overly conservative behavior of the agent, as tool calls might only be problematic in certain contexts. To overcome these challenges, we introduce MENTOR, which (i) additionally provides guidance for the agent to make procedural-compliant progress on the task, and (ii) ensures that this compliance is context-aware. We achieve these goals by building a novel history-dependent runtime shield that is obtained from the procedural manual via a multi-step autoformalization pipeline. At its core, MENTOR utilizes a game-based technique to ensure robustness against runtime uncertainty without over-resticting agents' behavior. This yields a formally assisted framework for procedural shielding of LLM agents that improves compliance well beyond existing methods. In particular, MENTOR lifts the compliance of shielded light-weight open-source LLMs above that of non-shielded proprietary models. Since a shield is synthesized once per manual and then serves every task, a MENTOR-shielded agent becomes a viable choice for repeatedly executed workflows, potentially reducing deployment costs when the offline construction cost is amortized over repeated tasks.

## Metadata
- **Published**: 2026-10-12T16:13:31Z
- **Authors**: Ashwani Anand, Ivi Chatzi, Ritam Raha, Anne-Kathrin Schmuck
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17039v1)