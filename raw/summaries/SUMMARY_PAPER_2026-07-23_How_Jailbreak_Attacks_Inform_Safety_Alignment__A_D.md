---
title: How Jailbreak Attacks Inform Safety Alignment: A Defender-Centric, Shapley-Based Evaluation of Jailbreak Contributions
url: http://arxiv.org/abs/2607.17152v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-19_09-18-35Z_HowJailbreakAttacksInformSafetyAlignment_ADefender.md
generated_at: 2026-07-23 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a defender‑centric evaluation of jailbreak attacks on large language models, moving beyond attacker‑centric metrics such as attack success rate. It introduces A‑MESS and its Shapley‑based metric AttackSHAP to attribute the marginal safety improvement each attack enables when used for red‑team training. Experiments show that ASR rankings do not strongly correlate with defender‑centric utility, while AttackSHAP can be estimated accurately with few utility queries and that directly optimizing attack subsets yields stronger safety improvements than attribution‑only or attacker‑centric approaches.

## Key Takeaways
- The paper demonstrates that jailbreak attacks are evaluated by the downstream safety gains they generate rather than solely by their success rate.  
- AttackSHAP provides a Shapley‑based score that accurately attributes marginal utility to individual attacks, enabling compact subset selection under user budgets.  
- Optimizing attack subsets directly improves safety outcomes more effectively than relying on attacker‑centric metrics or attribution alone.

## Context
Current AI safety research often focuses on preventing model misuse by measuring how easily an adversary can bypass safeguards. This work shifts attention to the utility of those very attacks as data for improving model robustness, highlighting a gap between technical evaluation and practical safety gains.

## Implications
For researchers and practitioners, this study suggests that evaluating jailbreak attacks through their contribution to safety is more informative than traditional success‑rate metrics. It also introduces a scalable attribution framework—AttackSHAP—that can guide resource allocation in red‑team testing, encouraging safer model development pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17152v1)
