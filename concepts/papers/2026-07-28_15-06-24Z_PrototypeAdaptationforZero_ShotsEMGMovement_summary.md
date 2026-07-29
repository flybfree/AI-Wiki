# Summary: 2026-07-28_15-06-24Z_PrototypeAdaptationforZero_ShotsEMGMovementClassif.md
Saved: 2026-07-28 22:53
Source: 2026-07-28_15-06-24Z_PrototypeAdaptationforZero_ShotsEMGMovementClassif.md
Model: None

---

## Summary  
The paper addresses the challenge of classifying combined sEMG movements in prosthetic control that cannot be covered by existing models trained only on basic gestures. It proposes two zero‑shot adaptation techniques—Compositional Prototype Interpolation (CPI) and Synthetic Adaptation for Prototypes (SAP)—that allow the model to recognize novel, unseen movement combinations without additional training data. By leveraging linear interpolation in embedding space, these methods extend the reach of prototype networks beyond their original training set. By extending prototype networks to unseen combinations, the approach aligns with the goal of creating flexible, data‑efficient prosthetic control systems.  

## Key Contributions  
- CPI and SAP enable zero‑shot classification of combined sEMG movements that were never seen during training.  
- The methods rely on a linear interpolation assumption in the embedding space; geometric inspection reveals that combined motions often lie near linear paths between basic prototypes, supporting interpolation.  
- Experimental results show SAP improves accuracy for combined movement recognition by over 20% compared to prior zero‑shot baselines.  

## Methodology  
The authors treat each basic movement as a prototype vector and generate synthetic prototypes for novel combinations via interpolation. First, sEMG signals are encoded into latent vectors using a pretrained Prototype Network. Then the centroid of the involved basic movements is computed, and linear interpolation between these centroids produces a representation for the combined motion that can be fed to the network for classification.  

## Results  
On NearLab, NinaPro DB3, and their newly recorded BasCom dataset, SAP achieved an accuracy increase exceeding 20% over previous zero‑shot baselines. Online inference in a user study confirmed that the improvement persists under real‑time conditions.  

## Significance  
This work reduces the need for extensive data collection and model retraining when users perform novel movement combinations, making sEMG prostheses more adaptable to everyday tasks and improving user experience.  

## Related Concepts  
Prototype Networks, zero‑shot learning, linear interpolation in embedding space, synthetic adaptation, sEMG signal encoding, prototype vectors, centroid computation.
