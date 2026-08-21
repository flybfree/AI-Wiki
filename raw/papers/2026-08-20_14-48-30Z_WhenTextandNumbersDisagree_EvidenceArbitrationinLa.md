---
title: When Text and Numbers Disagree: Evidence Arbitration in Large Language Models
published: 2026-08-20T14:48:30Z
authors: Mattia Carletti, Edward Phillips, Fredrik K. Gustafsson, Patitapaban Palo, Lei Clifton, Danielle Belgrave, Xiao Gu, David A. Clifton
url: http://arxiv.org/abs/2608.20116v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Text and Numbers Disagree: Evidence Arbitration in Large Language Models

## Abstract
Large language models (LLMs) are increasingly used in settings where textual summaries, numerical observations, and external tool outputs may provide conflicting evidence. We study how LLMs arbitrate between such sources when they support opposing decisions. To do so, we introduce a controlled synthetic benchmark in which latent risk trajectories generate both numerical time series and natural language summaries, allowing us to construct conflicts where exactly one evidence source is aligned with the ground-truth label. This design lets us independently manipulate modality, temporal recency, source reliability, and evidence provenance. Across open-weight instruction-tuned models, we find that arbitration behaviour is systematic rather than random: models exhibit distinct text-versus-number preferences, follow temporal recency more consistently than explicit reliability cues, and can over-rely on external forecasts even when they conflict with direct contextual evidence. These results suggest that current LLMs often rely on heuristic arbitration strategies when integrating heterogeneous evidence, highlighting a failure mode for tool-augmented decision systems.

## Metadata
- **Published**: 2026-08-20T14:48:30Z
- **Authors**: Mattia Carletti, Edward Phillips, Fredrik K. Gustafsson, Patitapaban Palo, Lei Clifton, Danielle Belgrave, Xiao Gu, David A. Clifton
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20116v1)