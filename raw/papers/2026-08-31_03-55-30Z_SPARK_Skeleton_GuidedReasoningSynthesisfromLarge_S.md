---
title: SPARK: Skeleton-Guided Reasoning Synthesis from Large-Scale Scientific Literature
published: 2026-08-31T03:55:30Z
authors: Yu Li, Wei Li, Xin Gao, Mengyuan Sun, Xiaoyang Wang, Qizhi Pei, Lijun Wu
url: http://arxiv.org/abs/2608.30214v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPARK: Skeleton-Guided Reasoning Synthesis from Large-Scale Scientific Literature

## Abstract
Scientific reasoning remains challenging for open-source models, largely due to the lack of high-quality scientific reasoning data. Existing datasets are often dominated by factual recall or formulaic problem solving, with limited emphasis on mechanism understanding, evidence-grounded reasoning, and hypothesis evaluation. To address this, we introduce SPARK (Scientific Paper Abstracted Reasoning sKeleton), a paper-oriented synthesis framework built on Sci-Base, a large-scale corpus of research papers spanning 10 scientific disciplines. Instead of directly converting papers into question-answer pairs, SPARK treats the claim-evidence-derivation structure of a paper as the fundamental unit of reasoning synthesis. Specifically, SPARK (1) distills each paper into a compact reasoning skeleton capturing its central claims and supporting evidence, enabling self-contained question generation, and (2) synthesizes reasoning tasks from four scientific perspectives: mechanistic reasoning, hypothesis falsification, quantitative derivation, and boundary calibration. A final consistency verification stage further removes unsupported or contradictory outputs. Using this framework, we construct Spark-234K, a scientific reasoning dataset with substantially higher difficulty and diversity than existing resources. Experiments show that Spark-234K consistently outperforms existing scientific reasoning datasets while achieving stronger performance with significantly fewer training samples.

## Metadata
- **Published**: 2026-08-31T03:55:30Z
- **Authors**: Yu Li, Wei Li, Xin Gao, Mengyuan Sun, Xiaoyang Wang, Qizhi Pei, Lijun Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30214v1)