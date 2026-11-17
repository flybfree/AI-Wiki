---
title: Beyond Plain MCP: Do Decision Models and Code Mode Make Tool Use Cheaper and Faster?
url: http://arxiv.org/abs/2611.19123v1
type: paper-summary
date: 2026-11-16
source_paper: 2026-11-14_03-15-59Z_BeyondPlainMCP_DoDecisionModelsandCodeModeMakeTool.md
generated_at: 2026-11-16 21:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper evaluates two architectural approaches for managing tool catalogs in Model Context Protocol (MCP) gateways: code mode, where agents write scripts against tool stubs, and decision layers, which act as lightweight routers that preselect tool subsets before agent invocation. Through a preregistered evaluation across 12 servers with up to 1,958 distractor tools and three open-weight agents (Qwen, Gemma, and Nemotron), the study finds that code mode substantially outperforms plain MCP by reducing token usage by 70 to 90 percent while improving task utility. However, the central hypothesis that combining a decision layer with code mode yields superior results is not confirmed, showing only minor and statistically non-significant improvements.

## Key Takeaways
- Code mode dramatically outperforms plain MCP in both efficiency and effectiveness, cutting token consumption by 70 to 90 percent while significantly boosting task utility. This suggests that allowing agents to write scripts against tool stubs is a far more efficient strategy than presenting full tool catalogs directly to the model, particularly in environments with large numbers of distractor tools (up to 1,958 in this study).
- Declaring return-shape hints in code mode stubs is identified as a first-order variable that can swing task success by up to 39.5 percentage points for lower-performing agents. This effect is larger than the benefit of adding a decision router, indicating that schema clarity in tool stubs is more impactful than architectural routing layers for weaker models.
- The hypothesis that a decision layer placed in front of code mode outperforms code mode alone is not confirmed. The evaluation shows only minor, statistically non-significant improvements for weaker agents and a slight cost penalty for the strongest agent, suggesting that the added complexity of a router does not justify its inclusion when code mode is already employed.

## Context
As language model agents increasingly interact with large tool ecosystems through protocols like MCP, the cost and latency of tool selection have become critical bottlenecks. This paper addresses a practical architectural question that practitioners face daily: how to structure tool access so that agents remain efficient without sacrificing capability. By using a controlled, preregistered harness with sealed test splits and open-weight models, the study provides reproducible evidence in a field where many claims about tool-use optimization remain anecdotal or proprietary. The release of the harness, a finetuned 4B tool selection model, and all evaluation traces supports the broader community effort toward local AI privacy and transparent agent architecture research.

## Implications
For practitioners building agentic systems, the findings suggest that investing effort in well-structured code mode stubs with explicit return-shape annotations will yield far greater returns than adding separate decision-routing layers. This has direct cost implications for production deployments, where token savings of 70 to 90 percent translate into meaningful reductions in API spending and latency. For the research community, the paper provides a reproducible benchmark and open artifacts that enable rigorous comparison of agent architectures, particularly for teams prioritizing local inference and privacy-preserving tool use rather than relying on closed commercial APIs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.19123v1)
