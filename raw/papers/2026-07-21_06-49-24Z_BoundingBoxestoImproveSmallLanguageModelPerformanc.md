---
title: Bounding Boxes to Improve Small Language Model Performance on Vision-Based Grading Tasks
published: 2026-07-21T06:49:24Z
authors: Lachlan McGinness
url: http://arxiv.org/abs/2607.18767v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bounding Boxes to Improve Small Language Model Performance on Vision-Based Grading Tasks

## Abstract
The deployment of Small Language Models (SLMs) in educational settings offers significant advantages in terms of privacy, cost, and scalability. However, SLMs often struggle with complex vision-based tasks, such as grading handwritten student exams, due to the high computational cost of processing large images and the visual distractions present on a full page. In this paper, we investigate whether cropping student responses using bounding boxes can improve the accuracy and computational efficiency of SLMs on a short-answer grading task. Using a dataset of scanned handwritten responses from the 2025 Australian Physics Olympiad, we evaluate the performance of several models ranging from 4B to 72B parameters under varying conditions of Chain of Thought (CoT) prompting and image cropping. Our results demonstrate that using bounding boxes significantly improves grading accuracy and reduces computational cost (FLOPs) across models. We conclude that bounding boxes are a crucial pre-processing step for deploying SLMs in large-scale, vision-based educational assessments.

## Metadata
- **Published**: 2026-07-21T06:49:24Z
- **Authors**: Lachlan McGinness
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18767v1)