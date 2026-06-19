---

title: "Summary: Beyond Text Following: Repairable Arbitration Reversals in Audio-Language Models"
url: http://arxiv.org/abs/2606.05161v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-03_17-57-51Z_BeyondTextFollowing_RepairableArbitrationReversals.md
generated_at: "2026-06-11 10:52"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper investigates why audio-language models sometimes ignore clear audio evidence when a conflicting text is present, showing that the model’s preference flips when only the text is removed. It demonstrates that 64.1% of conflict samples reverse to favor the audio‑supported answer and proposes a decoding rule called GACL.

## Key Takeaways
- The same‑audio branch prefers the audio‑supported answer while the joint branch prefers the text‑supported answer, indicating encoded but overridden evidence.
- Activation patching localizes the reversal to answer‑position computation with Spearman rho=0.93 linking it to candidate scores.
- Gated Audio Counterfactual Logit Correction (GACL) improves nAUC by 17.8 points and transfers to vision‑text arbitration without retuning.

## Context
Audio‑language models are increasingly used in multimodal settings where audio and text may conflict, yet current architectures do not reliably resolve such conflicts. This work provides a diagnostic for when textual dominance masks auditory cues, offering insight into model decision pathways.

## Implications
Practitioners can apply GACL to boost model faithfulness without retraining, reducing hallucination in multimodal applications. The findings suggest that arbitration mechanisms should be designed to preserve audio evidence, improving reliability across industries such as healthcare and autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.05161v1)
