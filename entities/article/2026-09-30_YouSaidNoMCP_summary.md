# Summary: 2026-09-30_YouSaidNoMCP.md
Saved: 2026-10-25
Source: 2026-09-30_YouSaidNoMCP.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://earendil.com/posts/you-said-no-mcp/)

---

## Summary
The article details a strategic shift by Earendil Engineering regarding their Pi platform, specifically explaining why they have transitioned from rejecting Model Context Protocol (MCP) support to integrating it into the core functionality. The authors argue that while MCP previously lacked sufficient composability and utility for their specific needs, recent improvements in both the protocol itself and Pi’s internal architecture—particularly around tool loading and sandboxing—have made native integration viable and beneficial. This change reflects a broader reevaluation of how AI agents should interact with external tools, moving toward structured data exchange and improved composability rather than simple text dumping.

## Key Takeaways
- **Policy Reversal:** Earendil Engineering previously publicly dismissed MCP support for Pi, but has now integrated it into the core product after re-evaluating its utility and compatibility with their evolving architecture.
- **Architectural Necessity:** The integration was driven by technical requirements within Pi, specifically the need to handle modern LLM capabilities like deferred tool loading and mid-conversation system messages, which required better metadata handling than previous extension-based approaches could provide.
- **Composability Challenges Remain:** Despite the integration, the authors acknowledge that MCP still struggles with composability. Many existing MCP servers are optimized for token efficiency by returning text rather than structured data, which hinders effective agent-to-agent or tool-to-tool composition.

## Context
This development occurs within a rapidly evolving AI landscape where the standardization of tool interaction is critical for interoperability. The article highlights a tension between different approaches to tool usage: some systems rely on "codemode" sandboxes (like Codex) that allow agents to write code to call tools, while others use direct tool injection. Earendil’s shift suggests that hybrid approaches are becoming necessary as models gain more sophisticated capabilities, such as reasoning level adjustments and deferred loading. The reference to "OpenAPI with intelligent tool discovery" indicates a move toward treating AI tools similarly to web APIs, emphasizing structured data and discoverability over opaque text outputs.

## Implications
For the broader AI industry, this case study illustrates that initial skepticism toward emerging standards like MCP may be premature if those standards evolve alongside agent architectures. It suggests that successful AI systems will likely require deep integration of tool protocols rather than treating them as optional add-ons. Furthermore, it highlights a critical gap in current MCP implementations: the need for server developers to shift from text-based outputs to structured data formats to enable true composability. This could drive future standardization efforts toward more rigorous API-like definitions for AI tools, potentially influencing how third-party developers build and expose capabilities to LLMs.
