# Summary: 2026-07-21_06-09-08Z_Contraction_GaugePreconditioningforQuantizedMatrix.md
Saved: 2026-07-24 00:48
Source: 2026-07-21_06-09-08Z_Contraction_GaugePreconditioningforQuantizedMatrix.md
Model: None

---

## Summary  
The paper tackles low‑precision matrix multiplication where both factors are quantized, seeking to reduce the product error by jointly selecting factor representations and sharing patterns before quantization. It derives an exact finite‑dimensional identity for the expected squared product error under independent zero‑mean entrywise errors with known variance fields, which holds for subtractive dither and stochastic rounding, and empirically validates deterministic round‑to‑nearest (RTN). Using the product‑preserving equivalence AB = (AT)(T⁻¹B), it introduces contraction‑gauge preconditioning—a geometric program that chooses a shared transform to minimize transformed error. Experiments on twelve linear products from a three‑block image classifier show median within‑product rank correlations of 0.937 at 8‑bit and 0.918 at 4‑bit, with the geometric‑program (GP) fold cutting product error by 18 % (8‑bit) and 20.5 % (4‑bit) versus the identity fold.

## Key Contributions  
- [Finding 1] Exact finite‑dimensional identity for expected squared product error under zero‑mean entrywise errors, valid for subtractive dither and independent stochastic rounding.  
- [Finding 2] A contraction‑gauge preconditioning framework that jointly chooses a factor representation and its sharing pattern to minimize product error, requiring only one or per‑block transformed copies of the opposite operand.  
- [Finding 3] A geometric program that computes a globally optimal shared fold within the family of positive diagonal gauges; for other gauge families it provides computable selection statistics (tail index, profile spread, coherence, weighted‑Gram energy, slice‑energy covariance) with upper bounds for ranking heuristics.

## Methodology  
The authors start from the identity AB = (AT)(T⁻¹B), which separates the quantizations of A and B. They model entrywise errors as independent zero‑mean Gaussian fields with known variance functions. For subtractive dither they derive an exact expression for the expected squared product error; for RTN they empirically confirm the same bound. Preconditioning selects a positive diagonal gauge (a “fold”) that scales and rotates each factor, turning the problem into a geometric program: the GP minimizes the transformed error while respecting a shared transform budget—one copy if the fold is global, up to one per block otherwise. A linear program checks whether the identity fold already yields the minimal error. For gauge families beyond positive diagonals the authors compute tail index (scaling), profile spread (partitioning), coherence and weighted‑Gram energy (rotations), slice‑energy covariance (hierarchy depth) as selection statistics, each bounded to rank heuristic candidates.

## Results  
Across twelve linear products from a trained three‑block image classifier, the median within‑product rank correlation between dither‑model predictions and deterministic‑RTN errors is 0.937 at 8‑bit precision and 0.918 at 4‑bit precision. The GP fold reduces product error by 18 % (geometric mean) at 8‑bit and 20.5 % at 4‑bit compared with the identity fold, outperforming a SmoothQuant‑style grid baseline on ten of twelve products. Composed logit MSE is lowered by 15.4 % (8‑bit) and 26.4 % (4‑bit). The GP also yields lower memory overhead: only one or per‑block transformed copies are needed versus full copies for the identity.

## Significance  
This work provides exact stochastic product‑error accounting, a certified selection method within the diagonal gauge family, and a common objective for evaluating reusable transform candidates under RTN. By offering a geometric program that globally optimizes shared folds and a set of computable selection statistics for other families, it enables higher‑precision matrix multiplication with minimal extra memory, directly supporting efficient deep learning inference on low‑bit hardware.

## Related Concepts  
- Quantization error analysis  
- Dithering (subtractive)  
- Round‑to‑nearest (RTN) quantization  
- Contraction‑gauge preconditioning  
- Positive diagonal gauge and fold selection  
- Geometric programming for optimization under memory constraints  
- Product error, rank correlation, SmoothQuant baseline
