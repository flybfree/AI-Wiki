# Summary: 2026-08-05_17-41-31Z_ABSeeker_TrainingLong_HorizonSearchAgentsviaAnswer.md
Saved: 2026-08-05 22:34
Source: 2026-08-05_17-41-31Z_ABSeeker_TrainingLong_HorizonSearchAgentsviaAnswer.md
Model: None

---

## Summary  
The paper proposes ABSeeker, a framework for training long‑horizon search agents that distinguishes useful actions from errors by converting sparse trajectory outcomes into dense step‑level supervision through answer‑backtracked credit assignment. It enables fine‑grained reinforcement learning on a 4B model with only 8.5 k examples, achieving performance comparable to larger models. The approach integrates supervised fine‑tuning and policy optimization using the derived step scores.

## Key Contributions  
- Introduces Answer‑Backtracked Credit Assignment (ABC), a method that traces clues back from the answer to generate dense binary rewards for each search step.  
- Develops ABC‑SFT, which reweights the loss of each turn according to these step‑level scores, and ABC‑GRPO, which uses them as policy rewards in gradient policy optimization.  
- Demonstrates that ABSeeker reaches 37.3 % on BrowseComp (55.3 % with context management) and 39.1 % on BrowseComp‑ZH (52.9 % with context), matching or surpassing agents of comparable scale.

## Methodology  
The authors first perform Answer‑Backtracked Clue Recovery, reconstructing intermediate clues from a ground‑truth answer to guide the search trajectory. Next, they apply Clue‑Anchored Step Scoring to evaluate each action against these clues, producing dense step‑level rewards. These scores are incorporated into ABC‑SFT by reweighting the loss function and into ABC‑GRPO as the reward signal for policy updates. The framework is applied to Qwen3.5‑4B with 8.5 k training examples.

## Results  
ABSeeker attains a BrowseComp score of 37.3 % (55.3 % when context management is added) and a BrowseComp‑ZH score of 39.1 % (52.9 % with context). These results exceed those of same‑scale agents and approach the performance of ~30B models, showing that fine‑grained credit assignment can significantly boost long‑horizon search capability.

## Significance  
By deriving step‑level rewards from sparse answer outcomes, ABSeeker eliminates the need for large datasets or massive model sizes to train effective long‑horizon search agents. This efficient fine‑grained credit assignment opens a path toward high‑performing retrieval and reasoning systems that can operate with minimal resources.

## Related Concepts  
- Long‑horizon search agents  
- Answer backtracking  
- Clue recovery  
- Step‑level supervision  
- Reward modeling  
- Fine‑grained credit assignment  
- Supervised fine‑tuning (SFT)  
- Reinforcement learning with gradient policy optimization (GRPO)
