---
title: RoguePrompt: Dual-Layer Encoding for Self-Reconstruction to Circumvent LLM Moderation
published: 2026-07-29T18:25:30Z
authors: Benyamin Tafreshian, Prathamesh Dhake
url: http://arxiv.org/abs/2607.27373v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RoguePrompt: Dual-Layer Encoding for Self-Reconstruction to Circumvent LLM Moderation

## Abstract
Large language models (LLMs) are becoming increasingly integrated into mainstream development platforms and daily technological workflows, typically behind moderation and safety controls. Despite these controls, preventing prompt-based policy evasion remains challenging, and adversaries continue to "jailbreak" LLMs by crafting prompts that circumvent implemented safety mechanisms. Prior work has established cipher-mediated interaction, code-embedded decryption, prompt decomposition and reconstruction, and layered custom encryption as viable attack primitives. However, reported evaluations generally collapse visible acceptance, successful recovery of the concealed request, and subsequent execution into an aggregate attack-success outcome. This leaves limited evidence about where multistage prompt-transformation attacks fail within an observable black-box interaction. This paper introduces RoguePrompt, a jailbreak pipeline that partitions a forbidden prompt and applies two nested encodings, Vigenere followed by ROT13, along with natural-language reconstruction instructions. RoguePrompt was developed and evaluated under a black-box threat model, with only API or user-interface access to the hosted models, and was tested on 313 real-world, hard-rejected prompts. Success was measured in terms of moderation bypass, instruction reconstruction, and execution when the relevant stage exceeded its automated criterion. RoguePrompt achieved average rates of 93.93% for filter bypass, 79.02% for reconstruction, and 70.18% for execution. These results demonstrate the effectiveness of layered prompt encoding while providing stage-level evidence of where multistage jailbreaks fail during moderation bypass, instruction reconstruction, and execution.

## Metadata
- **Published**: 2026-07-29T18:25:30Z
- **Authors**: Benyamin Tafreshian, Prathamesh Dhake
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27373v1)