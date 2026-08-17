---
title: ASSERT: A Measurement Pipeline for GenAI Audits
published: 2026-08-14T00:07:32Z
authors: Riccardo Fogliato, Abhinav Palia, Xiawei Wang, Emily Sheng, Chad Atalla, Jean Garcia-Gathright, Nicholas Pangakis, Sharman Tan, Dan Vann, Hannah Washington, P. Alex Dow, Heba Elfardy, Hanna Wallach, Sandeep Atluri
url: http://arxiv.org/abs/2608.13840v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ASSERT: A Measurement Pipeline for GenAI Audits

## Abstract
Audits of generative AI (GenAI) systems often summarize behavior as a reported rate: how often the audited system complies with policy. Researchers and stakeholders use that rate to compare systems, track regressions, and gate deployment. A reported rate reflects both the system under audit and the measurement choices behind it, so a change in the rate can leave it unclear whether the system or those choices moved. We introduce ASSERT, a specification-driven measurement pipeline for GenAI audits that ties each reported rate to a written specification of the measurement choices used to produce it. ASSERT helps draft a behavioral rubric and test cases, then runs the audit against a GenAI system and returns a reported rate. In a case study on conversational deception, we observe that the reported rate moves substantially with the dialogue setup, the simulated user, the judge, and the evidence bar for non-compliance. These measurement choices substantially change the reported rate and can reorder GenAI system rankings. Because each reported rate is tied to an explicit specification, differences across audits are easier to attribute and interpret.

## Metadata
- **Published**: 2026-08-14T00:07:32Z
- **Authors**: Riccardo Fogliato, Abhinav Palia, Xiawei Wang, Emily Sheng, Chad Atalla, Jean Garcia-Gathright, Nicholas Pangakis, Sharman Tan, Dan Vann, Hannah Washington, P. Alex Dow, Heba Elfardy, Hanna Wallach, Sandeep Atluri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13840v1)