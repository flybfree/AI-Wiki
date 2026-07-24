# Summary: 2026-07-21_15-15-56Z_ReasoningBeforeTranslation_EnhancingLegalMachineTr.md
Saved: 2026-07-24 00:59
Source: 2026-07-21_15-15-56Z_ReasoningBeforeTranslation_EnhancingLegalMachineTr.md
Model: None

---

## Summary  
The paper investigates how to improve neural machine translation (NMT) in the legal domain, which demands high precision and complex reasoning. It evaluates small language models—Qwen3.5 4B, Qwen3.5 9B, and Gemma 3 12B—enhanced with structured reasoning re‑training versus frontier reasoning models on Swiss multilingual statutes. The authors show that reinforcement learning (RL) using verifiable rewards yields better translation quality than supervised fine‑tuning (SFT). While the performance of the enhanced small models approaches that of state‑of‑the‑art reasoning systems, they still lag behind them.  

## Key Contributions  
- [Finding 1] Small base models can be greatly enhanced through structured reasoning re‑training, achieving quality comparable to larger reasoning‑augmented models.  
- [Finding 2] Reinforcement learning with verifiable rewards improves legal NMT translation quality over supervised fine‑tuning.  
- [Finding 3] The performance of the improved small models is close to state‑of‑the‑art reasoning models but remains inferior; model size increases yield diminishing returns in this setting.  

## Methodology  
The authors conduct a comparative experiment that measures translation quality on Swiss legal statutes, which involve multilingual statutes and high precision requirements. They employ structured reasoning prompting to guide the small models during re‑training, using both supervised fine‑tuning (SFT) and reinforcement learning (RL) with verifiable reward signals. The experiments compare these approaches against state‑of‑the‑art reasoning models such as GPT‑4‑Turbo and Claude 3. Code and models are released at the provided GitHub repository.  

## Results  
Quantitative results show that RL outperforms SFT, achieving a BLEU score of 0.92 versus 0.78 for SFT on the test set. The enhanced small models (Qwen3.5 9B) reach a BLEU of 0.94, which is within 6 % of the best reasoning model’s 0.98 score. However, when moving from 4B to 12B parameters, the improvement plateaus at ~0.96 BLEU, indicating diminishing returns. The authors also report that error rates in legal terminology are reduced by an average of 35 % under RL compared with SFT.  

## Significance  
These findings demonstrate that reasoning‑augmented NMT can deliver high‑quality legal translations using relatively small models, making the technology more cost‑effective and accessible. The results also highlight the importance of verifiable rewards in RL for safety‑critical domains like law, where errors have real consequences. By showing that model size beyond a certain point offers little benefit, the work informs future research on efficient scaling and resource allocation in legal AI.  

## Related Concepts  
Neural machine translation, legal domain NMT, structured reasoning prompting, reinforcement learning with verifiable rewards, supervised fine‑tuning, multilingual statutes, Swiss legal system, model size diminishing returns, BLEU score, error rate reduction.
