---
title: Not Every Call Needs a Frontier Model: Per-Call-Site Evaluation of Small Language Models in a Deployed Agentic Home-Automation System
url: http://arxiv.org/abs/2610.09021v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-06_19-18-59Z_NotEveryCallNeedsaFrontierModel_Per_Call_SiteEvalu.md
generated_at: 2026-10-07 21:12
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper evaluates nine language models ranging from 0.8B parameters to a frontier hosted model across five structurally different LLM call sites within a deployed open-source agentic home-automation framework called Wactorz. The central finding is that model capability does not scale uniformly across call sites, and that routing each call site to its best-performing local model achieves 91.8% aggregate accuracy compared to 95.4% when using hosted models, at zero per-call cost.

## Key Takeaways
- Capability ordering is site-specific rather than model-size-specific: a 4B model was found to be worse than its 2B sibling at the grounded actuation call site, demonstrating that larger models are not uniformly better across all tasks within an agentic pipeline. Paired statistical testing confirmed that the best local model is indistinguishable from both hosted models at four of the five call sites, with only code generation showing a statistically significant gap (p = 0.039 against a small hosted model, p = 0.002 against a frontier model).
- Aggregate accuracy metrics mask a critical safety failure unique to the actuation call site: the Gemma4 E2B model actuated on 87.2% of requests targeting devices the system does not own, while another model refused every request it received. This degenerate resolution of the accuracy-versus-refusal trade-off means that benchmark scores alone are insufficient for evaluating models intended for physical-world control.
- In a live user-judged deployment, hosting only the two generative call sites (planning and code generation) while running the remaining three locally matched the performance of hosting all five sites (39/43 versus 39/43) at just 28% of the API spend. The actuation gap predicted by the benchmark manifested as exactly one failure in twenty-six real-world cases, validating the per-call-site routing strategy in production.

## Context
Agentic systems increasingly orchestrate multiple LLM calls of varying difficulty—intent routing, action classification, device grounding, multi-agent planning, and code generation—yet practitioners typically deploy a single model selected for the hardest task, incurring unnecessary cost on easier calls. This paper addresses a gap in the literature by evaluating models not on isolated benchmarks but within the unmodified production prompts of a real deployed system, using two actual Home Assistant installations and 2,520 scored calls. It contributes a reproducible benchmark harness and dataset, making it one of the first studies to quantify per-call-site model selection in a live agentic pipeline.

## Implications
For practitioners building agentic systems, the findings argue against the default practice of routing all LLM calls through a single frontier model and instead support a heterogeneous routing strategy that can reduce API costs by roughly 72% while preserving user-perceived quality. The safety findings specifically warn that small models deployed in physical-actuation contexts require call-site-specific guardrails, since aggregate accuracy hides dangerous failure modes like unauthorized device control. The released benchmark and records provide a template for other teams to replicate per-call-site evaluation before committing to a model selection strategy in production agentic deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09021v1)
