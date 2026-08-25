---
title: CDEG: Learning Decision-Critical Evidence for Long-Horizon Diagnostic Agents
published: 2026-08-24T07:30:22Z
authors: Xiwei Dai, Zijie Meng, Zhiting Fan, Yixuan Tang, Ziru Niu, Zuozhu Liu
url: http://arxiv.org/abs/2608.22899v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CDEG: Learning Decision-Critical Evidence for Long-Horizon Diagnostic Agents

## Abstract
Unlike static medical question answering, long-horizon diagnosis captures the sequential nature of clinical practice: evidence is progressively acquired, integrated, and evaluated over multiple rounds of interaction before reaching a final diagnosis. However, existing doctor agents often fail when critical evidence is either not acquired or not adequately incorporated into diagnostic reasoning. Recent agentic approaches attempt to address these failures by reusing historical trajectories or distilled memories. But their diagnostic gains remain constrained because such experience may contain noisy or incidental information and is typically reused without validating which evidence actually drives diagnostic decisions. To address this limitation, we introduce CDEG, a graph-based framework that learns reusable decision-critical evidence from historical diagnostic trajectories. CDEG contrasts successful and failed trajectories from the same case to identify candidate evidence, validates their diagnostic impact through controlled counterfactual interventions, and organizes the resulting diagnosis--evidence--action relations into a structured graph. During inference, CDEG tracks the evolving patient evidence state to retrieve relevant diagnostic relations and selectively guide missing evidence acquisition or overlooked evidence reappraisal. Across in-domain and out-of-distribution benchmarks with multiple doctor agent backbones, CDEG consistently improves diagnostic performance, achieving up to an 11.5% accuracy gain over vanilla agents. These results demonstrate that reliable long-horizon diagnosis requires moving beyond trajectory-level experience reuse toward evidence-level learning of the factors that truly shape clinical decisions.

## Metadata
- **Published**: 2026-08-24T07:30:22Z
- **Authors**: Xiwei Dai, Zijie Meng, Zhiting Fan, Yixuan Tang, Ziru Niu, Zuozhu Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22899v1)