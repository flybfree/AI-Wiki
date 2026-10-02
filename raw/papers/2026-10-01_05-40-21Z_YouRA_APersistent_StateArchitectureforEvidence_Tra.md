---
title: YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents
published: 2026-10-01T05:40:21Z
authors: Yoonkyu Woo, Woojin Lee, Jin-Xia Huang
url: http://arxiv.org/abs/2610.01097v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents

## Abstract
End-to-end research agents can now produce complete scientific papers, yet manuscript claims often diverge from executed experiments. This gap is structural: research state, failure histories, and claim-evidence alignment are not maintained as persistent, verifiable state across long-horizon pipelines. We present YouRA (Your Research Agent), an architecture for stateful, evidence-traceable autonomous research. YouRA preserves research state, execution evidence, and failure history across the research trajectory by integrating three components: a Verification State Architecture (VSA) that tracks hypotheses, gates, and evidence pointers; an Independent Controller that turns state and reflection records into lifecycle, recovery, and debate/review control while separating control from execution; and Stateful Reflection that logs failures as structured lessons and routes recovery through bounded repair, redesign, or reset. On MLR-Bench's predefined ten-task end-to-end subset, YouRA improves over both MLR-Agent and AI Scientist V2 on scalar Overall across all three matched backbones. An automated diagnostic using MLR-Bench's hallucination taxonomy reports intersection/union counts for four fact-based failure types, and data-provenance diagnostic shows more real-data-based outputs. Ablating each of the four components (the VSA, the Independent Controller, MCP tool access, and reflection-guided recovery) supports their separable contributions. Removing either core-state component drops YouRA below the full system. Code: https://github.com/PrayPrey/Your-Research-Agent.

## Metadata
- **Published**: 2026-10-01T05:40:21Z
- **Authors**: Yoonkyu Woo, Woojin Lee, Jin-Xia Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.01097v1)