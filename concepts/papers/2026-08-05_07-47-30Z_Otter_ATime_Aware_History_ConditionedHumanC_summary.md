# Summary: 2026-08-05_07-47-30Z_Otter_ATime_Aware_History_ConditionedHumanChessAI.md
Saved: 2026-08-06 21:40
Source: 2026-08-05_07-47-30Z_Otter_ATime_Aware_History_ConditionedHumanChessAI.md
Model: None

---

## Summary  
Otter is a compact, human‑level chess AI that predicts the next move of a player by modeling play as a sequential process rather than evaluating each position in isolation. It leverages two conditioning signals: a move‑history encoder that captures the last 20 moves and the time‑control module that reflects clock pressure. The model is trained on an unprecedented 6.1 billion positions from Lichess rapid games, achieving state‑of‑the‑art performance with far fewer parameters than prior systems like Maia 2. This work demonstrates that a time‑aware, history‑conditioned approach can outperform position‑only models while using less data and compute.

## Key Contributions  
- [Finding 1] Otter’s move‑history encoder effectively captures opening preferences, positional drift, and intra‑game behavioral tendencies by conditioning on the last 20 moves.  
- [Finding 2] The time‑control module modulates predictions based on clock pressure, enabling the model to adapt to time‑sensitive phases of a game.  
- [Finding 3] Otter reaches 55.23 % top‑1 and 90.95 % top‑5 move‑prediction accuracy with only 15.3 M parameters, surpassing Maia 2 on the same benchmark.

## Methodology  
The authors treat a chess game as a time‑aware sequential process. First, they construct a dataset of 6.1 billion positions from 117 million Lichess rapid games spanning 30 days, encoding each position with its move history (last 20 moves) and the current clock state. A transformer‑based model with 15.3 M parameters is trained to predict the next move given these two conditioning signals. Training occurs on a single T4 GPU, allowing rapid iteration and full reproducibility.

## Results  
Across all Elo brackets from <1100 up to ≥2000, Otter attains peak accuracy of 57.38 % at the 1900‑1999 bracket. The model’s top‑1 prediction rate is 55.23 % and its top‑5 rate is 90.95 %, both exceeding Maia 2’s performance on the same dataset. These results are reported with complete training logs, code, and models publicly released.

## Significance  
By modeling chess as a time‑aware, history‑conditioned activity, Otter shows that sequential context can improve human‑level prediction without sacrificing model size or data efficiency. This approach could inspire other domains where temporal dynamics matter, such as language generation or game AI, offering a template for more accurate and lightweight agents.

## Related Concepts  
- Sequential modeling  
- Move‑history encoder  
- Time‑control module  
- Transformer architecture  
- Human‑level performance benchmarking
