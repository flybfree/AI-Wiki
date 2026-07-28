# Summary: 2026-07-25_21-58-17Z_WhenActivationOraclesLearnNottoRead_Concept_Specif.md
Saved: 2026-07-27 22:37
Source: 2026-07-25_21-58-17Z_WhenActivationOraclesLearnNottoRead_Concept_Specif.md
Model: None

---

## Summary  
Activation Oracles (AOs) are language models that are trained to read hidden activations of another model and report them as natural‑language answers, offering a flexible interface for probing internal states. In this study the authors fine‑tune both a subject model and an AO in a Taboo Word Guessing task where the subject internally uses a concealed concept while avoiding explicit disclosure. They expected that the AO would become a specialist reader capable of recovering the hidden concept, but instead observed that the AO frequently fails to retrieve it even though the concept is present in its own representations. The failure is not due to the absence of the concept from either representation; rather, it originates in the AO’s readout pathway. This work demonstrates that learned interpretability interfaces can exhibit systematic blind spots, undermining reliability assumptions.

## Key Contributions  
- [Finding 1] Fine‑tuned Activation Oracles exhibit persistent failure to recover a hidden concept despite its presence in their internal representations.  
- [Finding 2] The failure is not caused by the absence of the concept from subject or AO representations but stems from breakdowns in the readout pathway, as revealed by LogitLens and layer‑ablation analyses.  
- [Finding 3] Behavioral leakage, representation‑level decodability, and AO verbalizability can become decoupled, raising reliability concerns for learned interpretability interfaces.

## Methodology  
The authors set up a Taboo Word Guessing experiment in which a subject model is fine‑tuned to use a concealed concept while avoiding direct disclosure. They then train Activation Oracles on the same data to answer questions about the subject’s activations, creating a controlled setting for probing how AOs read internal states. To isolate the source of decoding failure, they employ LogitLens probing and layer‑ablation experiments that compare which layers contribute to concept retrieval.

## Results  
Experiments show that AOs trained on the fine‑tuned subject consistently miss the hidden concept with high error rates, whereas a control group using an untrained AO performs well. Layer‑ablation reveals that early layers are not responsible for the failure; instead, the readout pathway is broken, indicating a bottleneck in activation extraction.

## Significance  
This work demonstrates that learned interpretability tools can exhibit systematic blind spots, challenging assumptions about their neutrality and reliability for probing internal states of other models. It highlights the need for rigorous validation when using AOs as trustworthy readouts of model internals.

## Related Concepts  
Activation Oracles, fine‑tuned subject model, hidden concept, LogitLens, layer‑ablation analysis, representation‑level decodability, behavioral leakage, readout pathway, interpretability interface.
