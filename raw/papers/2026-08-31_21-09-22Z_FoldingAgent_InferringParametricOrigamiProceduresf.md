---
title: FoldingAgent: Inferring Parametric Origami Procedures from Demonstration Videos
published: 2026-08-31T21:09:22Z
authors: Maya Moriya, Sigal Raab, Yael Vinker, Tali Dekel
url: http://arxiv.org/abs/2609.00377v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FoldingAgent: Inferring Parametric Origami Procedures from Demonstration Videos

## Abstract
We present FoldingAgent, an agentic framework for inferring explicit parametric folding programs directly from origami demonstration videos. Our framework leverages the reasoning power of a pre-trained Vision-Language Model (VLM) equipped with a suite of specialized tools that enable the agent to simulate geometric transitions, verify physical plausibility, retrieve and compare visual content, and evaluate its own predictions. To translate visual content into folding programs, we define a parametric space that consists of the paper's geometry and a set of parametric folding actions. Unlike models that predict static crease patterns, our agent operates sequentially and possesses the ability to re-plan its actions, effectively mitigating the compounding errors inherent in multi-step folding. Our approach takes a step toward closing the gap between human origami knowledge, which is primarily shared through unstructured visual demonstrations, and computational methods, which typically rely on structured, parametric representations such as a crease pattern or an executable parametric plan. We evaluate our approach on PurelandFold, a newly curated benchmark of diverse Pureland origami videos with ground-truth geometry and action labels. Our results demonstrate that by combining VLM reasoning with a set of specialized tools and physical simulation, we can successfully transform unstructured visual demonstrations into executable, physically plausible folding procedures.

## Metadata
- **Published**: 2026-08-31T21:09:22Z
- **Authors**: Maya Moriya, Sigal Raab, Yael Vinker, Tali Dekel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00377v1)