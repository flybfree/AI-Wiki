# Summary: 2026-07-29_19-20-50Z_ECG_InterpBench_BenchmarkingtheInterpretabilityofE.md
Saved: 2026-07-30 20:22
Source: 2026-07-29_19-20-50Z_ECG_InterpBench_BenchmarkingtheInterpretabilityofE.md
Model: None

---

## Summary  
The paper introduces ECG‑InterpBench, a benchmark that systematically evaluates the interpretability of frozen electrocardiogram (ECG) foundation models rather than only their downstream predictive performance. It does so by using sparse autoencoders as standardized measurement instruments and matching each model’s capacity to enable controlled comparisons across multiple configurations. The study generates a 450‑cell interpretability atlas that records cell‑level metrics for six models under five encoder depths, five dictionary widths, and three random seeds. By quantifying reconstruction fidelity, single‑feature accessibility, coverage of 49 clinically meaningful measurements, and cross‑seed reproducibility, ECG‑InterpBench reveals distinct interpretability profiles among the models.

## Key Contributions  
- [Finding 1] ECG‑InterpBench provides a capacity‑controlled benchmark that compares six frozen ECG foundation models across multiple encoder depths and dictionary widths.  
- [Finding 2] The benchmark uncovers that reconstruction fidelity and clinical accessibility identify different leading models, indicating that interpretability dimensions can diverge from performance rankings.  
- [Finding 3] Patient‑sampling uncertainty, depth‑dependent variation, and sensitivity to sparsity parameterization are quantified, highlighting the non‑trivial variability of representation interpretability.

## Methodology  
The authors selected six pre‑trained ECG foundation models and froze their representations. They evaluated each model at five encoder depths and paired them with five matched dictionary widths for sparse autoencoders, while running three independent random seeds to capture sampling noise. This configuration yields 75 exactly matched comparison blocks, each containing a 450‑cell cell‑level interpretability atlas. Metrics such as reconstruction fidelity (how well the original ECG can be recovered), single‑feature accessibility (ability to isolate specific physiological measurements), coverage of the 49 clinically relevant features, and cross‑seed reproducibility are computed for every block. Patient‑sampling uncertainty is also measured by comparing results across seeds.

## Results  
The benchmark produced a comprehensive dataset of cell‑level metrics across all configurations. Reconstruction fidelity ranged from moderate to high depending on depth and sparsity, while single‑feature accessibility varied widely, with some features being easily recoverable and others nearly impossible. Coverage of the 49 clinically meaningful measurements reached only about 60 % on average, indicating gaps in interpretability. Cross‑seed reproducibility showed substantial variation (up to 30 % difference), confirming patient‑sampling uncertainty. Depth‑dependent effects were evident: deeper encoders improved fidelity but reduced accessibility, and sparsity parameterization strongly influenced both metrics.

## Significance  
ECG‑InterpBench bridges the gap between performance‑centric ECG benchmarks and interpretability research by offering a reproducible, capacity‑matched framework that can be applied to any foundation model. It provides clinicians and researchers with quantitative evidence on how well internal representations capture physiological meaning, which is essential for trustworthy AI deployment in cardiology.

## Related Concepts  
ECG foundation models, sparse autoencoders, interpretability benchmarks, representation fidelity, clinical accessibility, sparsity parameterization, patient‑sampling uncertainty, encoder depth, cross‑seed reproducibility.
