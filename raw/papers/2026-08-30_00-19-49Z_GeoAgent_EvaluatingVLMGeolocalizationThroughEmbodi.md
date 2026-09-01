---
title: GeoAgent: Evaluating VLM Geolocalization Through Embodied Navigation
published: 2026-08-30T00:19:49Z
authors: Arka Mukherjee, Soham Roy, Kartikeya Trivedi, Shreya Ghosh
url: http://arxiv.org/abs/2608.29483v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GeoAgent: Evaluating VLM Geolocalization Through Embodied Navigation

## Abstract
Modern Vision-Language Models (VLMs) perform well above the human baseline in image geolocalization, a task critically important in disaster response, OSINT verification, and location privacy. However, most efforts to study AI behavior on the task remain limited to static image-based retrieval, classification, and predictions. We argue that faithful recreation of the task should involve embodied navigation, where a multimodal agent autonomously explores its surroundings to gather observations before submitting a prediction. To this end, we introduce \textbf{GeoAgent}, an agentic environment-based benchmark that requires agents to navigate Street View environments to refine their geolocalization through sequential reasoning. Our analysis shows that modern VLMs struggle to discern regional patterns while succeeding at country- and continent-level predictions. When compared to static image-based baselines, agentic navigation significantly improves accuracy across established metrics. We also note severe bias in a developed/developing region context across frontier model architectures and poor self-improvement capabilities given incorrect priors. Overall, our work establishes the challenges of embodied navigation and geospatial reasoning. We publicly release our code and the GeoAgent environment: https://geoagent-benchmark.github.io

## Metadata
- **Published**: 2026-08-30T00:19:49Z
- **Authors**: Arka Mukherjee, Soham Roy, Kartikeya Trivedi, Shreya Ghosh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29483v1)