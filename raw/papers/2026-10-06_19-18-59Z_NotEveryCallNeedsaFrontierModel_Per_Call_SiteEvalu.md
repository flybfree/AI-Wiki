---
title: Not Every Call Needs a Frontier Model: Per-Call-Site Evaluation of Small Language Models in a Deployed Agentic Home-Automation System
published: 2026-10-06T19:18:59Z
authors: Panagiotis Kasnesis, Christos Chatzigeorgiou, Lazaros Toumanidis, Amalia Contiero Syropoulou
url: http://arxiv.org/abs/2610.09021v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not Every Call Needs a Frontier Model: Per-Call-Site Evaluation of Small Language Models in a Deployed Agentic Home-Automation System

## Abstract
An agentic system issues several structurally different kinds of LLM calls. It routes intent, classifies actions, grounds language in a device registry, plans multi-agent pipelines and writes the Python code those pipelines run. The difficulty of these call sites varies by an order of magnitude, yet in practice a single model, chosen for the hardest site, serves all of them. In this work, we evaluate 9 models from 0.8B to a frontier hosted model across the five call sites of a deployed open-source home-automation framework (Wactorz), using its unmodified production prompts and two real Home Assistant installations (280 cases, 2520 scored calls). We find that capability is not ordered the same way at every site, and that larger models are not uniformly better: one 4B model is worse than its 2B sibling at grounded actuation. Paired testing shows the best local model to be statistically indistinguishable from both hosted models at four of five sites. Only code generation separates them, against a small hosted model (p = 0.039) as well as a frontier one (p = 0.002). Aggregate accuracy also hides a safety failure specific to actuation, where small models resolve the accuracy/refusal trade-off in degenerate ways: one model (Gemma4 E2B) actuates on 87.2% of requests for devices the site does not own, while another refuses every request it receives. Routing each site to its best local model reaches 91.8% against 95.4% at no per-call cost. In a live deployment judged by a user, hosting only the two generative sites matches hosting everything (39/43 against 39/43) for 28% of the spend, and the actuation gap the benchmark predicted appears as exactly one case in twenty-six. Benchmark, harness and all records are released at https://github.com/waldiez/slm-callsite-eval.

## Metadata
- **Published**: 2026-10-06T19:18:59Z
- **Authors**: Panagiotis Kasnesis, Christos Chatzigeorgiou, Lazaros Toumanidis, Amalia Contiero Syropoulou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09021v1)