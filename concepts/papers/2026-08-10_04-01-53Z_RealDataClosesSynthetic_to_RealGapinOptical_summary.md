# Summary: 2026-08-10_04-01-53Z_RealDataClosesSynthetic_to_RealGapinOpticalChemica.md
Saved: 2026-08-10 23:35
Source: 2026-08-10_04-01-53Z_RealDataClosesSynthetic_to_RealGapinOpticalChemica.md
Model: None

---

## Summary  
The paper investigates why optical chemical‑structure recognition, which is already high on synthetic renders, degrades sharply when applied to real documents such as patents and journal figures. By systematically fine‑tuning a set of vision‑language models (VLMs) with mixtures of synthetically rendered structures and labeled real depictions, the authors demonstrate that incorporating even a modest amount of genuine data can dramatically improve exact‑match scores on benchmark datasets. Their experiments reveal that the choice of base model together with the proportion of real training data jointly determines performance gains, while certain adaptation strategies (e.g., LoRA) are more effective for some models than others. The work shows that the synthetic‑to‑real gap is largely closed when real data is integrated into the fine‑tuning pipeline.

## Key Contributions  
- Real‑world labeled images substantially boost exact‑match accuracy on ACS, CLEF‑IP, USPTO and other benchmarks, especially for Qwen2.5‑VL‑7B where performance rises from 0.15 to 0.46.  
- The value of a vision‑tower LoRA varies across base models: it is ineffective for Qwen (+0.00) but yields large gains (≈ +23 pt) for InternVL3‑8B and modest improvements for GLM‑4.1V‑9B, indicating that adaptation must be matched to the underlying model architecture.  
- The optimal configuration reaches 0.96 exact match on clean synthetic renders and achieves 0.49–0.84 on real benchmarks, establishing a new state of the art for optical chemical‑structure recognition.

## Methodology  
The authors selected 21 existing recognizers that rely on vision‑language models (e.g., Qwen2.5‑VL‑7B, InternVL3‑8B, GLM‑4.1V‑9B) and fine‑tuned them using mixtures of synthetic renders and real images sourced from patents, journal figures, and hand‑drawn collections. They varied three hyper‑parameters: the VLM base model, the fraction of real training data (ranging from 0 % to 50.2 %), and the vision‑tower adaptation strategy (plain fine‑tuning versus LoRA). Experiments were conducted on synthetic‑only, synthetic‑real mixtures, and fully real datasets to isolate the impact of each factor.

## Results  
On ACS exact match, Qwen2.5‑VL‑7B improved from 0.15 with no real data to 0.37 at 9.5 % real data and 0.46 at 50.2 %. Across three base models the trend is consistent: adding more real images reduces performance gaps between models (from 0.21 without real data down to 0.06 with 70 % real data). The LoRA adaptation adds +22.8–+34.6 points for InternVL3‑8B but not for Qwen (+0.00, p=1.00). The best overall configuration yields 0.96 exact match on clean renders and scores of 0.49 (ACS), 0.65 (CLEF‑IP), 0.84 (UOB) and 0.76 (USPTO).

## Significance  
By proving that real data can close the synthetic‑to‑real gap, this research provides a practical pathway for deploying chemical‑structure recognizers in high‑stakes domains such as patent analysis, scientific literature mining, and regulatory compliance where only unlabeled images are available. The findings also guide model selection and adaptation strategies, saving computational resources by avoiding unnecessary fine‑tuning on synthetic data alone.

## Related Concepts  
- Optical chemical structure recognition (OCSR)  
- Vision‑language models (VLMs) such as Qwen2.5‑VL‑7B, InternVL3‑8B, GLM‑4.1V‑9B  
- Fine‑tuning and LoRA (Low‑Rank Adaptation) for vision‑tower adaptation  
- Exact match metric for image classification tasks  
- Synthetic vs. real data in machine learning experiments
