---
title: HookEvo: A Framework for Coordinated Plugin Evolution on Hook-Enabled Agent Runtimes
url: http://arxiv.org/abs/2611.27294v1
type: paper-summary
date: 2026-11-23
source_paper: 2026-11-20_08-31-28Z_HookEvo_AFrameworkforCoordinatedPluginEvolutiononH.md
generated_at: 2026-11-23 21:27
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
HookEvo is a framework that leverages an existing agent runtime's lifecycle hooks to iteratively evolve task-specific harnesses for tool-using agents. By using a separate improver to diagnose failures from execution traces and propose coordinated edits to executable plugin handlers and their shared state, HookEvo enables a single candidate to jointly modify how tool receipts inform context and control subsequent actions. Evaluated with a frozen Qwen3-4B executor, the evolved harnesses achieve state-of-the-art results across ALFWorld, DBBench, WebShop, and OSBench, demonstrating that coordinated multi-component edits yield the largest performance gains.

## Key Takeaways
- HookEvo operates by iteratively evolving a harness through lifecycle hooks of an agent runtime (instantiated on DeepSeek Harness). Each round, a separate improver analyzes execution traces to diagnose failures and proposes a candidate harness modification. The candidate is evaluated against the current harness on matched tasks, and only the retained version carries forward, creating a principled evolutionary loop for harness improvement.
- A critical architectural innovation is that a single candidate can jointly edit executable plugin handlers and the shared state they maintain within a task. This allows a tool receipt to simultaneously inform context assembly and control a later action, enabling coordinated changes across multiple harness components rather than isolated single-component edits. This coordination is what distinguishes HookEvo from simpler prompt-tuning or single-plugin approaches.
- The experimental evaluation reveals a clear hierarchy of edit scope effectiveness: from skill text modifications to single-component edits to coordinated executable edits, broader scopes yield larger gains. Using a frozen Qwen3-4B executor, the selected harnesses achieve 95.41% on ALFWorld, 70.56% on DBBench, 48.17% on WebShop, and 41.67% on OSBench. Among three improvers tested, GPT-6.1 Sol produces the largest average gain when given the broadest edit scope, suggesting that more capable improvers benefit disproportionately from coordinated editing freedom.

## Context
This paper sits at the intersection of agent harness engineering, automated program repair, and evolutionary optimization for LLM-based tool-using agents. As agents increasingly rely on complex multi-step tool interactions across environments like embodied tasks, databases, web navigation, and operating systems, the harness—the scaffolding that interprets tool outputs, assembles context, and gates actions—becomes a critical performance bottleneck. HookEvo addresses this by treating the harness as an evolvable software artifact rather than a fixed configuration, building on prior work in prompt optimization and agent scaffolding but extending it to coordinated executable edits within a hook-enabled runtime.

## Implications
For practitioners building production agent systems, HookEvo demonstrates that harness-level optimization can yield substantial benchmark gains without retraining or modifying the underlying model, making it a practical lever for improving agent reliability in deployment. The finding that coordinated multi-component edits outperform isolated single-component changes suggests that future agent frameworks should expose richer hook interfaces and allow improvers to operate across handler boundaries. For the broader field, this work signals a shift toward treating agent scaffolding as a first-class optimization target, potentially accelerating the development of self-improving agent systems that adapt their own tool-use logic to new task domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.27294v1)
