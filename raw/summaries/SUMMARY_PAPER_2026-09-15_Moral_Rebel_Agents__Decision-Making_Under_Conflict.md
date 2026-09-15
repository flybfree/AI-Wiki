---
title: Moral Rebel Agents: Decision-Making Under Conflicting Obligations
url: http://arxiv.org/abs/2609.14716v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-13_18-19-02Z_MoralRebelAgents_Decision_MakingUnderConflictingOb.md
generated_at: 2026-09-15 03:31
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper investigates moral rebellion in autonomous agents, examining how systems should navigate conflicts between user-assigned tasks and emerging ethical obligations during execution. The authors formalize five distinct agent architectures ranging from purely task-focused to various combinations of utilitarian and deontological reasoning. Through empirical evaluation in a search-and-rescue scenario, the study demonstrates that preserving commitments to assigned tasks significantly influences moral decision-making outcomes and reveals clear trade-offs across different architectural designs.

## Key Takeaways
- The research formalizes four distinct forms of moral rebel agency alongside an amoral baseline, including utilitarian, deontic, utilitarian-deontic (UD), and dutiful architectures, each handling the tension between task completion and ethical constraints differently.
- Implementation within a hierarchical task network planning framework reveals that agents exhibit clear trade-offs among rescue outcomes, assigned-task fulfillment, and normative compliance, with no single architecture dominating across all metrics.
- The preservation of initial commitments emerges as a critical dimension of moral rebellion, causing UD and dutiful agents to diverge substantially in behavior despite sharing similar utilitarian and deontological foundations.

## Context
As autonomous systems increasingly operate in complex, real-world environments where ethical dilemmas arise dynamically, aligning machine decision-making with human values remains a critical challenge. This work contributes to the growing field of AI ethics by providing formalized architectures that explicitly model moral rebellion rather than enforcing rigid obedience or complete moral neutrality, bridging theoretical philosophy and practical agent design.

## Implications
Practitioners developing autonomous systems must recognize that strict task compliance can conflict with ethical imperatives, requiring careful architectural choices based on domain-specific priorities. The findings suggest that commitment-aware moral reasoning should be integrated into planning frameworks to ensure agents behave predictably and responsibly when facing competing obligations in high-stakes environments like disaster response or healthcare.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.14716v1)
