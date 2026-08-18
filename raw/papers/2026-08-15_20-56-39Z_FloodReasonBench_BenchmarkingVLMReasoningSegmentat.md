---
title: FloodReasonBench: Benchmarking VLM Reasoning Segmentation for Embodied Flood Response at the Edge
published: 2026-08-15T20:56:39Z
authors: Rajat Bhattacharjya, Yoomee Jung, Minwoo Kim, Sing-Yao Wu, Eli Bozorgzadeh, Nalini Venkatasubramanian, Nikil Dutt
url: http://arxiv.org/abs/2608.15410v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FloodReasonBench: Benchmarking VLM Reasoning Segmentation for Embodied Flood Response at the Edge

## Abstract
Reasoning segmentation enables vision-language models (VLMs) to translate mission-relevant language requests into pixel-level visual grounding, offering a natural perception interface for embodied agents. However, existing benchmarks largely focus on generic visual scenes and overlook the domain and resource constraints encountered in flood-response platforms. We present FloodReasonBench, a benchmark for VLM reasoning segmentation for embodied flood response at the edge. At its core, FloodReasonBench introduces FloodResponseSeg, a flood-specific reasoning-segmentation dataset constructed from real-world scenes and response-relevant targets. Beyond task accuracy, the benchmark characterizes reasoning-segmentation pipelines under lightweight visual encoding, hierarchical split inference, and compressed intermediate representations. We observe strong partition-dependent accuracy variation in the generic pre-adaptation setting, while the flood-adapted target-workload design space exhibits a substantially more compact accuracy range across partitions. Evaluation on an NVIDIA Jetson AGX Xavier further exposes the tradeoffs among reasoning-segmentation accuracy, edge-side latency, energy, and communication footprint, enabling quality-constrained selection of edge operating points. Together, these results provide a task- and system-level characterization of reasoning segmentation for resource-constrained embodied flood response at the edge.

## Metadata
- **Published**: 2026-08-15T20:56:39Z
- **Authors**: Rajat Bhattacharjya, Yoomee Jung, Minwoo Kim, Sing-Yao Wu, Eli Bozorgzadeh, Nalini Venkatasubramanian, Nikil Dutt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15410v1)