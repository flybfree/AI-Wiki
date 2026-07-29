# Summary: 2026-07-28_07-16-12Z_Explanation_BoundToolExecutionforAIAgents_Server_V.md
Saved: 2026-07-28 20:21
Source: 2026-07-28_07-16-12Z_Explanation_BoundToolExecutionforAIAgents_Server_V.md
Model: None

---

## Summary  
The paper introduces Explanation‑Bound Tool Execution (EBTE), a mediation layer that transforms free‑form rationales into typed action claims which are then verified against server‑held facts such as intent, policy, payload, tool capabilities, risk, provenance and freshness. By relying on explicit trusted‑fact assumptions rather than trusting the model’s own rationale, EBTE enables server‑verified execution without compromising the original explanation. The authors formalize this composition under a claim‑carrying mediation framework and implement it with a versioned reference profile that minimizes audit overhead.

## Key Contributions  
- **Claim‑to‑Fact Verification:** EBTE converts decision‑relevant rationale into structured action claims and checks them against a comprehensive set of server‑held facts, rejecting any claim that conflicts or is incomplete.  
- **Formal Mediation & Trusted‑Fact Assumptions:** The authors provide a formal model of the mediation process, grounding it in explicit trusted‑fact assumptions to guarantee that only matching claims are authorized for execution.  
- **Empirical Validation:** Across 136 authored conformance scenarios the full profile matches all specified dispositions, admits none of the 96 designated hard contradictions, and passes 232 metamorphic checks; integration with AgentDojo shows high‑risk attacks are denied both pre‑ and post‑EBTE.

## Methodology  
The authors designed EBTE as a claim‑carrying mediation layer that parses free‑form rationales into typed claims. The verification step consults server‑held facts—intent, policy, payload, tool, risk, provenance, freshness—to evaluate each claim’s eligibility for execution. Conflicts trigger denial; uncertain or incomplete claims are reviewed but not executed. To reduce audit burden, a versioned reference profile stores only the necessary facts in minimal packets. The system was integrated into AgentDojo’s semantic check pipeline and evaluated on a frozen 2026‑07‑12 record.

## Results  
The experimental evaluation demonstrates that EBTE fully aligns with authorial specifications: all 136 conformance scenarios are satisfied, no hard contradictions slip through, and the system passes extensive metamorphic checks. In draft‑only integration, none of the 48 hard cases are forwarded while preserving soft‑review (16) and aligned draft paths (4). Historical generation/runner agreement counts are 71/96, 66/96, and 19/32; a post‑hoc revalidation yields similar results (70/96, 65/96, 17/32). AgentDojo’s high‑risk controls already block all 12 attack proposals, and EBTE resolves them as deny.

## Significance  
These findings prove that server‑checked action claims are feasible and diagnostically valuable, offering a path to safer AI agents without requiring reliance on model rationales or extensive human review. The approach highlights the diagnostic value of explicit mediation rather than rationale faithfulness, and it shows how minimal audit packets can support robust governance.

## Related Concepts  
Explanation‑Bound Tool Execution (EBTE), claim‑carrying mediation layer, typed action claims, server‑held facts (intent, policy, payload, tool, risk, provenance, freshness), explicit trusted‑fact assumptions, formal mediated composition, versioned reference profile, audit packets, AgentDojo semantic check, metamorphic checks, conformance scenarios.
