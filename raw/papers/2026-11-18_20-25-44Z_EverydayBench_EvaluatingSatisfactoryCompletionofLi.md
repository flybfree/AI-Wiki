---
title: EverydayBench: Evaluating Satisfactory Completion of Live User-Facing Digital Work
published: 2026-11-18T20:25:44Z
authors: Fangrui Huang, Bingyang Wang, Chuhan Li, Yijiang Li, Arpandeep Khatua, Austin Shen, Riki R Z Choi, Cuiyuanxiu Chen, Jin Huang, Zachary Robertson, Kate Lin, Akshay Paruchuri, Sijun Tan, Xin Liu, Zhengmin Ni, Sanmi Koyejo, Ehsan Adeli
url: http://arxiv.org/abs/2611.25146v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EverydayBench: Evaluating Satisfactory Completion of Live User-Facing Digital Work

## Abstract
Everyday digital tasks, from selecting products and planning trips to conducting research and creating artifacts, require AI agents to deliver useful outcomes rather than merely retrieve web information. Yet evaluating these outcomes on the live web is challenging, as a single request may admit multiple valid results, and changing web information can alter which results remain valid over time. Although existing benchmarks address aspects of this setting, they do not fully integrate predefined success criteria, current evidence verification, and deliverable-quality assessment for agent-selected outcomes. To address this gap, we introduce EverydayBench, a benchmark of 77 human-authored tasks spanning eight domains of everyday life and work. Each task specifies success criteria before execution without prescribing an answer or workflow, allowing agents to select their own outcomes. To evaluate submissions under fixed success criteria, EverydayBench combines (1) deterministic checks of explicit constraints, (2) verification of claims against agent-cited webpages retrieved at evaluation time, and (3) rubric-based assessment of final deliverable quality. We further validate the protocol through human judgments, repeated scoring under fixed evidence, and controlled grounding failures. Across 23 reported agent-model configurations, Claude Opus 5.5 and Claude Fable 5.1 tie for the highest strict pass rate at 54.55%; a controlled GPT-6 Sol effort sweep ranges from 29.87% at low effort to 45.45% at max effort. Reliability varies substantially by task type: GPT-5.6 Sol leads lookup, Fable 5.1 leads planning, Opus 5.5 and Fable 5.1 tie on comparison, and GPT-6 Astra and Sonnet 5.5 tie on customized deliverables. Together, these findings highlight the difficulty of delivering complete, well-supported, and usable outcomes for everyday user requests.

## Metadata
- **Published**: 2026-11-18T20:25:44Z
- **Authors**: Fangrui Huang, Bingyang Wang, Chuhan Li, Yijiang Li, Arpandeep Khatua, Austin Shen, Riki R Z Choi, Cuiyuanxiu Chen, Jin Huang, Zachary Robertson, Kate Lin, Akshay Paruchuri, Sijun Tan, Xin Liu, Zhengmin Ni, Sanmi Koyejo, Ehsan Adeli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.25146v1)