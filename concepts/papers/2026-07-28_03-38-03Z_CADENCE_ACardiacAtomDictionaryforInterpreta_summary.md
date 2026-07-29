# Summary: 2026-07-28_03-38-03Z_CADENCE_ACardiacAtomDictionaryforInterpretableNeur.md
Saved: 2026-07-28 22:29
Source: 2026-07-28_03-38-03Z_CADENCE_ACardiacAtomDictionaryforInterpretableNeur.md
Model: None

---

## Summary  
The paper introduces CADENCE, a framework that extracts interpretable physiological concepts from ECG foundation models by decomposing Layer‑6 embeddings into sparse cardiac atoms. These atoms serve as a human‑readable dictionary linking neural representations to clinical phenotypes and waveform morphology. By mapping each atom to specific arrhythmias, conduction issues, infarction patterns, etc., CADENCE provides transparent explanations for model predictions.  

## Key Contributions  
- [CADENCE decomposes Layer‑6 embeddings into 8 192 sparse cardiac atoms that align better than dense dimensions with clinical phenotypes and waveform morphology.]  
- [The framework achieves AUROCs of 0.88 (phenotype) and 0.90 (morphology) for the best atoms, outperforming dense probes at 0.78 and 0.83.]  
- [An LLM‑driven pipeline generates atom descriptions that are validated by predicting held‑out activations, enabling automated auditing of physiological knowledge.]  

## Methodology  
CADENCE employs a BatchTopK sparse autoencoder to factorize the high‑dimensional Layer‑6 embeddings into low‑dimensional atomic vectors. The encoder is trained to reconstruct the original embedding using only a subset of atoms, enforcing sparsity and interpretability. Each atom is then mapped to a set of physiological concepts via an LLM that predicts corresponding activation patterns on held‑out data.  

## Results  
On internal datasets, the best CADENCE atoms achieve mean AUROCs of 0.88 for phenotype prediction and 0.90 for morphology prediction, compared with 0.78 and 0.83 for the top dense dimensions. Atom ablation shows that removing specific atoms alters downstream outputs, confirming causal links. The LLM‑generated atom descriptions are validated by achieving >95 % accuracy in predicting held‑out activations. On independent external ECG datasets, CADENCE recovers overlapping clinical concepts and maintains consistent performance.  

## Significance  
This work bridges the gap between black‑box deep learning and clinically actionable insights, enabling clinicians to understand why a model flags an arrhythmia or predicts age from ECG data. By providing a scalable atom dictionary, CADENCE supports trustworthy AI deployment in cardiology and opens avenues for automated concept verification.  

## Related Concepts  
- ECG foundation models  
- Sparse autoencoders (BatchTopK)  
- Cardiac atoms / physiological concepts  
- AUROC evaluation  
- LLM‑driven interpretability pipelines
