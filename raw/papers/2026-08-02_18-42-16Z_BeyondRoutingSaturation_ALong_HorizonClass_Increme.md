---
title: Beyond Routing Saturation: A Long-Horizon Class-Incremental Perspective on Expert Routing in Multimodal Continual Instruction Tuning
published: 2026-08-02T18:42:16Z
authors: Huiyu Yi, Yongqi Xu, Bogang Zhang, Dunwei Tu, Xu Zhiming, Zhen-Hao Xie, Baile Xu, Furao Shen
url: http://arxiv.org/abs/2608.01437v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Routing Saturation: A Long-Horizon Class-Incremental Perspective on Expert Routing in Multimodal Continual Instruction Tuning

## Abstract
Multimodal Continual Instruction Tuning (MCIT) enables multimodal large language models to acquire new tasks sequentially while retaining previously learned capabilities. Many recent methods maintain task-specific LoRA experts and route each input to one or more experts at inference. Yet the task-identification problem underlying expert routing remains under-explored. We show that routing is nearly saturated on widely used MCIT benchmarks. Textual fingerprints that leak task identity and short 4--10-task sequences with few competing experts jointly obscure the long-horizon routing problem. To expose this challenge, we introduce FLEX (Fingerprint-reduced Long-horizon Expert eXamination), a 34-task long-horizon MCIT benchmark with weakened textual fingerprints. FLEX groups tasks with similar instruction and answer formats but diverse visual and knowledge domains, normalizes their outer templates, and evaluates routing over a substantially larger expert pool. Crucially, we formulate progressive-LoRA routing as soft task-as-class Multimodal Class-Incremental Learning (MCIL): each task defines an incremental routing class, whose complete score distribution supplies the LoRA mixture weights, with hard routing as a discrete special case. FLEX exposes this expanding task-identification challenge, while the MCIL formulation provides a principled interface for transferring CIL methods to expert routing. We instantiate PureLoRA as a controlled baseline and adapt four CIL methods to four MCIT frameworks without modifying their LoRA experts or generation pipelines. Our plug-in routers improve strict LoRA matching by up to 16.3 percentage points and overall MacroScore by up to 4.6 points. Code is available at: https://github.com/RINC-CL/FLEX

## Metadata
- **Published**: 2026-08-02T18:42:16Z
- **Authors**: Huiyu Yi, Yongqi Xu, Bogang Zhang, Dunwei Tu, Xu Zhiming, Zhen-Hao Xie, Baile Xu, Furao Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01437v1)