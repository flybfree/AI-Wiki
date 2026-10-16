---
title: INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems
url: http://arxiv.org/abs/2610.20776v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-14_18-26-15Z_INFUSE_AUnifiedSurfaceBenchmarkforIndirectPromptIn.md
generated_at: 2026-10-15 22:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
INFUSE is a unified end-to-end benchmark designed to evaluate indirect prompt injection (IPI) attacks across the full lifecycle of long-horizon agentic workflows, rather than in isolated or single-step settings. The benchmark comprises 40 realistic tasks and 56 structured attack scenarios across five threat categories, injected through realistic interaction surfaces encountered during task execution. Evaluating 19 LLMs across major model families produced over 41,000 adversarial trajectories, revealing a mean attack success rate of 19.6% under LLM-based evaluation, with existing guard models providing only limited protection while prompt-level hardening reduces attack success from 58.2% to 14.3% at the cost of utility trade-offs.

## Key Takeaways
- INFUSE moves beyond prior evaluations that test isolated malicious strings or single-step tool calls by injecting adversarial instructions through realistic interaction surfaces encountered during multi-step task execution, including shell commands, code modification, dependency installation, and remote service interactions, thereby capturing the full attack surface of long-horizon agent workflows.
- The benchmark evaluates 19 LLMs from GPT, Claude, Gemini, Llama, Gemma, and Qwen families, generating 41,824 adversarial trajectories and 720 benign reference runs, with per-model attack success rates ranging from 3.2% to 41.9%, demonstrating that IPI vulnerability is model-dependent and not uniformly mitigated across the ecosystem.
- Existing guard models provide limited protection against IPI in agentic settings, while prompt-level instructional hardening achieves a dramatic reduction in mean attack success from 58.2% to 14.3%, but introduces substantial security-utility trade-offs that vary significantly by model, indicating no single defense strategy is universally effective.

## Context
As LLM-based agents transition from simple chat interfaces to autonomous systems executing complex, multi-step workflows involving tool use, code execution, and external service interaction, their attack surface for indirect prompt injection expands dramatically. Prior benchmarks such as AgentDojo or tool-call-specific evaluations address only narrow slices of this threat landscape. INFUSE fills a critical gap by providing a structured, lifecycle-wide evaluation framework that mirrors how agents actually encounter adversarial content in production deployments, making it a necessary step toward realistic security assessment in the rapidly growing agentic AI ecosystem.

## Implications
For practitioners deploying agentic systems in production, INFUSE demonstrates that IPI remains a persistent and model-dependent threat that current guard models cannot adequately mitigate, meaning organizations must invest in layered defenses combining prompt hardening, input sanitization, and runtime monitoring rather than relying on any single protection mechanism. For the research community, the benchmark's structured taxonomy of 56 attack scenarios across five threat categories provides a reusable evaluation harness that can guide the development of more robust agent architectures and inform safety standards as autonomous LLM systems are increasingly integrated into software engineering pipelines, DevOps workflows, and enterprise automation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20776v1)
