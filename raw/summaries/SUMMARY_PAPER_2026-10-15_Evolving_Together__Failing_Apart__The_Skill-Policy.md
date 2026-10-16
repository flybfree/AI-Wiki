---
title: Evolving Together, Failing Apart: The Skill-Policy Co-evolution Trap in Self-Improving Agents
url: http://arxiv.org/abs/2610.20845v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-14_19-29-45Z_EvolvingTogether_FailingApart_TheSkill_PolicyCo_ev.md
generated_at: 2026-10-15 21:02
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies a critical blind spot in skill-policy co-evolution methods for self-improving agents: current evaluations measure performance on the final skill bank the policy was trained with, but in deployment, skills drift through rewriting, addition, or removal far more frequently than the policy is retrained. Through both theoretical analysis and empirical testing across four co-evolution methods and five benchmarks, the authors demonstrate that co-evolved policies become increasingly fragile as training progresses, losing 52–93% of their performance gains under realistic skill drift. They introduce CODA, a deployment-oriented evaluation protocol that simulates drift and measures consistency under meaning-preserving edits and resistance to corrupted skills, reframing the goal from peak co-evolved performance to robust skill utilization.

## Key Takeaways
- The shared acceptance rule across co-evolution methods, termed "cooperative acceptance," structurally ties a policy's competence to the specific skill bank it co-evolved with, making fragility under drift an inherent property of the paradigm rather than an implementation bug. This means no current method escapes this vulnerability regardless of engineering choices.
- Empirical sensitivity to skill drift grows monotonically as co-evolution training proceeds, meaning longer training cycles produce policies that are paradoxically more brittle in deployment. Worst-case success drops 5–13 points below peak delivered-pair performance, erasing 52–93% of the gain over a no-skill baseline across six experimental settings.
- CODA introduces two novel metrics beyond standard success rate: a consistency rate measuring whether the policy still functions correctly under meaning-preserving skill edits, and a resistance rate measuring robustness against corrupted or adversarial skills. These metrics expose failure modes invisible to conventional evaluation and establish a shared auditing standard for future co-evolution research.

## Context
Self-improving agents that iteratively refine both their reasoning policy and their external skill library represent a leading frontier in autonomous AI systems, with applications spanning software engineering agents, research assistants, and multi-step tool-use systems. The co-evolution paradigm has shown impressive peak performance in controlled benchmarks, yet the field has lacked evaluation protocols that account for the operational reality that skill libraries are living documents updated by humans or automated pipelines between policy retraining cycles. This paper fills that evaluation gap by formalizing drift as a first-class concern rather than an afterthought.

## Implications
For practitioners deploying self-improving agents in production, this work signals that headline benchmark scores from co-evolution papers may substantially overestimate real-world reliability, and teams should audit policies against drifted skill banks before deployment rather than trusting delivered-pair metrics. For the research community, CODA provides a standardized auditing framework that future co-evolution methods must pass, shifting the design target from maximizing peak co-evolved performance to building policies that remain competent as skills evolve independently. This reframing could redirect methodological investment toward drift-robust training objectives and skill-bank versioning strategies that current pipelines largely ignore.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20845v1)
