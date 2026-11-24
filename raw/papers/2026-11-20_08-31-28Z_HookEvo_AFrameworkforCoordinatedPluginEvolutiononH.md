---
title: HookEvo: A Framework for Coordinated Plugin Evolution on Hook-Enabled Agent Runtimes
published: 2026-11-20T08:31:28Z
authors: Shengze Huang, Yanyu Mao, Xiaofei Yu, Baoshen Guo, Xiaorui Wang, Zhiwen Wu, Sheng Wu, Fukang Wen, Chengxu Wu, Linhao Li, Kailai Sun, Baotong Mi
url: http://arxiv.org/abs/2611.27294v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HookEvo: A Framework for Coordinated Plugin Evolution on Hook-Enabled Agent Runtimes

## Abstract
Repairing failures in tool-using agents can require coordinated changes to how the harness interprets tool receipts, assembles context, and checks actions. We introduce HookEvo, a framework that uses an existing agent runtime's lifecycle hooks to evolve task-specific harnesses. We instantiate HookEvo on DeepSeek Harness. In each round, a separate improver diagnoses failures from execution traces and proposes a candidate. HookEvo evaluates the candidate against the current harness on matched tasks and carries the retained version into the next round. A single candidate can jointly edit executable plugin handlers and the state they share within a task, allowing a tool receipt to inform context and control a later action. Using a frozen Qwen3-4B executor, the selected harnesses lead the reported Qwen3-4B comparisons, achieving 95.41% on ALFWorld, 70.56% on DBBench, 48.17% on WebShop, and 41.67% on OSBench. Across three improvers and three edit scopes, from skill text to single-component and coordinated executable edits, GPT-6.1 Sol shows the largest average gain from the broadest scope. Our code is available at https://huangshengzebluesky.github.io/hookevo/.

## Metadata
- **Published**: 2026-11-20T08:31:28Z
- **Authors**: Shengze Huang, Yanyu Mao, Xiaofei Yu, Baoshen Guo, Xiaorui Wang, Zhiwen Wu, Sheng Wu, Fukang Wen, Chengxu Wu, Linhao Li, Kailai Sun, Baotong Mi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.27294v1)