---
title: "2026 05 09 131500Z React Synergizingreasoningandactinginlanguagemodels"
date: 2026-05-09
tags: ['paper', 'research', 'ai']
---
title: 'ReAct: Synergizing Reasoning and Acting in Language Models'
source_arxiv: https://arxiv.org/abs/2210.03629
source_pdf: https://arxiv.org/pdf/2210.03629
source_pdf_local: /home/rich/wiki/raw/papers/2026-05-09_ReAct_SynergizingReasoningAndActing.pdf
source_code: https://react-lm.github.io
authors: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
venue: ICLR 2023 (v3 camera-ready)
date: 2026-05-09
tags: [reasoning, acting, agentic, LLM, chain-of-thought, tool-use, HOTPOTQA, ALFWORLD, WEBSHOP]

# ReAct: Synergizing Reasoning and Acting in Language Models



**Source**: [Original Paper](https://arxiv.org/abs/2210.03629)
## Source
- Paper: [[https://arxiv.org/abs/2210.03629|arXiv:2210.03629]]
- PDF: [[https://arxiv.org/pdf/2210.03629|PDF]]
- Project site / code: [[https://react-lm.github.io|react-lm.github.io]]
- Venue: ICLR 2023 (camera-ready v3, Mar 2023)

## Summary

ReAct addresses a fundamental limitation in earlier LLM research: **reasoning** (e.g., chain-of-thought / CoT) and **acting** (e.g., action-plan / tool-use generation) had been studied as separate paradigms. This paper shows they are deeply synergistic when combined in an **interleaved** pattern within the LLM's generation.

The core insight: reasoning traces and actions reinforce each other. Reasoning helps the model induce, track, and update action plans, plus handle exceptions. Actions let the model interface with external sources (knowledge bases, environments) to gather information it can then reason about. This interleaving -- ReAct style -- creates a loop:

```
Thought → Action → Observation → Thought → Action → ... → Answer
```

where "Thought" is the reasoning trace and "Action" is the tool/environment interaction, with "Observation" being the external feedback.

## Semantic links
- [[concepts/reasoning/reasoning-hub.md|Reasoning and Inference Hub]] — 2 title terms overlap; 160 backlinks; 4 summary/topic terms overlap
- [[concepts/papers/2026-06-17_17-54-04Z_RethinkingRewardSupervision_Rubric_Conditio_summary.md|Summary: 2026-06-17_17-54-04Z_RethinkingRewardSupervision_Rubric_ConditionedSelf.md]] — 1 title term overlap; shared tags: ai, paper, research; 7 summary/topic terms overlap
- [[concepts/papers/2026-06-11_17-59-36Z_SpatialClaw_RethinkingActionInterfaceforAge_summary.md|Summary: 2026-06-11_17-59-36Z_SpatialClaw_RethinkingActionInterfaceforAgenticSpa.md]] — 1 title term overlap; shared tags: ai, paper, research; 9 summary/topic terms overlap

## Key Contributions

1. **Re_act protocol**: An interleaved reasoning+action generation strategy (not just reasoning chains, not just direct action, a hybrid)
2. **Overcoming hallucination**: On HotpotQA and Fever, ReAct reduces hallucination and error propagation -- common failure modes in pure CoT -- by grounding reasoning in external facts retrieved via a Wikipedia API
3. **Few-shot efficiency**: On both language (HOTPOTQA, FEVER) and decision-making (ALFWorld, WebShop) benchmarks, one or two in-context examples are sufficient
4. **Improved interpretability**: The interleaved Thought+Action sequences produce traceable, human-like task-solving trajectories that are more interpretable than pure-CoT baselines

## Benchmark Results

- **HOTPOTQA** (question answering): Outperforms state-of-the-art baselines; overcomes hallucination by interacting with a Wikipedia API during reasoning
- **FEVER** (fact verification): Same advantage -- grounds claims in external evidence as reasoning unfolds
- **ALFWorld** (interactive decision-making): +34% absolute success rate over imitation/RL methods
- **WebShop** (interactive decision-making): +10% absolute success rate over imitation/RL methods

## Why This Matters for Agentic Systems

The Re_act framework is arguably the **architectural foundation** of the modern agentic AI paradigm:

- It formalizes the "thought-action-observation" loop that underlies today's agent architectures (ReAct-style agents, CoT-CoA, Plan-and-Execute, etc.)
- It shows that reasoning *during* action is more effective than reasoning *before* action or action *without* reasoning
- It provides the blueprint for tool-using agents that must gather information dynamically while deciding what to do next
- It connects directly to the CourseDesigner AI/ML Foundations curriculum -- Lesson 13 on Agentic Workflows

## Key Takeaways

1. **Synergy is real**: Interleaved reasoning+action outperforms both pure-CoT and pure-action approaches
2. **Few-shot works**: One or two examples are enough to bootstrap Re_act behavior
3. **External grounding beats internal reasoning alone**: Even simple Wikipedia API access dramatically reduces hallucination
4. **Interpretability as a side benefit**: The interleaved trajectories reveal *how* the model thinks, not just *what* it decides

## Related Concepts
- [[../concepts/prompting/prompting-hub.md|Prompting]]
- [[../concepts/reasoning/reasoning-hub.md|Chain of Thought]]
- [[2026-05-09_131500Z_ReAct_SynergizingReasoningAndActingInLanguageModels.md|ReAct]]
- Agentic Workflows (CourseDesigner Lesson 13)
- Tool Use / Function Calling
