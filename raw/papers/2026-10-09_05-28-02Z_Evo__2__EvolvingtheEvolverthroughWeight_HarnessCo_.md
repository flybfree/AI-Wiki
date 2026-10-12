---
title: Evo$^2$: Evolving the Evolver through Weight-Harness Co-Evolution
published: 2026-10-09T05:28:02Z
authors: Chejian Xu, Shujian Zhang, Wenxuan Zhou, John Lambert, Beck Chen, Bo Li, Andrew Hard, Rajiv Mathews
url: http://arxiv.org/abs/2610.13025v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evo$^2$: Evolving the Evolver through Weight-Harness Co-Evolution

## Abstract
Self-evolving agents are increasingly used to improve language model systems without human intervention through either weight updates or harness improvements. Existing approaches typically pursue these directions separately: some methods update model weights using self-generated experience, while others rewrite the harness that defines how an agent uses prompts, tools, context, and execution feedback. However, these approaches overlook the relationship between model weights and the agent harness. To connect these processes and ensure effective and smooth agent self-evolving, we propose Evo$^2$, a framework for weight-harness co-evolution. For harness updates, we design a unified dual-role pipeline that a single policy serves as both a Proposer, which writes harness edits, and a Reflector, which diagnoses their effects and guides revision. For weight updates, harness modifications and their execution outcomes guide the training of both the Proposer and the Reflector. We further develop EvoTIDE, a training pipeline that recovers usable trajectories through edit extraction and prefix continuation, then combines SFT with interleaved GRPO across the two roles. Extensive experiments across three coding benchmarks demonstrate that Evo$^2$ significantly outperforms existing self-evolution methods. It achieves 82.1% on Polyglot and 48.3% on SWE-bench Verified, compared with 62.6% and 41.0% for the strongest baseline, respectively. We also show that the evolved harnesses transfer to different tasks without further evolution and rank first in cross-benchmark evaluations. Our dual-role harness improvement framework is also able to extend to self-evolution with proprietary models, improving a GPT-5-mini agent's performance from 24.4% to 48.3%. These results demonstrate the applicability of the framework Evo$^2$ across domains and its broad transferability across models and tasks.

## Metadata
- **Published**: 2026-10-09T05:28:02Z
- **Authors**: Chejian Xu, Shujian Zhang, Wenxuan Zhou, John Lambert, Beck Chen, Bo Li, Andrew Hard, Rajiv Mathews
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13025v1)