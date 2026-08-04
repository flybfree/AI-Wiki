# Summary: 2026-08-02_16-22-27Z_EviSD_Evidence_ConditionedSelf_DistillationforSear.md
Saved: 2026-08-04 00:13
Source: 2026-08-02_16-22-27Z_EviSD_Evidence_ConditionedSelf_DistillationforSear.md
Model: None

---

## Summary  
The paper introduces EviSD, an evidence‑conditioned self‑distillation framework that tackles the challenge of attributing credit in search‑augmented reinforcement learning agents. By treating supporting evidence and golden answers as privileged information for their respective actions, EviSD bridges the gap between outcome‑derived reward signals and fine‑grained action contributions. The method operates solely during training, converting the detached teacher–student discrepancy into a bounded correction applied only to generated action spans. This approach improves performance on diverse QA benchmarks without altering inference time or requiring auxiliary distillation objectives.

## Key Contributions  
- EviSD provides an evidence‑conditioned self‑distillation mechanism that distinguishes between search actions and answer actions using instance‑level evidence as privileged data.  
- The framework integrates this privileged guidance into the outcome‑based GRPO advantage, yielding a bounded correction limited to action spans only.  
- Extensive experiments across seven QA benchmarks and three model backbones demonstrate the highest macro‑average Exact Match gains while affecting response tokens minimally.

## Methodology  
The authors start with an existing search‑augmented RL agent that learns from verifiable final answers, but cannot attribute credit to individual actions. EviSD introduces a teacher‑student paradigm: during training, the student samples actions from the original context, while the same model re‑scores those actions under an action‑aligned context as a privileged teacher. The difference between the two scores is bounded and added to the outcome reward only for the generated action spans, preserving the update direction set by the final answer. No auxiliary loss or inference modifications are required.

## Results  
Across seven question‑answering benchmarks and three model backbones spanning scales from small to large, EviSD achieves the highest macro‑average Exact Match scores reported. The improvement over the strongest competing methods ranges from 1.3 to 2.3 points, with a modest token‑level impact of only 6.7%–15.1%. These gains are consistent across model sizes and generation lengths, indicating robustness.

## Significance  
By localizing privileged guidance to action spans, EviSD enhances credit assignment in multi‑turn search processes without sacrificing the simplicity of outcome‑based reinforcement learning. The method’s minimal token‑level overhead makes it practical for large language models, offering a clear path toward more interpretable and efficient agent training.

## Related Concepts  
- Outcome‑based reinforcement learning  
- Self‑distillation frameworks  
- Evidence‑conditioned learning  
- Grounded response generation  
- Action‑aligned context re‑scoring
