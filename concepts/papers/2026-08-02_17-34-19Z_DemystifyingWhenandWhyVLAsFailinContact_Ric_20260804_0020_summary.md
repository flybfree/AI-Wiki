# Summary: 2026-08-02_17-34-19Z_DemystifyingWhenandWhyVLAsFailinContact_RichTasksa.md
Saved: 2026-08-04 00:20
Source: 2026-08-02_17-34-19Z_DemystifyingWhenandWhyVLAsFailinContact_RichTasksa.md
Model: None

---

## Summary  
The paper seeks to understand why vision‑language‑action (VLA) models fail in contact‑rich manipulation tasks that require precise physical interaction. It identifies two failure modes — precision failures due to a flow‑matching policy mismatch and force failures arising from the distinctive structure of force signals. The authors propose targeted fixes, combining them into a new framework called FACT, which improves performance on these challenging tasks.

## Key Contributions  
- Finding 1: Precision failures stem from a mismatch between the flow‑matching policy used for visual‑language reasoning and the action‑generation component, leading to inaccurate spatial predictions.  
- Finding 2: Force signals have a distinctive temporal structure that is not well captured by standard VLA encoders, causing force‑related errors in contact tasks.  
- Finding 3: The authors introduce FACT, a unified framework that jointly corrects the policy mismatch and improves force signal processing.

## Methodology  
The authors first conducted extensive rollouts of five real‑world contact‑rich manipulation benchmarks to collect failure data. They then performed root‑cause analysis separating precision from force failures. For each mode they designed a specific correction: a policy‑alignment module that aligns the flow‑matching visual‑language encoder with the action generator, and a signal‑conditioner that reshapes force embeddings to match their unique dynamics. These components are integrated into FACT, which is trained end‑to‑end on the same data.

## Results  
FACT achieves an average success rate of 66 % across the five tasks, compared with 41 % for the best prior baseline. The improvement is measured over almost 2,500 rollouts, demonstrating robust gains in both precision and force handling.

## Significance  
Understanding these failure modes enables more reliable VLA systems that can safely interact with physical objects. By providing a clear diagnostic framework (precision vs. force) and a unified corrective architecture, FACT advances the field toward trustworthy embodied AI.

## Related Concepts  
- Vision‑Language‑Action (VLA) models  
- Flow‑matching policy training  
- Force signal encoding  
- Contact‑rich manipulation tasks  
- Precision vs. force failure modes  
- Unified corrective framework (FACT)
