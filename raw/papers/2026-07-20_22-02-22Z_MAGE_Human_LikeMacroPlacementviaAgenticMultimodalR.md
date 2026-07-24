---
title: MAGE: Human-Like Macro Placement via Agentic Multimodal Reasoning
published: 2026-07-20T22:02:22Z
authors: Andrew B. Kahng, Sayak Kundu, Bodhisatta Pramanik
url: http://arxiv.org/abs/2607.18536v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MAGE: Human-Like Macro Placement via Agentic Multimodal Reasoning

## Abstract
Macro placement still requires substantial manual refinement in industrial physical design flows. We present MAGE (Macro Placement Agentic Engine), a multimodal multi-agent framework for macro placement refinement. MAGE decomposes the macro placement task into a six-phase workflow that combines structured floorplanning rules, visual checks, and iterative refinement. Expert floorplanning knowledge is encoded through natural-language directives and validation criteria, rather than learned from labeled placement data. A tournament-style refinement mode evaluates multiple candidate placements and propagates feedback from higher-quality solutions. We also introduce four metrics for quantifying human-likeness in macro placement: notch score, whitespace score, pocket score, and alignment score. These metrics capture structural properties used by expert designers but not directly measured by conventional PPA metrics. Across nine designs in NanGate45 and GlobalFoundries 12nm enablements, MAGE achieves geometric-mean improvements of 11.1%-19.3% in WNS and 70.0%-74.0% in TNS over commercial macro placers. On the three NanGate45 designs, for which human-expert and Hier-RTLMP baselines are available, MAGE improves WNS and TNS by 18.3% and 72.5% over the human expert, and by 47.0% and 80.4% over Hier-RTLMP, with comparable wirelength and power. On human-likeness metrics, MAGE improves the overall score by 6%-48% over all baselines. Additional case studies on anonymized netlists, unseen designs, dense rectilinear floorplans, and high-utilization settings show that the framework transfers to new placement settings without design-specific retraining.

## Metadata
- **Published**: 2026-07-20T22:02:22Z
- **Authors**: Andrew B. Kahng, Sayak Kundu, Bodhisatta Pramanik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18536v1)