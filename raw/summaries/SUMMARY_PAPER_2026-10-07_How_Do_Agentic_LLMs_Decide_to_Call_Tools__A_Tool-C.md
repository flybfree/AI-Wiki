---
title: How Do Agentic LLMs Decide to Call Tools? A Tool-Call Vector Shaped by Suppression
url: http://arxiv.org/abs/2610.09624v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_08-01-39Z_HowDoAgenticLLMsDecidetoCallTools_ATool_CallVector.md
generated_at: 2026-10-07 21:13
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the mechanistic basis of tool-calling decisions in agentic LLMs by isolating a single controllable variable within complex, heavily scaffolded prompts. The authors discover that a compact internal vector, denoted μ_Δ, is both causally necessary and sufficient to determine whether a model invokes an external tool or responds directly, and this mechanism generalizes across multiple programming languages, multi-turn benchmarks, and seven different model families.

## Key Takeaways
- The authors introduce a contrastive-pair methodology that reduces noisy agentic prompts to minimal pairs where swapping a single request verb (e.g., "write" versus "discuss") reliably flips the tool-call decision, revealing that the decision is mediated by a compact internal state rather than distributed across the entire scaffolded context. They construct 500 such paired prompts across Python, Java, and C++, with 300 used for mechanistic analysis and 200 held out for evaluation.
- Behavioral ablations demonstrate that the agentic scaffold establishes a tool-call prior, and Transcoder decomposition shows that analysis verbs suppress this prior through features signaling that tool use is unnecessary, while execution verbs largely leave the prior intact. Downstream scaffold-reading attention heads and MLP features then read out the resulting state, confirming a clear causal pathway from verb choice to tool-call output.
- The discovered μ_Δ vector generalizes beyond the discovery prompts to native multi-turn τ²-Bench trajectories and verb-free requests, and the same suppression mechanism recurs across seven models from the Qwen, Mistral, and Granite families, indicating a shared architectural basis for tool-calling decisions across diverse model architectures.

## Context
Agentic LLMs rely on tool calling as a core capability, yet the internal decision process that determines whether a model invokes a tool or generates a direct response has remained poorly understood due to the entangled nature of long, scaffolded prompts. This paper addresses a fundamental gap in mechanistic interpretability by providing the first causal identification of a tool-call decision vector within agentic LLMs, bridging the gap between behavioral observations of tool use and the internal representations that drive those behaviors.

## Implications
For practitioners building agentic systems, understanding that a compact internal vector governs tool-call decisions opens pathways for targeted interventions, such as steering models toward or away from tool use without retraining, and for auditing whether scaffolded prompts inadvertently bias models toward unnecessary tool invocations. For the broader AI safety and reliability community, the cross-model generalization of the suppression mechanism suggests that tool-call behavior can be systematically analyzed and controlled across model families, which is critical for deploying trustworthy autonomous agents in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09624v1)
