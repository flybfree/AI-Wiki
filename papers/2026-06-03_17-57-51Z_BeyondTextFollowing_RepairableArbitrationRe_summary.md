---
title: "Summary: 2026-06-03_17-57-51Z_BeyondTextFollowing_RepairableArbitrationReversals.md"
date: 2026-06-03
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-03_17-57-51Z_BeyondTextFollowing_RepairableArbitrationReversals.md


**Source**: [Original Paper](http://arxiv.org/abs/2606.05161v1)
Saved: 2026-06-04 00:01
Source: 2026-06-03_17-57-51Z_BeyondTextFollowing_RepairableArbitrationReversals.md
Model: None

---


## Summary  
Audio‑language models (ALMs) frequently ignore clear audio evidence when it conflicts with textual input, raising the question of whether the audio signal is merely unavailable or is encoded but lost during arbitration. The authors investigate this by using same‑audio counterfactuals that keep the audio fixed while removing only the conflicting text, and they propose a training‑free decoding rule—Gated Audio Counterfactual Logit Correction (GACL)—to recover the suppressed audio influence within a strict faithfulness budget.

## Semantic links
- [[concepts/papers/2026-06-18_15-35-40Z_AutoPass_Evidence_GuidedLLMAgentsforCompile_summary.md|Summary: 2026-06-18_15-35-40Z_AutoPass_Evidence_GuidedLLMAgentsforCompilerPerfor.md]] — 3 title terms overlap; shared tags: ai, paper, research; 8 summary/topic terms overlap
- [[concepts/papers/2026-06-10_17-52-15Z_TAHOE_Text_to_SQLwithAutomatedHintOptimizat_summary.md|Summary: 2026-06-10_17-52-15Z_TAHOE_Text_to_SQLwithAutomatedHintOptimizationfrom.md]] — 3 title terms overlap; shared tags: ai, paper, research; 6 summary/topic terms overlap
- [[concepts/papers/2026-06-15_17-52-27Z_DEEPRUBRIC_Evidence_TreeRubricSupervisionfo_summary.md|Summary: 2026-06-15_17-52-27Z_DEEPRUBRIC_Evidence_TreeRubricSupervisionforEffici.md]] — 3 title terms overlap; shared tags: ai, paper, research; 5 summary/topic terms overlap

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

- [[concepts/llm-models/llm-models-hub.md|LLM Models Hub]]
- [[concepts/multimodal-ai/multimodal-ai-hub.md|Multimodal AI Hub]]
- [[concepts/software-development/software-development-hub.md|Software Development Hub]]
- [[concepts/alignment-safety/alignment-hub.md|Alignment Hub]]
