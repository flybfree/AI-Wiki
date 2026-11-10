---
title: Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs
url: http://arxiv.org/abs/2611.10258v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-06_21-46-25Z_BeyondthePrompt_LeveragingPre_DecodingStatesforJai.md
generated_at: 2026-11-09 21:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ReFuse (Representation Fusion), a lightweight inference-time jailbreak detector for diffusion large language models (dLLMs) that leverages hidden states over masked response positions before any tokens are generated. The authors demonstrate that dLLMs' unique architecture—bidirectional conditioning and parallel masked-token refinement—creates a safety-relevant detection surface absent from autoregressive models, and that fusing prompt-based and pre-decoding response-based classifiers yields substantially stronger jailbreak detection than either approach alone.

## Key Takeaways
- dLLMs expose a novel detection surface: even when a jailbreak is difficult to identify from prompt representations alone, it can be detected from hidden states over masked response positions before any tokens are generated. This is a property unique to the parallel, bidirectional refinement process of diffusion-based generation, and it does not exist in standard autoregressive decoding pipelines.
- Neither prompt-only nor response-only classifiers strictly dominate the other. The authors empirically show that each view detects attacks the other misses, motivating the fusion approach. ReFuse combines sigmoid harmfulness scores from two linear classifiers trained on prompt representations and pre-decoding response representations, respectively, without modifying model weights or the decoding procedure.
- On LLaDA-8B, ReFuse reduces average Attack Success Rate (ASR) across multiple jailbreaks from 63.29% for the undefended model and 11.27% for a prompt-only classifier down to 3.31%, while keeping average benign refusal on standard utility benchmarks below 1%. This demonstrates that the detector adds meaningful safety without degrading model utility.

## Context
As diffusion large language models such as LLaDA gain traction as alternatives to autoregressive transformers, their distinct generation mechanics introduce new attack surfaces that existing safety tools—designed around sequential token-by-token decoding—cannot adequately address. This paper is among the first to systematically exploit dLLM-specific internal representations for safety monitoring, bridging a gap between the rapidly growing dLLM ecosystem and the need for practical, deployable jailbreak defenses.

## Implications
For practitioners deploying dLLMs in production, ReFuse offers a plug-in safety layer that requires no retraining, no architectural changes, and negligible computational overhead, making it immediately applicable to existing dLLM deployments. More broadly, the finding that pre-decoding masked-state representations carry safety-relevant signals suggests a new class of detection tools for any model with parallel or iterative refinement architectures, potentially reshaping how safety monitoring is designed for next-generation language models beyond autoregressive paradigms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.10258v1)
