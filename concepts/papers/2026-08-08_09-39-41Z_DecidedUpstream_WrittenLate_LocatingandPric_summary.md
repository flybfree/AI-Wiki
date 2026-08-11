# Summary: 2026-08-08_09-39-41Z_DecidedUpstream_WrittenLate_LocatingandPricingtheC.md
Saved: 2026-08-10 22:52
Source: 2026-08-08_09-39-41Z_DecidedUpstream_WrittenLate_LocatingandPricingtheC.md
Model: None

---

## Summary  
The paper investigates why multilingual models refuse harmful requests inconsistently across languages, tracing a cross‑lingual refusal circuit in the Indic‑multilingual MoE sarvam. It shows that harm is encoded as an internal direction that remains nearly language‑invariant at layer L11 (cosine ≈0.9), while the actual refusal is written later in generation rather than read off a single forward pass.

## Key Contributions  
- [Finding 1] Harm encoding appears as a near‑language‑invariant internal direction persisting at L11, with high cosine similarity between English and Indic embeddings.  
- [Finding 2] The refusal is assembled late in the generation process across multiple steps, not produced by a single forward pass.  
- [Finding 3] A specific MiE writer circuit is constrained by an attention opposer; interventions such as damping, amplifying, or editing heads have distinct cost implications.

## Methodology  
Researchers probed internal representations and generation dynamics of sarvam using cosine similarity measurements between language‑specific embeddings at L11 to quantify the invariance of the harm direction. Gradient‑based probing was employed to locate the writer head and its controlling opposer attention pattern, after which the cost (parameter change) of perturbing each component was measured.

## Results  
Cosine similarity ≈0.9 indicates a nearly language‑invariant harm signal. Refusal generation occurs late across layers, assembled over the course of output. Damping the opposer reduces harmful outputs by roughly 30 % with minimal parameter alteration, whereas amplifying the writer dramatically increases refusals at high cost. Surgical edits to the writer heads have negligible effect on refusal behavior.

## Significance  
The work provides a cost‑measured map of multilingual safety repair points, showing where interventions can be applied efficiently while respecting architectural constraints and language diversity. This enables researchers to target costly “late” generation steps rather than expensive early detection mechanisms.

## Related Concepts  
Mixture‑of‑Experts (MoE), cross‑lingual alignment, internal direction encoding, gradient probing, attention mechanisms, safety alignment, late‑stage generation assembly.
