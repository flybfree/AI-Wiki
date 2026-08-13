# Summary: 2026-08-13_DeepSeekV4Pro0813.md
Saved: 2026-08-13 00:06
Source: 2026-08-13_DeepSeekV4Pro0813.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
DeepSeek V4 Pro 0813 is a high‑performance language model offered through OpenRouter, which aggregates and routes all requests to a single provider without any routing decisions. The article reports its pricing, latency/throughput metrics, uptime reliability, and the real‑world applications that are currently using it.

## Key Takeaways  
- Weighted average input price is $0.0335 per M tokens and output price is $0.8696 per M tokens, indicating a relatively low cost for inference.  
- Throughput reaches 56 tokens per second (P50) with latency of 1.5 seconds (P50), delivering fast response times for real‑time applications.  
- Provider uptime is consistently 100 % over the last three days, thanks to OpenRouter’s automatic failover routing.

## Context  
OpenRouter acts as a marketplace that hosts multiple AI models from various providers and ensures seamless delivery by monitoring each endpoint continuously. The DeepSeek V4 Pro model exemplifies how aggregators can combine technical performance with price transparency, allowing developers to compare real‑world usage against advertised rates.

## Implications  
The low per‑token pricing combined with sub‑second latency makes this model attractive for cost‑sensitive production workloads such as chatbots, coding assistants, and agentic tools. Its 100 % uptime reliability reduces the risk of downtime in mission‑critical deployments, while the lack of benchmark data suggests that performance is being validated through actual user traffic rather than isolated tests. Consequently, DeepSeek V4 Pro could become a baseline for evaluating emerging open‑source models in commercial AI services.
