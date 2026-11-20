---
title: "Summary: How OpenAI’s Performance Factory keeps ChatGPT fast"
date: "2026-11-19"
type: article-summary
source_url: "https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/"
tags: [agents, software-engineering, reliability, evaluation, orchestration]
---
# Summary: How OpenAI’s Performance Factory keeps ChatGPT fast

OpenAI describes an internal system that turns recurring ChatGPT performance regressions into durable tasks managed by Codex agents and engineers. A task moves from alert and investigation through root-cause review, a proposed code change, human pull-request review and deployment, and then agent verification that service performance returned to baseline.

The system combines a task service with configurable workflow states, a dispatch loop that starts agents when work is ready, cloud Codex execution with scoped service identity, and event subscriptions that resume work after a review or deployment. Findings persist outside any individual agent context, so another agent or engineer can continue the work. A separate adversarial agent challenges proposed diagnoses and fixes. Engineers retain the decision to merge and deploy changes.

OpenAI reports that in just over three months the workflow tracked more than 1,700 investigations and root-caused over 600 cases. In a manual sample of 100 root-cause suggestions, OpenAI rated 70% accurate; the remaining suggestions needed refinement or did not fully establish causality. The company says fixes can still be unnecessarily complex or introduce new problems, and it is developing additional evaluation and synthetic-performance tests. These are internal company-reported results, not independent evidence of general coding-agent reliability.

**Takeaway:** The important pattern is not unsupervised code repair. It is a stateful, observable workflow that narrows the agent’s job, challenges its causal claims, routes consequential changes through human review, and verifies the outcome after deployment. This is a useful production template for repeatable engineering work, provided teams independently measure failures, review burden, regressions, and recovery quality.

## Original source

- [OpenAI — How OpenAI’s Performance Factory keeps ChatGPT fast](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/)
