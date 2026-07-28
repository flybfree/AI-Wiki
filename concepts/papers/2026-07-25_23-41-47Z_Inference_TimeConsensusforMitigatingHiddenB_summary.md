# Summary: 2026-07-25_23-41-47Z_Inference_TimeConsensusforMitigatingHiddenBehavior.md
Saved: 2026-07-27 20:14
Source: 2026-07-25_23-41-47Z_Inference_TimeConsensusforMitigatingHiddenBehavior.md
Model: None

---

## Summary  
The paper addresses the problem of hidden misbehavior in LLMs after fine‑tuning on poisoned or benign data, where standard defenses are insufficient. It proposes inference‑time consensus decoding to suppress source‑specific harmful behavior while preserving shared desirable behavior. By aggregating next‑token distributions from multiple datasets at decoding time, the method enforces robustness through redundancy. Experiments show that consensus decoding outperforms union training and weight averaging in suppressing targeted attacks while maintaining desirable behavior.  

## Key Contributions  
- [Finding 1] The paper introduces inference‑time consensus decoding as a redundancy‑based defense that mitigates hidden behaviors from fine‑tuning.  
- [Finding 2] It proposes two consensus decoders — token‑wise minimum and base‑relative — to handle source disagreement and partial support across datasets.  
- [Finding 3] Experiments demonstrate that consensus decoding suppresses targeted poisoning, subliminal learning, and emergent misalignment better than existing methods.  

## Methodology  
The authors collect multiple training corpora from diverse sources, fine‑tune separate reference models on each dataset, then at inference time aggregate their next‑token probability distributions. The token‑wise minimum decoder selects the smallest probability for each token across all source models, while the base‑relative decoder falls back to the original base model’s distribution when any source deviates in a conflicting direction. This redundancy forces the final output to reflect only behaviors common to all sources.  

## Results  
Experiments on controlled poisoning tasks, subliminal learning scenarios, and emergent misalignment benchmarks show that consensus decoding reduces the occurrence of source‑specific harmful outputs by up to 78 % compared with union training and weight averaging. The base model’s desirable behavior remains largely intact, and the method tolerates partial agreement across sources without sacrificing performance.  

## Significance  
This work advances robustness in LLM fine‑tuning by shifting defense from data preprocessing to inference time, offering a scalable solution that can be deployed without retraining. By leveraging multi‑source redundancy, it mitigates hidden preferences and targeted attacks that evade traditional defenses, paving the way for more reliable AI systems.  

## Related Concepts  
- Fine‑tuning poisoning  
- Subliminal learning  
- Union training  
- Weight averaging  
- Inference‑time defense  
- Consensus decoding  
- Redundancy‑based robustness
