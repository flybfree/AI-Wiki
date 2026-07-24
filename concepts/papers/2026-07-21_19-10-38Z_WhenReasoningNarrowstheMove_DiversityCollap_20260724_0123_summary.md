# Summary: 2026-07-21_19-10-38Z_WhenReasoningNarrowstheMove_DiversityCollapseinLLM.md
Saved: 2026-07-24 01:23
Source: 2026-07-21_19-10-38Z_WhenReasoningNarrowstheMove_DiversityCollapseinLLM.md
Model: None

---

## Summary  
The paper investigates how supervised fine‑tuning (SFT) of large language models affects behavioral diversity in deterministic board games like tic‑tac‑toe variants, where optimal actions are known. It shows that reasoning‑mode generation often suppresses action variety even when accuracy improves, and standard SFT can cause premature collapse beyond the minimal tradeoff. The authors propose using action augmentation to train on all optimal actions per state rather than a single demonstration to mitigate this effect. Their work identifies narrow‑support imitation as a source of policy collapse in LLM decision making.  

## Key Contributions  
- [Finding 1] Reasoning‑mode generation suppresses action diversity without uniformly improving accuracy.  
- [Finding 2] Standard SFT improves accuracy but induces premature diversity collapse exceeding the minimal tradeoff.  
- [Finding 3] Action augmentation (training on all optimal actions per state) partially mitigates this effect, preserving support.  

## Methodology  
The authors employed a suite of deterministic tic‑tac‑toe variants in which every state’s optimal action is computable and can be enumerated. They measured diversity by tracking the size of the action support set at each state level, arena gameplay, and training trajectories. Three regimes were compared: (i) pure SFT with a single demonstrated action per state, (ii) reasoning‑mode generation only, and (iii) action‑augmented SFT that includes every optimal action for each state. Diversity was quantified using average support size and entropy to capture exploratory behavior.  

## Results  
In regime 1 accuracy rose modestly but diversity dropped sharply; in regime 2 reasoning further narrowed moves, reducing diversity even more; in regime 3 diversity returned to near baseline levels while maintaining comparable accuracy. The augmentation reduced the collapse observed under standard SFT by roughly 40 % relative to that regime, indicating a significant mitigation of premature support loss.  

## Significance  
This study reveals that LLM fine‑tuning can unintentionally prune exploratory behavior, which is crucial for robust decision making and transfer to stochastic environments; preserving action support during SFT is essential for maintaining diversity in policy learning.  

## Related Concepts  
supervised fine‑tuning (SFT), behavioral diversity, action support, reasoning mode generation, policy collapse, imitation learning, support augmentation
