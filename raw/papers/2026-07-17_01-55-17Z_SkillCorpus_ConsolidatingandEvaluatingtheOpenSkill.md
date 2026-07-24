---
title: SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents
published: 2026-07-17T01:55:17Z
authors: Yanze Wang, Pengfei Yao, Tianyi Sun, Chuanrui Hu, Yan Xiao, Yunyun Han, Yifan Chen, Jun Sun, Yafeng Deng
url: http://arxiv.org/abs/2607.15557v4
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents

## Abstract
Agent skills, SKILL files that package reusable procedural knowledge for an LLM agent, are a popular mechanism for extending agent capabilities. Public repositories now host them in large and growing numbers, yet these artifacts are fragmented, redundant, and uneven in quality, and their value in practice is unclear. A core question remains open, namely how to consolidate this open-source SKILL ecosystem into a single usable corpus, and what bounds its benefit on real-world agent tasks. We present SkillCorpus, a framework that aggregates, curates, matches, and evaluates the open skill ecosystem at scale. It filters ~821,000 crawled skills through a multi-stage pipeline into 96,401 skills organised by a 16-class taxonomy and three quality facets (utility, robustness, safety), and pairs them with a fine-tuned retrieval-and-selection stack that matches task-relevant skills. We evaluate end-to-end across three benchmarks (SkillsBench, GDPVal, QwenClawBench), two harnesses, and two open backbones with a frontier robustness check. Integrating SkillCorpus yields consistent gains across all three benchmarks, largest on SkillsBench (+7.5 pp). An operational analysis traces the gains to a coverage boundary and a harness boundary. SkillCorpus is, to our knowledge, the first end-to-end account of when a curated, retrieval-served community corpus improves real agent tasks, and where it does not. The dataset, models, and code will be released upon acceptance.

## Metadata
- **Published**: 2026-07-17T01:55:17Z
- **Authors**: Yanze Wang, Pengfei Yao, Tianyi Sun, Chuanrui Hu, Yan Xiao, Yunyun Han, Yifan Chen, Jun Sun, Yafeng Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.15557v4)