---
title: FORK: Co-Evolving Safe Disclosure and Decision Skills Against Attackers Who Read Every Refusal
url: http://arxiv.org/abs/2611.33879v1
type: paper-summary
date: 2026-11-26
source_paper: 2026-11-25_06-57-56Z_FORK_Co_EvolvingSafeDisclosureandDecisionSkillsAga.md
generated_at: 2026-11-26 21:48
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper studies safe disclosure for LLM agent guardrails: when a guardrail rejects an action, the rejection message is visible to any attacker observing the trajectory, so a fixed refusal can leave benign users unable to recover, while an explanation may tell an adaptive attacker what to try next. FORK co-evolves a guardrail's natural-language decision and disclosure skills with an attacker that reads every public message, using each exploited message and permissive decision as evidence for gradient-free revision of the skill library. Across four benchmarks, FORK substantially reduces adaptive attack success while preserving benign utility.

## Key Takeaways
- The central tension is that rejection text is public: a fixed refusal blocks recovery for authorized users, whereas an explanation can leak actionable information to an attacker, so both what the guardrail blocks and what it reveals must be designed jointly.
- Hand-written rules cannot anticipate how adaptive attackers probe decisions or exploit messages; FORK instead co-evolves natural-language decision and disclosure skills with an attacker that reads every public message, and turns exploited messages and permissive decisions into evidence for gradient-free revision of the skill library.
- On FORK-World, averaged over three agents, FORK cuts adaptive attack success rate from 78.4% to 14.1% while keeping utility above 85%, outperforming baselines on both ASR and utility; on MT-AgentRisk, whose environments and tasks are unseen in training, FORK lowers ASR from 70.6% to 9.1% with 93.1% benign utility.

## Context
LLM agents are increasingly deployed in environments where adversaries can observe trajectories and adapt their attacks to the system's behavior. Guardrails must therefore balance safety against usefulness, and static, hand-written rules are poorly matched to adaptive probing. FORK reframes disclosure as a learned, co-evolving skill rather than a fixed policy, connecting guardrail design to adversarial adaptation.

## Implications
For practitioners, rejection text should be treated as a security surface rather than only a user-experience detail. A co-evolution approach that trains against an attacker reading every public message offers a practical route to guardrails that generalize to unseen tasks and environments while preserving benign utility, which matters for deploying agents in sensitive or high-stakes settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.33879v1)
