# Summary: 2026-07-26_10-29-20Z_AreYouStilltheAgentIAuthorized_EarnedAuthorityunde.md
Saved: 2026-07-27 23:54
Source: 2026-07-26_10-29-20Z_AreYouStilltheAgentIAuthorized_EarnedAuthorityunde.md
Model: None

---

## Summary  
The paper tackles the problem of authorization continuity for AI agents that continue to evolve after deployment, retaining experience and acquiring new tools or skills. It introduces a formal model that defines when an existing grant remains valid as the agent mutates, ensuring its authority never exceeds a ceiling set by the user at grant time. The authors fix a transition envelope and an immutable effect ceiling, thereby bounding all possible actions of the evolving agent. They prove that under certain safety conditions mutation cannot amplify protected effects beyond this original limit.

## Key Contributions  
- [Finding 1] The authors formalize authorization continuity by defining a fixed “effect ceiling” at grant issuance, which caps every action an evolving agent may perform.  
- [Finding 2] They distinguish between requested and realized effects and demonstrate that only evidence‑driven authority allocation can expand authority, never surpassing the original ceiling.  
- [Finding 3] The paper maps six mutation classes to precise authorization consequences, providing a taxonomy of how evolution impacts granted powers.

## Methodology  
The authors approach the problem theoretically by modeling agents as stateful systems with mutable capabilities. They fix a transition envelope that captures permissible changes and an immutable effect ceiling derived from the original grant. Using abstraction of effects, attenuating delegation, and monitor integrity, they prove bounds on authority expansion. The analysis is formalized in terms of state transitions and evidence allocation.

## Results  
The model proves that under complete mediation, sound effect abstraction, attenuating delegation, and monitor integrity, mutation cannot amplify protected effects beyond the user‑issued ceiling. It also classifies six mutation types (e.g., tool acquisition, workflow revision, cross‑task phase shift) and their impact on authority (contraction, expansion under evidence, incomparability). The theoretical guarantees are presented without empirical experiments.

## Significance  
This work resolves a critical safety gap in long‑lived AI agents by providing a principled framework for maintaining authorized behavior as agents evolve. It enables developers to set immutable ceilings that protect users even when the agent’s internal state changes, fostering trust and regulatory compliance.

## Related Concepts  
Authorization continuity, effect ceiling, transition envelope, state‑bound model, evidence‑driven authority allocation, mutation classes, tool‑enabled agency, prompt injection mitigation, delegated workflow revision.
