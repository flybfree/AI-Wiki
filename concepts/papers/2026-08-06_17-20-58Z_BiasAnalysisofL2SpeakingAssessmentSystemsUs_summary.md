# Summary: 2026-08-06_17-20-58Z_BiasAnalysisofL2SpeakingAssessmentSystemsUsingConc.md
Saved: 2026-08-06 23:08
Source: 2026-08-06_17-20-58Z_BiasAnalysisofL2SpeakingAssessmentSystemsUsingConc.md
Model: None

---

## Summary  
The paper aims to evaluate whether L2 speaking assessment systems exhibit bias toward irrelevant speaker attributes such as first language or age, using Concept Activation Vectors (CAVs) to measure how concepts are encoded and influence model outputs. It extends CAV analysis from feature‑based graders to two neural models—a text‑only BERT grader and a multimodal Whisper‑BERT system—by representing human interpretable concepts as directions in activation space and measuring sensitivity via gradients. The study also investigates whether sparse autoencoders (SAEs) can provide cleaner concept directions by learning them in a low‑dimensional latent space, which may improve recoverability while preserving interpretability. Finally, the work highlights that concept recoverability depends on model architecture rather than the concept itself.  

## Key Contributions  
- CAV analysis reveals that certain concepts are not merely present in embeddings but actually affect predicted scores, measured by gradient sensitivity.  
- SAEs improve linear recoverability of concepts compared to original activation space, especially in low‑dimensional layers.  
- Concept influence is architecture‑dependent; SAE‑derived directions attenuate original activation‑space sensitivity.  

## Methodology  
The authors construct CAVs for each concept (e.g., L1, age) by projecting human‑defined vectors onto the model’s hidden layer activations and normalizing them. They compute gradient sensitivity by varying the input while keeping the concept vector constant, measuring score change per unit CAV length. For SAEs, they train a sparse autoencoder to compress activations into a low‑dimensional latent code, then decode back to original activation space; the resulting mapping is used as a new CAV. Experiments compare recoverability (reconstruction error) and sensitivity across BERT, Whisper‑BERT, and SAE variants.  

## Results  
The text‑only BERT grader shows moderate sensitivity for age but low sensitivity for L1, indicating limited bias. The multimodal Whisper‑BERT system is more sensitive to both concepts, especially age. SAEs increase concept recoverability (reconstruction error drops by ~30%) and reduce activation‑space sensitivity (gradient magnitude decreases), suggesting that while biases are still present, they are less pronounced in the sparse representation.  

## Significance  
Understanding whether a concept merely appears in model representations or actually drives predictions is crucial for fairness auditing of automated speaking tests. The findings guide practitioners to use sparse autoencoders when interpretability matters but caution that such methods may mask underlying biases if sensitivity is attenuated.  

## Related Concepts  
Concept Activation Vectors, CAV analysis, gradient‑based sensitivity, sparse autoencoders (SAE), latent space representation, linear separability, activation space, bias detection in NLP evaluation.
