---
title: On the Effectiveness of Kernel-Level Evidence for Agent Security
published: 2026-09-24T01:46:57Z
authors: Spencer King, Zhilu Zhang, Mikhail Kuznetsov, Kay Liu, Baris Coskun, Wei Ding
url: http://arxiv.org/abs/2609.28915v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Effectiveness of Kernel-Level Evidence for Agent Security

## Abstract
LLM agents are deployed into infrastructure that grants them broad host authority, yet existing agent-security benchmarks and defenses operate almost exclusively at the application telemetry layer: the served tool manifest, the user prompt, and the model's messages. Some threats, however, smuggle malicious instructions and actions past the application boundary, leaving them invisible to that layer. In this work, we bridge that gap by pairing application-level agent telemetry with kernel-level syscall traces to present the first paired-evidence characterization of kernel-level versus application-layer signal for agent security. To quantify the value of the enhanced telemetry, we introduce Agent Cross-Layer Evidence (ACE), a paired-session corpus of 4,047 sessions and 17 threat models spanning six delivery-vector families and 14 of the 25 OWASP LLM and agentic threat categories, organized into 12 attack mechanics with per-mechanic characterization of where the most discriminative evidence lies. Across four distinct detector families, we find that kernel evidence is discriminative on its own and that composing it with application-layer evidence generally outperforms either single-layer view, revealing complementary signals that single-layer analyses can miss. We further demonstrate generalization to unseen attack families and transfer to an alternate agent runtime. Together, these findings establish the value of cross-layer evidence for agent security.

## Metadata
- **Published**: 2026-09-24T01:46:57Z
- **Authors**: Spencer King, Zhilu Zhang, Mikhail Kuznetsov, Kay Liu, Baris Coskun, Wei Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28915v1)