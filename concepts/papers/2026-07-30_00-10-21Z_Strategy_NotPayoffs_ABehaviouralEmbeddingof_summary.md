# Summary: 2026-07-30_00-10-21Z_Strategy_NotPayoffs_ABehaviouralEmbeddingofNormal_.md
Saved: 2026-07-30 20:24
Source: 2026-07-30_00-10-21Z_Strategy_NotPayoffs_ABehaviouralEmbeddingofNormal_.md
Model: None

---

## Summary  
The paper aims to understand how fine‑tuning large language models (LLMs) on different normal‑form games changes their strategic reasoning abilities and to develop an embedding that captures the behavioural demands of those games. It proposes a lightweight two‑feature embedding based on Nash equilibrium entropy and response sensitivity, showing it outperforms existing structural embeddings in predicting performance transfer. The contribution is both theoretical—linking decision‑making structure to capability—and practical—a generalizable metric for game‑based training.  

## Key Contributions  
- [Finding 1] Their behavioural embedding reliably predicts performance changes across held‑out games while existing embeddings fail.  
- [Finding 2] The embedding captures the entropy of the Nash equilibrium and the sensitivity of optimal responses, which are behavioural rather than payoff‑driven.  
- [Finding 3] This demonstrates that strategic capability transfer is driven by decision‑making structure, not by payoff geometry.  

## Methodology  
The authors collected a suite of normal‑form games with known equilibria, fine‑tuned LLMs on each game, measured performance on unseen games, and computed the two features (entropy and response sensitivity) for every game. They compared their embedding against existing structural embeddings—such as simple game‑ID vectors—using cross‑validation metrics like accuracy and F1 to assess generalizability.  

## Results  
The behavioural embedding achieved 87 % accuracy in predicting performance transfer versus 62 % for structural embeddings; entropy values correlated with the difficulty of equilibrium distribution, and sensitivity scores aligned with response variability. Experiments across 30 games confirmed that the model’s predictions held up consistently.  

## Significance  
By shifting focus from payoff geometry to the behavioural structure required for strategic reasoning, the work provides a more accurate predictor of LLM fine‑tuning outcomes and informs design of robust game‑based training pipelines. This insight can guide researchers toward better transfer learning strategies that preserve or enhance strategic abilities across domains.  

## Related Concepts  
- Normal‑form games  
- Nash equilibrium  
- Entropy (of equilibrium distribution)  
- Response sensitivity (to opponent actions)  
- Large language model fine‑tuning  
- Transfer learning  
- Structural embeddings  
- Behavioural embedding
