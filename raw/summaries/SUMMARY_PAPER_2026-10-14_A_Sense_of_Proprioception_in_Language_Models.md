---
title: A Sense of Proprioception in Language Models
url: http://arxiv.org/abs/2610.17495v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_23-35-16Z_ASenseofProprioceptioninLanguageModels.md
generated_at: 2026-10-14 01:06
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes a digital analog of proprioception for language models, drawing an analogy to the human sense of self-movement and body position. The author argues that because a model's internal states—such as which experts are activated in a mixture-of-experts layer—are inherently accessible and can be constructed into verifiable signals, they provide a foundation for training models to "sense" their own internal operations. Through supervised fine-tuning and on-policy training, the paper demonstrates that modern language models can be equipped with awareness of routing decisions, token entropy, decision depth, and logit lens information without degrading their core capabilities.

## Key Takeaways
- Proprioception in humans is a distinct sensory system with dedicated receptors and verifiable outcomes, separate from introspection. The paper carefully distinguishes this from self-reflection, establishing a rigorous framework for what "self-sensing" means before applying it to language models. This distinction matters because conflating proprioception with introspection leads to vague or unverifiable claims about model self-awareness.
- Language models cannot naturally observe their own internal states during training—for example, they cannot report which experts were activated in a specific MoE layer. However, because this information is internal to the model, it is both accessible and readily constructible into verifiable training signals. The paper leverages this by training models via SFT and on-policy methods to report on routing decision awareness, token entropy, decision depth, and logit lens information.
- The trained models are evaluated across a broad suite of tests covering situational awareness, legibility, and epiphenomenality. This evaluation framework assesses not just whether models can report internal states, but how access to proprioception changes model behavior in practice, distinguishing genuine internal sensing from superficial pattern matching.

## Context
Current interpretability research often treats model internals as opaque, requiring external tools like probes or logit lens analyses to inspect hidden states. This paper reframes the problem: rather than only external observers interpreting model internals, the model itself can be trained to sense and report on its own computational processes. This bridges interpretability research with model training methodology, suggesting that self-knowledge of internal states is not inherently incompatible with strong task performance. It also connects to broader discussions about introspection, self-awareness, and the limits of what language models can legitimately claim about their own cognition.

## Implications
For practitioners building MoE architectures or deploying models in safety-critical settings, training models to report on routing decisions and decision depth could provide a built-in monitoring mechanism that reduces reliance on external interpretability tooling. For the research community, the distinction between proprioception and introspection offers a more rigorous vocabulary for evaluating claims about model self-knowledge, potentially raising the bar for future "self-awareness" benchmarks. Industry teams may find that proprioception-trained models offer improved debuggability and transparency without sacrificing performance, which could influence how future model training pipelines incorporate self-monitoring objectives.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17495v1)
