---
title: VICBench: A Multi-Language Benchmark for Code Vulnerability Detection
published: 2026-08-12T16:45:49Z
authors: Jin Lu, Xuening Han, Yang Zhong, Lin Tan, Kevin Luo, Andrew Gacek, Neha Rungta
url: http://arxiv.org/abs/2608.12246v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VICBench: A Multi-Language Benchmark for Code Vulnerability Detection

## Abstract
Evaluating security vulnerability detection tools requires benchmark datasets with vulnerability-inducing commits (VICs) - the commits that first introduce vulnerabilities into codebases. VICs are essential for determining the full range of vulnerable software versions. Existing vulnerability datasets suffer from limited programming language coverage, restricted patch complexity, and narrow project scope. Through our dual annotation by human experts and an agentic workflow, we create a benchmark - VICBench - of 100 verified VICs for 100 CVEs across 88 projects in Python, Java, and C++, covering 48 CWE types. VICBench features complex real-world vulnerability fixes averaging 38.6 lines and corresponding VICs of 252.5 lines - significantly larger than prior work. Our evaluation shows that state-of-the-art algorithms V-SZZ and LLM4SZZ achieve only 33.3%-40.1% F1, confirming that using existing approaches still entails significant manual effort. VICBench enables robust evaluation of vulnerability detection approaches.

## Metadata
- **Published**: 2026-08-12T16:45:49Z
- **Authors**: Jin Lu, Xuening Han, Yang Zhong, Lin Tan, Kevin Luo, Andrew Gacek, Neha Rungta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12246v1)