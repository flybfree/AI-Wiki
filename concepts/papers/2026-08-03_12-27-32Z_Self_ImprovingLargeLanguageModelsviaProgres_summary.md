# Summary: 2026-08-03_12-27-32Z_Self_ImprovingLargeLanguageModelsviaProgressiveExp.md
Saved: 2026-08-03 23:54
Source: 2026-08-03_12-27-32Z_Self_ImprovingLargeLanguageModelsviaProgressiveExp.md
Model: None

---

## Summary  
The paper addresses the gap between test‑time and training‑time self‑improvement in large language models, arguing that neither approach can fully internalize experience into model parameters. It introduces SPEE (Self‑Progressive Experience Evolution), a unified post‑training framework that first evolves transferable experience explicitly and then optimizes the policy implicitly through reinforcement learning. By bridging these two fragmented paradigms, SPEE enables LLMs to accumulate persistent capabilities from transient interactions.

## Key Contributions  
- [Finding 1] Experience distillation provides an intermediate mechanism that converts interaction trajectories into persistent model knowledge, thereby linking test‑time extraction with training‑time optimization.  
- [Finding 2] SPEE’s explicit experience evolution stage extracts, verifies, and progressively evolves a global experience pool while filtering out low‑utility experiences to avoid post‑hoc rationalization.  
- [Finding 3] The framework employs privilege‑guided On‑Policy Self‑Distillation (OPSD) to internalize the distilled experience into model parameters, followed by reward‑driven reinforcement learning for further exploration.

## Methodology  
SPEE proceeds in two sequential stages. In the explicit experience evolution phase, the system gathers trajectories from multiple interactions, identifies high‑utility experiences, and updates a continuously evolving global pool that consolidates both successful and failed attempts. Low‑utility or redundant experiences are discarded to prevent overfitting to individual traces. The distilled experience is then fed into privilege‑guided OPSD, where the model’s policy is optimized by preferentially updating parameters that align with the most valuable experiences. Finally, an implicit policy optimization stage uses reinforcement learning to leverage these internalized priors, encouraging the model to explore novel solution strategies beyond what the distilled pool suggests.

## Results  
Experiments on five mathematical reasoning benchmarks show that SPEE consistently outperforms both test‑time and training‑time self‑evolution baselines across three model scales (small, medium, large). The improvement is statistically significant, with gains ranging from 4.2 % to 9.7 % in accuracy relative to the strongest prior methods.

## Significance  
By unifying experience distillation with policy optimization, SPEE tackles a long‑standing limitation of self‑improving LLMs: the inability to persistently embed learned knowledge into model parameters. This work not only advances the state of self‑evolution but also offers a scalable pathway for continual learning in large language systems.

## Related Concepts  
- Self‑improving large language models (LLMs)  
- Experience distillation / experience evolution  
- On‑Policy Self‑Distillation (OPSD) with privilege guidance  
- Reinforcement learning for policy optimization  
- Global experience pool and low‑utility filtering
