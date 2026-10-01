---
title: When Correct Memory Goes Wrong: Fuzzing Persistent Memory Use in LLM Agents
url: http://arxiv.org/abs/2609.38275v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-29_15-35-58Z_WhenCorrectMemoryGoesWrong_FuzzingPersistentMemory.md
generated_at: 2026-09-30 22:21
model: qwen3.6-35b-a3b
---

## Summary
This paper addresses the challenge of memory-use failures in LLM agents, where persistent memory is correctly stored but applied incorrectly due to evolving queries or states. The authors formulate this issue as a fuzzing problem and introduce U-Fuzz, a systematic testing framework that mutates queries and memory states starting from checkpoints to uncover these hidden errors. Evaluation demonstrates that U-Fuzz consistently detects more confirmed failures than existing baselines across diverse memory architectures and even in black-box API settings where internal retrieval is inaccessible.

## Key Takeaways
- Memory-use failures occur when agents apply correct memory information incorrectly due to query shifts or state evolution, a category distinct from content errors that existing evaluation methods struggle to detect systematically.
- U-Fuzz operates by initializing test seeds from memory checkpoints and performing mutations on queries or memory states under explicit obligations, using observed agent behavior to guide iterative testing without relying on failure labels during the search process.
- The proposed method outperforms diverse fuzzing baselines in uncovering confirmed failures and maintains effectiveness across various memory architectures, including challenging output-only scenarios with API-based LLMs where memory retrieval mechanisms are hidden from the tester.

## Context
As LLM agents increasingly rely on persistent memory to maintain coherence and perform complex tasks over extended interactions, ensuring the reliability of how this memory is utilized becomes critical for real-world deployment. Current evaluation methods often focus on static correctness or content accuracy, overlooking dynamic usage errors that arise when agent states change, leaving a significant gap in robust

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38275v1)
