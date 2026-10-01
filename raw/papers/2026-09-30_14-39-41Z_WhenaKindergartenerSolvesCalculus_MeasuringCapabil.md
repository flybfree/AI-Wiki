---
title: When a Kindergartener Solves Calculus: Measuring Capability Leakage in Role-Prompted Reasoning Models
published: 2026-09-30T14:39:41Z
authors: Pakhapoom Sarapat, Saksorn Ruangtanusak, Kunat Pipatanakul, Pittawat Taveekitworachai
url: http://arxiv.org/abs/2609.39846v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When a Kindergartener Solves Calculus: Measuring Capability Leakage in Role-Prompted Reasoning Models

## Abstract
We investigate the problem of role-capability leakage (RCL), in which a role-prompted reasoning model generates convincing in-role text while continuing to exhibit capabilities on benchmarks that exceed those implied by the assigned role. For example, when a model is prompted to assume the role of a kindergarten student, one might expect its performance on a mathematics benchmark to reflect kindergarten-level ability rather than expert-level proficiency in solving calculus problems. We introduce RoleCapBench, a curriculum-grounded benchmark for evaluating RCL across six educational roles and four assessment levels spanning elementary school through A-level, and use it to evaluate three open-weight reasoning models. We find that although the models can generate stylistically convincing in-role responses, they consistently fail to align their underlying capabilities with their assigned roles. Naive role prompting yields strong role-voice scores of 1.218--1.389 while retaining above-role accuracy of 0.811--0.898. RCL persists across a range of prompting conditions, including prompts that explicitly instruct the model to match the role's capability level. To mitigate this problem, we propose Injection, an inference-time intervention that combines explicit, role-specific capability guidelines with a guiding prefilled response prefix. Injection improves role-capability alignment across models, reducing above-role accuracy by up to 0.562 while preserving in-role accuracy with a marginal drop of less than 0.058 across most models. All artifacts, including scripts and evaluation data, will be released upon acceptance.

## Metadata
- **Published**: 2026-09-30T14:39:41Z
- **Authors**: Pakhapoom Sarapat, Saksorn Ruangtanusak, Kunat Pipatanakul, Pittawat Taveekitworachai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39846v1)