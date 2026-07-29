# Summary: 2026-07-27_23-22-17Z_HowAffectPropagatesamongLLMAgents_EmergentEmotiona.md
Saved: 2026-07-28 20:20
Source: 2026-07-27_23-22-17Z_HowAffectPropagatesamongLLMAgents_EmergentEmotiona.md
Model: None

---

## Summary  
The paper investigates how affect spreads among language‑model agents in a multi‑agent crowd simulation, showing that emotional contagion can emerge without any direct transfer mechanism between agents. By linking perception, appraisal via an LLM, and outward expression, the authors demonstrate that affective dynamics are shaped by spatial layout, temporal spread, and individual personality profiles.

## Key Contributions  
- **Finding 1:** The system exhibits spontaneous emotional contagion where an initial alarmed agent triggers a spatially propagating alarm front in small crowds.  
- **Finding 2:** The mean alarmed fraction stabilizes at a non‑zero plateau, indicating sustained affective influence beyond transient spikes.  
- **Finding 3:** Appraisal dynamics are backend‑dependent across LLM models and prompt variations, affecting whether ambiguous alarms trigger panic or anger.

## Methodology  
The authors constructed a simulation in which each agent perceives neighbors through visual, auditory, and tactile channels, appraises these inputs using an LLM informed by the Big Five personality model and Russell’s circumplex affect model, updates its internal affective state, and selects an outward expression. Low‑level navigation is handled independently by a conventional crowd simulator to limit latency. Experiments were run across five environments (alarming, joyful, neutral) with different spatial layouts.

## Results  
In sparse crowds the alarm spreads as a traveling front; the average fraction of alarmed agents settles at a stable value greater than zero. Personality profiles moderate interpretation: ambiguous alarms may become panic or fear depending on the profile. Controlled experiments across four LLM backends and temperature settings reveal that appraisal outcomes vary widely, confirming backend dependence.

## Significance  
This work reveals emergent affective contagion in AI agents without explicit transfer mechanisms, highlighting the pivotal role of perception‑appraisal loops in shaping social dynamics; it informs design of socially aware systems and understanding of model variability.

## Related Concepts  
Emotional contagion, affect propagation, multi‑agent simulation, LLM‑driven cognition, Big Five personality traits, Russell circumplex model, spatial‑temporal dynamics, affective front, backend dependence.
