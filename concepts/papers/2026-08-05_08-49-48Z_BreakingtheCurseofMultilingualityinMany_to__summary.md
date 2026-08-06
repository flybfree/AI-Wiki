# Summary: 2026-08-05_08-49-48Z_BreakingtheCurseofMultilingualityinMany_to_ManySpe.md
Saved: 2026-08-05 22:25
Source: 2026-08-05_08-49-48Z_BreakingtheCurseofMultilingualityinMany_to_ManySpe.md
Model: None

---

## Summary  
Multimodal large language models have shown promise for speech‑to‑text translation across many languages, but a single shared encoder creates a “curse of multilinguality,” where high‑resource languages dominate and low‑resource ones suffer. This paper introduces MSRT, a resource‑aware Mixture of Speech Encoders (MoSE) that mitigates this imbalance by routing each utterance to an appropriate expert encoder. The framework also employs a five‑stage curriculum learning strategy that dramatically reduces the amount of paired data needed per language. Experiments on 45 languages demonstrate that MoSE improves performance for high, medium, and low‑resource speech simultaneously, breaking the curse without sacrificing top‑tier results.

## Key Contributions  
- [Finding 1] A resource‑aware Mixture of Speech Encoders (MoSE) with an explicit language router that separates a frozen high‑resource expert from a trainable medium/low‑resource expert.  
- [Finding 2] A five‑stage curriculum learning protocol that aligns utterances across languages using only about ten hours of paired S2TT data per language, drastically lowering data dependence.  
- [Finding 3] The MoSE model achieves state‑of‑the‑art performance on all 45 × 44 translation directions while delivering the largest gains for low‑resource languages.

## Methodology  
The authors address multilingual S2TT by constructing a mixture of experts where each expert is specialized to a language group. A frozen high‑resource encoder preserves its strong capabilities, while a trainable expert adapts to medium and low‑resource speech. The language router assigns an utterance to the most suitable expert based on estimated resource level. Curriculum learning proceeds through five stages: (1) pre‑training each expert individually, (2) joint fine‑tuning with balanced batches, (3) progressive data augmentation, (4) domain‑specific adaptation, and (5) final cross‑lingual transfer. This staged approach reduces the need for extensive paired S2TT data, making MoSE feasible even for languages with scarce resources.

## Results  
A 4 billion‑parameter MoSE model outperforms larger baselines across all language pairs tested on a benchmark of 45 languages. Empirical analyses reveal consistent improvements: high‑resource languages retain their strong performance, medium‑resource languages see moderate gains, and low‑resource languages experience the most substantial boosts. The five‑stage curriculum cuts required paired data from hundreds of hours to roughly ten per language, confirming the method’s efficiency.

## Significance  
By decoupling representation capacity among languages through a resource‑aware mixture, MoSE breaks the curse of multilinguality without penalizing high‑resource models. This enables consistent, high‑quality speech‑to‑text translation across the entire spectrum of linguistic resources, fostering broader adoption of multilingual S2TT systems and encouraging more equitable AI development.

## Related Concepts  
- Multilingual speech‑to‑text translation (S2TT)  
- Curse of multilinguality in shared encoders  
- Mixture of Experts (MoE) architectures  
- Resource‑aware training strategies  
- Curriculum learning for limited data scenarios
