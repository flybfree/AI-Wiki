# Summary: 2026-07-23_00-18-39Z_TheGeometryofPersonality_ActivationSteeringwithJun.md
Saved: 2026-07-24 02:19
Source: 2026-07-23_00-18-39Z_TheGeometryofPersonality_ActivationSteeringwithJun.md
Model: None

---

## Summary  
This paper proposes a novel approach to modeling personality in large language models by treating it as a set of eight Jungian Cognitive Functions rather than static Big‑Five traits. The authors demonstrate that activation steering can be used to control all cognitive functions, revealing how personality information is encoded within the model’s transformer layers and how these controls form geometric structures. Their work establishes a framework for interpretable, multi‑dimensional personality manipulation in LLMs.

## Key Contributions  
- Personality can be represented as a set of cognitive processes using the eight Jungian Cognitive Functions, enabling activation steering beyond static trait frameworks.  
- Activation steering vectors exhibit structured geometric relationships that align with distinctions between rational and irrational functions.  
- Effective multi‑dimensional personality control cannot be recovered as linear combinations of single‑function directions.

## Methodology  
The authors introduced a Jungian evaluation protocol and assembled a dataset of over 2,100 role‑playing character narrations to serve as stimuli for personality measurement. They extracted activation steering vectors from Llama‑3.1‑8B by conditioning the model on these narratives and then evaluated monotonic control over each cognitive function.

## Results  
Personality information is concentrated in middle transformer layers, where the influence of cognitive functions peaks. The steering vectors display geometric patterns that separate rational (e.g., introversion) from irrational (e.g., extraversion) functions. Moreover, multi‑dimensional steering directions cannot be expressed as linear combinations of individual function vectors, indicating a non‑linear representation.

## Significance  
These findings provide new insights into how personality is encoded in the activation space of LLMs and open a pathway for interpretable, effective, and multi‑dimensional personality control that transcends traditional trait models. The framework may enable more nuanced user interactions and deeper research into cognitive architectures within AI systems.

## Related Concepts  
Jungian Cognitive Functions, Activation Steering, Transformer Activation Space, Big Five traits, Personality Representation, Geometric Relationships, Multi‑dimensional Control
