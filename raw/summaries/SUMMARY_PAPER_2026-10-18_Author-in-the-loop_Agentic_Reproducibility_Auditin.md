---
title: Author-in-the-loop Agentic Reproducibility Auditing for a Machine Learning Conference
url: http://arxiv.org/abs/2610.22465v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-15_17-28-51Z_Author_in_the_loopAgenticReproducibilityAuditingfo.md
generated_at: 2026-10-18 20:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces an author-in-the-loop collaborative audit system that integrates authors' explicit reproduction declarations into an AI agent's workflow for verifying reproducibility of machine learning conference papers. Deployed across 36 conference papers and 133 experimental tables and figures, the system raised 20 issues after human review, with further checks supporting the closure of all identified issues, though full reproduction remained unverified in some cases. The authors also conducted controlled comparisons between audits using complete versus blank checklists to quantify how author-provided declarations shape the agent's investigation and assessment quality.

## Key Takeaways
- The system employs a structured checklist that records reproduction instructions and limitations as explicit inputs to the AI agent, creating a two-stage GitHub-based workflow where agent checks trigger author clarification, revision, and agent reassessment cycles, ensuring that author knowledge actively guides the auditing process rather than being bypassed.
- The agent design separates two distinct assessment tasks: determining whether results have been reproduced, and determining whether authors need to provide clarification or make repairs, while human reviewers retain authority to approve requests and decide whether concerns are resolved, preserving human oversight in the decision chain.
- Empirical deployment across 36 conference papers and 133 experimental tables and figures produced 20 issues after human review, and comparative experiments with complete versus blank checklists demonstrated that author declarations measurably shaped the agent's investigation scope and assessment accuracy, validating the collaborative design.

## Context
Reproducibility remains a persistent and well-documented challenge in machine learning research, with peer review processes often lacking systematic mechanisms to verify that published code and results can be independently reproduced. This paper addresses a gap in the growing field of AI-assisted scientific auditing by proposing a framework where the author's own knowledge and declarations are treated as structured inputs rather than being ignored, bridging the divide between fully automated reproducibility checks and purely human-driven review. The work sits at the intersection of agentic AI systems, scientific workflow automation, and conference peer review infrastructure.

## Implications
For conference organizers and program committees, this approach offers a practical, deployable workflow that can be integrated into existing peer review pipelines to systematically surface reproducibility problems before publication, reducing the burden on human reviewers while maintaining their final decision authority. For practitioners and researchers, the findings suggest that providing clear reproduction instructions and limitations upfront materially improves the effectiveness of automated auditing, incentivizing better documentation practices. The controlled comparison between complete and blank checklists provides early empirical evidence that agentic auditing quality is sensitive to input completeness, which has direct implications for how future AI-assisted review tools should be designed and deployed across scientific communities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22465v1)
