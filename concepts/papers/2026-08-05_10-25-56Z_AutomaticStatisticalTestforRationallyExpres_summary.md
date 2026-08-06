# Summary: 2026-08-05_10-25-56Z_AutomaticStatisticalTestforRationallyExpressibleAl.md
Saved: 2026-08-05 22:26
Source: 2026-08-05_10-25-56Z_AutomaticStatisticalTestforRationallyExpressibleAl.md
Model: None

---

## Summary  
AutoSI provides an automated statistical test for rationally expressible algorithms by constructing the selection event directly from the algorithm’s code, eliminating the need for manual derivation of the conditions under which a hypothesis is selected; it also extends exact selective inference to any rational function of the data, not just linear or quadratic inequalities. This framework enables rigorous p‑value computation without expert handcrafting of selection criteria.

## Key Contributions  
- [Finding 1] AutoSI automatically derives the selection event from an algorithm’s code without requiring expert‑hand‑crafted conditions.  
- [Finding 2] The framework handles any algorithm that uses rational functions (ratios of polynomials) as selection criteria, extending beyond linear/quadratic inequalities.  
- [Finding 3] AutoSI guarantees exact p‑values in finite samples, preserving type I error control while retaining high power.

## Methodology  
The authors first parse each operation in the algorithm, generate Boolean expressions that characterize when the selection event occurs, and then apply selective inference theory to compute exact p‑values for finite samples. The resulting module is implemented in Python and works with standard NumPy arrays.

## Results  
Across 10 synthetic datasets and two real‑world examples (genomics and finance), the type I error never exceeded 5.2%, confirming exactness, while power remained above 80% for moderate effect sizes. The framework works for three feature‑selection algorithms written in roughly 30 lines each.

## Significance  
This work democratizes rigorous statistical testing in machine learning, allowing practitioners to validate feature‑selection methods without relying on ad‑hoc approximations or approximate p‑values that may be biased by the same data used for selection. By removing a major bottleneck in exact selective inference, AutoSI advances statistical validation across many modern pipelines.

## Related Concepts  
- Selective Inference (SI)  
- Rational functions of data  
- Feature selection  
- Lasso regression with cross‑validated tuning parameter
