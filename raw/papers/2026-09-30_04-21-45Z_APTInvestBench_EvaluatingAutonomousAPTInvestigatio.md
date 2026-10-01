---
title: APTInvestBench: Evaluating Autonomous APT Investigation under Varying Telemetry
published: 2026-09-30T04:21:45Z
authors: Yu Wang, Shuhao Li, Tao Yin, Ziyang Li, Xueying Zhao, Peishuai Sun, Jiang Xie
url: http://arxiv.org/abs/2609.38954v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# APTInvestBench: Evaluating Autonomous APT Investigation under Varying Telemetry

## Abstract
Large language model (LLM) agents could help security operations centers (SOCs) investigate advanced persistent threats (APTs) by turning weak leads into evidence for intrusion scoping and response. Yet success under one telemetry setting does not establish robustness to changes in log collection, retention, or sampling. We introduce APTInvestBench, a benchmark for evaluating cross-telemetry robustness in autonomous APT investigation. It comprises 370 cases across seven SOC-inspired conditions, derived from 56 report-informed attack reconstructions with 16.4 million log records. Agents investigate unverified leads and submit reports with record-level citations. Fixed action-level support requirements track sufficient evidence across available logs, query returns, and formal citations, separating telemetry limitations from acquisition and reporting gaps. Across eleven LLMs, agents acquire sufficient evidence for 44.3% of recoverable attack actions on average, while formal citations support only 25.0%. More importantly, aggregate coverage can conceal substantial instability: from Full to endpoint-only telemetry, coverage declines by only 1.6 percentage points, yet 35.5% of previously covered actions lose sufficient citation support despite remaining recoverable. Across four frameworks, such losses persist even when registered supporting records remain unchanged. APTInvestBench provides reusable investigation environments and diagnostic evaluation for identifying these gaps and developing more reliable defensive agents.

## Metadata
- **Published**: 2026-09-30T04:21:45Z
- **Authors**: Yu Wang, Shuhao Li, Tao Yin, Ziyang Li, Xueying Zhao, Peishuai Sun, Jiang Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38954v1)