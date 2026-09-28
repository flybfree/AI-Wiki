---
title: Muslim: A Deployed Arabic Voice AI Platform for Grounded Islamic Knowledge
published: 2026-09-25T16:51:22Z
authors: Yahya Mohamed Elnawasany
url: http://arxiv.org/abs/2609.31511v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Muslim: A Deployed Arabic Voice AI Platform for Grounded Islamic Knowledge

## Abstract
We present Muslim, a production Arabic voice AI platform serving grounded, sourced Islamic knowledge to real users. Beyond a real-time voice pipeline (NeMo Arabic ASR, an OpenAI-compatible LLM endpoint, self-hosted TTS) and a deterministic multi-source retrieval layer routed across six Model Context Protocol servers, we report three things a research prototype typically lacks. First, a released family of fine-tuned Arabic Islamic model artifacts: an efficient tool-routing LLM (Muslim-6B-PRO, 5.94B parameters) and a Modern Standard Arabic TTS model (Fasih-TTS-V1) that ranks 5th of 17 overall and 2nd of 11 open-weight systems on the community-voted Arabic TTS Arena for MSA. Second, an account and metering layer - a free per-account turn allowance, capacity-aware refusal, and email verification deferred to the point it actually matters - that turns an open demo into an operable, abuse-resistant product. Third, a three-layer observability stack (liveness, error reporting, product analytics) built specifically around the system's characteristic failure mode: a GPU-bound agent host going silent while the web tier keeps serving normally. We report real, measured latency and accuracy figures (98.4% recitation-validation accuracy on 124 cases; end-to-end voice latency of 0.9-1.7s) and discuss the concrete engineering trade-offs and limitations of running an Islamic-knowledge voice product in production.

## Metadata
- **Published**: 2026-09-25T16:51:22Z
- **Authors**: Yahya Mohamed Elnawasany
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31511v1)