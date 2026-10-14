---
title: Why Agentic Workflows Fail: A Taxonomy Derived from Literature and Empirical Data
url: http://arxiv.org/abs/2610.17418v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_21-32-14Z_WhyAgenticWorkflowsFail_ATaxonomyDerivedfromLitera.md
generated_at: 2026-10-14 00:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a source-aware taxonomy for diagnosing failures in agentic workflows—systems that combine large language models with planning, memory, tool use, execution environments, and iterative feedback loops. The authors construct a two-axis localization matrix that maps failures across workflow stages (horizontal axis) and agent capabilities (vertical axis), enabling precise identification of where and why failures occur. Applying this taxonomy to both academic literature and GitHub issue data reveals a critical divergence: research-focused failures concentrate on cognitive mechanisms like planning and reasoning, while real-world failures overwhelmingly stem from execution-stage, tool, API, and infrastructure breakdowns.

## Key Takeaways
- The taxonomy's central innovation is a two-axis localization matrix that moves beyond classifying only final failure manifestations. By localizing intermediate process states within agent operation, it distinguishes whether a user-visible symptom originates from model behavior, workflow orchestration, external tools, infrastructure, or their interaction—addressing the core diagnostic difficulty in agentic systems.
- Empirical comparison between literature-derived and GitHub-derived failure data reveals a stark split: academic literature emphasizes failures in planning, reasoning, learning, perception, and knowledge-related mechanisms, whereas GitHub-derived failures concentrate heavily on execution-stage, actuation-related, tool, API, and infrastructure failures. The dominant hotspot across both sources is iterative execution and actuation, suggesting a gap between research focus and practical failure modes.
- The authors argue that agentic workflow reliability must be treated as a systems problem rather than solely a model-output problem. The taxonomy provides a structured foundation for evaluation, root cause analysis, failure injection testing, and engineering triage, offering practitioners a concrete failure-type dictionary and workflow-stage localization framework for systematic debugging.

## Context
As agentic systems proliferate across software engineering, autonomous research, and enterprise automation, their failure modes have become increasingly opaque and multi-causal. Existing taxonomies in AI safety and model evaluation tend to classify only terminal failure outputs, leaving practitioners unable to trace failures back through the orchestration pipeline. This paper fills that gap by bridging academic failure analysis with empirical developer-reported issues, reflecting a growing recognition in the AI engineering community that agent reliability is fundamentally a distributed systems challenge involving heterogeneous components rather than a single-model accuracy problem.

## Implications
For practitioners building and deploying agentic workflows, this taxonomy provides an actionable framework for structured failure triage, targeted failure injection in testing pipelines, and root cause analysis that avoids misattributing infrastructure or tool failures to model deficiencies. For the broader field, the finding that real-world failures cluster around execution and actuation rather than reasoning suggests that research investment and safety evaluation should rebalance toward orchestration robustness, tool integration reliability, and infrastructure resilience. Engineering teams can use the failure-type dictionary and localization matrix to build more targeted monitoring, debugging, and remediation strategies for production agentic systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17418v1)
