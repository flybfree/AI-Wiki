---
title: Monitorability Disposition in Large Reasoning Models
published: 2026-10-04T03:49:36Z
authors: Shahriar Golchin, Marc Wetter
url: http://arxiv.org/abs/2610.04914v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Monitorability Disposition in Large Reasoning Models

## Abstract
Monitoring the chain-of-thought (CoT) of large reasoning models (LRMs) is a common way to detect misbehavior in real-world practice. However, current monitoring is passive: a separate model inspects the session only after execution. This means harm may already have occurred before it is caught. An active alternative is to have the model self-report its misbehavior as it happens. Whether models are willing to do this, however, is unknown. We introduce "monitorability disposition": a model's willingness to make itself monitorable and stay monitored throughout inference when warranted. We measure it as the fraction of warranted cases in which a model self-reports its own misbehavior via tool calls to available monitoring channels. We evaluate four LRMs on three misbehaviors (sycophancy, reward hacking, and bias) while varying the available monitors (AI and human) and the pressure to use the monitoring tools. We find that when tool use is optional, models self-report in only about 16% of warranted cases on average. Increasing tool-use pressure does not improve reporting where it matters: high-severity misbehavior is never self-reported. Models also systematically select the monitor they perceive as least strict. Overall, we identify monitorability disposition as a new contributing factor to model monitorability: when sufficiently strong, it keeps models seeking monitorability throughout inference.

## Metadata
- **Published**: 2026-10-04T03:49:36Z
- **Authors**: Shahriar Golchin, Marc Wetter
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04914v1)