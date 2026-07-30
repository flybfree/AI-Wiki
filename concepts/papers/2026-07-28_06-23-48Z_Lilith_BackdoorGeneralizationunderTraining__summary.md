# Summary: 2026-07-28_06-23-48Z_Lilith_BackdoorGeneralizationunderTraining_Inferen.md
Saved: 2026-07-29 22:11
Source: 2026-07-28_06-23-48Z_Lilith_BackdoorGeneralizationunderTraining_Inferen.md
Model: None

---

## Summary  
The paper addresses a critical blind spot in backdoor research: whether a malicious behavior implanted during training can persist when the trigger used at inference time belongs to a different family that was never seen during training. To explore this, the authors introduce **Lilith**, a black‑box framework that creates a compact vulnerability using a single training anchor and then builds an inference‑only trigger family that preserves the induced representation geometry. Their analysis shows that such generalization is possible under mild conditions, offering a new lens on backdoor robustness beyond exact‑trigger studies.

## Key Contributions  
- [Finding 1] Lilith can induce a persistent backdoor with only one training anchor and then generalize it to an entire inference‑time trigger family without exposing the victim’s data.  
- [Finding 2] The generalization mechanism is captured by two theoretical metrics—anchor clearance (how much the original vulnerability persists) and family reach (the size of the trigger set that can be activated).  
- [Finding 3] Experiments demonstrate high attack success rates across diverse datasets, architectures, poisoning levels, and defenses while keeping utility loss minimal.

## Methodology  
Lilith operates in two phases. First, it selects a single training example as an anchor and injects a malicious label that is invisible to the model’s decision boundary at inference time. Second, using only surrogate data (no access to the victim’s weights), it constructs a bounded set of trigger functions that align with the representation subspace created by the anchor. The framework relies on local regularity in the target space and a bounded discrepancy between surrogate and victim feature distributions to guarantee that the family can activate the backdoor.

## Results  
Across benchmark datasets (CIFAR‑10, ImageNet) and models (ResNet‑50, MobileNetV2), Lilith achieves an average attack success rate of 84 % with a 7 % utility degradation. The trigger generalization gap—difference between the original anchor’s activation probability and the family’s average activation—remains under 10 %. Sensitivity analysis confirms that the effect is robust to common defenses such as adversarial training, gradient masking, and out‑of‑distribution detection.

## Significance  
This work reveals that backdoors can survive a shift from training‑time to inference‑time triggers, challenging existing evaluations that assume trigger reuse. By providing theoretical conditions and empirical evidence of family‑wide generalization, Lilith expands the threat model for security practitioners and researchers focused on protecting deployed models.

## Related Concepts  
- Backdoor attack  
- Trigger generalization  
- Representation geometry  
- Anchor clearance  
- Family reach  
- Surrogate data  
- Local regularity  
- Bounded discrepancy
