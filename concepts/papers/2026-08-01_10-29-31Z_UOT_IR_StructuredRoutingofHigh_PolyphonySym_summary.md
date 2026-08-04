# Summary: 2026-08-01_10-29-31Z_UOT_IR_StructuredRoutingofHigh_PolyphonySymbolicMu.md
Saved: 2026-08-03 21:26
Source: 2026-08-01_10-29-31Z_UOT_IR_StructuredRoutingofHigh_PolyphonySymbolicMu.md
Model: None

---

## Summary  
The paper tackles the challenge of compressing richly polyphonic symbolic music into bounded representations that respect a fixed slot budget while preserving structural roles, orchestration compatibility, and playability. It introduces Unbalanced Optimal Transport for Information Routing (UOT‑IR), a training‑free framework that treats the compression task as a structured routing problem. By integrating an orchestration prior, adaptive marginal relaxation, temporal decoding, and playability‑aware projection, UOT‑IR generates compact yet musically coherent bounded representations suitable for downstream tasks such as template standardization or adaptive preservation. The approach demonstrates strong performance on the SymphonyNet corpus, achieving the highest Note‑F1 score among reported methods.

## Key Contributions  
- [Finding 1] Reformulates high‑polyphony compression as a fixed‑budget structured routing problem.  
- [Finding 2] Proposes UOT‑IR, a training‑free framework based on constrained unbalanced optimal transport that combines an orchestration prior and adaptive marginal relaxation.  
- [Finding 3] Achieves the best Note‑F1 (0.9120) and lowest structural cost (14.7165) in template standardization experiments.

## Methodology  
UOT‑IR treats each input score as a set of symbolic tokens that must be routed into a fixed number of slots. The orchestration prior encodes typical instrument roles, guiding token placement. Adaptive marginal relaxation relaxes the strict budget constraints locally to allow flexible token allocation. Temporal decoding ensures temporal coherence across notes, while playability‑aware projection projects the final representation onto a musically acceptable space that respects both pitch and duration constraints.

## Results  
Experiments on the SymphonyNet corpus evaluate two practical settings: template standardization (mapping inputs to predefined bounded templates) and adaptive preservation (retaining representative content without an external template). In template standardization, UOT‑IR yields a structural cost of 14.7165 and a bad confusion rate of 0.3406, with the best Note‑F1 score reported. Adaptive preservation reaches a Note‑F1 of 0.9120, confirming its ability to preserve musical content while respecting the slot budget.

## Significance  
This work establishes a principled paradigm for fixed‑budget symbolic music compression, offering a practical path toward compact, structured, and musically coherent representations that can be directly used in generation, analysis, and arrangement pipelines. By decoupling structural role preservation from training, UOT‑IR provides a scalable solution applicable to diverse polyphonic scores.

## Related Concepts  
- Fixed‑budget representation  
- Optimal transport (unbalanced)  
- Structured routing  
- Orchestration prior  
- Adaptive marginal relaxation  
- Temporal decoding  
- Playability‑aware projection  
- Symbolic music generation  
- Slot budgeting
