# Summary: 2026-07-29_12-33-12Z_ThinkingUnderUncertainty_EvidenceUseandInformation.md
Saved: 2026-07-29 20:33
Source: 2026-07-29_12-33-12Z_ThinkingUnderUncertainty_EvidenceUseandInformation.md
Model: None

---

## Summary  
The paper investigates how large language models (LLMs) use available evidence versus seek additional information when making decisions under uncertainty. By comparing thinking and non‑thinking modes in a controlled two‑armed bandit setting, the authors show that thinking improves current evidence exploitation but does not necessarily drive more systematic information‑seeking behavior. The study reveals distinct cognitive signatures—value‑guided action and reduced noise—that are independent of exploration heuristics such as UCB or Thompson sampling.

## Key Contributions  
- [Finding 1] Thinking strengthens value‑guided actions and reduces uncertainty‑independent choice noise, yet does not generate stronger UCB‑like exploration or enhanced Thompson‑like variability.  
- [Finding 2] The information‑imbalanced history condition, which provides more observations than the balanced condition, is linked to longer thinking lengths; reported confidence becomes more sensitive to decision difficulty and correlates with the evidence actually used.  
- [Finding 3] Decoder sweeps (e.g., temperature) alter both choice noise and thinking length, but they fail to reproduce a joint pattern that would indicate a coordinated shift toward information‑seeking.

## Methodology  
The authors conducted ten open‑weight LLMs in matched horizon‑style two‑armed bandit trials under both thinking and non‑thinking modes. Each trial measured action preference, the length of internal reasoning, and reported confidence while maintaining constant uncertainty. A cognitive model separated value‑guided actions from noise that is independent of uncertainty, identifying two behavioral exploration signatures: a UCB‑like preference for the less‑seen arm and Thompson‑like variability that grows with total uncertainty.

## Results  
On average, thinking improved alignment between chosen arms and current evidence while decreasing random noise. No evidence emerged for stronger UCB or Thompson exploration patterns. The information‑imbalanced condition produced longer thinking durations than the balanced counterpart. Reported confidence varied more with decision difficulty and was tightly bound to the amount of task evidence used. Decoder sweeps affected both choice noise and thinking length but did not reproduce a consistent cross‑output relationship, indicating that temperature alone cannot explain the observed joint effect.

## Significance  
These findings clarify that thinking in LLMs primarily enhances exploitation of present information rather than prompting a systematic shift toward more aggressive information seeking. The results support interpretations linking thinking length to metacognitive control and confidence to metacognitive monitoring, offering insights for designing policies that balance exploration and exploitation.

## Related Concepts  
Two‑armed bandit, UCB (Upper Confidence Bound), Thompson sampling, information‑imbalanced history, uncertainty, choice noise, thinking length, reported confidence, cognitive model, value‑guided action, metacognitive control, metacognitive monitoring.
