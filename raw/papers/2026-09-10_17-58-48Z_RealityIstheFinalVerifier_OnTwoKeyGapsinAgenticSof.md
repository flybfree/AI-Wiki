---
title: Reality Is the Final Verifier: On Two Key Gaps in Agentic Software Engineering
published: 2026-09-10T17:58:48Z
authors: Alexander Krentsel, Shubham Agarwal, Mert Cemri, Shu Liu, Sidharth Sankhe, Ziming Mao, Matei Zaharia, Ion Stoica
url: http://arxiv.org/abs/2609.12039v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reality Is the Final Verifier: On Two Key Gaps in Agentic Software Engineering

## Abstract
Software development follows an implementation-verification loop in which developers or agents iteratively revise an implementation until an evaluator, such as a test suite, accepts it. The evaluator checks the implementation against a set of requirements under a model of the deployment environment. Yet even a formal proof that the implementation satisfies the requirements under the model cannot guarantee acceptable behavior after deployment. Requirements only approximate stakeholder intent, and the model only approximates the real deployment environment. We call these together - requirement gap and model gap - the two-gap framework, which unifies the main failure modes of agentic software engineer-ing: reward hacking exploits omissions in the requirements or model, while hallucination widens the gaps by fabricating requirements or environment assumptions.   Because neither gap can generally be certified closed in an open, changing world, the goal shifts from closing them to continuously narrowing them. We therefore propose an assurance-revision loop that uses deployment evidence to revise the requirements, model, or evaluator when stakeholders reject the resulting behavior. We then cast assured agentic development as a resource-allocation problem over human judgment, agent capability, and compute. The two principal bottlenecks mirror the two gaps: human judgment for the requirement gap and faithful, costly evaluation for the model gap. Reality remains the final verifier: acceptable behavior under actual deployment conditions is the ultimate test, while predeployment evaluations remain proxies for it.

## Metadata
- **Published**: 2026-09-10T17:58:48Z
- **Authors**: Alexander Krentsel, Shubham Agarwal, Mert Cemri, Shu Liu, Sidharth Sankhe, Ziming Mao, Matei Zaharia, Ion Stoica
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12039v1)