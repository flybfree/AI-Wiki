---
title: Closed-World Resolution Against Tool Hallucination in LLM Agents
url: http://arxiv.org/abs/2609.19425v1
type: paper-summary
date: 2026-09-17
source_paper: 2026-09-16_21-02-31Z_Closed_WorldResolutionAgainstToolHallucinationinLL.md
generated_at: 2026-09-17 21:09
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper identifies a critical structural flaw in current tool-augmented large language model (LLM) agents, specifically regarding how they hallucinate non-existent tools and invalid arguments. The authors argue that existing security measures—which focus on selecting the correct tool or gating permissions—fail because they presuppose the existence of the tool being called; therefore, a hallucinated call cannot be "gated" because it doesn't correspond to any real action. To address this, the paper proposes a five-class taxonomy of hallucinations and introduces the "Resolution Rung," a training-free, closed-world resolver designed to verify registry membership before any other logic is applied.

## Key Takeaways
- Structural Blind Spot: The research demonstrates that hallucination is a structural blind spot because a hallucinated call is not a decision that can be gated; since it doesn't refer to a real tool, no current gate can reject it. Therefore, the authors prove that hallucination defense must precede any causal gating mechanism or permission check.
- Scale Ineffectiveness: Empirical testing across ten hosted models reveals that increasing model scale does not mitigate tool hallucination. Specifically, a 675B parameter model exhibited similar levels of hallucination to much smaller 7-8B parameter models, particularly when presented with unconstrained raw-JSON surfaces.
- MCP Complexity and Shadowing: The research extends into the Model Context Protocol (MCP), revealing that merging multiple servers into a single namespace creates unique "M1-M5" hallucinations caused by collisions and shadowing. These structural issues mean that even frontier models can hallucinate when faced with complex, merged namespaces, requiring more sophisticated resolution than simple registry checks.

## Context
This research is significant as AI agents move from sandbox environments into real-world production systems where they interact with live APIs and sensitive data. While much of the current research focuses on "safe" behavior or permissioning, this paper identifies a fundamental architectural gap in how we verify the validity of an agent's intent against the available toolset.

## Implications
For practitioners and researchers, these findings suggest that building safer agents requires more than just larger models; it requires the implementation of explicit, closed-world verification layers like the "Resolution Rung." By providing a standardized Hallucinated-Tools Benchmark (HTB), the authors offer a path for the community to systematically evaluate and improve the robustness of tool-calling mechanisms across different model architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.19425v1)
