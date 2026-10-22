---
title: ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination
url: http://arxiv.org/abs/2610.29934v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_16-05-54Z_ToM2Vec_ContinuousTheory_of_MindTokensforMulti_Age.md
generated_at: 2026-10-21 23:07
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ToM2Vec introduces a method for multi-agent coordination in which agents learn to form abstract theories-of-mind through a fixed budget of continuous reasoning tokens embedded in a latent space, rather than relying on text-based descriptions of a single partner state. The approach is trained by supervising these latent tokens against the partner's actual thoughts and evaluated across collaborative, competitive, and mixed-motive environments, demonstrating consistent improvements over base models and competitive baselines while generalizing to partner models unseen during training, including proprietary systems like GPT-5.4.

## Key Takeaways
- ToM2Vec addresses a fundamental limitation of LLM-based agents: text representations naturally describe a single partner state, making it difficult to reason under uncertainty about multiple possible partner mental states. By introducing continuous latent reasoning tokens, the system captures the richness of multiple possible partner states in a structured, abstract form that text-based reasoning cannot easily replicate.
- The training mechanism is distinctive: supervision for the ToM tokens comes directly from the partner's actual thoughts, which the tokens are trained to abstract and match. At inference time, these generated tokens act as conditioners for the agent's own thoughts and actions, creating a pipeline where understanding the partner directly shapes one's own behavior.
- The paper provides strong evidence that latent reasoning is critical to performance. When reasoning is forced into text form, performance drops significantly. Furthermore, the latent tokens are shown to encode genuine theory-of-mind information rather than task-specific shortcuts, as they improve the agent's ability to directly answer questions about partner beliefs, desires, and next actions across diverse environments including Overcooked-AI, multiparty negotiation, Decrypto, Hanabi, and Collab Escape/Capture.

## Context
This work sits at the intersection of multi-agent systems, latent reasoning in large language models, and cognitive science-inspired modeling of mental states. As LLM agents increasingly interact with one another in collaborative and competitive settings, the ability to model what a partner is thinking, wanting, or planning becomes a bottleneck for effective coordination. Prior approaches have relied on prompting strategies or text-based chain-of-thought reasoning to approximate theory-of-mind, but these struggle with the combinatorial complexity of representing multiple possible partner states. ToM2Vec represents a shift toward structured latent reasoning as a mechanism for social cognition in artificial agents, building on growing interest in continuous reasoning tokens and internal representations that go beyond surface-level text generation.

## Implications
For practitioners building multi-agent systems, ToM2Vec suggests that investing in latent-space reasoning architectures can yield more robust coordination than text-prompting approaches, particularly in environments where partner behavior is uncertain or adversarial. The demonstrated generalization to unseen partner model families, including proprietary models like GPT-5.4, indicates that such latent ToM representations could serve as a transferable coordination layer across heterogeneous agent ecosystems. For the broader field, the finding that text-expressed reasoning degrades performance while latent reasoning improves it challenges the prevailing assumption that explicit chain-of-thought is the optimal path to complex reasoning, opening new directions for how AI systems model social and strategic cognition.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29934v1)
