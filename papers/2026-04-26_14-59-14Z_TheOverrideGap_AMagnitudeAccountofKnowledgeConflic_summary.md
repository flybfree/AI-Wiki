---
title: "Summary: 2026-04-26_14-59-14Z_TheOverrideGap_AMagnitudeAccountofKnowledgeConflic.md"
date: 2026-04-26
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-04-26_14-59-14Z_TheOverrideGap_AMagnitudeAccountofKnowledgeConflic.md


**Source**: [Original Paper](http://arxiv.org/abs/2604.23750v1)
Saved: 2026-05-07 22:29
Source: 2026-04-26_14-59-14Z_TheOverrideGap_AMagnitudeAccountofKnowledgeConflic.md
Model: None

---

## Summary
Hypernetwork-based methods such as Doc-to-LoRA internalize a document into an LLM's weights in a single forward pass, but they fail systematically on conflicts: when the document contradicts pretraining knowledge, accuracy collapses to 46.4% on the deepest facts. We show the failure is a magnitude problem rather than a representational one. The hypernetwork already targets the right layers, but its adapter margin is approximately constant across documents while the pretrained margin grows with training frequency, so deep conflicts lose by construction.

## Key Takeaways
- Hypernetwork-based methods such as Doc-to-LoRA internalize a document into an LLM's weights in a single forward pass, but they fail systematically on conflicts: when the document contradicts pretraining knowledge, accuracy collapses to 46.4% on the deepest facts.
- We show the failure is a magnitude problem rather than a representational one.
- The hypernetwork already targets the right layers, but its adapter margin is approximately constant across documents while the pretrained margin grows with training frequency, so deep conflicts lose by construction.

## Context
Hypernetwork-based methods such as Doc-to-LoRA internalize a document into an LLM's weights in a single forward pass, but they fail systematically on conflicts: when the document contradicts pretraining knowledge, accuracy collapses to 46.4% on the deepest facts.

## Implications
We release KID-Bench, a 489-question benchmark that separates novel recall, cross-knowledge combination, and prior-graded conflicts.

## Original Reference
- Title: The Override Gap: A Magnitude Account of Knowledge Conflict Failure in Hypernetwork-Based Instant LLM Adaptation
- Authors: Shuaizhi Cheng, Xiang Shi, Mingwei Li
- Published: 2026-04-26T14:59:14Z
- URL: http://arxiv.org/abs/2604.23750v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-04-26_14-59-14Z_TheOverrideGap_AMagnitudeAccountofKnowledgeConflic.md

[[The Override Gap: A Magnitude Account of Knowledge Conflict Failure in Hypernetwork-Based Instant LLM Adaptation]]