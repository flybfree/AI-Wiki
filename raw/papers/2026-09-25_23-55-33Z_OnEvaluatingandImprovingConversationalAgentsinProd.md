---
title: On Evaluating and Improving Conversational Agents in Production
published: 2026-09-25T23:55:33Z
authors: Kasra Hosseini, Wen-Sen Cheng, Marco-Andrea Buchmann, Emir Mulabegovic, Weiwei Cheng
url: http://arxiv.org/abs/2609.32092v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On Evaluating and Improving Conversational Agents in Production

## Abstract
We present a framework for evaluating and improving a large-scale, multi-agent shopping assistant in production, and report lessons from its use. Offline evaluation of such a system faces three obstacles. (i) A logged conversation cannot be replayed against a modified system, because a different response changes every turn that follows. (ii) The unchanged system itself varies from run to run. Its LLM components are stochastic, and in product search the available products, their prices, and the customer's personalization signals change. (iii) Aggregate quality scores combine distinct behaviors, so they show that quality has changed but not which behavior caused the change. Our framework addresses each obstacle in turn. For a reported behavior, an Evaluation Harness generates targeted assertions and a fixed cohort of customer scenarios. It then reproduces the behavior in a local instance of the assistant through grounded user simulation. Instead of replaying the log, the simulator writes new customer turns conditioned on the recorded messages and context. Repeated runs of the unchanged system form a stored baseline. An Improvement Orchestrator turns the assertion results into hypotheses, implements each as an isolated modification, and compares it with the baseline using paired percentile bootstrap intervals over scenario-level differences. When an investigation ends, the harness may propose revisions to future evaluations, subject to human approval and without altering past decisions. We report production investigations with this framework. Assertion profiles showed which positions of a product carousel a failure affected, and repeated runs distinguished a real improvement from run-to-run fluctuation. Audits of the evaluation itself found a judge that lacked the evidence it needed and a model setting that was configured but not applied.

## Metadata
- **Published**: 2026-09-25T23:55:33Z
- **Authors**: Kasra Hosseini, Wen-Sen Cheng, Marco-Andrea Buchmann, Emir Mulabegovic, Weiwei Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32092v1)