---
title: Control the Harness, Control the Cost: Routing and Governing AI Coding Agents in the Enterprise
published: 2026-09-24T02:00:20Z
authors: Arian Abbasi, Alan Aqrawi, Ted Kwartler
url: http://arxiv.org/abs/2609.28919v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Control the Harness, Control the Cost: Routing and Governing AI Coding Agents in the Enterprise

## Abstract
Harnesses, the products that run AI coding agents, are multiplying, and enterprises are rolling them out to their employees: what started as pilots with a few hundred seats is scaling to tens of thousands. Most enterprises do not build these harnesses but buy them from large vendors, such as Anthropic's Claude Code or OpenAI's Codex. A harness decides which model answers, what the model reads, how the prompt cache is used and which subagents run, so it picks the rate on the price sheet and sets the volume bought at it. Enterprises that keep a proprietary or untuned harness at its defaults inherit these choices and their bill. We build a fast, customisable router in which Jev, a classifier with calibrated probabilities, labels every prompt against a bring-your-own taxonomy of agentic requests. Because one user turn is many requests over a prompt cache that belongs to one model, the router moves work only where no running conversation has to rebuild its cache: at session start, in side lanes and at subagent launch. From the price sheet we derive when a mid-task switch pays back, and a crossover: on long tool-heavy sessions the highest-priced model costs less than the next tier, as repricing about 10,000 real sessions from public datasets confirms. In an emulated enterprise of 10,000 seats with user behaviour taken from these datasets, the router recovers 14 to 21% of model spend at Anthropic's list prices of 21 September 2026, \$3.3M to \$5.0M a year. The paper also maps the risks across twenty harnesses, prices the dependence on one vendor's models, and proposes a control plane that enterprises can run from within, starting now, with a ladder for deciding later whether to own the harness.

## Metadata
- **Published**: 2026-09-24T02:00:20Z
- **Authors**: Arian Abbasi, Alan Aqrawi, Ted Kwartler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28919v1)