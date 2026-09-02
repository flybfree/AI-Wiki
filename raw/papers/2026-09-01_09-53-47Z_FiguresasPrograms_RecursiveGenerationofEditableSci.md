---
title: Figures as Programs: Recursive Generation of Editable Scientific Figures
published: 2026-09-01T09:53:47Z
authors: Yepeng Liu, Dasen Dai, Chengzhi Liu, Yiren Song, Hai Ci, Yu Zhang, Qi Zhang, Mike Zheng Shou, Xin Eric Wang, Yuheng Bu
url: http://arxiv.org/abs/2609.01006v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Figures as Programs: Recursive Generation of Editable Scientific Figures

## Abstract
Scientific methodology figures are essential for communicating complex methods clearly, yet creating them remains labor-intensive and typically requires multiple rounds of refinement. Recent image-generation models can synthesize visually appealing raster figures, but producing a human-satisfactory result in a single generation step remains difficult. Moreover, precise edits to raster figures are challenging for both humans and models. We formulate scientific figure generation as recursive SVG program construction and propose \textsc{FigTree}, a \textit{multi-agent} system that automatically transforms a scientific paper into a structured vector figure. \textsc{FigTree} grounds figure content in the source paper, decomposes a figure into a hierarchy of local regions, generates each region as a short SVG program, and assembles the resulting fragments. A render-critic refinement loop jointly inspects the rendered figure and its underlying program, enabling visual defects to be traced to specific statements and accurately repaired. We conduct extensive evaluations of \textsc{FigTree} on figure quality and editability, showing that \textsc{FigTree} produces high-quality figures, while also enabling more effective editing than existing raster-based methods.

## Metadata
- **Published**: 2026-09-01T09:53:47Z
- **Authors**: Yepeng Liu, Dasen Dai, Chengzhi Liu, Yiren Song, Hai Ci, Yu Zhang, Qi Zhang, Mike Zheng Shou, Xin Eric Wang, Yuheng Bu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01006v1)