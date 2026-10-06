---
title: TrustMI: Causally controlling how assistants trust their users
url: http://arxiv.org/abs/2610.06064v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-05_09-56-52Z_TrustMI_Causallycontrollinghowassistantstrusttheir.md
generated_at: 2026-10-05 22:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces TrustMI, a framework for causally controlling how large language model assistants decide whether to trust their users. The authors construct 2,000 contrastive conversation pairs spanning ability, benevolence, and integrity dimensions, then learn steering matrices that shift trust decisions monotonically in both directions across six instruction-tuned models from three different families. The findings demonstrate that trust behavior can be causally manipulated along linear directions in model activations, extending to safety-relevant agent settings including harmful requests, prompt injections, and insider threats.

## Key Takeaways
- Trust is formally defined as an assistant's willingness to accept vulnerability to another party's actions, and the authors show this behavior is not merely a surface-level output pattern but is causally encoded in model activations that can be steered through learned matrices while keeping all model parameters frozen. This means trust decisions are not fixed by fine-tuning but can be dynamically modulated at inference time.
- The experimental design uses 2,000 contrastive conversation pairs where paired responses complete the same request but differ in whether the assistant trusts the user, spanning three trust dimensions (ability, benevolence, integrity). Steering matrices learned from these pairs produce monotonic changes in trust decisions across six models from three families, demonstrating generalizability of the causal control mechanism.
- The causal control of trust extends beyond simple conversational trust to safety-critical agent scenarios including compliance with harmful requests, vulnerability to prompt injection attacks, and susceptibility to insider threats, with benign-task and reasoning controls confirming the effect is specific to trust rather than general capability changes.

## Context
This work sits at the intersection of mechanistic interpretability and AI safety, addressing a fundamental question about how LLM-based agents make trust judgments when they cannot verify the competence, intentions, or integrity of users and third parties encountered during tool use. As LLM assistants increasingly operate as autonomous agents interacting with external tools, APIs, and multi-party workflows, their trust calibration directly determines whether they comply with harmful instructions or act on malicious injected content. The paper contributes to the growing field of activation steering and causal control in language models by extending it from stylistic or factual editing to a nuanced social-cognitive behavior like trust.

## Implications
For practitioners building agentic AI systems, TrustMI offers a practical mechanism to adjust trust calibration without retraining models, enabling deployment-time safety tuning that could reduce compliance with harmful requests or susceptibility to prompt injection attacks. For the research community, the demonstration that trust is linearly steerable in activation space provides a new experimental tool for studying how trust shapes safety-relevant behavior, potentially informing future alignment methods that go beyond instruction-following to address the social dynamics of human-AI interaction.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06064v1)
