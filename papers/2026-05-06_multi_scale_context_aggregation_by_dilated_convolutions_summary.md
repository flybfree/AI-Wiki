---
title: "Summary: Multi-Scale Context Aggregation by Dilated Convolutions"
date: 2026-05-06
tags: ['paper', 'research', 'ai']
---
# Summary: Multi-Scale Context Aggregation by Dilated Convolutions


**Source**: [Original Paper](https://arxiv.org/abs/1511.07122)
Saved: 2026-05-07 22:08
Source: 2026-05-06_multi_scale_context_aggregation_by_dilated_convolutions.md

---

## Summary
This paper explains how dilated convolutions can aggregate multi-scale context without reducing spatial resolution. By spacing convolutional filters apart, the model expands its receptive field while keeping the feature map dense. The result is a simple and effective architectural trick for dense prediction tasks.

## Key Takeaways
- Dilated convolutions enlarge receptive fields without downsampling.
- Multi-scale context can be captured while preserving resolution.
- The idea is broadly useful for dense vision problems.

## Context
The source file is a reading-list entry pointing to the original arXiv paper. Its central contribution is a practical architecture pattern for context aggregation.

## Implications
Dilated convolutions became a standard tool in segmentation and related tasks because they balance context and detail. The idea also influenced later designs that need large receptive fields without pooling.

## Original Reference
- Title: Multi-Scale Context Aggregation by Dilated Convolutions
- Authors: Fisher Yu and Vladlen Koltun
- Published: 2015
- URL: https://arxiv.org/abs/1511.07122
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-05-06_multi_scale_context_aggregation_by_dilated_convolutions.md