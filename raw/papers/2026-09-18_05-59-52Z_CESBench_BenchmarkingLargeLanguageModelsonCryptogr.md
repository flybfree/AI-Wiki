---
title: CESBench: Benchmarking Large Language Models on Cryptographic Engineering Security for IoT Devices
published: 2026-09-18T05:59:52Z
authors: Wenquan Zhou, An Wang, Jing Liang, Peien Feng, Jingqi Zhang, Yaoling Ding, Liehuang Zhu
url: http://arxiv.org/abs/2609.21344v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CESBench: Benchmarking Large Language Models on Cryptographic Engineering Security for IoT Devices

## Abstract
For Internet of Things (IoT) devices, a secure algorithm alone is not enough: an attacker with physical access can attack the implementation directly, and its flaws are hard to fix once deployed. Large language models (LLMs) are now used to build and analyze such implementations. LLM benchmarks exist for cryptography and general cybersecurity, but none covers cryptographic engineering. In this paper, we present CESBench, 380 expert-written items across six sub-domains of cryptographic engineering security for IoT devices: side-channel, fault injection, implementation, countermeasures, evaluation, and integration. Four task types target different competences: 209 multiple-choice items test recall, 67 judgment items require a security verdict and its justification, 63 scenario items require an engineering diagnosis, and 41 code tasks are graded by 572 test cases. To validate the benchmark, 11 open-weight and proprietary LLMs answer every item. Multiple-choice and code responses are scored automatically, and judgment and scenario responses by an LLM judge, whose scores are checked against a second judge from another model family and human re-scoring. Composite scores range from 54.4% to 83.6%. The top score on each task type is 98.6% for multiple choice, 95.1% for code, and 88.4% for scenario diagnosis, but only 58.8% for judgment. Across models, 88.5% of verdicts are correct, yet their justifications earn only 53.4% of the rubric marks. Multiple choice is near its ceiling for the strongest models and most code tasks are solved, whereas justifying a security verdict remains the weakest competence. The benchmark, prompts, and per-item results are public.

## Metadata
- **Published**: 2026-09-18T05:59:52Z
- **Authors**: Wenquan Zhou, An Wang, Jing Liang, Peien Feng, Jingqi Zhang, Yaoling Ding, Liehuang Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21344v1)