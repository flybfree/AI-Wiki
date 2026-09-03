---
title: Harness Engineering in LLM Tool Use via Agent-Native Reusable Tool Primitives
url: http://arxiv.org/abs/2609.01736v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_18-07-09Z_HarnessEngineeringinLLMToolUseviaAgent_NativeReusa.md
generated_at: 2026-09-02 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Tool Primitives, a design that replaces rigid API schemas with natural language interfaces for tool calling, enabling flexible multi‑step reasoning. It also presents ToolFace as a repository of functions and HEART as a harness framework that orchestrates dynamic tool use. Experiments show HEART outperforms several state-of-the-art models by 6-10% while cutting API costs up to 85%.

## Key Takeaways
- The abstract highlights that existing LLM‑tool approaches suffer from brittle multi‑step reasoning due to incompatible output types and schemas.
- Tool Primitives resolves this by using natural language as the interface, with each tool wrapped in an LLM interface that handles schema resolution internally.
- HEART orchestrates dynamic planning, execution, and recovery through a Planner, Router, and Verifier, achieving high task completion rates.

## Context
Current AI research focuses on integrating large language models with external tools to solve complex tasks. However, the lack of robust handling for heterogeneous tool APIs limits performance and scalability. This work addresses those limitations by abstracting API details behind natural language prompts.

## Implications
For practitioners, HEART offers a practical way to deploy LLMs with many tools without managing raw schemas, reducing costs and improving reliability. The approach could become a standard pattern in AI agents aiming for efficient, multi‑step task execution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01736v1)
