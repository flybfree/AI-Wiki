---
title: Code Monitor Red Teaming for Public-Test-Passing Code
published: 2026-07-23T02:23:09Z
authors: Junchi Liao, Jiawen Deng, Fuji Ren
url: http://arxiv.org/abs/2607.20852v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Code Monitor Red Teaming for Public-Test-Passing Code

## Abstract
Visible tests are a common gate for LLM-generated code, but passing them does not certify specification correctness. We study a deployment-like monitoring problem: after code has passed public tests, can a weaker LLM verifier identify the residual hidden bugs? We introduce Code Monitor Red Teaming, a monitor-red-teaming protocol that fixes a public-check information boundary while varying generator pressure, verifier scaffolding, and weak-to-strong capability. We instantiate it as CodeMonitorBench, spanning function-level, data-science, and workflow code. Across 71,000 generated candidates, 43,677 pass public tests and 23,081 of those fail hidden tests. Weak verifiers improve with scaffolding and model family, but still miss most hidden bugs at 5% false-positive rate. As a robustness stress test, adversarial public-test-overfit pressure lowers verifier AUROC and raises low-FPR miss rates in most cells. A GLM-5.1 verifier recovers part of the gap under the same evidence boundary; an inferability audit shows that remaining misses mix verifier failures with M1 evidence limits.

## Metadata
- **Published**: 2026-07-23T02:23:09Z
- **Authors**: Junchi Liao, Jiawen Deng, Fuji Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20852v1)