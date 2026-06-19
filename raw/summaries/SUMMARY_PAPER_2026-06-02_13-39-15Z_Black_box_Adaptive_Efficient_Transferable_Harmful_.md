---

title: Black-box, Adaptive, Efficient, Transferable, Harmful, Applicable... Attacks Are All You Need to Break LLMs
url: http://arxiv.org/abs/2606.03647v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-02_13-39-15Z_Black_box_Adaptive_Efficient_Transferable_Harmful_.md
generated_at: "2026-06-11 10:51"
model: nvidia/nemotron-3-nano-4b

---


## Summary  
The paper presents Indirect Harm Optimization (IHO), a black‑box, adaptive, and transferable attack for large language models that significantly outperforms existing methods. IHO is trained via iterative preference optimization against a harmfulness judge and requires only access to the target model.

## Key Takeaways  
- IHO works entirely in a black‑box setting, needing no defense‑specific details or fine‑tuning of the attacker.  
- It can serve as both a strong adaptive attack on individual behaviors and an efficient amortized policy that transfers to held‑out tasks and unseen models.  
- Even when layered defenses such as a Circuit Breaker model with an auxiliary detector are applied, IHO improves attack success compared to state‑of‑the‑art approaches.

## Context  
LLM jailbreak evaluation lacks standardized attacks like AutoAttack for images, making robustness assessments unreliable. This gap limits trustworthy risk assessment and defense comparison in the field of large language models.

## Implications  
IHO provides a practical, transferable attack that enables reliable evaluation of LLM defenses, encouraging industry practitioners to adopt robust security testing frameworks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.03647v1)
