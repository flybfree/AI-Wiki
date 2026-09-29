---
title: Agents Can Use Base Models to Evade AI Detection
published: 2026-09-25T18:13:40Z
authors: Bhuwan Dhingra, Danish Pruthi
url: http://arxiv.org/abs/2609.31876v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agents Can Use Base Models to Evade AI Detection

## Abstract
We show that coding agents equipped with a base language model can successfully assemble responses from its samples to evade detection. Base models have been shown to evade commercial detectors, however, prior "humanization" techniques rely on using these models to paraphrase AI outputs over several iterations, which invariably results in semantic drift. In contrast, equipping coding agents to directly orchestrate the writing process by stitching text samples from a base model allows it to produce outputs that are coherent, task-specific and generally high quality. We find that Claude Opus 5 operating in a Claude Code harness effectively orchestrates a local 32B parameter OLMo-2 base LM and sacrifices little task accuracy across benchmarks spanning creative writing, factual grounding, health QA and instruction following, while using up to 90% base LM tokens. Responses constructed in this manner reduce the effectiveness of both post-hoc detectors (Pangram v4 detection rate drops from 77% to 24%) and soft watermarking applied a priori to the agent's generations (down to a simulated 10% detection at low FPR). While effective, this evasion requires a significantly larger number of input and output tokens from the agent, increasing the dollar cost per query up to 30x at API-pricing. Overall, this work demonstrates the effectiveness of a new class of adversarial attacks against AI text detection, and urges post-hoc detection providers to include outputs of base models in their training.

## Metadata
- **Published**: 2026-09-25T18:13:40Z
- **Authors**: Bhuwan Dhingra, Danish Pruthi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31876v1)