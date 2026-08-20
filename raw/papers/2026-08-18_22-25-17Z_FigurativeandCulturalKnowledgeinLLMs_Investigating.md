---
title: Figurative and Cultural Knowledge in LLMs: Investigating Cross-Domain Transfer through Fine-Tuning
published: 2026-08-18T22:25:17Z
authors: Mena Attia, Mona Diab, Thamar Solorio
url: http://arxiv.org/abs/2608.18361v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Figurative and Cultural Knowledge in LLMs: Investigating Cross-Domain Transfer through Fine-Tuning

## Abstract
Figurative language is deeply culturally embedded; fluent use requires not just linguistic competence but cultural immersion. We ask whether LLMs can learn this link: does fine-tuning on cultural data improve figurative language understanding, and vice versa? We conduct a systematic study across four models (ALLaM-7B, Fanar-1-9B, Qwen3-8B, Llama-3.1-8B) and six Arabic datasets spanning cultural commonsense, proverbs, and poetry across diverse dialects and regions. Fine-tuning on poetry improves idiom comprehension (+2.33%, p<0.05), a gain our ArabicMMLU control does not reproduce, indicating that it stems from figurative content rather than Arabic language adaptation and pointing to a sensitivity to non-literal meaning that transfers across figurative types. Cultural fine-tuning, by contrast, lowers proverb-interpretation accuracy in both Arabic-centric models. Transfer between the two domains is otherwise indistinguishable from noise, with Arabic models frequently regressing after fine-tuning, suggesting prior saturation of relevant knowledge, while multilingual models show greater adaptation headroom. Error analysis further reveals that fine-tuning reinforces experiential cultural knowledge while destabilizing historically grounded factual knowledge. Our findings suggest that the relationship between culture and figurative language, though conceptually natural, is not straightforwardly captured through fine-tuning alone.

## Metadata
- **Published**: 2026-08-18T22:25:17Z
- **Authors**: Mena Attia, Mona Diab, Thamar Solorio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18361v1)