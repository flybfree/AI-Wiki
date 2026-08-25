---
title: PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies
url: http://arxiv.org/abs/2608.23028v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_09-33-26Z_PsychJail_ExploringPsychologicalJailbreaksviaMulti.md
generated_at: 2026-08-24 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PsychJail, a psychology‑guided framework for red‑team testing large language models through multi‑turn persuasion attacks. Experiments show that the approach achieves an average success rate of 87.3% across four aligned victim models and outperforms both single‑turn and multi‑turn baselines on every model.

## Key Takeaways
- PsychJail maps established social‑psychological persuasion techniques into a tactic‑conditioned attack policy, factorizing each attacker action into a Change‑of‑Meaning analysis, tactic selection, and victim‑visible message.  
- The framework uses trajectory‑level reinforcement learning with a PKM‑gated reward that only credits early jailbreak success when every turn contains a well‑formed Change‑of‑Meaning analysis.  
- Susceptibility measurements reveal four distinct model‑level fingerprints—rationalist, credibility‑driven, narrative‑monoculture, and broadly persuadable—that explain cross‑model transfer asymmetry.

## Context
Most LLM safety research focuses on single‑turn prompt optimization or iterative attack refinement, which often ignores the sustained social interaction typical of educational, healthcare, or policy advising settings. This paper addresses that gap by exploring vulnerabilities that arise from multi‑turn persuasion dynamics.

## Implications
Psychological jailbreaks constitute a new red‑teaming frontier for increasingly interactive LLMs. Practitioners can use these model‑specific psychological profiles to design more effective defenses and better understand where persuasion levers are most effective.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23028v1)
