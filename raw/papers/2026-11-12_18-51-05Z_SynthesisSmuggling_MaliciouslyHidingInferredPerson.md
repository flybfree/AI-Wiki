---
title: Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs
published: 2026-11-12T18:51:05Z
authors: Gautam Galada, Supreeth Shastri, Sagnik Ray Choudhury
url: http://arxiv.org/abs/2611.17280v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs

## Abstract
We propose Synthesis Smuggling, a novel threat model in which an adversarial LLM infers sensitive information about a user from routine assistance-seeking interactions and steganographically encodes that into innocuous-looking model-generated content. The user may then unknowingly transmit that information by sharing the generated artifact, say as an email, social-media post, or message, through ordinary communication channels. An adversary monitoring these channels can discover this information. We demonstrate this threat by training two open-weight models to infer gender and age-group labels from conversational cues and encode their predictions using invisible characters or word choices. These results show that user-shared model outputs can become a covert channel for personal inferences, even when the model itself has no direct means of contacting an adversary.

## Metadata
- **Published**: 2026-11-12T18:51:05Z
- **Authors**: Gautam Galada, Supreeth Shastri, Sagnik Ray Choudhury
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.17280v1)