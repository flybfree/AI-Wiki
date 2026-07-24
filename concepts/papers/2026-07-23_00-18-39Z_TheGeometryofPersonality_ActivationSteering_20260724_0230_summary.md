# Summary: 2026-07-23_00-18-39Z_TheGeometryofPersonality_ActivationSteeringwithJun.md
Saved: 2026-07-24 02:30
Source: 2026-07-23_00-18-39Z_TheGeometryofPersonality_ActivationSteeringwithJun.md
Model: None

---

## Summary  
The paper proposes representing personality as a set of eight Jungian cognitive functions and uses activation steering to control them in large language models, moving beyond static Big Five traits. It introduces a framework that combines a Jungian evaluation protocol with a dataset of over 2,100 role‑playing character narrations to evaluate monotonic control over all functions via Llama‑3.1‑8B. By treating personality as geometric vectors in activation space, the authors aim to provide interpretable, multi‑dimensional steering that aligns with cognitive theory.

## Key Contributions  
- Finding 1: Personality information is concentrated in middle transformer layers.  
- Finding 2: Steering vectors exhibit structured geometric relationships consistent with distinctions between rational and irrational functions.  
- Finding 3: Effective multi‑dimensional steering directions cannot be recovered as linear combinations of single‑function directions.

## Methodology  
The authors built a Jungian evaluation protocol that maps each personality trait onto one of the eight cognitive functions (thinking, feeling, introversion, extraversion, sensing, intuition, etc.). They collected over 2,100 role‑playing character narrations to create a rich behavioral corpus. Using activation steering vectors extracted from Llama‑3.1‑8B, they steered model outputs toward desired functions and measured the resulting activation patterns across all transformer layers.

## Results  
Experiments demonstrate that each of the eight cognitive functions can be steered monotonically with an appropriate vector, confirming controllability. Activation maps peak in layers 6‑12, indicating that personality‑related information is concentrated in middle layers rather than at the extremes. Geometric analysis reveals orthogonal clusters separating rational (e.g., thinking, intuition) from irrational (extraversion, sensing) functions, establishing a clear geometric structure. Crucially, multi‑dimensional steering directions that combine several functions are not linearly decomposable into single‑function vectors, confirming non‑linear relationships in the activation space.

## Significance  
This work bridges personality theory with LLM interpretability, offering a geometric view of cognitive processes in activation space and enabling precise, multi‑modal control—potentially unlocking more nuanced AI behavior aligned with human personality models. The findings open new avenues for designing AI agents whose responses reflect coherent cognitive functions rather than merely static trait scores.

## Related Concepts  
Activation steering, Jungian cognitive functions (thinking, feeling, introversion, extraversion, sensing, intuition), Big Five traits, transformer layers, monotonic control, geometric representation of vectors, multi‑dimensional steering.
