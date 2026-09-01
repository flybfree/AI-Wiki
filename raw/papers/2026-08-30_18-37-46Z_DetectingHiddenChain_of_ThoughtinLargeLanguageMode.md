---
title: Detecting Hidden Chain-of-Thought in Large Language Models with Linguistic, Behavioral, and Mechanistic Indicators
published: 2026-08-30T18:37:46Z
authors: Armaan Singh, Ryan Trinh Le, Jasmine Kaur, Abdullah Sultan, Edward Lue Chee Lip, Kiran Nijjer, Adnan Ahmed, Vasu Sharma
url: http://arxiv.org/abs/2608.29956v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Detecting Hidden Chain-of-Thought in Large Language Models with Linguistic, Behavioral, and Mechanistic Indicators

## Abstract
Large language models often answer complex reasoning questions without revealing intermediate steps, raising whether they reason latently or complete patterns. We propose the Hidden CoT Detection Score (HCDS), a comparative behavioral and mechanistic signal measuring whether neutral-prompt behavior aligns more closely with explicit CoT or explicit no- CoT. Here, hidden CoT operationally denotes this neutral-prompt CoT-like alignment; HCDS does not directly observe or prove an unexposed reasoning trace. On GSM8K, HCDS is significantly positive for both Qwen3-4B variants (Thinking $+1.87$, $p = 1.2 \times 10^{-7}$; Instruct $+1.41$, $p = 1.9 \times 10^{-4}$), replicates across a different inference stack and quantization within $0.08$ ($+1.80$ and $+1.45$), and is not significantly positive in seven of eight length-adjusted calibration-control cells. The unadjusted score produces large positive scores on single-step arithmetic and numeric factual lookup. The variants also respond differently to no-CoT instructions: Instruct complies from the prompt alone, whereas Thinking continues reasoning and requires intervention. These findings show stronger, less prompt-conditional CoT-like behavior in the reasoning-tuned model, consistent with but not proof of latent reasoning. HCDS thus investigates latent reasoning without relying on models' self-reported traces.

## Metadata
- **Published**: 2026-08-30T18:37:46Z
- **Authors**: Armaan Singh, Ryan Trinh Le, Jasmine Kaur, Abdullah Sultan, Edward Lue Chee Lip, Kiran Nijjer, Adnan Ahmed, Vasu Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29956v1)