---
title: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
published: 2026-05-18T10:54:55Z
authors: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
url: http://arxiv.org/abs/2605.18209v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning

## Abstract
Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.

## Metadata
- **Published**: 2026-05-18T10:54:55Z
- **Authors**: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.18209v1)