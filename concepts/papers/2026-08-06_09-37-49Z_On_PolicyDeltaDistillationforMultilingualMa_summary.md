# Summary: 2026-08-06_09-37-49Z_On_PolicyDeltaDistillationforMultilingualMathReaso.md
Saved: 2026-08-06 22:11
Source: 2026-08-06_09-37-49Z_On_PolicyDeltaDistillationforMultilingualMathReaso.md
Model: None

---

## Summary  
The authors investigate On‑Policy Delta Distillation (OPD²), an advanced variant of on‑policy distillation that leverages the probability gap between a post‑trained teacher and its base model as a learning signal. Their goal is to apply this technique to multilingual mathematical reasoning across English, Korean, and Japanese, aiming to improve LLM performance without relying on reinforcement learning. OPD² consistently outperforms the original On‑Policy Distillation (OPD) and narrows the performance gap between English and Korean models while delivering strong gains in Japanese. The work also reveals that English‑only OPD can boost Korean/Japanese outputs but often shifts responses toward English, underscoring the need for multilingual data to preserve target‑language answers.

## Key Contributions  
- [Finding 1] On‑Policy Delta Distillation (OPD²) improves over baseline OPD and yields significant performance gains, especially in Korean and Japanese.  
- [Finding 2] English‑only OPD can increase performance for Korean and Japanese tasks but often causes the model to generate responses in English instead of preserving the target language.  
- [Finding 3] The use of the probability gap as a learning signal narrows the English–Korean performance gap, demonstrating that delta distillation is effective across languages.

## Methodology  
The authors employ an on‑policy distillation framework where a high‑quality teacher model (Qwen3) generates responses to math problems in three languages. A base model receives these outputs and updates its parameters using the probability gap between the teacher’s distribution and the base’s distribution as the training signal. The process is conducted with multilingual datasets that preserve language labels, ensuring that the delta signal reflects genuine linguistic differences rather than mere translation artifacts.

## Results  
Experiments show that OPD² consistently outperforms OPD across all three languages, with Korean and Japanese models achieving the largest absolute improvements. Moreover, the English–Korean performance gap narrows by roughly 15 % relative to baseline OPD. When only English data is used for OPD, Korean and Japanese models see modest gains (≈3‑4 %) but a noticeable shift toward English responses, indicating that multilingual grounding is crucial.

## Significance  
This research provides an efficient, off‑policy fine‑tuning method that can be applied to any multilingual LLM without the complexity of reinforcement learning. By using delta distillation, practitioners can boost reasoning abilities while maintaining language fidelity, which is vital for applications requiring precise multilingual output such as educational tools and cross‑cultural AI assistants.

## Related Concepts  
- On‑Policy Distillation (OPD)  
- Delta Distillation (using probability gap as signal)  
- Multilingual LLM fine‑tuning  
- Probability gap learning signal  
- Reinforcement learning alternatives for LLMs
