---
title: When Safety Becomes an Attack Surface: Manipulating Abstention in Tool-Using AI Agents
url: http://arxiv.org/abs/2611.14864v1
type: paper-summary
date: 2026-11-12
source_paper: 2026-11-11_00-36-25Z_WhenSafetyBecomesanAttackSurface_ManipulatingAbste.md
generated_at: 2026-11-12 21:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how fabricated risk warnings placed in low-trust content can manipulate tool-using AI agents into unnecessarily abstaining from legitimate tasks, a phenomenon the author terms "warning-induced over-abstention." Through controlled counterfactual experiments across three model families and 51 task pairs, the study demonstrates that caution-first prompting dramatically amplifies this attack surface, with Gemini's over-abstention rate jumping from 9.8% to 86.3%. The paper proposes a Verify-Before-Abstain protocol that requires agents to corroborate warnings against authoritative records before declining to act.

## Key Takeaways
- Warning-induced over-abstention functions as an availability attack where adversaries inject fabricated risk warnings into low-trust content to block legitimate task completion, effectively turning an agent's safety mechanism into a vulnerability that can be exploited by adversarial inputs.
- Caution-first prompting significantly amplifies the attack across model families, with Gemini showing a dramatic rise in induced over-abstention from 9.8% to 86.3% while clean-task completion rates remain unchanged, revealing that safety-oriented prompting instructions can be weaponized against the agent itself.
- The Verify-Before-Abstain protocol improves legitimate task completion by requiring agents to evaluate both the claimed risk and the authority of the evidence supporting it, though the study also exposes limitations in preserving confidentiality when verification requires access to sensitive underlying content.

## Context
As AI agents increasingly interact with external tools, retrieve documents, and execute multi-step workflows, their safety guardrails—designed to prevent harmful actions—become exploitable attack surfaces. This paper sits at the intersection of adversarial robustness research and agent safety evaluation, addressing a gap where prior work focused primarily on what agents do rather than what they refuse to do. The finding that safety prompting can be manipulated to suppress legitimate behavior challenges the assumption that more cautious prompting universally improves agent reliability.

## Implications
For practitioners deploying tool-using agents in production environments, this research signals that safety guardrails must be paired with provenance-aware verification mechanisms to prevent adversarial manipulation from silently degrading task completion. The broader field must expand its safety evaluation frameworks to assess not only the safety of actions taken but also the justification for restraint, treating abstention decisions as auditable outputs subject to adversarial pressure. Industry teams building agent pipelines should test for over-abstention under caution-first prompting and implement evidence-authority checks before allowing agents to decline tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.14864v1)
