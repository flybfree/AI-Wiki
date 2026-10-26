# Summary: 2026-09-30_Pi_dev_YouSaidNoMCP.md
Saved: 2026-10-25
Source: 2026-09-30_Pi_dev_YouSaidNoMCP.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://earendil.com/posts/you-said-no-mcp/)

---

## Summary
The article details a strategic shift by Earendil Engineering regarding their Pi.dev platform, specifically reversing previous public dismissals of the Model Context Protocol (MCP) to integrate it directly into the core functionality. This decision stems from an acknowledgment that while MCP has evolved, its current implementation still suffers from poor composability and reliance on text-based outputs rather than structured data. The integration is driven by technical necessities within Pi’s architecture, particularly the need for better metadata handling to support advanced LLM capabilities like deferred tool loading and code-mode execution.

## Key Takeaways
- **Strategic Reversal:** Earendil Engineering previously advocated against MCP support in Pi.dev, citing its limitations, but has now integrated it into the core after re-evaluating the protocol's evolution and utility.
- **Composability Challenges:** The primary criticism of current MCP implementations remains their difficulty in composition; many servers return unstructured text to optimize token efficiency, which hinders effective agent orchestration compared to traditional CLI tools or OpenAPI-style structured data.
- **Architectural Necessity:** Integrating MCP into the core was necessary to enable features like "Jev" and to properly configure tool availability for modern LLMs that support deferred tool loading and mid-conversation system messages, which standard extensions could not adequately support due to insufficient metadata exposure.

## Context
This development highlights a broader industry tension between standardized interoperability protocols (like MCP) and the practical needs of agentic workflows. While MCP aims to provide a universal interface for AI tools, its current adoption often clashes with the desire for efficient, composable code execution environments like "Codemode." The article reflects a growing consensus that tool interfaces must evolve from simple text-dumping mechanisms toward structured, discoverable APIs akin to OpenAPI, allowing agents to wire together complex operations efficiently. It also underscores the rapid pace of change in AI infrastructure, where previous architectural stances may become obsolete as underlying models and protocols mature.

## Implications
For the AI development community, this shift signals that rigid opposition to standardization protocols is becoming untenable as model capabilities advance. Developers must now consider how to bridge the gap between standardized tool interfaces (MCP) and high-performance execution environments (Codemode/JavaScript sandboxes). The integration suggests that future AI platforms will likely require hybrid architectures that support both structured data discovery for interoperability and sandboxed code execution for composability. Furthermore, it implies that tool metadata and configuration are becoming critical components of LLM harnesses, moving beyond simple function calling to more sophisticated management of tool availability and reasoning levels. This may pressure MCP server developers to adopt stricter structured output standards to remain compatible with advanced agent frameworks.
