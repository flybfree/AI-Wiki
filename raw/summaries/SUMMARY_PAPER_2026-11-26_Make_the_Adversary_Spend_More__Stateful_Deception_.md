---
title: Make the Adversary Spend More: Stateful Deception as a Cost-Exchange Primitive for AI-Era Cyber Defense
url: http://arxiv.org/abs/2611.34770v1
type: paper-summary
date: 2026-11-26
source_paper: 2026-11-25_17-35-27Z_MaketheAdversarySpendMore_StatefulDeceptionasaCost.md
generated_at: 2026-11-26 21:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper argues that cyber deception in the AI era should be judged by the cost exchange it imposes, not by realism or detection. It proposes adversary-specific persistent state as the primitive that makes that exchange favorable: each recognized adversary re-enters a world coherent with its own past actions and isolated from every other adversary, while the language model acts only as a constrained renderer of explicit state, never as its store. The authors formalize the trade-off as a Deception Exchange Rate (DER) and instantiate it in an SSH honeypot pairing Cowrie with a local LLM, reporting that deterministic-layer and prompt optimizations cut per-session defender cost by around 63% across five open-weight models versus a naive all-LLM decoy.

## Key Takeaways
- LLMs are transforming the economics of intrusion by reducing the attacker's cost to scan and adapt, while tempting defenders into unbounded compute; deception should therefore be evaluated by the cost exchange it imposes rather than by realism or detection.
- Adversary-specific persistent state is the central primitive: rather than a honeypot that resets or merges sessions, each recognized adversary re-enters the world it believes it has compromised, kept coherent with its own past actions and isolated from every other adversary, with the LLM serving only as a constrained renderer of explicit state and never as its store.
- The authors formalize the trade-off as DER, relating mission-weighted adversary effort burned to defender resources spent, instantiate it in an SSH honeypot pairing Cowrie with a local LLM, and report roughly 63% lower per-session defender cost across five open-weight models; per-adversary state and the adversary side of the DER are specified but not yet measured.

## Context
This work sits at the intersection of generative AI and security economics, where attackers can now scan and adapt cheaply while defenders risk unbounded compute if LLMs are allowed to drive decoys freely. It reframes deception as a resource-exchange problem, elevating state management and cost accounting above surface realism as the central design concerns for AI-era defense.

## Implications
Practitioners should design decoys around explicit, per-adversary state and cost-aware rendering rather than unbounded LLM generation. The DER framing gives defenders a measurable objective for balancing attacker effort against defender spend, though the adversary-side and per-adversary state measurements remain open for future work.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.34770v1)
