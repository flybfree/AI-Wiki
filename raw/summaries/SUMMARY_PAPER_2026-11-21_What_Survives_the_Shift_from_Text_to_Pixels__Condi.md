---
title: What Survives the Shift from Text to Pixels? Conditional Protection against Prompt Injection in Image-Rendered Documents
url: http://arxiv.org/abs/2611.24231v1
type: paper-summary
date: 2026-11-21
source_paper: 2026-11-18_11-08-07Z_WhatSurvivestheShiftfromTexttoPixels_ConditionalPr.md
generated_at: 2026-11-21 21:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether rendering untrusted text content as page images provides meaningful protection against indirect prompt injection attacks in multimodal language models. Through paired text and image experiments across 191 question-answering sources and six models, the authors find that image rendering reduces some injection operations but fails to eliminate them entirely, with protection being highly conditional on the specific model, attack type, and rendering configuration. The work further reveals that failed image-based attacks often stem not from illegibility but from models reading injected commands without executing them, and that visual encoding distributes command influence differently across attention layers compared to text-based commands.

## Key Takeaways
- Rendering text as images reduces marker-appending and answer-formatting injection attacks across all six tested models, but Qwen3-VL-8B still executes image-borne answer replacement at 77.96%, demonstrating that no single rendering strategy universally neutralizes all injection operations. A search over eight fixed attack candidates largely closes the image deficit for Qwen and Gemini in appending and formatting, but not for GPT-5-nano, highlighting model-specific vulnerability profiles.
- Utility preservation is uneven: clean question-answering accuracy on original questions ranges from 93.31% to 101.61% across models, but Qwen's utility drops sharply to 61.99% when answers require combining two evidence spans, indicating that rendering imposes hidden costs on complex reasoning tasks that simple accuracy metrics miss.
- Mechanistic analysis inside Qwen shows that patching early attack-region states induces all three injection operations, more weakly in images, and attention blocking reveals a structural difference: text commands act through their own token positions, while visual encoding spreads an image command and its target across the instruction page. Additionally, models frequently transcribe and identify image-borne commands they do not execute, and trusted user authorization raises execution rates on unchanged pages, proving that illegibility alone cannot explain failed attacks.

## Context
As multimodal language models increasingly serve as retrieval-augmented assistants that process external documents, indirect prompt injection—where adversarial commands are planted in untrusted content to hijack model outputs—has become a critical security concern. Prior work established that rendering text as images reduces average attack success, but left open which specific operations survive, at what utility cost, and whether apparent protection reflects genuine unreadability or a deeper failure to act on visible instructions. This paper fills that gap by systematically disentangling legibility from execution and by providing mechanistic explanations for why visual encoding alters injection dynamics.

## Implications
For practitioners deploying multimodal RAG systems, the findings argue against treating image rendering as a blanket security mitigation and instead motivate evaluations that report security outcomes disaggregated by model, injection operation, and attack budget alongside utility metrics. For the broader AI safety community, the mechanistic insight that visual encoding spreads command influence across attention layers suggests new defense strategies targeting attention routing rather than mere content obfuscation. Industry teams building document-processing pipelines should treat rendering settings, wording, and repetition as tunable security parameters rather than fixed preprocessing choices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.24231v1)
