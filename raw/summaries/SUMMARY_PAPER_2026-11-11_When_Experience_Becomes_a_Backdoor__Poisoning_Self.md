---
title: When Experience Becomes a Backdoor: Poisoning Self-Evolving LLM Agents via Failure-Aware Task Optimization
url: http://arxiv.org/abs/2611.10542v1
type: paper-summary
date: 2026-11-11
source_paper: 2026-11-07_07-17-53Z_WhenExperienceBecomesaBackdoor_PoisoningSelf_Evolv.md
generated_at: 2026-11-11 21:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a novel security threat to self-evolving LLM agents: task-level backdoor attacks where an attacker injects poisoned evolution tasks to induce the agent to implant malicious rules into its own internally constructed skills. The authors propose BadEvolve, a failure-aware task-poisoning framework that diagnoses attack failures across four distinct stages of skill evolution and downstream execution, directing targeted updates toward the failing stage while employing rollback and failure memory mechanisms to preserve progress and avoid redundant ineffective updates. Extensive experiments across multiple self-evolution frameworks, benchmarks, and backbone LLMs validate the effectiveness of the proposed approach.

## Key Takeaways
- Self-evolving LLM agents that distill execution experience into persistent, reusable skills create a new attack surface: malicious rules implanted into skills can silently compromise all subsequent agent behavior, and existing skill backdoor attacks assume direct manipulation of skills, which is impractical when skills are constructed internally by a trusted evolver. The paper shifts the threat model to task-level attacks where the attacker can only inject poisoned evolution tasks, making the attack more realistic but also more challenging.
- Two critical challenges hinder naive iterative optimization of poisoned tasks: failures at different stages of skill evolution and downstream execution produce indistinguishable outcomes, providing little guidance for targeted updates, and unsuccessful updates may undermine earlier progress while simply discarding them leads to repeated ineffective attempts. These challenges motivate the need for stage-aware diagnosis rather than blind iterative refinement.
- BadEvolve addresses these challenges by decomposing the attack pipeline into four diagnosable stages—Induction, Activation, Following, and Effect—and directing poisoned-task updates specifically toward whichever stage is failing. It further incorporates rollback to preserve earlier progress and a failure memory mechanism to avoid repeating ineffective updates, yielding a more efficient and targeted attack strategy.

## Context
As LLM agents increasingly adopt self-evolution mechanisms—where they autonomously distill execution experience into persistent, reusable skills—the assumption that these skills are trustworthy and benign becomes a critical vulnerability. This paper sits at the intersection of adversarial robustness research, agent safety, and the emerging paradigm of self-improving AI systems. It highlights that the very mechanisms designed to make agents more capable and autonomous also introduce new, harder-to-detect security risks that traditional prompt injection or direct skill manipulation attacks do not capture.

## Implications
For practitioners deploying self-evolving agents in production, this work signals that the skill induction pipeline itself is an attack vector requiring dedicated monitoring and defense, not just the final skill library. Industry teams building autonomous agent frameworks should consider auditing the evolution tasks that feed into skill construction, since a poisoned task can silently corrupt downstream behavior across many future interactions. The BadEvolve framework also provides a diagnostic template for security researchers to stress-test agent self-improvement pipelines against stage-specific adversarial perturbations, informing the design of more robust self-evolution architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.10542v1)
