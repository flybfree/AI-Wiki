# Summary: 2026-07-21_15-15-56Z_ReasoningBeforeTranslation_EnhancingLegalMachineTr.md
Saved: 2026-07-24 01:18
Source: 2026-07-21_15-15-56Z_ReasoningBeforeTranslation_EnhancingLegalMachineTr.md
Model: None

---

## Summary  
The paper investigates how reasoning‑capable language models can be combined with small neural machine translation (NMT) systems for legal texts, focusing on the Swiss multilingual statute domain where linguistic precision is critical. It evaluates three approaches—supervised fine‑tuning, reinforcement learning (RL) with verifiable rewards, and scaling up model size—to determine which yields the best translation quality. The contribution is that RL can significantly boost the performance of modest base models and even approach state‑of‑the‑art reasoning models.

## Key Contributions  
- Finding 1: Reinforcement learning with verifiable rewards outperforms supervised fine‑tuning on legal NMT tasks, delivering higher BLEU scores.  
- Finding 2: Small language models (Qwen3.5 4B, Qwen3.5 9B, Gemma 3 12B) can achieve translation quality close to large reasoning models when enhanced via RL.  
- Finding 3: Increasing model size yields diminishing returns; performance plateaus after moving from 4B to 9B parameters.

## Methodology  
The authors constructed a benchmark of Swiss legal statutes translated into French and German, using parallel corpora as training data. They fine‑tuned base models with supervised fine‑tuning (SFT) and RL where the reward function is derived from human judges rating translation adequacy and consistency. Model scaling experiments compared small vs. large models to assess diminishing returns.

## Results  
Supervised fine‑tuning achieved baseline performance, while RL improved BLEU scores by roughly 12 % over SFT and was within 3 % of the best reasoning model (e.g., GPT‑4). Performance did not improve further when moving from a 4B to a 9B model, indicating diminishing returns. The strongest small model matched the top reasoning model in quality.

## Significance  
This work shows that structured reasoning can be integrated into smaller legal NMT systems, lowering computational cost while preserving high accuracy and providing a practical pathway for deploying RL‑enhanced translation without massive models.

## Related Concepts  
Neural machine translation, reinforcement learning, verifiable rewards, small language models, legal domain, multilingual statutes, BLEU score, state‑of‑the‑art reasoning models.
