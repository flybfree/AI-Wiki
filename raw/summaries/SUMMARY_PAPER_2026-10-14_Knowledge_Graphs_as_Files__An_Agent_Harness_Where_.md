---
title: Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve
url: http://arxiv.org/abs/2610.18616v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_16-00-50Z_KnowledgeGraphsasFiles_AnAgentHarnessWhereToolCrea.md
generated_at: 2026-10-14 02:02
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Direct Knowledge Graph Interaction (DKGI), a novel agent harness in which language model agents dynamically create their own graph access tools by writing Python code directly over complete node and edge files, rather than relying on predefined graph interfaces. The core finding is that training-free DKGI outperforms the strongest published baselines by at least 6.7 Hit@1 points across three benchmark domains, demonstrating that letting tool creation and tool use co-evolve during graph search yields substantial performance gains without any model fine-tuning.

## Key Takeaways
- DKGI replaces fixed graph query interfaces with an open-ended programming environment where agents write Python code to follow relations, combine node sets, and select textual evidence from knowledge graphs. This interleaving of code execution with shell search and file inspection allows agents to process large node sets in bulk while selectively returning text for the model to assess, overcoming the evidence-access constraints imposed by predefined graph tools.
- The co-evolutionary loop between tool creation and tool use is central to the method's success: execution feedback guides agents to revise and extend their code, while the evolving tools determine what evidence the agent gathers in subsequent turns. Trajectory analysis confirms agents actively revise code to extend searches or correct errors, showing genuine adaptive behavior rather than static tool invocation.
- Controlled ablations isolate the contributions of multi-turn programming versus shell-only access versus predefined graph tools, confirming that the combination of iterative code writing and direct file-level access is what produces the performance gains. Notably, these improvements hold even with a minimal harness and no training, making the approach broadly accessible.

## Context
This work sits at the intersection of agentic AI, knowledge graph reasoning, and tool-augmented language models. As LLM agents increasingly tackle complex retrieval and reasoning tasks over structured data, the design of the tool interface has become a critical bottleneck. Prior approaches constrain agents to fixed query APIs or predefined graph traversal primitives, limiting the kinds of evidence an agent can access. DKGI challenges this paradigm by treating the entire knowledge graph as a filesystem that the agent can programmatically interrogate, aligning with the broader trend toward code-generating agents and open-ended tool creation in agentic systems.

## Implications
For practitioners building graph-based retrieval systems, DKGI suggests that investing in flexible, file-level access and iterative code-generation loops may yield larger performance gains than engineering increasingly sophisticated predefined query APIs. The training-free nature of the approach lowers barriers to adoption, as no fine-tuning or specialized infrastructure is required. More broadly, the co-evolution principle—where tools are created and refined in response to task demands—points toward a future where agent harnesses are not static scaffolds but adaptive environments that grow alongside the agent's reasoning capabilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18616v1)
