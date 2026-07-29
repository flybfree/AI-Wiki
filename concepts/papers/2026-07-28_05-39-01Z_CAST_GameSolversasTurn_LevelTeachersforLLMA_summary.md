# Summary: 2026-07-28_05-39-01Z_CAST_GameSolversasTurn_LevelTeachersforLLMAgents.md
Saved: 2026-07-28 22:32
Source: 2026-07-28_05-39-01Z_CAST_GameSolversasTurn_LevelTeachersforLLMAgents.md
Model: None

---

## Summary  
Training large language models to act in long‑horizon games is a promising path toward generalist decision‑making, but reinforcement learning with verifiable rewards (RLVR) suffers from sparse final rewards that hide which individual decisions matter. The CAST paper proposes using the incremental changes of a game solver’s state value as cheap, turn‑level credit signals to fill this gap. By converting these scalar differences into solver advantages and injecting them directly into RLVR, the authors create a teacher‑free method for dense reward assignment. They also demonstrate that, under a soft‑optimal solver assumption, maximizing this advantage is mathematically equivalent to on‑policy distillation from the solver using only scalars rather than full logits.  

## Key Contributions  
- [Finding 1] The delta between consecutive state values of a game solver provides a reliable, low‑cost turn‑level credit signal that can replace dense reward signals in RLVR.  
- [Finding 2] Under the soft‑optimal assumption, maximizing the solver advantage is equivalent to on‑policy distillation from the solver, requiring only scalar values instead of teacher logits.  
- [Finding 3] CAST achieves the highest average zero‑shot performance across Sokoban, Minesweeper, Rush Hour, ALFWorld, and WebShop, outperforming all trained baselines in both in‑domain and unseen‑difficulty settings.  

## Methodology  
The authors first run a known game solver (e.g., for Sokoban or Minesweeper) to obtain the state value at each turn. The difference between successive values is taken as the “solver advantage” for that action, which is then added to the RLVR reward signal. This injects dense, interpretable credit into the learning process without requiring a teacher model’s full logits. The method relies on a soft‑optimal solver assumption: if the solver’s policy is close to optimal, maximizing its advantage aligns with on‑policy distillation from that policy. Because only scalar values are needed, the approach is computationally cheap and scalable for long‑horizon games.  

## Results  
CAST outperforms all previously trained baselines in every evaluated game (Sokoban, Minesweeper, Rush Hour) under both in‑domain and unseen‑difficulty conditions. Its zero‑shot performance on ALFWorld and WebShop is the highest among the methods tested, indicating strong generalization to tasks it has never seen during training. The improvements are consistent across all games, suggesting that the turn‑level credit signal is a robust augmentation for RLVR in long‑horizon settings.  

## Significance  
This work addresses a fundamental limitation of sparse reward environments by providing a cheap, interpretable teacher signal derived from game solvers. By turning solver value changes into advantage scores, CAST enables dense credit assignment without the need for high‑dimensional teacher outputs, making it suitable for scalable reinforcement learning in long‑horizon games and beyond. The findings suggest that auxiliary teacher signals can dramatically improve performance when final rewards are too sparse to guide learning effectively.  

## Related Concepts  
Long‑horizon reinforcement learning, credit assignment, sparse reward problem, on‑policy distillation, soft‑optimal assumption, value‑based teacher signals, Reinforcement Learning with Verifiable Rewards (RLVR), Sokoban, Minesweeper, Rush Hour, ALFWorld, WebShop.
