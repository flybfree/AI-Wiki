# Summary: 2026-08-06_20-22-21Z_WhichDecisionsLow_BitQuantizationBreaks_andHowtoPr.md
Saved: 2026-08-10 22:37
Source: 2026-08-06_20-22-21Z_WhichDecisionsLow_BitQuantizationBreaks_andHowtoPr.md
Model: None

---

## Summary  
This paper investigates how low‑bit integer quantization degrades the reasoning of large language models by quantifying the margin between a model’s chosen action and its best alternative before and after compression. It demonstrates that not all decisions are equally affected: at 3‑bit levels the decision to invoke a tool collapses toward inaction while the choice of which tool remains stable, and the damage grows proportionally with bit‑width rather than following a fixed threshold. The authors also show that additive noise models cannot fully explain these failures and propose a per‑model margin‑based predictor that accurately forecasts flip rates with near‑perfect calibration.

## Key Contributions  
- [Finding 1] Low‑bit quantization causes variable, proportional loss of decision margins; the median margin factor drops from 0.86 at 4 bits to 0.33 at 3 bits and reaches zero at 2 bits.  
- [Finding 2] The damage is not a fixed set of broken decisions but varies per model, with tool‑call inaction emerging specifically at the 3‑bit threshold.  
- [Finding 3] Additive noise models fail to capture the observed behavior; instead, a calibrated predictor using measured margins predicts flip probabilities with a calibration error of only 0.004 over 131 758 predictions.

## Methodology  
The authors collected decision data from 16 language‑model agents across three quantization methods (e.g., GPTQ, AWQ, BitsAndBytes) and evaluated them at bit depths from 2 to 8. For each condition they computed the margin between the selected option and its best alternative before and after compression. They then fitted this data against additive noise competitors—models that assume a constant‑size error—and compared their predictions with the empirical outcomes. The predictor was trained on a held‑out set of decisions, yielding per‑decision probabilities without any flips being used in the training process.

## Results  
Across all models and bit depths, the median margin factor collapses as described above, indicating that each additional bit restores roughly half of the lost decision confidence. The fitted predictor predicts a flip probability with a calibrated error of 0.004 (≈ 95 % confidence) over 131 758 predictions. When using borrowed constants from other models, the predicted probabilities are off by 18–33 points at 3‑bit depth, underscoring that per‑model margins must be measured independently.

## Significance  
These findings reveal a concrete mechanism behind safety failures in compressed agents: a shrinking margin leads to reduced tool calls and missed refusals, which benchmark scores cannot capture. The work shows that one additional bit dramatically improves reliability, making quantization decisions safer for high‑stakes applications such as autonomous assistants.

## Related Concepts  
- Quantization (integer‑bit compression)  
- Decision margins / confidence intervals  
- Additive noise models in machine learning  
- Safety refusals and tool invocation in LLMs  
- Calibration of probability estimates
