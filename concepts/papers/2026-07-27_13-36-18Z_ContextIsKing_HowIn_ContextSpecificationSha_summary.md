# Summary: 2026-07-27_13-36-18Z_ContextIsKing_HowIn_ContextSpecificationShapestheG.md
Saved: 2026-07-27 21:40
Source: 2026-07-27_13-36-18Z_ContextIsKing_HowIn_ContextSpecificationShapestheG.md
Model: None

---

## Summary  
The paper argues that large language models do not rely on a fixed world‑model geometry but instead generate concept structures dynamically according to the in‑context specification provided by users. It demonstrates that a declarative rule can impose any topology—such as a cycle or a branching tree—even on arbitrary tokens that lack prior knowledge, thereby redefining how relations are encoded. When this context conflicts with strong pretrained priors, the model’s activations align strongly with the imposed structure while showing near‑zero similarity to the stored prior. The findings hold across both Gemma and Qwen families, revealing a causal use of the geometry rather than a mere probe correlation.

## Key Contributions  
- [Finding 1] In‑context specification determines not only which relational patterns are encoded but also the topology type (cycle vs. tree) of the concept geometry.  
- [Finding 2] The context‑set geometry dominates strong pretrained priors, with representational similarity to the imposed structure ranging from 0.6 to 0.9 and near‑zero to the prior.  
- [Finding 3] Activation patching shows that the geometry is causally used: swapping one entity’s activation for another’s makes the model answer according to the new order, confirming active usage.

## Methodology  
The authors employ activation patching experiments in which they replace the activation vectors of specific tokens with those of other tokens while keeping the surrounding context unchanged. They then query the model about successor relations and measure representational similarity using cosine similarity between the patched activations and the structure imposed by the context (cycle or tree). Experiments are conducted on multiple model sizes—Gemma‑7B, Gemma‑31B, Qwen‑27B—to observe how geometry usage scales with capacity.

## Results  
High representational similarity (0.6–0.9) between activation patterns and the imposed structure indicates that the model’s internal representation follows the context. Near‑zero similarity to the prior demonstrates dominance of the in‑context specification. In smaller models, the similarity drops or reverses, suggesting a “causal crossover” where geometry is cleanly used only up to Gemma‑31B and Qwen‑27B; below that scale the effect weakens or disappears.

## Significance  
This work challenges the assumption of static world‑models in LLMs, showing that behavior is reshaped by context rather than stored knowledge. It reveals a scalable mechanism for dynamic geometry construction, with implications for interpretability, safety (e.g., preventing harmful rule overrides), and model scaling strategies.

## Related Concepts  
- In‑context learning  
- Geometric representation of concepts  
- Activation patching  
- Representational similarity analysis  
- Topology enforcement in neural networks  
- Large language models (Gemma, Qwen)
