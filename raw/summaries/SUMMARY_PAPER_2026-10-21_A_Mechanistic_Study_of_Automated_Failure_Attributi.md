---
title: A Mechanistic Study of Automated Failure Attribution in LLM-based Agentic Systems
url: http://arxiv.org/abs/2610.28811v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-20_18-33-19Z_AMechanisticStudyofAutomatedFailureAttributioninLL.md
generated_at: 2026-10-21 20:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether the poor performance of LLMs in automated failure attribution (AFA) for multi-agent systems stems from a genuine capability limitation or a behavioral gap. Through linear probes applied to internal model activations, the authors discover a "knows-but-won't-say gap," where models internally encode sufficient information to correctly identify the failing agent step but fail to surface it in their output. They propose "grafting," a lightweight intervention that extracts this latent knowledge to improve attribution accuracy without requiring ground-truth labels at inference time, demonstrating consistent improvements over direct-prompting baselines across multiple LLMs and benchmarks.

## Key Takeaways
- The paper identifies a fundamental disconnect between what LLMs internally represent and what they explicitly output when tasked with failure attribution. Linear probes on internal activations reveal that models encode correct attribution information in their hidden states, yet direct prompting strategies fail to elicit this knowledge, suggesting the bottleneck is not a lack of understanding but a failure of expression or retrieval.
- The proposed "grafting" technique is a manual intervention that leverages knowledge already encoded within the model's internal representations to improve AFA performance. Critically, it does not require ground-truth labels at inference time, making it practical for real-world deployment where labeled failure data is scarce or expensive to obtain.
- Extensive evaluations across multiple LLM architectures and benchmark settings show that grafting consistently outperforms direct-prompting approaches and alternative prompting strategies, establishing that latent model knowledge is a viable and underexploited resource for reliable failure diagnosis in agentic systems.

## Context
As LLM-based agentic systems grow in complexity, with multiple agents collaborating on subtasks in parallel, diagnosing which specific agent step caused a final incorrect outcome becomes a critical but labor-intensive challenge. Prior work has attempted to automate this process through various prompting strategies and inference-time interventions, but these approaches have plateaued in performance. This paper shifts the research question from "how do we prompt better?" to "do models already know the answer internally?" — a mechanistic inquiry that reframes the problem from a prompting engineering challenge into an interpretability and representation-level investigation.

## Implications
For practitioners building and debugging multi-agent LLM pipelines, grafting offers a practical path to more reliable failure attribution without the overhead of collecting labeled failure data or redesigning complex prompting pipelines. For the broader AI research community, the "knows-but-won't-say gap" finding suggests that many apparent capability limitations in LLMs may actually be retrieval or expression failures, opening new directions in interpretability research and model steering techniques that could benefit tasks beyond failure attribution, including reasoning, planning, and tool use in agentic workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28811v1)
