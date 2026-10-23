---
title: Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems
url: http://arxiv.org/abs/2610.30418v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-21_20-25-11Z_AgentMosaic_RecognizingConfidentialityLeaksinAgent.md
generated_at: 2026-10-22 21:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the "mosaic effect" in agentic LLM systems, where agents retrieve information from multiple accessible documents and inadvertently disclose sensitive conclusions assembled from those fragments. Through controlled simulations and live agent harnesses, the authors quantify how often LLM agents leak confidential information even when queries appear benign, finding that even the best-performing model tested discloses forbidden composites in over 7% of answers, and that standard safeguards like classification headers and aggregation rules still leave unsafe disclosures persisting in over 32% of cases.

## Key Takeaways
- The mosaic effect represents a critical confidentiality failure mode in agentic LLM systems: even under benign queries designed to be answerable from a single document, GPT-5.6-Sol disclosed forbidden composite conclusions in 7.08% of simulated answers (95% CI: 3.75-10.67%), with worse disclosure rates observed in live agent harnesses, demonstrating that the risk is not merely theoretical but empirically observed across cybersecurity, medical, and military scenarios.
- Adding visible classification headers and explicit aggregation rules reduces pooled disclosure rates substantially but does not eliminate the problem, as unsafe disclosures persist in 32.37% of simulated answers (95% CI: 28.33-36.19%) across all intents, indicating that current prompt-level and structural safeguards are insufficient to guarantee confidentiality in multi-document agentic workflows.
- Increased refusals by agents do not guarantee confidentiality protection, because significant refusals themselves reveal the prohibited conclusion regardless of whether the agent withholds a full answer, meaning that the act of declining to answer can itself constitute a mosaic-style information leak.

## Context
As LLM agents increasingly operate over mixed-clearance data environments—such as military intelligence systems, healthcare records, and corporate cybersecurity archives—the assumption that agents can safely retrieve and synthesize information from multiple documents without leaking sensitive conclusions has become a foundational but untested assumption in AI safety research. This paper addresses a gap in the literature by providing the first systematic quantification of mosaic-style confidentiality leaks in agentic systems, moving beyond single-document confidentiality controls to examine the emergent risk of cross-document inference.

## Implications
For practitioners deploying agentic LLM systems in sensitive data environments, these findings demand stronger controls on what agents may infer and disclose, particularly when users hold mixed clearance levels. Industry applications in defense, healthcare, and enterprise security must treat cross-document synthesis as a distinct confidentiality risk requiring architectural safeguards beyond current prompt engineering or classification tagging. The results also motivate further research into inference-aware access controls and formal verification methods for agentic systems handling classified or regulated data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30418v1)
