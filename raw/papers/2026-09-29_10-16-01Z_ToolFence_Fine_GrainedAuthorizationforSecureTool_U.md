---
title: ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents
published: 2026-09-29T10:16:01Z
authors: Yanjie Li, Xiangyu He, Xuelong Dai, Bin Xiao
url: http://arxiv.org/abs/2609.37196v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents

## Abstract
Tool-using LLM agents remain vulnerable to indirect prompt injection because trusted instructions and untrusted observations share one context, allowing malicious content to steer consequential input-filtering defenses. Multi-path consensus defenses still leave a high attack success rate because they examine content or aggregated outputs rather than authorizing effects, especially for the within-tool attack, which preserves the intended tool but manipulates its arguments. Data-Flow Control such as CaMeL provides stronger guarantees, but incurs substantial time latency that limits practical deployment. We introduce ToolFence, which compiles a typed authorization blueprint before execution, enforces it through a deterministic monitor, and when the blueprint is incomplete asks a judge to grant new capabilities rather than adjudicate each concrete call. ToolFence provides two key advantages. First, its fine-grained provenance-aware authorization enables the system to distinguish user-authorized values from untrusted observations, effectively addressing the within-tool attack. Second, its deterministic fast path and capability-level runtime grants substantially reduce the frequency of expensive judge calls, improving runtime efficiency. On AgentDojo with Qwen3-max, ToolFence reduces overall ASR to near zero with only a 3.80 percentage-point clean-utility drop and practical runtime overhead.

## Metadata
- **Published**: 2026-09-29T10:16:01Z
- **Authors**: Yanjie Li, Xiangyu He, Xuelong Dai, Bin Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37196v1)