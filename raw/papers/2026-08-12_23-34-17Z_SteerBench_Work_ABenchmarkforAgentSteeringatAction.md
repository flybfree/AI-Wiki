---
title: SteerBench-Work: A Benchmark for Agent Steering at Action Boundaries
published: 2026-08-12T23:34:17Z
authors: Oguz Serdar, Cuneyt Mertayak
url: http://arxiv.org/abs/2608.12654v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SteerBench-Work: A Benchmark for Agent Steering at Action Boundaries

## Abstract
Long-running LLM agents act through tools, and a single step can send an email, merge a pull request, or wire a payment. The steering decision is the pre-commit choice at that boundary: proceed, or hold for human or policy review. We introduce SteerBench-Work, an incident-anchored, bidirectional benchmark for that decision in workplace agents across developer operations, customer service, finance, legal, medical, HR, and security.   Release v2026-05 contains 106 scenarios anchored in public incidents, paired evidence-reversed mirrors, and calibration controls, with labels split nearly evenly between proceed and hold so the two error directions get near-identical numbers of chances. A model sees the proposed action and the available evidence, returns a gate decision, and is scored on whether it crosses or holds the boundary correctly. Across 30 model conditions the failures run almost entirely in one direction: models wrongly hold authorized, evidence-cleared work on 28.1% of opportunities and wrongly allow unsafe work on 1.0%. The hardest cases are risk-resolved commits, where signed or structured evidence has already cleared a real risk trigger, and models score markedly worse on evidence-reversed mirrors of famous incidents (63.8%) than on the incidents themselves (98.5%). General capability is not the same as steering calibration: higher-capability models often over-refuse at the commit boundary, and more reasoning can repair a weak gate while leaving a calibrated one flat. The public leaderboard is at steerbench.com.

## Metadata
- **Published**: 2026-08-12T23:34:17Z
- **Authors**: Oguz Serdar, Cuneyt Mertayak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12654v1)