---
title: PainterBench: A Figural Divergent-Thinking Benchmark for Tool-Using Language Models
published: 2026-09-28T03:08:43Z
authors: Shane K. A. Dalumura Hettige, Jonas Oppenlaender
url: http://arxiv.org/abs/2609.34195v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PainterBench: A Figural Divergent-Thinking Benchmark for Tool-Using Language Models

## Abstract
Figural divergent thinking is the ability to develop a given shape fragment into an original drawing. In humans, this ability is assessed with incomplete-drawing tasks. We introduce PainterBench, a benchmark that ports the incomplete-drawing task to the agentic setting. The agent draws on a canvas through tool calls and observes the result after every turn. The canvas includes a starting shape which cannot be erased, and the agent's goal is to incorporate this shape into the most original drawing it can produce. The task is open-ended, and the agent itself decides when the drawing is finished. The benchmark tests incremental visual planning over a short horizon and the transfer of creative ability from pretraining to multi-turn tool use. We evaluate 14 multimodal language models from small to frontier scale. Across the primary study and six sensitivity analyses, we collect 2,700 drawings and crowdsource creativity and recognizability ratings for every drawing and for 300 human reference drawings. We also present ViDrA-adapted, an automated scorer that predicts human creativity ratings of agent drawings (r = 0.85 on random held-out test split). Figural divergent thinking varies widely across the 14 models, and GPT-6 Astra produces the most creative drawings. Relative to the human drawings, the agent drawings score higher in creativity but lower in recognizability. We release the final drawings, per-round canvas snapshots, tool call traces, stimulus bank, benchmark harness, crowdsourced ratings (N = 72,000), and ViDrA checkpoint.

## Metadata
- **Published**: 2026-09-28T03:08:43Z
- **Authors**: Shane K. A. Dalumura Hettige, Jonas Oppenlaender
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34195v1)