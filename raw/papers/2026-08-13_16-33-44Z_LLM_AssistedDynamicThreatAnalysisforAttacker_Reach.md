---
title: LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses in Autonomous Vehicles
published: 2026-08-13T16:33:44Z
authors: Md Wasiul Haque, Sagar Dasgupta, Mizanur Rahman, Md Rayhanur Rahman
url: http://arxiv.org/abs/2608.13450v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses in Autonomous Vehicles

## Abstract
Autonomous vehicles depend on large safety-critical software stacks, where weaknesses reachable from adversarial inputs may affect steering, braking, or other control decisions. Static analysis can identify candidate sites, but dynamically confirming exploitability requires executable test artifacts that are difficult to construct manually. We investigate whether large language models (LLMs) can automate this process for Autoware, an open-source autonomous-driving stack. We perform compiler-precise static analysis across 185 packages, identifying 1,375 decision rules, 2,274 validation checks, and 482 input-to-safety-output flows, from which we derive a weakness taxonomy and sample 740 reachable sites. Two local open-weight LLMs, a no-static-context ablation, and a naive-template baseline generate 3,700 artifact sets, which are compiled against the real build under sanitizers, repaired through compiler-in-the-loop feedback, and fuzzed when executable. The main result is a build-integration failure taxonomy showing that 80% of first-shot compilation failures arise from dependency wiring rather than program logic. The reasoning model compiled 64% of harnesses on the first attempt, compared with 6% for the code-specialized model. Repair achieved full object-compileability for the reasoning model only through extensive stubbing; fewer than half of its harnesses reached the fuzzer, and all 37 observed crashes originated in stubbed code rather than Autoware. No candidate weakness was dynamically confirmed within budget. These results show that build integration, not candidate generation or fuzzing, is the primary barrier to reliable LLM-assisted dynamic analysis of full autonomous-vehicle software stacks.

## Metadata
- **Published**: 2026-08-13T16:33:44Z
- **Authors**: Md Wasiul Haque, Sagar Dasgupta, Mizanur Rahman, Md Rayhanur Rahman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13450v1)