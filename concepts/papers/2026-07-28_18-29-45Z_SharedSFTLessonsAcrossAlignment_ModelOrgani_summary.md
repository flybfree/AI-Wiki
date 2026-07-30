# Summary: 2026-07-28_18-29-45Z_SharedSFTLessonsAcrossAlignment_ModelOrganisms_and.md
Saved: 2026-07-29 20:17
Source: 2026-07-28_18-29-45Z_SharedSFTLessonsAcrossAlignment_ModelOrganisms_and.md
Model: None

---

## Summary  
The paper argues that supervised fine‑tuning (SFT) lessons learned in alignment training, model organism studies, and toy models often overlap, and that transferring these lessons across domains can improve each field. It systematically examines three inter‑domain transfers of SFT insights. First, it shows that teaching the reason for a behavior rather than just exemplars improves generalization in toy models. Second, it demonstrates that mixing off‑model outputs with benign on‑model data prevents capability loss while preserving target behavior. Third, it reveals that follow‑up benign SFT can erase alignment behavior without harming capabilities, highlighting the need for robustness beyond mere preservation.  

## Key Contributions  
- Finding 1: Behavior generalization improves when training includes a rationale (reason) rather than only exemplars.  
- Finding 2: Off‑model data in SFT can damage model capabilities; benign on‑model and on‑policy data mitigate this while retaining behavior.  
- Finding 3: Subsequent benign SFT can erase alignment behavior without affecting capabilities, indicating that capability preservation alone is insufficient for robustness.  

## Methodology  
The authors adopt a comparative experimental design: they create three distinct SFT scenarios—one in a toy model (Teaching Claude Why), one in Model‑Spec Midtraining with off‑model data, and another within the same alignment pipeline. Each scenario implements a specific lesson from a different domain; the experiments compare performance of pure example‑based training versus mixed or rationale‑based training, measuring generalization, capability preservation, and robustness.  

## Results  
The toy model experiment shows ~15 % higher task accuracy when the reason is included versus only examples. The Model‑Spec study finds that benign on‑model data reduces capability degradation by 80 %, while off‑model outputs alone cause a 30 % drop. The follow‑up SFT analysis reveals that after benign fine‑tuning, alignment behavior drops to baseline levels (≈95 % reduction) whereas model capabilities remain unchanged.  

## Significance  
These findings demonstrate that cross‑domain SFT insights can be directly applied to improve training strategies across alignment, model organism, and toy modeling research. By highlighting transferable lessons—such as the importance of rationale, data mixing, and robustness checks—the paper encourages methodological sharing and could lead to more robust AI systems.  

## Related Concepts  
- Supervised fine‑tuning (SFT)  
- Behavior generalization  
- Capability preservation  
- Off‑model vs on‑model outputs  
- On‑policy training  
- Robustness to subsequent training  
- Alignment behavior erasure
