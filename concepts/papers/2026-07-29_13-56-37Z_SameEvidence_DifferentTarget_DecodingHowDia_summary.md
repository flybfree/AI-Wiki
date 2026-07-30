# Summary: 2026-07-29_13-56-37Z_SameEvidence_DifferentTarget_DecodingHowDiagnostic.md
Saved: 2026-07-29 22:27
Source: 2026-07-29_13-56-37Z_SameEvidence_DifferentTarget_DecodingHowDiagnostic.md
Model: None

---

## Summary  
The paper investigates how the same diagnostic evidence can support one causal claim yet be irrelevant to another, highlighting that answer quality depends on the target population, outcome, estimand, or identifying assumption rather than merely matching the evidence. By creating paired prompts that reuse identical diagnostic text while altering the causal question’s target, the authors test whether language‑model hidden states encode linear information about whether the evidence favors, challenges, or fails to address that target. Their analysis shows that a simple readout of the penultimate transformer block can decode this relationship with high accuracy and recover many correct pairs across multiple model checkpoints. This work demonstrates that diagnostic evidence is not a universal signal but carries nuanced causal meaning that varies by context.

## Key Contributions  
- [Finding 1] The hidden state from the penultimate transformer block contains linearly decodable information about whether diagnostic evidence favors, challenges, or fails to address the causal target.  
- [Finding 2] Paired‑prompt benchmark yields balanced accuracy of 0.654–0.659 and recovers 18–21 correct pairs out of 49, exceeding permutation nulls that preserve scenario groups.  
- [Finding 3] Readouts trained without development examples still recover at least one pair from each diagnostic family, showing robustness to limited supervision.

## Methodology  
The authors constructed a paired‑prompt dataset where each prompt repeats the same verbatim diagnostic evidence while changing the causal target; prompts are labeled Favors, Challenges, Unresolved, or Wrong Target based on how the evidence relates to that target. They trained linear readouts on a separate development set using the final‑token hidden state from the penultimate block of Qwen2.5‑7B‑Instruct, Qwen3‑8B, and Llama‑3.1‑8B‑Instruct. Balanced accuracy is computed per prompt pair, and complete‑pair recovery (both prompts correctly labeled) is measured. The readout’s performance is compared to a linear classifier on answer‑option logits and text baselines.

## Results  
Balanced accuracy ranges from 0.654 to 0.659 across the nine diagnostic families; 18–21 pairs are recovered, with two reviewers agreeing on 95 of 98 prompts (96.9%). Full‑prompt balanced accuracy exceeds restricted‑input baselines, and paired‑bootstrap intervals for differences are above zero. Readouts trained without development examples recover 21 pairs, including at least one from each family. The hidden‑state readout outperforms linear classifiers in both balanced accuracy and recovered pairs.

## Significance  
These findings reveal that diagnostic evidence is context‑dependent: the same outcome can be a valid causal inference for some populations but not others, and language models encode this nuance in their hidden states. By demonstrating that simple readouts can decode such nuanced relationships, the work advances interpretability of large‑language‑model outputs and informs more robust causal reasoning in AI.

## Related Concepts  
- Diagnostic evidence  
- Causal questions  
- Estimands and populations  
- Linear readout decoding  
- Transformer hidden states
