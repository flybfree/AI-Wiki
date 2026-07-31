# Summary: 2026-07-29_12-40-04Z_FlatScore_AmplifiedFailures_HowtheErrorBudgetMasks.md
Saved: 2026-07-30 21:33
Source: 2026-07-29_12-40-04Z_FlatScore_AmplifiedFailures_HowtheErrorBudgetMasks.md
Model: None

---

## Summary  
The authors investigate whether post‑training 4‑bit quantization of large language models (LLMs) truly preserves performance on multi‑turn, tool‑calling agents that are sensitive to subtle errors. They demonstrate that the standard task score remains unchanged because the benchmark’s ten‑error budget absorbs additional failures introduced by quantization, while a stricter two‑error budget reveals a 17‑point drop in the most affected cell. The paper shows that error volume grows (≈ 2.5×) but novel failures do not appear, and that targeted error‑repair prompts eliminate the damage precisely where it occurs.  

## Key Contributions  
- [Finding 1] Quantization does not alter the task score on τ²‑bench because the existing ten‑error budget masks the extra failure volume introduced by 4‑bit weight compression.  
- [Finding 2] The same set of failures is observed across all precision levels, with a rank correlation ≥ 0.94 and only 0.18 % novel events added at lower precisions.  
- [Finding 3] Shrinking the error budget to two errors exposes a 17‑point score gap that aligns exactly with the predicted masking effect of quantization on tool‑call hallucinations in telecom domains.  

## Methodology  
The authors evaluate three open‑weight model families (dense and MoE variants) across eight benchmark cells, each containing 456 episodes. They run experiments at 16‑bit, 8‑bit, and 4‑bit weight precisions while tracking per‑channel error rates and success metrics under both the default ten‑error budget and a constrained two‑error budget. Error‑repair prompts are applied to telecom models at each precision to isolate the source of damage. All diagnostics—per‑channel error rates, task reward scores, and novel event counts—are extracted from logs that the benchmark already collects.  

## Results  
Across all configurations, the average task score stays flat (standard deviation < 2 points) because the ten‑error budget absorbs up to 17.6 additional failures per task. When the error budget is reduced to two errors, only the telecom cell shows a 17‑point decline, matching the expected amplification of existing tool‑name hallucinations by ≈ 2.5× in failure volume. Per‑channel error rates increase modestly at lower precisions, but novel events remain below 0.2 % across all runs. The targeted prompts eliminate the damage exactly where it resides, confirming that the observed score gap is a direct consequence of masked failures rather than new errors.  

## Significance  
This work clarifies why quantization appears lossless on standard benchmarks while silently degrading agent reliability in high‑stakes domains such as telecom. By linking error volume to visible task regressions under tighter budgets, the authors provide empirical support for reporting per‑channel diagnostics alongside task reward, a practice that can guide safer model deployment and more honest benchmark design.  

## Related Concepts  
- Quantization (post‑training weight compression)  
- Error budget / failure budget in benchmarking  
- Tool‑call hallucination in LLM agents  
- Per‑channel error rate monitoring  
- Success under constrained evaluation budgets
