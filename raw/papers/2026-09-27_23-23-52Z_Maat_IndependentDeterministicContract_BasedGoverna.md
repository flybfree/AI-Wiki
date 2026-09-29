---
title: Maat: Independent Deterministic Contract-Based Governance for Multi-Agent LLM Workflows
published: 2026-09-27T23:23:52Z
authors: Uliana Elina
url: http://arxiv.org/abs/2609.34017v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Maat: Independent Deterministic Contract-Based Governance for Multi-Agent LLM Workflows

## Abstract
Large-language-model multi-agent systems (LLM-MAS) introduce a characteristic reliability problem: an error produced by one agent can be accepted as context by downstream agents and propagate across the workflow. Many proposed safeguards rely on learned or LLM-based judges whose verdicts are themselves probabilistic; we ask whether a deterministic layer can instead stop contract-detectable handoff defects. We present Maat, a runtime governance layer that validates agent-to-agent handoffs against a versioned workflow contract, or anchor, with no language model in the validation or scoring path. We evaluate it in six controlled domain workflows (6-15 agents, 522 trials) with injected data-level defects and a deterministic seven-check rubric. Version 1 reported gains in all six workflows (2.9-26.5%). A post-publication audit found that three benchmark scorers credited any early halt as a prevented defect. On paired trials where the governed run completed or halted on a finding attributable to a verified defect, the rubric score changes by +7.7% to +29.1% in five workflows and is flat in software development; model-call cost falls 17-53% where attributable halts occur early. A hand review of all 94 governed-arm halts found 35 false alarms (37%), caused by validator defects rather than model behaviour; counting those halts as failed work, the governed arm scores below the ungoverned arm in four of six workflows. The results support deterministic handoff validation for contract-expressible defects and show that validator configuration and halt attribution must themselves be tested; they do not establish universal correctness, hallucination detection, or model-independent effectiveness.

## Metadata
- **Published**: 2026-09-27T23:23:52Z
- **Authors**: Uliana Elina
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34017v1)