---
title: Authority Bias in Language Models: Source Deference and User Agreement Are Not Interchangeable
published: 2026-09-29T13:58:04Z
authors: Abhinav Rajeev Kumar, Paras Chopra
url: http://arxiv.org/abs/2609.37616v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Authority Bias in Language Models: Source Deference and User Agreement Are Not Interchangeable

## Abstract
Language models tend to agree with whatever a user asserts, and post-training increasingly targets this sycophancy so that models evaluate claims on their merits rather than deferring to the user. Yet the same models are far more compliant when a wrong answer is attributed to a verified source, which is how retrieval results, tool outputs, and grounded-search content often present information. We measure this gap across five open-weight families and three closed APIs. A single verified-source note endorsing a wrong answer flips 45-88% of baseline-correct responses in seven of eight models, and compliance rises with how authoritative the note sounds. Source deference and user agreement are not behaviorally interchangeable inside the model: on matched items with the same wrong answer, causal interventions can selectively suppress one without equally affecting the other. In three open-weight families, removing a fitted source direction lowers source compliance by 65-80 percentage points while removing a user or assistant direction has far smaller effects, and removing the user direction shows the reverse preference. A separately fitted intervention derived from source-versus-user cue activations moves compliance in both directions while leaving the prompt text unchanged. An authority direction fitted on trivia also transfers to PIQA and multi-turn SYCON dialogues without refitting, and removing it lowers wrong-source compliance by tens of percentage points in four of five families with no detected change in MMLU-Pro or GSM8K accuracy at our evaluation sizes. Source deference and user agreement therefore need separate evaluation.

## Metadata
- **Published**: 2026-09-29T13:58:04Z
- **Authors**: Abhinav Rajeev Kumar, Paras Chopra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37616v1)