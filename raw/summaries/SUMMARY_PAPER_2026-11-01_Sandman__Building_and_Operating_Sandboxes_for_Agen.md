---
title: Sandman: Building and Operating Sandboxes for Agentic Reinforcement Learning on Shared Kubernetes
url: http://arxiv.org/abs/2610.39711v1
type: paper-summary
date: 2026-11-01
source_paper: 2026-10-29_09-45-57Z_Sandman_BuildingandOperatingSandboxesforAgenticRei.md
generated_at: 2026-11-01 21:23
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Sandman is a sandbox service developed and operated at Amazon to support agentic reinforcement learning workloads that require thousands of isolated, task-specific execution environments running concurrently on shared Kubernetes clusters. The system manages the full lifecycle of sandbox creation, readiness verification, and cleanup, enabling training frameworks to interact with persistent file systems and processes within each sandbox until the environment is explicitly released. In production, Sandman handled 11,858 concurrent sandboxes in a scale test and supported four SWE-bench Verified training campaigns that collectively created 3.1 million sandboxes in a single month.

## Key Takeaways
- Sandman implements each sandbox as a standard Kubernetes pod containing a small daemon mounted into an unmodified task image, allowing training frameworks to issue commands and file operations against a persistent environment. This design avoids modifying task images while still providing stateful interactions across multiple tool calls within a single RL episode, which is critical for agentic tasks that require multi-step reasoning and code execution.
- The system addresses the operational challenge of creation bursts inherent to agentic RL training, where a single training job may spawn thousands of sandboxes simultaneously while sharing cluster resources with other production workloads. Sandman's architecture handles these bursts through careful management of creation, readiness checks, and cleanup, including mechanisms for reclaiming abandoned sandboxes that training frameworks fail to release explicitly.
- The paper reports concrete production metrics from four SWE-bench Verified training campaigns in October 2026 that generated 3.1 million sandboxes, demonstrating that the approach scales to real-world software engineering evaluation workloads. The authors plan to open-source the daemon, provider, and pool components, making the infrastructure available for broader adoption beyond Amazon's internal use.

## Context
Agentic reinforcement learning has emerged as a dominant paradigm for training language models to perform multi-step tasks involving tool use, code execution, and environment interaction. Unlike traditional RL training that operates on static datasets, agentic RL requires dynamic, isolated execution environments that can be created and destroyed at massive scale during training rollouts. Existing infrastructure solutions struggle with the bursty, stateful, and resource-contended nature of these workloads on shared Kubernetes clusters, making purpose-built sandbox management a critical gap in the training pipeline.

## Implications
For practitioners building agentic RL training pipelines, Sandman provides a battle-tested reference architecture for managing thousands of concurrent, stateful execution environments without modifying task images or dedicating exclusive cluster capacity. The planned open-sourcing of the daemon, provider, and pool components could lower the barrier for research labs and smaller organizations to adopt production-grade sandboxing for their own agentic RL experiments. For the broader industry, the paper's operational lessons around creation bursts, abandoned sandbox reclamation, and controlled evaluation conditions offer practical guidance for any team scaling RL training on shared Kubernetes infrastructure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.39711v1)
