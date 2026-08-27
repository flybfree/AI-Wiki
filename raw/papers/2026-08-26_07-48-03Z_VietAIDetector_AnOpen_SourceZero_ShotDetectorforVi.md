---
title: VietAIDetector: An Open-Source Zero-Shot Detector for Vietnamese AI-Generated Text
published: 2026-08-26T07:48:03Z
authors: Trieu Hai Nguyen, Van-Dung Hoang
url: http://arxiv.org/abs/2608.25478v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VietAIDetector: An Open-Source Zero-Shot Detector for Vietnamese AI-Generated Text

## Abstract
In recent years, distinguishing between AI-generated text and human-written text has remained a challenge. In this paper, we introduce VietAIDetector, an open-source tool designed specifically for detecting Vietnamese AI-generated text. It allows users to interact through a Gradio web interface with inputs ranging from raw Vietnamese text to common text file formats, including scanned documents and exceptionally long texts that exceed the context size of the employed Large Language Models (LLMs). The core component of the tool employs a Zero-Shot approach to detect AI-generated text without requiring domain-specific training data, building upon the previous VietBinoculars and Binoculars research. The tool is built upon a Vietnamese-specific language model and has been evaluated on out-of-domain datasets, demonstrating superior performance compared to existing methods primarily developed for English. Additionally, users can select optimal detection thresholds based on F1 score, accuracy, or TPR@0.05FPR requirements. The results are presented through the web interface, allowing users to easily review and verify suspicious texts or download them as a PDF report. The tool is publicly available at https://github.com/trieuntu/VietAIDetector

## Metadata
- **Published**: 2026-08-26T07:48:03Z
- **Authors**: Trieu Hai Nguyen, Van-Dung Hoang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25478v1)