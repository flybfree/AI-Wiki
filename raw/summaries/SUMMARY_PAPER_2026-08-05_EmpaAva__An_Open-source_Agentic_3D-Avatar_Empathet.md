---
title: EmpaAva: An Open-source Agentic 3D-Avatar Empathetic Live Chatbot
url: http://arxiv.org/abs/2608.04709v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_11-23-40Z_EmpaAva_AnOpen_sourceAgentic3D_AvatarEmpatheticLiv.md
generated_at: 2026-08-05 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EmpaAva, an open-source agentic 3D avatar chatbot that translates text-only empathetic responses into live face-to-face interaction using video-call style interface. It uses a tri-agent architecture with perception, response planning, and embodied rendering to generate emotional speech, lip-sync facial motion, and photorealistic 3D Gaussian rendering. Human and automatic evaluations show it outperforms baselines in emotion understanding, response quality, and audio-visual consistency.

## Key Takeaways
- EmpaAva integrates perception from speech and optional vision into a unified multimodal plan that drives voice, expression, and rendering as a single empathetic intent.
- The tri-agent architecture separates perception, empathetic response planning, and embodied rendering while maintaining control and inspectability through open-source modules.
- Evaluations demonstrate superior performance across emotion understanding, response quality, and audio-visual consistency compared to text-only, 2D avatar, and multimodal baselines.

## Context
This work advances affective computing by bridging the gap between language models and embodied interaction, enabling real-time emotional expression in virtual humans. It highlights the need for closed-loop systems that coordinate perception, planning, and rendering to achieve naturalistic avatars.

## Implications
For developers, EmpaAva provides a modular framework that can be customized for research or commercial applications requiring empathetic 3D avatars. The open-source release fosters community contributions and rapid prototyping, accelerating the deployment of affective AI in customer service, therapy, and entertainment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04709v1)
