---
title: LMM Modality Transfer: A Pre-requisite for Autonomous GIS Agents
published: 2026-08-07T08:25:14Z
authors: Ivan Majic, Zexian Huang, Franziska Hübl, Krzysztof Janowicz, Meilin Shi, Mina Karimi, Zilong Liu, Alexandra Fortacz-Lazan
url: http://arxiv.org/abs/2608.06948v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LMM Modality Transfer: A Pre-requisite for Autonomous GIS Agents

## Abstract
AI models are becoming increasingly adept at understanding and processing spatial information, thereby facilitating agentic problem-solving in spatial tasks and workflows. However, most of the research on their spatial capabilities (e.g., spatial reasoning) has focused on the textual modality as input and output. This contrasts with the human approach to GIS workflows, where text and visual modalities are often used together, interchangeably, and in a complementary manner. Thus, to truly achieve an automated GIS analysis pipeline or carry out human-designed GIS workflows, AI models --- Large Multimodal Models (LMMs) in particular --- need to be able to seamlessly transition between image- and text-based modalities that are traditionally used in such workflows. We present a modality transfer task that (1) asks an LMM to first describe an input image of colored squares in a regular grid, and (2) asks a new LMM instance to re-generate an image of the original spatial scene using the textual description output by the former model. This task quantifies the ability of LMMs to transfer spatial information between image and text modalities. Ultimately, by examining the modality transfer capability of LMMs through the lens of spatial information theory, this work highlights a critical bottleneck: achieving strong and robust geospatial understanding in LMMs requires rigorous, multi-modal alignment. Our results indicate that recent LMMs (here from OpenAI) still struggle with modality transfer, when tasked with re-generating an image of a simple spatial grid of color squares.

## Metadata
- **Published**: 2026-08-07T08:25:14Z
- **Authors**: Ivan Majic, Zexian Huang, Franziska Hübl, Krzysztof Janowicz, Meilin Shi, Mina Karimi, Zilong Liu, Alexandra Fortacz-Lazan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06948v1)