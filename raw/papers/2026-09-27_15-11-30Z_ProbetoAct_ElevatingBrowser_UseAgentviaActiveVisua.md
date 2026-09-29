---
title: Probe to Act: Elevating Browser-Use Agent via Active Visual Probing
published: 2026-09-27T15:11:30Z
authors: Keliang Li, Heng Wang, Chen Hu, Daxin Jiang, Hong Chang, Shiguang Shan
url: http://arxiv.org/abs/2609.33646v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Probe to Act: Elevating Browser-Use Agent via Active Visual Probing

## Abstract
Browser-use agents require seamless alignment between structured web metadata and visual information, while preserving relevant context across long interactions. Existing interfaces often rely on either screenshot-level action prediction or static Set-of-Marks overlays, leaving the model to resolve dense DOM-pixel alignment before every operation. We introduce Probe to Act (P2A), an active probing framework for the browser-agent loop that moves this alignment into decision time. P2A addresses an asymmetric bridge between symbolic DOM hypotheses and screenshot layout by rendering on-demand symbolic DOM structure back into pixels. Before committing a state-changing browser operation, the agent can issue lightweight probes to translate DOM handles into pixel evidence, map screen regions back to DOM candidates, register visual-only targets, and commit verified notes. These interleaved processes naturally produce evidence-based memory: only probed, acted-on, or explicitly committed observations are kept across steps, preserving only decision-critical evidence in long-horizon contexts. P2A can be used as a prompting strategy for proprietary models under the standard DOM+SoM interface, and can be distilled into open-weight models through cold-start synthesis and self-bootstrapped SFT. Across three browser-use benchmarks, P2A shows clear gains on task success rate for both proprietary and fine-tuned models; on VisualWebArena, for example, it improves Gemini-3-Pro from 54.1% to 61.2% and Qwen3-VL-8B from 24.6% to 32.9%, while matching the costly full-observation history ($\sim$3$\times$) at only $\sim$1.2$\times$ the peak retained input context of action-only history.

## Metadata
- **Published**: 2026-09-27T15:11:30Z
- **Authors**: Keliang Li, Heng Wang, Chen Hu, Daxin Jiang, Hong Chang, Shiguang Shan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33646v1)