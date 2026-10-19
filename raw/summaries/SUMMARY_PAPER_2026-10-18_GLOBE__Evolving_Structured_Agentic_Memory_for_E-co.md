---
title: GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization in Generative Search
url: http://arxiv.org/abs/2610.23709v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_16-33-17Z_GLOBE_EvolvingStructuredAgenticMemoryforE_commerce.md
generated_at: 2026-10-18 21:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces GLOBE, an agentic framework designed to optimize e-commerce product listings for generative search by maintaining an evolving, structured memory of optimization behaviors rather than relying on monolithic prompts. The framework cycles through an Editor, Reflector, Moderator, and Curator to transform episodic rank-based feedback into persistent, field-scoped optimization knowledge. Experiments demonstrate that structured behavioral memory outperforms traditional prompt-based optimization and that learned behaviors transfer effectively to unseen product categories.

## Key Takeaways
- GLOBE replaces implicit, prompt-embedded optimization strategies with an explicit "handbook" of field-scoped behaviors that accumulate across episodes, enabling continual self-improvement without retraining the underlying language model. Each behavior is scoped to a specific product field, making the memory interpretable and auditable rather than buried in free-form text or search trajectories.
- The framework employs a multi-agent pipeline where an Editor applies stored behaviors to rewrite listings, a Reflector converts rank-based performance feedback into candidate behavior updates, a Moderator filters out redundant or conflicting proposals, and a Curator commits only validated changes while deactivating consistently harmful behaviors. This governance structure reduces downside risk and prevents memory corruption over time.
- Empirical results show that structured behavioral memory significantly outperforms monolithic prompt optimization approaches, and the feedback-driven evolution cycle with moderation further improves effectiveness. Critically, behaviors learned on one product category remain effective on unseen categories, indicating that the agentic memory captures transferable optimization principles rather than category-specific tricks.

## Context
As generative search engines increasingly reshape how consumers discover products, the ability of language agents to iteratively refine structured product listings becomes a critical capability for e-commerce platforms. Prior work in prompt optimization and agentic self-improvement typically treats optimization knowledge as ephemeral, embedded within prompts or discarded after each episode. GLOBE addresses a gap in the agentic memory literature by formalizing how structured, domain-specific knowledge can be accumulated, validated, and governed within an autonomous agent loop, bridging the divide between one-shot prompt engineering and long-horizon continual learning.

## Implications
For practitioners in e-commerce and search optimization, GLOBE offers a path toward interpretable, auditable agent systems where optimization decisions are traceable to specific behavioral rules rather than opaque prompt mutations, which is essential for compliance, debugging, and trust in production environments. For the broader AI research community, the paper demonstrates that structured agentic memory with built-in moderation and curation mechanisms can outperform unconstrained self-improvement loops, suggesting that governance-aware memory architectures are a necessary component for deploying reliable autonomous agents in high-stakes commercial settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23709v1)
