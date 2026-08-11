# Summary: 2026-08-09_15-23-25Z_LearningfromConsensusandDisagreement_UnsupervisedO.md
Saved: 2026-08-10 23:24
Source: 2026-08-09_15-23-25Z_LearningfromConsensusandDisagreement_UnsupervisedO.md
Model: None

---

## Summary  
CoDA (Consensus and Disagreement Alignment) is a fully unsupervised on‑policy self‑distillation framework that improves language‑model reasoning by extracting reliable privileged information directly from the model’s own unlabeled rollouts. It creates two complementary signals: a positive consensus branch that conditions a frozen teacher on stable reasoning modes, and a negative minority‑trajectory branch that penalizes unstable alternatives using KTO‑style calibration. This approach eliminates the need for gold solutions or external verifiers while harnessing the latent uncertainty structure of the model’s own behavior to guide learning.

## Key Contributions  
- Finding 1: CoDA constructs both consensus and disagreement signals purely from the model’s unlabeled rollouts, providing a self‑generated supervision signal without any external supervision.  
- Finding 2: The positive branch uses answer‑level consensus to condition a frozen teacher, while the negative branch applies KTO‑style calibration with reference anchors to gently penalize minority trajectories that represent alternative (often erroneous) reasoning paths.  
- Finding 3: Empirical evaluation on competition‑level mathematical benchmarks shows CoDA significantly outperforms self‑generated baselines, improves accuracy, and stabilizes training by preventing error amplification from false consensus.

## Methodology  
The authors generate a batch of unlabeled rollouts from the student model. For each rollout they compute the answer‑level consensus across all trajectories to identify a stable reasoning mode; this consensus is used as a frozen teacher that provides dense distributional guidance for new student states. Simultaneously, trajectories whose answers deviate (minority trajectories) are identified and subjected to a KTO‑style calibration loss anchored to reference points, producing a negative feedback term. The overall objective combines the positive distillation term with the negative regularization term, yielding a single unsupervised loss that simultaneously encourages correct reasoning and discourages error propagation.

## Results  
On benchmark sets such as MATH and GSM8K, CoDA achieves higher accuracy than existing self‑distillation methods (e.g., teacher‑student distillation, contrastive learning). The negative minority branch reduces variance in reasoning scores and accelerates convergence, while the positive consensus branch yields more consistent output. Ablation studies confirm that removing either the consensus or the KTO penalty degrades performance, highlighting the necessity of both signals.

## Significance  
CoDA demonstrates that intrinsic uncertainty can serve as a powerful supervision signal for on‑policy distillation, enabling scalable improvement in complex reasoning tasks without relying on costly external verifiers. This work advances the field by providing a principled way to turn disagreement into regularization and consensus into guidance, offering a template for future unsupervised self‑improvement methods.

## Related Concepts  
- On‑policy self‑distillation  
- KTO (KL‑divergence with temperature) calibration  
- Consensus learning  
- Minority trajectory regularization  
- Latent uncertainty exploitation
