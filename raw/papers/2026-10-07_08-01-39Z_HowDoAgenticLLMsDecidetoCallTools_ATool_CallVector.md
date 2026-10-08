---
title: How Do Agentic LLMs Decide to Call Tools? A Tool-Call Vector Shaped by Suppression
published: 2026-10-07T08:01:39Z
authors: Xijie Gong, Tingxu Han, Jiahao Zhang, Wei Song, Ziqi Ding, Hanqi Yan, Youcheng Sun, Lijie Hu
url: http://arxiv.org/abs/2610.09624v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Do Agentic LLMs Decide to Call Tools? A Tool-Call Vector Shaped by Suppression

## Abstract
Tool calling, invoking external tools on demand, is central to agentic LLMs, yet the mechanism that decides whether a model calls a tool or responds directly remains poorly understood. Agentic prompts are long and heavily scaffolded, combining role instructions, tool schemas, format templates, and the user's request across hundreds of tokens, creating a noisy, highly entangled context in which no single controllable variable for mechanistic analysis is obvious. To obtain such a variable, we propose a method that converts complex agentic prompts into minimal contrastive pairs in which a single request verb determines the tool-call decision: replacing an execution-verb (e.g., \textit{write}) with an analysis-verb (e.g., \textit{discuss}) reliably flips the decision, suggesting it is mediated by a compact internal state. We construct 500 such paired prompts across Python, Java, and C++ (300 for mechanistic analysis, 200 held out for evaluation). We trace the decision to a vector, $μ_Δ$, that is both causally necessary and sufficient and generalizes beyond the discovery prompts to native multi-turn $τ^2$-Bench trajectories and verb-free requests. Behavioral ablations show that the scaffold establishes a tool-call prior; Transcoder decomposition then reveals that analysis verbs suppress this prior through features signaling that tool use is unnecessary, whereas execution verbs largely leave it intact. Downstream scaffold-reading attention heads and MLP features read out the resulting state, and the same mechanism recurs across seven models from the Qwen, Mistral, and Granite families. Our code is available at https://github.com/XijieGo/MI4ToolCalling.

## Metadata
- **Published**: 2026-10-07T08:01:39Z
- **Authors**: Xijie Gong, Tingxu Han, Jiahao Zhang, Wei Song, Ziqi Ding, Hanqi Yan, Youcheng Sun, Lijie Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09624v1)