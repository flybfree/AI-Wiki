# Summary: 2026-07-28_15-50-16Z_DistributingSecurityControlsThroughHarnessEngineer.md
Saved: 2026-07-28 22:55
Source: 2026-07-28_15-50-16Z_DistributingSecurityControlsThroughHarnessEngineer.md
Model: None

---

## Summary  
The paper proposes a framework for distributing security controls to AI coding agents through a custom harness called SHarD (Secure Harness Distribution), aiming to eliminate vendor‑specific dependencies and enable scalable, consistent protection across diverse deployment contexts. By embedding OS sandboxing, skill scanning, and tool restriction directly into the Pi‑based agent harness, SHarD demonstrates that off‑the‑shelf controls can be applied uniformly while preserving the efficacy of commercial agents’ built‑in protections. The study uses a 23‑test suite derived from the OWASP Top 10 for Agentic Applications to evaluate these controls across four configurations: two commercial agents with and without controls, a baseline harness, and a security‑hardened harness. The results show that SHarD achieves an adjusted security score of 100 %, matching the best secured commercial agent, with no regression in any test category.

## Key Contributions  
- [Finding 1] A single install command can distribute three categories of security controls (OS sandboxing, skill scanning, tool restriction) to a distributed user base without compromising performance.  
- [Finding 2] SHarD’s adjusted score reaches 100 %, indicating that the harness provides security parity with the most securely configured commercial agent.  
- [Finding 3] Model non‑determinism can lead to inconsistent security outcomes, and autonomous agents may cross system boundaries, a risk directly mitigated by OS sandboxing.

## Methodology  
The authors employed a phased testing methodology across four distinct agent configurations: (1) two commercial AI coding agents with built‑in security controls, (2) the same agents without any added controls, (3) a baseline harness that installs no additional protections, and (4) a security‑hardened version of the Pi‑based SHarD harness. A 23‑test suite extracted from the OWASP Top 10 for Agentic Applications was used to measure outcomes in each configuration. The tests evaluated control effectiveness, system stability, and any impact on agent functionality.

## Results  
SHarD achieved an adjusted security score of 100 %, matching the best secured commercial agent across all test categories. No regression was observed between the baseline harness and SHarD, confirming that added controls do not degrade performance. The study also noted that model non‑determinism caused inconsistent security outcomes in some configurations, highlighting a limitation of purely software‑level checks.

## Significance  
This work bridges the gap between commercial AI coding agents and enterprise‑wide security governance by providing a distributable harness that enforces consistent protections without vendor lock‑in. It enables organizations to scale secure agentic workflows across heterogeneous environments while maintaining high protection levels, thereby addressing a key barrier to rapid adoption of AI agents.

## Related Concepts  
- AI coding agents  
- OWASP Top 10 for Agentic Applications  
- OS sandboxing  
- Skill scanning  
- Tool restriction  
- Harness engineering (SHarD)  
- Distributed security controls
