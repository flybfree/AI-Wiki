# Summary: 2026-05-27_17-59-51Z_PEFT_Arena_UnderstandingParameter_EfficientFinetun.md
Saved: 2026-05-27 23:01
Source: 2026-05-27_17-59-51Z_PEFT_Arena_UnderstandingParameter_EfficientFinetun.md
Model: None

---


## Summary  
The paper argues that parameter‑efficient fine‑tuning (PEFT) should be evaluated not only on downstream accuracy but also on the retention of pretrained capabilities, framing this as a stability‑plasticity trade‑off. To address this gap, the authors introduce PEFT‑Arena, a benchmark that jointly measures task performance and general‑capability preservation across fine‑tuning methods. Their analysis reveals distinct stability‑plasticity profiles, with orthogonal fine‑tuning attaining the most favorable Pareto frontier under comparable parameter budgets. The work also proposes geometric insights—spectral analysis of weight updates and activation‑space retention metrics—to explain why some PEFT strategies degrade general knowledge.

## Key Contributions  
- [Finding 1] Distinct stability‑plasticity profiles emerge across different PEFT methods, and orthogonal fine‑tuning yields the most favorable Pareto frontier when parameter budgets are equal.  
- [Finding 2] Spectral analysis of weight updates shows how PEFT parameterizations interact with the pretrained singular‑value structure, influencing stability.  
- [Finding 3] Activation‑space retention metrics reveal that forgetting is linked to non‑isometric distortion of general‑capability representations; final SFT checkpoints often overshoot a better target‑retention operating point.

## Methodology  
The authors built PEFT‑Arena by applying a suite of downstream tasks and measuring both task accuracy and the preservation of pretrained knowledge using activation‑space metrics. They performed spectral analysis on weight matrices to examine how fine‑tuning alters the singular‑value basis, and they compared representation distortion across methods. To explore optimal operating points, they examined SFT checkpoints and introduced path‑wise rewinding as a post‑hoc improvement strategy.

## Results  
Orthogonal PEFT consistently achieves higher downstream performance while retaining more pretrained capability than other approaches such as adapter or prefix fine‑tuning. The spectral analysis confirms that orthogonal updates preserve the pretrained singular‑value structure, whereas non‑orthogonal updates introduce instability. Activation‑space retention scores show a clear degradation for methods that cause non‑isometric distortion, and SFT checkpoints often overshoot the optimal trade‑off point, requiring path‑wise rewinding to recover better performance.

## Significance  
By introducing PEFT‑Arena, this study shifts the evaluation paradigm of PEFT beyond accuracy alone, providing a more holistic view of model adaptation. The findings guide practitioners in selecting fine‑tuning strategies that balance task learning with general capability preservation, informing future research on parameter budgets and training dynamics.

## Related Concepts  
Parameter-efficient fine-tuning (PEFT), stability‑plasticity dilemma, Pareto frontier, spectral analysis, singular‑value structure, activation space representation distortion, forgetting, isometric transformation, path‑wise rewinding.

[[2026-05-27_17-59-51Z_PEFT_Arena_UnderstandingParameter_EfficientFinetun.md]]