---
title: PEAM: On-device Communication Agent for Personalized, Efficient and Autonomous Mobile Network Configuration
url: http://arxiv.org/abs/2610.14855v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_12-21-05Z_PEAM_On_deviceCommunicationAgentforPersonalized_Ef.md
generated_at: 2026-10-13 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
PEAM is an on-device LLM-based communication agent designed to autonomously generate personalized network-configuration rules that can be executed within milliseconds on smartphones, addressing the stringent latency constraints imposed by real-time mobile network decisions. The system fine-tunes a compact 4B-parameter model on manually annotated real-user data and operates through a two-phase architecture—batch rule generation during idle periods and rapid rule execution during context changes—achieving 99.13% correct network configuration decisions and 92.50% valid rule generation, substantially outperforming traditional expert-rule methods.

## Key Takeaways
- PEAM employs a two-phase operational design: a rule-generation phase performed during device idle periods (e.g., overnight) that analyzes historical network-configuration records in batches, reflects across batches to consolidate consistent evidence and reduce local bias, and a rule-execution phase triggered by communication context changes such as app switching or connectivity shifts, which searches a pre-built rule library for millisecond-level execution. This separation of heavy reasoning from time-critical inference is critical for meeting mobile latency constraints.
- The system constructs a persistent user profile from high-confidence rules to capture individual network preferences, incorporating this profile into each subsequent rule-generation cycle to improve accuracy and stability over time. This personalization mechanism allows PEAM to adapt to individual usage patterns rather than relying on static, one-size-fits-all configuration heuristics.
- PEAM fine-tunes a 4B-parameter on-device LLM using a dataset constructed from manually annotated real-user data, integrating domain-specific communication knowledge directly into the local model. The resulting system outperforms traditional expert-rule-based methods by 4.41% in correct configuration decisions and by 84.50% in valid rule generation, demonstrating that compact fine-tuned models can surpass hand-crafted heuristics for network configuration tasks.

## Context
This paper sits at the intersection of on-device large language model deployment and autonomous mobile system management, a rapidly growing area as compact LLMs become viable on consumer hardware. As mobile GUI agents and on-device decision-making systems proliferate, the challenge shifts from merely running models locally to ensuring they can make time-critical decisions under strict latency budgets. PEAM addresses a concrete, high-frequency decision domain—network configuration during app switching and connectivity changes—where traditional rule-based systems are brittle and cloud-based inference is too slow, making it a representative case study for how fine-tuned on-device agents can replace hand-engineered heuristics in latency-sensitive mobile workflows.

## Implications
For mobile OS developers and network optimization practitioners, PEAM demonstrates that fine-tuned compact models can autonomously learn and maintain personalized configuration policies that outperform expert-designed rules, potentially reducing the maintenance burden of hand-crafted network heuristics across diverse user populations. For the broader on-device AI community, the two-phase architecture—batch reflection during idle time and millisecond retrieval during execution—offers a reusable pattern for deploying LLM-based agents in any mobile context where inference latency must be decoupled from reasoning complexity, suggesting a pathway toward fully autonomous, personalized device management without cloud dependency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.14855v1)
