---
title: MOF-VERIFY: A Failure-Aware Agentic Harness for MOF Hypothesis Verification
published: 2026-10-02T09:36:55Z
authors: Donghyun Lee, Taehoon Lee, Geonhee Ahn, Jieun Kim, Jihyun Park, Suyeon Cho, Yoona Kim, Chaerim Shin, Hoi Ri Moon, Jonggeol Na, Sukho Hong, Jihwan Oh, Soo Kyung Kim
url: http://arxiv.org/abs/2610.03056v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MOF-VERIFY: A Failure-Aware Agentic Harness for MOF Hypothesis Verification

## Abstract
Large language models are increasingly used as reasoning components in AI-driven materials Co-Scientists, yet the reliability of the resulting verification pipeline remains unclear. Metal-organic frameworks (MOFs) provide a particularly challenging setting because structures may appear under different identifiers, synthesis outcomes depend strongly on experimental conditions, evidence is distributed across heterogeneous sources, and some hypotheses require computation rather than literature alone. We introduce a diagnostic benchmark with four task families covering structural grounding, synthesis-condition verification, evidence-sufficiency verification, and MLIP-based computational verification. T-MOF-1-3 are evaluated under closed-book, retrieval-enabled, and oracle-evidence settings to localize failures in knowledge access, evidence acquisition, and reasoning, while T-MOF-4 separately evaluates computational verification. Guided by these diagnosed failure modes, we develop MOF-Verify, a failure-aware agentic harness that targets structural, literature, evidence-sufficiency, and computational bottlenecks before producing a final verdict. Across multiple backbone LLMs, MOF-Verify substantially improves hypothesis-verification performance over direct inference and retrieval-based baselines. Benchmark datasets are released at https://github.com/IMMS-Ewha/MOF-Verify-Benchmark.

## Metadata
- **Published**: 2026-10-02T09:36:55Z
- **Authors**: Donghyun Lee, Taehoon Lee, Geonhee Ahn, Jieun Kim, Jihyun Park, Suyeon Cho, Yoona Kim, Chaerim Shin, Hoi Ri Moon, Jonggeol Na, Sukho Hong, Jihwan Oh, Soo Kyung Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.03056v1)