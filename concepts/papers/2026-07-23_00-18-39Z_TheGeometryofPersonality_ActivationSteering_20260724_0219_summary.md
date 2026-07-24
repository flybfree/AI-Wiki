# Summary: 2026-07-23_00-18-39Z_TheGeometryofPersonality_ActivationSteeringwithJun.md
Saved: 2026-07-24 02:19
Source: 2026-07-23_00-18-39Z_TheGeometryofPersonality_ActivationSteeringwithJun.md
Model: None

---

## Summary  
This paper proposes a novel framework that treats personality not as static trait vectors but as dynamic activation steering across eight Jungian cognitive functions within large language models (LLMs). By applying activation‑steering techniques to Llama‑3.1‑8B, the authors demonstrate monotonic control over all functions and uncover a geometric structure in the resulting steering vectors. The work bridges personality theory with LLM interpretability, offering a new lens for multi‑dimensional character modeling.

## Key Contributions  
- [Finding 1] Personality information is concentrated in middle transformer layers, suggesting that higher‑level cognitive processes are encoded there rather than at surface token embeddings.  
- [Finding 2] Steering vectors exhibit structured geometric relationships that align with the rational versus irrational dichotomy of Jungian functions, indicating a consistent spatial ordering across the eight dimensions.  
- [Finding 3] Effective multi‑dimensional steering directions cannot be recovered as simple linear combinations of single‑function directions, revealing inherent non‑linear interdependencies among cognitive processes.

## Methodology  
The authors introduced a Jungian evaluation protocol that maps each of the eight functions to a distinct activation vector and collected over 2,100 role‑playing character narrations as training data. They then extracted steering vectors from Llama‑3.1‑8B using gradient‑based control and performed systematic experiments to assess monotonicity, geometric consistency, and linear‑combination feasibility.

## Results  
Experiments confirmed that activation steering can steer the model’s output toward any desired combination of cognitive functions without violating monotonic constraints. Visualizations showed that vectors from rational functions (e.g., introverted thinking) cluster together while those from irrational functions (e.g., extraverted intuition) form a distinct geometric region. Moreover, attempts to reconstruct composite directions by linearly blending single‑function vectors failed, indicating that the personality space is intrinsically non‑linear.

## Significance  
This research provides a concrete, interpretable representation of personality within LLM activation spaces, enabling researchers and developers to manipulate character behavior with finer granularity than traditional trait models. By exposing geometric constraints on cognitive function control, it opens avenues for more nuanced AI‑driven role‑playing systems.

## Related Concepts  
- Jungian Cognitive Functions (e.g., introverted thinking, extraverted intuition)  
- Activation Steering in LLMs  
- Geometric representation of high‑dimensional data  
- Multi‑modal personality modeling
