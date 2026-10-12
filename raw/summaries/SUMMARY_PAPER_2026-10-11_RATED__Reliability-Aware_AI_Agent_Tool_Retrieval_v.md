---
title: RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics
url: http://arxiv.org/abs/2610.13889v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_17-38-11Z_RATED_Reliability_AwareAIAgentToolRetrievalviaExec.md
generated_at: 2026-10-11 21:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces RATED, a retrieval framework for AI agent tool selection that augments semantic matching with real-time reliability adaptation based on execution feedback. The authors demonstrate that combining a frozen dual-encoder with a lightweight contextual bandit re-ranking module yields a 52.2% relative MRR improvement over ToolLLM and dramatically reduces fault selection rates under API outage conditions, all while adding less than 1 ms of latency overhead.

## Key Takeaways
- RATED addresses a critical gap in existing tool retrieval systems: while prior methods optimize semantic relevance between queries and tools, they ignore whether a tool is actually available and functional during execution. The framework bridges this gap by layering a contextual bandit module on top of a frozen dual-encoder, enabling dynamic re-ranking based on real-time execution feedback without requiring expensive model retraining.
- The authors introduce EcoAgent, a benchmark comprising 5,172 real-world tools and over 210,000 query-tool pairs, providing a standardized evaluation environment for both offline retrieval accuracy and dynamic reliability under failure conditions. This benchmark enables reproducible assessment of how retrieval systems behave when tools experience outages or degraded performance.
- Under severe API outage scenarios with a 30% failure rate, RATED reduces the fault selection rate from 86.2% down to 2.9%, demonstrating that execution-aware re-ranking can effectively steer agents away from unreliable tools. The system achieves this while incurring negligible latency overhead of less than 1 ms over encode-only inference, making it practical for production deployment.

## Context
As AI agents increasingly depend on external tool APIs for tasks ranging from code execution to web search, the reliability of tool retrieval has become a bottleneck for agent performance. Existing retrieval pipelines treat tool selection as a static semantic matching problem, assuming all candidate tools are equally available at query time. RATED represents a shift toward treating tool retrieval as a dynamic, feedback-driven process that accounts for runtime failures, aligning with broader trends in robust AI systems engineering and adaptive agent architectures.

## Implications
For practitioners deploying AI agents in production environments, RATED offers a practical path toward reducing tool failure cascades without retraining large language models or retrieval encoders, making it feasible to retrofit reliability awareness into existing agent pipelines. The EcoAgent benchmark provides the community with a standardized testbed for evaluating retrieval robustness under realistic failure distributions, which could accelerate the development of more dependable agent systems across industry applications where API outages and degraded tool availability are common operational hazards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13889v1)
