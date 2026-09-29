---
title: "You're Right, Let Me Fix It": How LLM Agents Damage Correct Work When Falsely Accused
published: 2026-09-26T13:38:31Z
authors: Xutao Mao, Rui Qian, Longxiang Wang, Xinjian Yi, Mingxuan Li, Linghan Chen, Yudong Gao, Xiang Zheng, Cong Wang
url: http://arxiv.org/abs/2609.32616v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# "You're Right, Let Me Fix It": How LLM Agents Damage Correct Work When Falsely Accused

## Abstract
LLM agents increasingly keep working after a task succeeds as they resume after compaction or take over handoffs. Their finished work keeps receiving follow-up input that sometimes falsely accuses it for later failures. We call an agent's acceptance of such a false accusation gaslight sycophancy, and destructive over-correction when acting on it damages previously correct work. We introduce CAVE-Bench, a benchmark of 365 agentic tasks across six domains built around opaque tasks. Every scored run first reaches a verified correct state, whose supporting rationale and history stay in the workspace while the facts that would settle the accusation lie in external or runtime state beyond the agent's reach. The agent cannot confirm or refute the claim with a local check, so the right response should keep the work and ask for the missing evidence. Each task either hands the agent correct work with saved evidence or let it build and verify that work first, and five risk factors set how the accusation enters the workflow. We score accusation acceptance and evidence use from the trajectory and measure harm by deterministic replay of downstream events. Across 14 of the latest models in Claude Code, false accusations damage correct work in up to 60.06% of runs, and stronger models often do so after recovering the supporting evidence. The same model behaves differently across OpenCode, Codex, and Hermes, and a harness gate driven by the benchmark's live signals cuts replayed harm by 74%. These results show that preserving already-correct work under unsupported accusation is a distinct safety challenge for long-lived agents. Our project is in https://henrymao2004.github.io/agent-over-correction/.

## Metadata
- **Published**: 2026-09-26T13:38:31Z
- **Authors**: Xutao Mao, Rui Qian, Longxiang Wang, Xinjian Yi, Mingxuan Li, Linghan Chen, Yudong Gao, Xiang Zheng, Cong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32616v1)