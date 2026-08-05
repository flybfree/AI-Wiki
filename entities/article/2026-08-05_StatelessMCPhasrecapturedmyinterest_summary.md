# Summary: 2026-08-05_StatelessMCPhasrecapturedmyinterest.md
Saved: 2026-08-05 01:33
Source: 2026-08-05_StatelessMCPhasrecapturedmyinterest.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Simon Willison revisits the Model Context Protocol (MCP) after its 2026‑07‑28 “stateless” specification rollout reignited his personal interest. He contrasts the legacy stateful MCP, which required two HTTP calls and server‑side session handling, with the new stateless version that uses a single request and eliminates session IDs entirely.

## Key Takeaways  
- **Simplified implementation:** The stateless spec removes the need for client‑ or server‑side state tracking of session IDs, making both clients and servers easier to implement.  
- **Cleaner API:** A single HTTP POST replaces two calls, resulting in a more readable request that can be integrated directly into web applications.  
- **Broader adoption potential:** MCP tools are now lightweight enough for smaller models running on laptops, unlike the risk‑laden terminal/curl approach of legacy stateful MCP.

## Context  
The article situates MCP within the broader AI landscape where Anthropic introduced both MCP and Skills to expose tools to LLM agents. While Skills gained traction with a terminal‑plus‑curl workflow, MCP’s stateless design offers an alternative that is more auditable and scalable for web‑based agent frameworks.

## Implications  
For the field, this shift encourages developers to adopt standardized, stateful‑free protocols that reduce complexity and security risks. It also democratizes tool integration by allowing smaller models to participate in agent workflows without heavy infrastructure, potentially accelerating innovation across AI‑driven applications.
