# Summary: 2026-08-06_23-09-37Z_MI_MIDI_MechanisticInterpretabilityofText_to_MIDIG.md
Saved: 2026-08-09 22:26
Source: 2026-08-06_23-09-37Z_MI_MIDI_MechanisticInterpretabilityofText_to_MIDIG.md
Model: None

---

## Summary  
The paper tackles the problem of mechanistic interpretability for text‑to‑MIDI generation, a field that has largely focused on audio models while symbolic systems remain understudied. It conducts a comparative analysis of two public text‑to‑MIDI frameworks—purpose‑built encoder–decoder *text2midi* and the Llama‑based *MIDI‑LLM*—using probing, lensing, activation patching, and steering techniques to uncover how musical concepts are encoded. The authors demonstrate that pitch, instrumentation, harmony, and texture can be linearly decoded in both models, revealing architecture‑driven pathways for these meanings. By applying a two‑orientation protocol they isolate directional control and show that all‑layer interventions behave differently across the systems.

## Key Contributions  
- [Finding 1] Musical structure is linearly decodable: pitch, instrumentation, harmony, and texture can be recovered from model outputs in both *text2midi* and *MIDI‑LLM*.  
- [Finding 2] Architectural differences shape formation of musical concepts: *text2midi* refines predictions gradually across depth, whereas *MIDI‑LLM* largely operates on its textual basis before a sharp late rotation into the musical vocabulary. Patching reveals a matching late attenuation of prompt‑driven instrument transfer in both cases.  
- [Finding 3] Steering enables bidirectional control: it produces changes in register and polyphony (and tempo/energy) in *MIDI‑LLM*, while two‑orientation protocol isolates directional control, showing robust all‑layer interventions in *text2midi* but disruptive accumulation in *MIDI‑LLM*.

## Methodology  
The authors approached the interpretability problem by employing a suite of mechanistic tools. Linear probing was used to extract scalar representations of musical elements from hidden states. Logit and tuned lenses were applied as interpretable interfaces that map textual prompts onto MIDI parameters. Activation patching isolated the contribution of late‑layer activations, while difference‑in‑means steering allowed bidirectional adjustments to register, polyphony, tempo, and energy. A two‑orientation protocol was introduced to separate forward and reverse control directions.

## Results  
Across both models the authors recovered musically meaningful structure: pitch, instrumentation, harmony, and texture were linearly decodable. *text2midi* exhibited a smooth, depth‑wise refinement of predictions, whereas *MIDI‑LLM* showed a predominantly textual behavior followed by a sudden shift into musical output; patching confirmed that the late rotation is accompanied by attenuation of prompt‑driven instrument transfer. Steering produced reversible changes in register and polyphony in both systems, with additional tempo/energy modulation in *MIDI‑LLM*. The two‑orientation protocol demonstrated that all‑layer interventions are stable in *text2midi* but accumulate inconsistently in *MIDI‑LLM*.

## Significance  
This work provides a practical toolkit for tracing and controlling musical concepts within symbolic text‑to‑MIDI generators, bridging the gap between audio interpretability and symbolic AI. By exposing architecture‑driven pathways and offering steering mechanisms, it enables researchers to design more transparent and controllable music generation systems.

## Related Concepts  
Mechanistic interpretability, probing, lenses (logit and tuned), activation patching, difference‑in‑means steering, two‑orientation protocol, text‑to‑MIDI generation, symbolic AI, linear decoding of musical elements.
