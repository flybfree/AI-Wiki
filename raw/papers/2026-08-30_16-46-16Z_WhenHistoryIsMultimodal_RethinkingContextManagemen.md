---
title: When History Is Multimodal: Rethinking Context Management for Long-Horizon Agents
published: 2026-08-30T16:46:16Z
authors: Jiaqi Su, Cong Pang, Jiawei Hong, Tiankuo Yao, Zixuan Chen, Xin Lou, Lewei Lu
url: http://arxiv.org/abs/2608.29897v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When History Is Multimodal: Rethinking Context Management for Long-Horizon Agents

## Abstract
Long-horizon agents need a context manager to compress growing interaction histories into a bounded working context, via passive strategies or active strategies that decide how memory is accessed and reorganized. Meanwhile, prior optical-memory work mainly treats pixels as a dense codec for textualized histories, often presupposing that rendering context into optical memory incurs a significant performance drop relative to text, thus coupling this representation with SFT, self-distillation, or reinforcement learning to close this gap, leaving unresolved (i) how visual rendering performs as a context manager under a fair, controlled comparison, and (ii) whether this carrier offers a native advantage when history is inherently multimodal. In this paper, we formulate context management as a budget-constrained history transformation and introduce Visual Rendering (VR) as a representational context manager. Under a shared harness, policy model, trigger, and task domain, we evaluate VR on four text-centric and three multimodal benchmarks against four baselines (No Compression, Discard-All, Sliding Window, Summarization), finding visual memory is a natural carrier of native visual evidence. Building on this finding, we propose VERA (Visual Evidence-Retaining strategy for long-horizon Agents), a training-free context manager built on deterministic rendering with no exposed memory operations: on text-centric benchmarks it renders textual history as VR does, while on multimodal benchmarks it retains native visual observations instead of translating them into text. Across nearly all benchmarks, VERA cuts cumulative non-cache tokens by 31.5%-63.1% versus No Compression, matches existing managers on text-centric tasks, and achieves the highest accuracy among all baselines on multimodal tasks, supporting a modality-preserving view of long-horizon context management.

## Metadata
- **Published**: 2026-08-30T16:46:16Z
- **Authors**: Jiaqi Su, Cong Pang, Jiawei Hong, Tiankuo Yao, Zixuan Chen, Xin Lou, Lewei Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29897v1)