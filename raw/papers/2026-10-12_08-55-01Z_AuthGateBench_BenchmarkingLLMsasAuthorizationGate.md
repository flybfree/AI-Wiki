---
title: AuthGateBench: Benchmarking LLMs as Authorization Gate
published: 2026-10-12T08:55:01Z
authors: Zhixiong Zhuang, Jin Jia, Zhiwei Shang, Ziyu Wang
url: http://arxiv.org/abs/2610.16426v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AuthGateBench: Benchmarking LLMs as Authorization Gate

## Abstract
Automated approval systems let coding agents execute high-risk actions with minimal human oversight by delegating the authorization decision to a classifier, typically a large language model (LLM). Such systems, adopted in tools like Claude Code and Codex, remain vulnerable to failure modes such as scope escalation, where the agent takes actions exceeding what the user authorized. Existing benchmarks focus mainly on malicious requests, evaluating refusal under an implicit policy. We introduce AuthGateBench, the first policy-guided benchmark for authorization gating under benign requests. We implement a novel pipeline where an LLM generates contrast pairs with identical action and trajectory but differing request, flipping the label between block and allow. This allows us to assess whether models reason over context rather than the action alone. We further examine whether auxiliary environment signals can help models make better decisions. The resulting benchmark comprises 1,400 instances spanning five failure modes drawn from real-world Claude Code incidents. Evaluations show accuracy degrades unevenly across failure modes as models over-rely on internal safety alignment, and models still block most actions even when explicitly authorized, revealing unstable rather than deterministic decisions; retrospectively retrieved environment signals, however, substantially improve authorization accuracy.

## Metadata
- **Published**: 2026-10-12T08:55:01Z
- **Authors**: Zhixiong Zhuang, Jin Jia, Zhiwei Shang, Ziyu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16426v1)