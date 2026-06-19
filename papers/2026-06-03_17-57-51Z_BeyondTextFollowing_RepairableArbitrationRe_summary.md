---
title: "2026 06 03 17 57 51Z Beyondtextfollowing Repairablearbitrationre Summary"
date: 2026-06-03
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-03_17-57-51Z_BeyondTextFollowing_RepairableArbitrationReversals.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-06-04 00:01
Source: 2026-06-03_17-57-51Z_BeyondTextFollowing_RepairableArbitrationReversals.md
Model: None

---


## Summary  
Audio‑language models (ALMs) frequently ignore clear audio evidence when it conflicts with textual input, raising the question of whether the audio signal is merely unavailable or is encoded but lost during arbitration. The authors investigate this by using same‑audio counterfactuals that keep the audio fixed while removing only the conflicting text, and they propose a training‑free decoding rule—Gated Audio Counterfactual Logit Correction (GACL)—to recover the suppressed audio influence within a strict faithfulness budget.

## Key Contributions  
- [Finding 1] In five ALMs across four conflict tasks, 64.1 % of samples show a sign flip: the same‑audio branch prefers the audio‑supported answer while the joint branch still favors the text‑supported one.  
- [Finding 2] Activation patching isolates the reversal to answer‑position computation and correlates it closely with output candidate‑score differences (Spearman ρ = 0.93).  
- [Finding 3] GACL, which interpolates between joint and same‑audio logits, improves nAUC by 17.8 points over the best contrastive baseline and transfers to vision‑text arbitration with a +40.5 pp gain.

## Methodology  
The authors employ same‑audio counterfactuals that retain the audio stream while eliminating only the conflicting textual evidence, measuring how model preference shifts under these controlled variations. They then apply activation patching to specific neurons involved in answer‑position computation, allowing them to quantify the impact of those activations on output scores. From this diagnostic they derive GACL: a rule that blends the joint and same‑audio logits according to a gating mechanism, without retraining the model.

## Results  
Across all experiments, 64.1 % of conflict samples exhibit the sign flip described in Finding 1. The activation‑patching analysis yields a Spearman correlation of 0.93 between patch effects and score differences, confirming that answer‑position computation is central to the reversal. GACL raises nAUC by 17.8 points relative to the leading contrastive baseline and, when applied to vision‑text arbitration, delivers an additional +40.5 pp improvement.

## Significance  
These findings reveal a systematic loss of audio evidence during multimodal arbitration in ALMs, offering a practical decoding correction that restores faithfulness within a 5 pp budget. The work bridges theory and deployment by providing a training‑free rule that can be integrated into existing pipelines, thereby improving downstream multimodal performance.

## Related Concepts  
Audio‑language models, arbitration, counterfactual analysis, activation patching, logit interpolation, faithfulness budget, nAUC (normalized area under the curve), vision‑text arbitration.

[[Beyond Text Following: Repairable Arbitration Reversals in Audio-Language Models]]