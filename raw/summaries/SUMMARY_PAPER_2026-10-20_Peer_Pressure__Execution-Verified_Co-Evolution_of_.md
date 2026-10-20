---
title: Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security
url: http://arxiv.org/abs/2610.24896v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-17_22-36-09Z_PeerPressure_Execution_VerifiedCo_EvolutionofAttac.md
generated_at: 2026-10-20 00:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Peer-Relative Policy Optimization (PRPO), a method that co-trains attacker and defender populations of LoRA adapters over a single frozen base model, using execution-verified rewards to drive adversarial co-evolution for code security. The approach demonstrates that a 7B diff reviewer can outperform both supervised security fine-tuning and a frontier model (Claude Opus 4.8) on vulnerability detection across unseen applications and untrained languages, while the same algorithm generalizes to jailbreak defense with dramatic reductions in attack success rates.

## Key Takeaways
- Execution-verified rewards enforce strict grounding: an attacker earns reward only if its patch applies to a real repository, builds successfully, passes tests, completes the development task, and reproduces a real exploit in an isolated container whose execution path labels the entry point, critical operation, and trace between them. This eliminates reward hacking and ensures adversarial pressure is tied to genuine code behavior rather than superficial pattern matching.
- PRPO places the population inside the policy-gradient baseline rather than the opponent pool, crediting each agent against same-role peers that faced an identical condition. This matching cancels condition difficulty, yielding 2.3 points of balanced accuracy over a baseline computed on other conditions at equal coverage, and matches a within-policy control at half the verifier spend, making adversarial training computationally tractable.
- The 7B diff reviewer achieves 64.8% balanced accuracy on four unseen applications in three untrained languages, surpassing supervised fine-tuning by 5.5 points and Claude Opus 4.8 by 4.4 points. The 9B repository agent recovers 23 of 172 held-out VulnGym advisories versus 10 after supervised fine-tuning, and generalizes unchanged to jailbreak defense, cutting attack success from 36.0% to 4.6% under a judge distinct from its training oracle.

## Context
As LLM code agents increasingly ship production code with minimal human oversight, static vulnerability datasets and supervised fine-tuning pipelines struggle to keep pace with adapting adversaries that exploit novel attack surfaces. This paper addresses a fundamental gap in adversarial training for code security: prior approaches train defenders against fixed or synthetic threat distributions, leaving them brittle when real-world attackers evolve. By co-evolving both sides through execution-grounded rewards and peer-relative credit assignment, the work bridges reinforcement learning methodology with practical software security, offering a scalable alternative to frontier-model reliance for vulnerability detection and defense.

## Implications
For practitioners deploying code agents in production, this work suggests that small, co-trained adversarial populations can match or exceed frontier-model security review at a fraction of the inference cost, potentially enabling continuous self-improving security pipelines without dependence on expensive external APIs. For the broader AI safety and alignment community, the execution-verified reward structure and peer-relative baseline design offer a template for adversarial training that resists reward hacking and generalizes across task domains—from code vulnerability detection to jailbreak defense—without task-specific retraining, pointing toward more robust and economically accessible safety infrastructure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24896v1)
