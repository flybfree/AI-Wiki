---
title: MEMO: Multimodal Evidence Memory Organization for Long-Horizon LLM Agents
published: 2026-09-07T13:24:40Z
authors: Xian Gao, Jinpeng Wang, Jiacheng Ruan, Guangyu Cao, Ting Liu, Yuzhuo Fu
url: http://arxiv.org/abs/2609.07471v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MEMO: Multimodal Evidence Memory Organization for Long-Horizon LLM Agents

## Abstract
Long-running LLM agents rely on external memory to store and reuse information beyond a single context window, yet there is a fundamental tension between the continuous accumulation of interaction trajectories and the limited context capacity. The key challenge in agent memory is therefore not only to retrieve relevant records, but also to select necessary evidence under a given budget and organize it in an appropriate modality. Existing memory readout methods mainly use textual or visual forms. Text preserves high fidelity, but its linear token representation makes contents with different importance compete for the limited context at nearly uniform unit cost. Visual readout renders text into document-like images, which can use two-dimensional layouts to expose structure and emphasize key information, but it may lose fine-grained details during rendering and compression. To address this issue, we propose MEMO, a multimodal evidence memory organization method for LLM agents. MEMO first uses a trained evidence extractor to select relevant memory blocks and form evidence units with source information and presentation requirements. A trained query-conditioned memory manager assigns each unit to a textual, visual, or dual-channel carrier and selects a layout that matches the evidence structure. A deterministic memory construction module then generates the textual package and visual pages. The memory manager is trained with feedback from an offline reader that measures the utility of the guided memory plan, so that retention and presentation decisions align with downstream usage. We evaluate MEMO on four benchmarks, HotpotQA, 2WikiMultiHopQA, LoCoMo, and ALFWorld, with multiple reader backends. The results show that MEMO presents memory more efficiently with fewer memory tokens, improves downstream task performance, and builds more effective working memory under constrained budgets.

## Metadata
- **Published**: 2026-09-07T13:24:40Z
- **Authors**: Xian Gao, Jinpeng Wang, Jiacheng Ruan, Guangyu Cao, Ting Liu, Yuzhuo Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07471v1)