---
title: Where Did the Repair First Go Wrong? Localizing the Origins of Silent Failures in Agentic Vulnerability Repair
url: http://arxiv.org/abs/2610.06163v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-05_11-31-16Z_WhereDidtheRepairFirstGoWrong_LocalizingtheOrigins.md
generated_at: 2026-10-05 22:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Security Awareness Gap Evaluation (SAGE), a trace-based diagnostic method designed to pinpoint the exact turn in an LLM agent's repair workflow where a silent failure first originates—meaning a patch that passes syntactic and functional validation yet still harbors a security vulnerability. Evaluated across 95 confirmed silent failures drawn from 3,684 repair traces spanning six agent frameworks and six base models, SAGE successfully assigned a failure origin in 93 cases, revealing that most failures stem from unaddressed security requirements or inadequate defence choices rather than from the code-writing step itself.

## Key Takeaways
- SAGE works by combining a per-turn assessment of the agent's recorded security reasoning with a reconstructed code history, enabling identification of the earliest turn at which the repair diverges from the task's security intent. This is critical because silent failures produce no observable failure signal, making traditional failure attribution methods—which depend on observed task failures and labelled failure steps—ineffective for diagnosing them.
- The empirical findings show that the origin of a silent failure is overwhelmingly upstream of the actual code change: only five out of 93 assigned origins coincided with the code-writing step, and when the agent did introduce vulnerable code, the causal origin preceded the write in 14 of 19 cases. This indicates that safeguarding efforts should target earlier reasoning and planning stages rather than post-hoc code review.
- Reliability analysis reveals that repeated scoring and a second independent judge reproduced the origin type (e.g., unaddressed requirement vs. inadequate defence) more consistently than the exact turn number, and agreement was lowest for traces that retained only the final file rather than intermediate reasoning steps, highlighting the importance of preserving full agent traces for effective diagnosis.

## Context
Agentic vulnerability repair—where LLM-driven agents autonomously patch security flaws in software—is increasingly deployed in developer tooling and automated maintenance pipelines. However, the community lacks robust methods for understanding why an agent produces a patch that looks correct on the surface yet still fails to close a security gap. This paper addresses that gap by reframing failure attribution for agentic workflows: instead of waiting for a downstream test to fail, SAGE audits the agent's internal reasoning trace turn by turn, aligning with broader efforts in AI safety and interpretability to make agent decision processes inspectable and auditable.

## Implications
For practitioners building agentic repair systems, the findings suggest that adding safeguards at the code-generation stage alone is insufficient; instead, frameworks should enforce explicit security-requirement tracking and defence-choice validation during planning and reasoning turns. For the research community, SAGE provides a reproducible evaluation protocol that can be applied across agent frameworks and base models to benchmark where security reasoning breaks down, guiding the design of next-generation agents that are not merely syntactically correct but genuinely security-aware. The finding that trace completeness strongly affects diagnostic reliability also argues for standardized logging of intermediate agent reasoning in production repair pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06163v1)
