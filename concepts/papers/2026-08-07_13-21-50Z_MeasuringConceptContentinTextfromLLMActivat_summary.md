# Summary: 2026-08-07_13-21-50Z_MeasuringConceptContentinTextfromLLMActivations_ES.md
Saved: 2026-08-09 22:57
Source: 2026-08-07_13-21-50Z_MeasuringConceptContentinTextfromLLMActivations_ES.md
Model: None

---

## Summary  
The paper investigates whether the internal activations of a frozen Large Language Model can be used to measure how much a piece of text is about a given concept, going beyond surface‑level cues such as word frequencies or topic proportions. By extracting two types of measures—binary classification scores via linear probing and continuous scores via Recursive Feature Machine (RFM)—the authors compare these activations against embedding baselines, simple surface baselines, and the model’s own answer to a concept question on an annotated ESG dataset. Their experiments show that a simple linear probe can achieve accuracy within 0.6 percentage points of a fine‑tuned domain classifier without any task‑specific fine‑tuning and often beats the model’s own response. The continuous RFM scores provide a graded notion of concept presence that binary classifiers cannot capture.

## Key Contributions  
- **Linear probe outperforms fine‑tuned domain classifier**: A simple linear probing method reaches classification accuracy within 0.6 percentage points of a fine‑tuned ESG classifier, demonstrating that frozen activations encode concept content without task‑specific training.  
- **Simple probes beat RFM vectors in binary tasks**: The straightforward linear probe yields higher accuracy than the more complex Recursive Feature Machine approach when evaluating whether a text contains a concept as a yes/no decision.  
- **RFM offers continuous concept scores**: Unlike binary classifiers, the RFM algorithm produces a graded score reflecting how strongly a concept is present, which can be validated against human‑graded labels.

## Methodology  
The authors extract measures from frozen LLM activations using two algorithms: (1) Recursive Feature Machine (RFM), which computes a continuous vector representing feature importance, and (2) linear probing, which linearly maps activation patterns to class probabilities. They evaluate these measures against an embedding baseline, surface‑based baselines that rely on word‑level statistics, and the model’s own answer to a concept question. The evaluation is performed on a human‑annotated ESG dataset of financial text, where each document is labeled for presence of specific environmental, social, or governance concepts.

## Results  
The linear probe achieves classification accuracy within 0.6 percentage points of a fine‑tuned domain classifier and outperforms the model’s own answer in eleven out of twelve comparisons. The simple probe also exceeds the RFM vector’s performance on binary tasks. While the RFM method provides richer, continuous scores that could be calibrated against graded labels, it does not surpass the linear probe for classification accuracy.

## Significance  
These findings reveal a practical advantage to monitoring frozen LLM activations: they can serve as an efficient proxy for concept content without requiring costly fine‑tuning. The work bridges the gap between internal knowledge and external output, offering both binary and continuous metrics that could improve downstream tasks such as ESG text analysis.

## Related Concepts  
- Concept content measurement  
- Linear probing (activation monitoring)  
- Recursive Feature Machine (RFM) algorithm  
- Embedding baseline  
- Surface baselines (word‑level statistics)  
- Fine‑tuned domain classifier  
- ESG dataset and annotation  
- Activation monitoring for concept detection
