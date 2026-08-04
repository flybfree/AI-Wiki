---
title: MemSIF: From Structured Interactions to Dual-Track Fact Memory for LLM Agents
published: 2026-08-03T06:09:57Z
authors: YuFei Luo, Xiucheng Xu, Zhen Yang
url: http://arxiv.org/abs/2608.01742v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemSIF: From Structured Interactions to Dual-Track Fact Memory for LLM Agents

## Abstract
Long-term memory is critical for LLM agents operating over long-horizon interactions. However, several persistent limitations of existing memory systems can be traced to two recurring misalignment patterns in long-term interaction settings: Temporal-Structural Misalignment (TSM) and Delayed Utility Manifestation (DUM). TSM arises when temporal proximity does not reliably align with topical or event-level relatedness, whereas DUM arises when write-time salience does not reliably predict future query utility. To mitigate these misalignment patterns, we propose MemSIF (Memory with Structured Interactions and Facts), a structured interaction-to-fact memory framework. Structured Interaction Memory organizes raw interactions into Topical Segments that preserve local topical coherence and Event Trajectories that maintain cross-time event continuity. Dual-Track Fact Memory uses two complementary tracks: CoreFact memory consolidates stable, schema-guided information at write time, whereas ActiveFact memory forms facts on demand and promotes those supported by multiple historical sources and recurring query demand for reuse. Experiments on LoCoMo and LongMemEval-S across five backbone LLMs show that MemSIF achieves the highest Total ACC in all settings, outperforming the strongest baseline by 2.29%-8.79% on LoCoMo and 2.87%-6.15% on LongMemEval-S. These results support the effectiveness of combining Structured Interaction Memory with Dual-Track Fact Memory to mitigate TSM and DUM. Code is available at https://github.com/luoyufeihaha/MemSIF.

## Metadata
- **Published**: 2026-08-03T06:09:57Z
- **Authors**: YuFei Luo, Xiucheng Xu, Zhen Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01742v1)