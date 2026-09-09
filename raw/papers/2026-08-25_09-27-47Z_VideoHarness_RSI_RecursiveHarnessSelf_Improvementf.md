---
title: VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models
published: 2026-08-25T09:27:47Z
authors: Guoyang Xu, Hao Chen
url: http://arxiv.org/abs/2608.24302v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models

## Abstract
Long-video understanding depends not only on the capability of a vision-language model (VLM), but also on how its limited context is constructed from a much longer video. Existing systems typically introduce hand-designed sampling, retrieval, memory, or agentic control strategies, making the context-construction program itself difficult to study as an independent optimization target. We introduce VideoHarness-RSI, a controlled framework that recursively searches executable context constructors around a frozen VLM while keeping the answering model and interface fixed. We study this baseline under complementary weak- and strong-initialization regimes. From a weak uniform constructor, recursive search progressively discovers more structured context-construction programs; from a stronger AKS harness, the same process further advances an already competitive hand-crafted frontier. The resulting harness retains its advantage under a matched cumulative visual-token control and transfers directly to additional long-video benchmarks without further search. Together, these results establish executable context construction as a distinct optimization layer and provide an auditable baseline for studying harness discovery, transfer, and efficiency around frozen VLMs.

## Metadata
- **Published**: 2026-08-25T09:27:47Z
- **Authors**: Guoyang Xu, Hao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24302v2)