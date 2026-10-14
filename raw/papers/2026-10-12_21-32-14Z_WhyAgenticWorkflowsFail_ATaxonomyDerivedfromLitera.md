---
title: Why Agentic Workflows Fail: A Taxonomy Derived from Literature and Empirical Data
published: 2026-10-12T21:32:14Z
authors: Xin Li, Rami Bahsoon, Tao Chen
url: http://arxiv.org/abs/2610.17418v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why Agentic Workflows Fail: A Taxonomy Derived from Literature and Empirical Data

## Abstract
Agentic workflows combine large language models with planning, memory, tools, execution environments, and iterative feedback. Their failures are difficult to diagnose because the same user-visible symptom may originate from model behavior, workflow orchestration, external tools, infrastructure, or their interaction. This paper presents a source-aware taxonomy of agentic workflow failures and applies it to evidence from academic literature and GitHub. The taxonomy combines source attribution with three empirical dimensions: a concrete failure-type dictionary, workflow-stage localization, and agent-capability localization. Its central structure is a two-axis localization matrix: workflow stages form the horizontal process axis and agent capabilities form the vertical functional axis. This design moves beyond taxonomies that mainly classify final failure manifestations by localizing intermediate process states inside agent operation. Our empirical comparison shows that literature-derived failures emphasize planning, reasoning, learning, perception, and knowledge-related mechanisms, whereas GitHub-derived failures concentrate on execution-stage, actuation-related, tool, API, and infrastructure failures. The dominant hotspot is iterative execution and actuation. These findings indicate that agentic workflow reliability should be treated as a systems problem rather than only a model-output problem. The taxonomy provides a basis for structured evaluation, root cause analysis, failure injection, and engineering triage.

## Metadata
- **Published**: 2026-10-12T21:32:14Z
- **Authors**: Xin Li, Rami Bahsoon, Tao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17418v1)