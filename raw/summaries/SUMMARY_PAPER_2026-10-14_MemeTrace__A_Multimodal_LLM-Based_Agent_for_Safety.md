---
title: MemeTrace: A Multimodal LLM-Based Agent for Safety-Aware Meme Provenance Analysis
url: http://arxiv.org/abs/2610.19267v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_22-38-06Z_MemeTrace_AMultimodalLLM_BasedAgentforSafety_Aware.md
generated_at: 2026-10-14 21:02
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MemeTrace is a multimodal LLM-based agent designed to automatically trace the provenance and potential safety risks of emerging online memes, addressing the gap left by existing moderation systems that classify memes only as safe or unsafe based on individual images. Evaluated on a dataset of 100 real-world memes (Meme100), MemeTrace substantially outperforms vision-language model baselines in detecting unsafe memes involving disinformation and sensitive content, while maintaining robustness under visual perturbations.

## Key Takeaways
- MemeTrace moves beyond binary safe/unsafe classification by performing broader provenance analysis, including tracing where a meme originates, how it spreads across platforms, what cultural symbolism it encodes, and whether it poses potential societal risks. This represents a significant expansion over prior moderation approaches that treat each meme image in isolation without considering its evolutionary context or propagation history.
- The system is evaluated on Meme100, a curated dataset of 100 real-world memes, using both human annotation and automatic metrics. Results show MemeTrace substantially outperforms a VLM baseline, particularly in detecting unsafe memes involving disinformation and sensitive content, demonstrating that multimodal LLM agents can capture nuanced contextual and cultural signals that simpler vision models miss.
- MemeTrace remains robust under visual perturbations, meaning it can still correctly identify unsafe content even when memes undergo visual modifications such as cropping, resizing, or minor alterations. This robustness is critical for real-world deployment where memes are frequently edited, remixed, and recontextualized across social media platforms.

## Context
Online memes evolve rapidly in response to breaking news events and carry strong dependence on contextual and cultural information, making them difficult for platforms and human moderators to track and moderate at scale. Existing AI moderation research has largely focused on single-image classification, leaving a critical gap in understanding meme provenance, propagation dynamics, and embedded cultural symbolism. MemeTrace addresses this gap by leveraging multimodal LLM agents to perform holistic, multi-step provenance analysis, representing a shift from reactive content filtering toward proactive, understanding-driven safety assessment in the broader landscape of AI-powered content moderation and misinformation detection.

## Implications
For social media platforms and content moderation teams, MemeTrace offers a scalable tool that can automatically trace meme origins, propagation paths, and embedded risks, reducing the burden on human moderators who currently struggle to keep pace with the rapid evolution of meme-based disinformation and propaganda. For the AI research community, the work demonstrates that multimodal LLM agents can outperform traditional vision-language baselines in safety-critical tasks involving cultural context and provenance reasoning, suggesting a promising direction for building more contextually aware and robust content safety systems that practitioners can deploy in production moderation pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19267v1)
