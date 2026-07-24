# Summary: 2026-07-21_06-09-08Z_Contraction_GaugePreconditioningforQuantizedMatrix.md
Saved: 2026-07-24 00:31
Source: 2026-07-21_06-09-08Z_Contraction_GaugePreconditioningforQuantizedMatrix.md
Model: None

---

## Summary  
The paper tackles the challenge of low‑precision matrix multiplication when both operands are quantized, seeking a method that minimizes the expected squared product error under realistic quantization noise. It introduces **contraction‑gauge preconditioning**, which jointly selects a factor representation and its sharing pattern before quantization to reduce this error while accounting for extra transformed copies of the opposite operand. The authors derive an exact finite‑dimensional identity for the error, formulate a geometric program that computes globally optimal shared folds within the family of positive diagonal gauges, and provide computable selection statistics for other gauge families. Their approach yields measurable improvements over standard dithering and round‑to‑nearest (RTN) strategies, especially in high‑bit scenarios.

## Key Contributions  
- [Finding 1] An exact finite‑dimensional identity is derived that gives the expected squared product error under independent, zero‑mean entrywise errors with known variance fields for both subtractive dither and stochastic rounding.  
- [Finding 2] A contraction‑gauge preconditioning scheme is presented that jointly chooses a factor representation and sharing pattern to reduce product error, requiring only one shared transform or up to one block‑specific transform per operand.  
- [Finding 3] Within the positive diagonal gauge family a geometric program computes a globally optimal shared fold; for other families computable selection statistics (tail index, profile spread, coherence, weighted‑Gram energy, slice‑energy covariance) with upper bounds are derived to rank heuristic candidates.

## Methodology  
The authors start from the product‑preserving identity AB = (AT)(T⁻¹B), which allows them to treat one factor as a transformed version of the other. They then formulate contraction‑gauge preconditioning: for each possible gauge (a diagonal matrix that scales rows/columns) they compute how many copies of the opposite operand must be stored after transformation. A geometric program solves the optimization problem of minimizing total error plus copy cost, yielding a shared fold that is globally optimal in the diagonal family. For non‑diagonal gauges, selection statistics are derived analytically to bound performance and rank candidates without exhaustive search.

## Results  
Across twelve linear products from a trained three‑block image classifier, the median within‑product rank correlation between dither‑model predictions and deterministic RTN errors is 0.937 at 8 bits and 0.918 at 4 bits. The geometric program’s fold reduces held‑out product error by 18.0 % (8‑bit) and 20.5 % (4‑bit) compared with the identity fold, outperforming a SmoothQuant‑style grid baseline on ten of twelve products. It also lowers composed logit MSE by 15.4 % (8‑bit) and 26.4 %.

## Significance  
By providing exact stochastic product‑error accounting, certified selection within the diagonal gauge family, and a unified objective for evaluating reusable transform candidates under RTN, this work advances practical low‑precision linear algebra. It enables designers to choose transforms that trade off extra memory copies against error reduction, offering a principled framework for quantization‑aware matrix multiplication.

## Related Concepts  
quantization, matrix multiplication, dithering, round‑to‑nearest (RTN), Gaussian processes, geometric programming, linear programming, positive diagonal gauges, block‑specific transforms, shared folds, variance fields, error analysis.
