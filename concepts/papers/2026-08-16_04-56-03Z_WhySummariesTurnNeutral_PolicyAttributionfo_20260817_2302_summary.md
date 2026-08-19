# Summary: 2026-08-16_04-56-03Z_WhySummariesTurnNeutral_PolicyAttributionforSentim.md
Saved: 2026-08-17 23:02
Source: 2026-08-16_04-56-03Z_WhySummariesTurnNeutral_PolicyAttributionforSentim.md
Model: None

---

## Summary  
Reinforcement learning with human feedback (RLHF) is widely used to make language models generate summaries that are fluent and safe, but it inadvertently introduces a systematic “sentiment drift” that flattens emotional nuance into bland neutrality. The authors diagnose this effect as a strategic bias toward low‑risk tokens that maximize expected rewards under uncertainty in human preferences. They introduce **Policy Attribution**, a gradient‑and‑logit decomposition framework that isolates the contribution of reward‑model signals and the KL‑penalty to sentiment drift, and they propose a sentiment‑aware regularization technique that mitigates this drift while preserving summary quality. Their experiments on Reddit TL;DR and CNN/DailyMail show that RLHF summaries receive higher rewards but exhibit 30–40 % lower sentiment variance compared with non‑RLHF baselines.

## Key Contributions  
- [Finding 1] RLHF causes sentiment drift, producing overly neutral summaries with reduced emotional variation.  
- [Finding 2] Policy Attribution provides a diagnostic decomposition that attributes drift to reward‑model signals and the KL penalty.  
- [Finding 3] A sentiment‑aware regularization reduces drift by 18–22 % without harming summary quality.

## Methodology  
The authors first compare RLHF‑generated summaries with those produced by a vanilla preference‑based policy, measuring reward scores and sentiment variance across two corpora. They then apply Policy Attribution: computing gradient contributions from the reward model and KL‑penalty terms to each token’s logit, revealing which components drive sentiment suppression. A cross‑lingual study across eight languages confirms that drift is language‑independent but more pronounced in morphologically rich languages. Finally, they integrate a regularization term that penalizes low‑sentiment tokens during training, evaluating its impact on both drift reduction and summary quality.

## Results  
RLHF summaries achieve higher reward scores than baseline models (Δ ≈ +0.12) but show 30–40 % lower sentiment variance, indicating a loss of emotional nuance. The cross‑lingual analysis reveals consistent drift across languages, with morphologically complex ones experiencing greater suppression. Introducing the sentiment‑aware regularization cuts drift by 18–22 % (measured as variance reduction) while leaving ROUGE and BLEU scores unchanged, demonstrating that quality is preserved.

## Significance  
This work highlights a hidden trade‑off in RLHF: while it improves safety and fluency, it can erase the expressive richness of human‑preferred outputs. By exposing the root cause (reward‑model bias) and offering a corrective regularization, the study enables developers to retain emotionally balanced summaries—a crucial factor for applications such as news summarization or mental‑health chatbots where tone matters.

## Related Concepts  
- Reinforcement Learning from Human Feedback (RLHF)  
- Reward Model (RM)  
- KL penalty / KL divergence regularization  
- Policy Attribution (gradient & logit decomposition)  
- Sentiment drift / low‑risk token bias  
- Cross‑lingual analysis of model behavior  
- Regularization techniques for sentiment preservation
