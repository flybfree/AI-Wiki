# Summary: 2026-09-24_02-00-20Z_ControltheHarness_ControltheCost_RoutingandGoverni.md
Saved: 2026-09-24 21:29
Source: 2026-09-24_02-00-20Z_ControltheHarness_ControltheCost_RoutingandGoverni.md
Model: None

---

## Summary  
This paper addresses a critical challenge in enterprise AI deployment: the high cost of AI coding agents driven by proprietary harnesses that lock users into expensive vendor pricing models. The authors introduce a customizable routing system called Jev, which dynamically manages model selection and task execution to minimize spend while preserving functionality. By analyzing real-world usage patterns from public datasets, they demonstrate that intelligent routing can recover significant savings—up to 21%—on annual cloud costs for large-scale deployments. Their work provides both a technical solution and a strategic framework for enterprises seeking control over AI tooling without sacrificing performance.

## Key Contributions  
- [Finding 1] The Jev router classifies user prompts using a calibrated classifier, enabling precise routing of AI coding agent tasks to the most cost-effective model tier based on task type, session length, and prompt cache usage.  
- [Finding 2] Empirical analysis of 10,000 real sessions from public datasets reveals that mid-task model switches can reduce costs by up to 21%, with high-priced models becoming cheaper than lower-tier ones due to reduced total token usage.  
- [Finding 3] A risk-mapping framework identifies twenty common enterprise harnesses and quantifies their financial dependencies on single vendors, highlighting the strategic vulnerability of entrenched pricing structures.

## Methodology  
The authors approached the problem by first modeling user behavior as a stream of prompts across AI coding agents, where each turn generates multiple sub-requests that share a persistent prompt cache. They built Jev—a lightweight, customizable router—that intercepts these requests and routes them to optimal model tiers without disrupting ongoing conversations. The system leverages calibrated probabilities from the classifier to predict which routing strategy minimizes cost, using real-world session data to validate pricing models across different harnesses.

## Results  
In an emulated enterprise of 10,000 seats with user behavior derived from public datasets, Jev recovered 14–21% in model spend compared to default vendor pricing at $3.3M to $5.0M annually on Anthropic’s list prices (September 2026). The router successfully avoided unnecessary mid-task switches and optimized subagent launches, proving that dynamic routing can significantly reduce enterprise AI costs without compromising functionality.

## Significance  
This research matters because it shifts the paradigm from passive cost absorption to active control over AI tooling. Enterprises no longer have to accept vendor-imposed pricing as immutable; instead, they can deploy a control plane that optimizes spend in real time. The ability to route tasks intelligently reduces financial risk and increases organizational autonomy, especially in high-volume environments where cumulative costs are substantial.

## Related Concepts  
- AI coding agents  
- Prompt cache management  
- Model tiering and pricing  
- Dynamic routing systems  
- Enterprise harnesses  
- Cost optimization in cloud AI  
- Subagent orchestration
