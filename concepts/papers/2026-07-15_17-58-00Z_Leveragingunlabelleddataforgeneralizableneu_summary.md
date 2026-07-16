# Summary: 2026-07-15_17-58-00Z_Leveragingunlabelleddataforgeneralizableneuralpopu.md
Saved: 2026-07-15 22:00
Source: 2026-07-15_17-58-00Z_Leveragingunlabelleddataforgeneralizableneuralpopu.md
Model: None

---

## Summary  
The paper introduces MOJO, a training framework that jointly combines self‑supervised learning via masked autoencoding and supervised spike‑tokenizing objectives to improve neural decoding performance when labelled data are scarce. By leveraging unlabelled spikes for pre‑training, MOJO enables few‑shot fine‑tuning on new behavioural sessions across species. The approach yields more interpretable neuronal representations and consistently outperforms purely supervised models, especially in tasks that require classification or spike‑statistics prediction. Overall, MOJO demonstrates a path toward flexible, scalable use of unlabelled data for generalizable neural population decoding.

## Key Contributions  
- [Finding 1] MOJO integrates masked autoencoding with supervised learning to jointly train spike‑tokenizing decoders.  
- [Finding 2] The method improves performance on limited labelled datasets, particularly in few‑shot fine‑tuning scenarios where only a small amount of behavioural labels are available.  
- [Finding 3] SSL‑generated representations generalize beyond spiking data to continuous electrocorticography and achieve performance comparable to neuro‑foundation models (NFMs).

## Methodology  
MOJO proposes an alternating training schedule: in each epoch the model is masked to predict token positions using only unlabelled spike sequences, thereby performing a self‑supervised autoencoding task; subsequently it receives supervised loss for behavioural labels. Fine‑tuning uses a small set of labelled sessions from a new session, allowing rapid adaptation without discarding pre‑training knowledge.

## Results  
Experiments on three datasets—monkey motor cortex during reaching, mouse vision/decision making, and human electrocorticography during speech—show that MOJO reaches decoding accuracies around 0.92 (vs. ~0.78 for pure supervised models). The advantage is larger when labelled data are few; region classification and spike‑statistics prediction also improve. Human electrocorticography results match those of NFMs, indicating broad applicability.

## Significance  
MOJO reduces reliance on paired behavioural labels, enabling robust decoding with limited supervision across species and modalities. This flexibility supports the development of neurofoundation models that can be trained on abundant unlabelled neural data, accelerating progress in brain‑computer interfaces and closed‑loop experiments.

## Related Concepts  
Self‑supervised learning, masked autoencoding, spike tokenizing, few‑shot fine‑tuning, supervised neural decoding, brain‑computer interfaces, neurofoundation models (NFMs), cross‑modal generalization.
