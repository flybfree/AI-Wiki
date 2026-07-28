# Summary: 2026-07-27_13-47-44Z_BiggerorCheaper_ScaleandQuantizationEffectsonUncer.md
Saved: 2026-07-27 21:41
Source: 2026-07-27_13-47-44Z_BiggerorCheaper_ScaleandQuantizationEffectsonUncer.md
Model: None

---

## Summary  
The paper investigates how model scale and 4‑bit quantization influence the internal uncertainty signals of vision‑language models (VLMs) when processing degraded images, a problem critical for consumer hardware where memory is limited. It proposes that practitioners must balance three configurations—small full‑precision, small quantized, or large quantized—each pushing confidence metrics in opposite directions. The study demonstrates that larger models provide stronger error‑detection signals while their spoken confidence remains weak and often at chance. Finally, it recommends a larger quantized model (7B‑4bit) as the optimal trade‑off for fixed memory budgets.

## Key Contributions  
- [Finding 1] Scale sharply improves the model's internal uncertainty signal (mean error‑detection AUROC rises from 0.80 to 0.98 when moving from a 2B to a 7B model), whereas its verbalized confidence stays weak and near chance (mean 0.61 to 0.69).  
- [Finding 2] 4‑bit quantization is nearly free for accuracy (‑1.6 points) but significantly harms the confidence signal, reducing internal AUROC from 0.95 to 0.80 and collapsing the verbalized‑confidence parse rate from 99 % to 64 %.  
- [Finding 3] For a fixed memory budget, the 7B‑4bit configuration yields both the highest accuracy (lowest loss) and the best uncertainty signal among all three configurations.

## Methodology  
The authors conducted an empirical study on 5,700 model predictions across six realistic photographic degradations evaluated at three severity levels. For each prediction they measured two confidence signals: the model’s internal mean token‑probability error (AUROC) and its explicit verbalized confidence score. The experiments compared three configurations—2B full‑precision, 2B 4‑bit quantized, and 7B 4‑bit quantized—ensuring each fit within a constant memory budget.

## Results  
Scale improves internal AUROC from 0.80 to 0.98 (a 19 % relative gain) while the verbalized confidence remains near random guessing (mean 0.61–0.69). Quantization preserves accuracy only marginally (‑1.6 points loss), but it degrades internal AUROC from 0.95 to 0.80 and reduces parse‑rate of explicit confidence statements from 99 % to 64 %. The best overall configuration, 7B‑4bit, achieves the highest accuracy (lowest loss) and the strongest uncertainty signal (AUROC 0.98). These results are presented as selective‑prediction operating points that map directly onto deployment recommendations.

## Significance  
The findings clarify a longstanding trade‑off: larger models increase internal reliability but do not translate into better spoken confidence, while quantization preserves accuracy at low cost yet erodes the model’s ability to signal uncertainty. By highlighting AUROC as the metric that exposes this discrepancy rather than calibration error, the paper offers actionable guidance for deploying VLMs on resource‑constrained devices where users must decide when to answer versus defer.

## Related Concepts  
- Vision‑Language Models (VLMs)  
- Quantization (4‑bit)  
- Uncertainty signals and confidence metrics  
- Error‑detection AUROC  
- Calibration error vs. AUROC  
- Memory budget constraints in AI deployment
