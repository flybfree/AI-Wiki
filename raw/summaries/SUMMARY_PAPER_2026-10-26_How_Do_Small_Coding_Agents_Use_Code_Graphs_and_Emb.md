---
title: How Do Small Coding Agents Use Code Graphs and Embeddings?
url: http://arxiv.org/abs/2610.33958v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-25_00-16-32Z_HowDoSmallCodingAgentsUseCodeGraphsandEmbeddings.md
generated_at: 2026-10-26 20:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether structured code-navigation tools—embedding search and code-graph traversal—genuinely help small open-weight coding agents localize and fix bugs in SWE-bench Verified tasks, or whether the assumed benefit is overstated. Through large-scale ablation experiments across ten models ranging from 0.6B to 32B parameters (79,000 episodes), the authors find that structured tools provide substantial gains for models in the 1.7–4B range but the advantage shrinks sharply at larger sizes, and that small agents fundamentally rely on a one-hop, largely lexical understanding of their repository rather than multi-hop graph reasoning.

## Key Takeaways
- Structured tools (embedding search plus code-graph navigation) roughly double grep-only accuracy for Qwen3-8B and Gemma 4 E4B, with peak gains of 17–21 percentage points at 1.7–4B parameters. However, the benefit decays to only 4–5 points at 32B, with an odds ratio of 0.77–0.82 per doubling of parameters, indicating that larger models internalize repository structure in their weights and extract diminishing returns from external tools.
- A deterministic hop-depth metric (shortest code-graph path from issue-mentioned code to gold-patch code) reveals that each additional hop multiplies the odds of correct localization by 0.50–0.67 regardless of model size or tool configuration. Traces show graph tools primarily assist with name lookup at hop 0 and a single expansion at hop 1, while agents chain multiple expansions in only 12–14% of episodes, meaning multi-hop reasoning is rarely exercised in practice.
- Linear probes on model representations confirm that small agents encode a one-hop, largely lexical picture of their repository: direct call edges are decodable at AUC 0.74 but fall below a lexical baseline of 0.99, and two-hop edges drop to 0.57. From 8B upward, roughly half of the apparent tool gain is attributable to the format of the agent's submission rather than to actually locating the correct target code.

## Context
This work sits at the intersection of agentic software engineering and model-capability scaling, directly challenging a widely adopted design assumption in coding-agent frameworks: that external code-graph and embedding tools compensate for a model's supposed inability to reason about repository structure. By stratifying SWE-bench tasks with a validated hop-depth metric and running ablations across seven model families and dozens of decoding configurations, the paper provides the first systematic evidence that the utility of structured retrieval tools is strongly model-size-dependent and that small agents' internal representations already encode a shallow, lexical view of code relationships.

## Implications
For practitioners building coding-agent pipelines, the findings suggest that tool augmentation should be calibrated to model size: small models (under ~4B) benefit enormously from graph and embedding tools, while models at 14B and above gain little and may even misattribute formatting artifacts to genuine localization improvements. For the research community, the hop-depth gradient and the lexical-baseline probe results imply that improving multi-hop code reasoning in small agents requires architectural or training interventions rather than simply adding more retrieval tools, and that benchmark evaluation should separate localization success from submission-format effects to avoid overstating tool efficacy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33958v1)
