---
title: Living off the Local Model: Abusing Browser-Embedded Language Models for Post-Exploitation
published: 2026-11-18T19:23:44Z
authors: William Fleshman, Joseph Lucas
url: http://arxiv.org/abs/2611.25086v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Living off the Local Model: Abusing Browser-Embedded Language Models for Post-Exploitation

## Abstract
Browsers now ship local language models to ordinary endpoints. Google includes Gemini Nano in Chrome to enable productivity features such as summarization, with inference running entirely on the device. These browser-embedded models provide new living-off-the-land opportunities for attackers, each instance a potential post-exploitation engine already installed, signed by the vendor, and invisible to network monitoring. The Gemini model is multimodal, capable of processing files, analyzing screenshots, or conversing with an attacker. We show that it can be driven from the host using only interpreters that ship with the operating system and find that the one-time user-activation check before the model is downloaded is easily satisfied with a simulated click or bypassed entirely.We measure and report the current model's ability to identify credentials on the host, detect PII in email, classify images, and call custom tools. We combine these capabilities and use the model to carry out a simulated cyber operation: reading a password from a webcam image, unlocking an encrypted archive, triaging the contents, and staging a private key for exfiltration, end-to-end without user-interaction.

## Metadata
- **Published**: 2026-11-18T19:23:44Z
- **Authors**: William Fleshman, Joseph Lucas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.25086v1)