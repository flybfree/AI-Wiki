title: "Summary: 2026-06-26_17-16-04Z_Vision_Default_Prior_Override_CausalMechanismsofPe.md"
# Summary: 2026-06-26_17-16-04Z_Vision_Default_Prior_Override_CausalMechanismsofPe.md
Saved: 2026-06-28 21:01
Source: 2026-06-26_17-16-04Z_Vision_Default_Prior_Override_CausalMechanismsofPe.md
Model: None

---


## Summary  
Vision‑language models must decide whether to rely on what the camera sees or on stored world knowledge when those two sources disagree. This paper introduces a component‑level causal account of that conflict, showing how visual grounding is produced automatically while prior (knowledge) grounding depends on a tiny set of attention heads. By ablating these heads we can flip predictions from knowledge‑based to visually based answers in most cases, revealing an asymmetric causal structure. The work also identifies the internal routing and writing mechanisms that enable this behavior across different VLM families.

## Key Contributions  
- [Finding 1] Visual grounding is produced by default; prior grounding relies on a sparse set of attention heads (2.5‑4.8 %) located in the second half of the network.  
- [Finding 2] Ablating those heads switches predictions from knowledge‑grounded to visually grounded answers in 68‑96 % of prior‑knowledge prompts, yet only 0.8‑7.5 % of visual‑grounded predictions are affected, establishing an asymmetric causal structure.  
- [Finding 3] The identified heads decompose into routing heads that modulate information flow and writing heads that directly project answer tokens to the residual stream, forming a sparse causal circuit common to all VLM scales.

## Methodology  
The authors combined activation patching across three granularities—residual‑stream activations, attention‑head outputs, and MLP sublayer outputs—to isolate component contributions. They performed model‑component ablation studies and mechanistic analysis on three vision‑language model families (e.g., CLIP, Flamingo, LLaVA) to determine which heads are causally necessary for prior grounding.

## Results  
Across the models, visual grounding occurs without any intervention, while prior grounding is contingent on the 2.5‑4.8 % attention heads. When these heads are removed, knowledge‑based answers dominate in a high proportion of prior prompts (68‑96 %) and only marginally alter visual answers (0.8‑7.5 %). The routing/writing head decomposition holds true for all scales, indicating a consistent causal circuit.

## Significance  
Understanding the precise causal mechanisms behind perception‑knowledge conflict improves the reliability and interpretability of multimodal systems. By pinpointing a sparse set of attention heads that mediate prior grounding, researchers can design interventions or architectures that preserve visual fidelity while still leveraging world knowledge when appropriate.

## Related Concepts  
perception‑knowledge conflict, multimodal models, activation patching, attention heads, routing heads, writing heads, causal circuits, visual grounding, prior grounding, residual stream, MLP sublayers.
