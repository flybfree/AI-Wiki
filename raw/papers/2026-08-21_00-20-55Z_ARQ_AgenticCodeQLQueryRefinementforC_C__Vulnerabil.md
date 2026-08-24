---
title: ARQ: Agentic CodeQL Query Refinement for C/C++ Vulnerability Detection
published: 2026-08-21T00:20:55Z
authors: Chunyi Wang, Yunfei Ke, Junfeng Yang, Yun-Yun Tsai, Penghui Li
url: http://arxiv.org/abs/2608.20637v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ARQ: Agentic CodeQL Query Refinement for C/C++ Vulnerability Detection

## Abstract
Static analyzers have been widely adopted for vulnerability detection in C/C++ programs. Query-based static analyzers (e.g., CodeQL) encode vulnerable code patterns in detection queries and match them against source code. However, existing queries still suffer from false positives (FPs, incorrectly flagging benign code as vulnerable) and false negatives (FNs, missing real vulnerabilities). We present ARQ, an agentic framework that automatically refines C/C++ CodeQL queries using execution-grounded evidence from synthesized C/C++ programs. Our key insight is that a synthesized program exposes a query's weakness whenever its execution disagrees with the query's verdict. If the program is genuinely vulnerable but the query stays silent, the query has an FN weakness; if the program is safe but the query fires anyway, it has an FP weakness. ARQ then runs an LLM-based refinement loop that repairs the query using these disagreements as ground truth. Unlike previous query refining methods, ARQ requires no labeled datasets, no commit history, and no vulnerability-specific templates. We demonstrate the effectiveness of ARQ by refining 12 official CodeQL queries using three commercial LLMs (GPT-5.4, Claude-Sonnet-4.6, and Gemini-3.5-flash). We compare both ARQ-refined and original CodeQL queries on the Juliet v1.3 and FormAI v2 datasets and show that ARQ-refined queries detect substantially more true positives, by up to 119.8\%, with a Precision of at least 98.0\% throughout. ARQ successfully fixed three unresolved GitHub issues raised in the official CodeQL query repository that had remained open for as long as \textit{27 months}. The refined queries also exposed two previously undiscovered bugs in the real-world libraries libpng and zlib.

## Metadata
- **Published**: 2026-08-21T00:20:55Z
- **Authors**: Chunyi Wang, Yunfei Ke, Junfeng Yang, Yun-Yun Tsai, Penghui Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20637v1)