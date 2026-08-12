---
title: On Understanding, Identifying, and Mitigating Vulnerabilities in Agentic Large Language Models
url: http://arxiv.org/abs/2608.10530v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_06-11-26Z_OnUnderstanding_Identifying_andMitigatingVulnerabi.md
generated_at: 2026-08-11 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper aims to map the security landscape of agentic large language models by conducting a systematic literature review that identified 85 relevant papers from 2023 to 2025 across six databases. It found that perception‑layer attacks are far more common than action‑layer threats, revealing a gap between attack research and defensive measures.

## Key Takeaways
- Perception‑layer vulnerabilities such as prompt injection and jailbreaking account for 66% of the surveyed papers, indicating they are the primary focus of current research.  
- Action‑layer issues like tool misuse or code injection appear only in 4.7% of studies, suggesting a misalignment between theoretical risk and real‑world impact.  
- Code execution security contributes just 3.5% of papers while tool‑augmented agents are mentioned in 12%, highlighting uneven coverage across attack categories.

## Context
Agentic LLMs extend beyond chatbots to perform real actions, making them attractive targets for malicious actors seeking unauthorized data access or system disruption. The paper’s taxonomy helps researchers categorize threats and prioritize mitigation efforts.

## Implications
For practitioners, the taxonomy provides a structured approach to evaluate vulnerabilities across perception, brain, action, and interaction layers. Addressing this gap is essential as agentic AI becomes embedded in critical infrastructure and reduces long‑term risk of cascading failures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10530v1)
