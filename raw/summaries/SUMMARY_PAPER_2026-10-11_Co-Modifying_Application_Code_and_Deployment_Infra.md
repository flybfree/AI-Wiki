---
title: Co-Modifying Application Code and Deployment Infrastructure: A Causal Study of AI Agent Pull Requests
url: http://arxiv.org/abs/2610.12849v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_01-16-04Z_Co_ModifyingApplicationCodeandDeploymentInfrastruc.md
generated_at: 2026-10-11 21:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the causal integration overhead introduced when AI software engineering agents submit pull requests that modify both application code and deployment infrastructure (CI/CD pipelines, containers, provisioning manifests) simultaneously. By analyzing 26,999 PRs across two large datasets spanning six agent architectures and a human baseline, the authors find that dual-scope modifications are rare yet produce a bimodal outcome: either severe review delays or silent, uninspected merges that compromise build verification.

## Key Takeaways
- Dual-scope pull requests constitute only 4.48% to 4.55% of all agentic contributions, yet they trigger a bimodal integration pattern. When these PRs are explicitly reviewed, they incur a median penalty of +13.13 hours and multiply time-to-merge by 3.24x, driven mechanically by the complexity of CI/CD and provisioning manifest changes that agents do not fully understand.
- A structural bypass exists in maintainer gatekeeping: agent identity reduces the odds of human review by 63.7% compared to human peers, even for external contributors lacking repository write access. As a result, 43.1% to 56.2% of dual-scope PRs bypass inspection entirely and merge silently in a median of under 31 minutes, introducing unverified dependencies into asynchronous integration pipelines.
- Agents operate predominantly as application coders or chore workers, with maintenance tasks capturing 17.70% to 25.41% of agent PRs. The study employs a deterministic four-tier file taxonomy and an exact 4D strata-matching framework to isolate integration metrics under conditional exchangeability while controlling for application volume, ensuring the causal findings are not confounded by task composition.

## Context
Current benchmarks for software engineering agents evaluate performance inside isolated sandboxes against synchronous local tests, which fails to capture the collaborative, asynchronous reality of deploying features in production repositories. This gap between evaluation methodology and real-world deployment workflows means that agents are optimized for narrow code generation tasks while remaining blind to the infrastructure dependencies that govern whether their contributions actually integrate safely into a shared codebase.

## Implications
For practitioners and platform teams, these findings argue for deployment-aware benchmarks that evaluate agents not just on code correctness but on their ability to reason about CI/CD pipelines, container configurations, and provisioning manifests as part of a unified change. Industry adoption of agentic coding tools should incorporate strict path-based access controls to prevent agents from silently modifying infrastructure files without human inspection, thereby preserving build verification integrity and preventing the accumulation of unverified dependencies in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.12849v1)
