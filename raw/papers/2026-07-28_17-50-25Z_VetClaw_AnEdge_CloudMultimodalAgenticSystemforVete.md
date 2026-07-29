---
title: VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening
published: 2026-07-28T17:50:25Z
authors: Syed Mhamudul Hasan, Anas AlSobeh, Hussein Zangoti, Abdur R. Shahid
url: http://arxiv.org/abs/2607.26042v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening

## Abstract
We present VetClaw, an edge-cloud multimodal agentic system for early veterinary disease screening. VetClaw uses a camera module as an edge sensing device and sends captured images, together with optional symptom descriptions, to a server-hosted vision-language model for zero-shot disease classification. The system separates agent interaction from workflow orchestration: OpenClaw provides scheduling, tool access, user interaction, and notification services on the edge device, while LangGraph manages the stateful screening workflow, including input validation, image transmission, model invocation, safety checks, conditional routing, failure handling, and structured logging. This design moves beyond static image classification by enabling the system to collect visual evidence, invoke external models, apply deterministic safety rules, and generate diagnostic-support alerts. Results show that image-only VLM prediction remains limited, whereas symptom-guided and multimodal inputs improve zero-shot classification performance. Thus, VetClaw transforms a static prediction model into a coordinated, safety-aware system that can use tools, manage workflows, handle failures, and escalate uncertain cases.

## Metadata
- **Published**: 2026-07-28T17:50:25Z
- **Authors**: Syed Mhamudul Hasan, Anas AlSobeh, Hussein Zangoti, Abdur R. Shahid
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26042v1)