# Summary: 2026-08-16_04-56-03Z_WhySummariesTurnNeutral_PolicyAttributionforSentim.md
Saved: 2026-08-17 22:54
Source: 2026-08-16_04-56-03Z_WhySummariesTurnNeutral_PolicyAttributionforSentim.md
Model: None

---

## Summary  
This paper investigates why reinforcement learning from human feedback (RLHF) causes summaries to become overly neutral, stripping away emotional nuance and reducing sentiment variance by 30–40%. The authors identify RL as a strategic bias toward "low-risk" tokens that maximize expected rewards under preference uncertainty. To diagnose this drift, they introduce Policy Attribution, a framework that decomposes policy changes into contributions from the reward model (RM) signals and the KL divergence penalty. Their analysis reveals sentiment drift is language-independent but more pronounced in morphologically rich languages, where summaries are disproportionately suppressed.

## Key Contributions  
- [Finding 1] RLHF induces sentiment drift by favoring low-risk tokens to maximize expected rewards under preference uncertainty, leading to overly neutral summaries with reduced emotional variance.  
- [Finding 2] Policy Attribution decomposes policy changes into RM signal and KL penalty contributions, enabling precise attribution of sentiment drift to specific components of the training objective.  
- [Finding 3] Sentiment-aware regularization reduces sentiment drift by 18–22% across eight languages without compromising summary quality.

## Methodology  
The authors approached sentiment drift as a policy optimization problem where the RL agent, guided by human preferences via an RM, inadvertently suppresses emotional content. They applied Policy Attribution to decompose the policy gradient into two parts: one driven by the reward model’s preference signals and another from the KL divergence penalty that enforces distribution consistency with the training data. By analyzing summaries on Reddit TL;DR and CNN/DailyMail datasets across eight languages, they measured how RL affects sentiment variance and identified that morphologically complex languages experience stronger suppression. The proposed sentiment-aware regularization adds a constraint to limit excessive reward-seeking behavior, thereby preserving emotional nuance.

## Results  
Across all experiments, the baseline RLHF summaries showed 30–40% lower sentiment variance compared to human-written summaries, confirming the drift effect. Policy Attribution revealed that RM signals dominate policy changes in early training phases but gradually give way to KL penalties as the model stabilizes. The sentiment-aware regularization technique successfully reduced drift by 18–22%, with minimal impact on BLEU or ROUGE scores. Notably, the reduction was consistent across languages, though morphologically rich languages like Russian and Arabic showed the largest improvements in emotional retention.

## Significance  
This work matters because RLHF, widely used to align LLMs with human preferences, inadvertently creates summaries that are too bland for real-world applications requiring emotional expressiveness. By exposing sentiment drift as a systematic bias rather than an artifact, the authors provide a diagnostic tool (Policy Attribution) and a corrective mechanism (sentiment-aware regularization), enabling more nuanced and contextually appropriate outputs.

## Related Concepts  
- Reinforcement Learning from Human Feedback (RLHF)  
- Sentiment drift  
- Policy attribution  
- KL divergence penalty  
- Reward model signal  
- Preference uncertainty  
- Morphological richness in language
