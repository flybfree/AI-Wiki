# Summary: 2026-08-03_17-07-41Z_BeyondModernAsymptoticsforLog_LikelihoodRatiosinLo.md
Saved: 2026-08-04 00:51
Source: 2026-08-03_17-07-41Z_BeyondModernAsymptoticsforLog_LikelihoodRatiosinLo.md
Model: None

---

## Summary  
This paper attacks the problem of bounding the finite‑sample log‑likelihood ratio statistic in binary logistic regression without relying on asymptotic approximations. The authors obtain a uniform, nonasymptotic quantile bound that holds for all design matrices and any target parameter, even when it varies with \(n\), \(d\) and \(\delta\). Their work extends the classical Wilks χ²\(_d\) phenomenon to exact finite‑sample regimes and resolves the low‑dimensional anomalies. The result is a sharp, universal bound that does not assume regularity or i.i.d. Gaussian data.

## Key Contributions  
- Finding 1: For \(n\ge d\ge3\) the worst‑case \((1-\delta)\) quantile of the log‑likelihood ratio over all fixed designs and target parameters is \(\displaystyle d\log\!\Big(\frac{e n}{d}\Big)+\log\!\Big(\frac{1}{\delta}\Big)\).  
- Finding 2: In low dimensions the behavior is unusual: for \(d=2\) the quantile scales as \(\log\log\log n+\log(1/\delta)\), while for \(d=1\) it reduces to \(\log(1/\delta)\) with no dependence on \(n\).  
- Finding 3: The authors prove a sharp bound of \(d+\log(1/\delta)\) that holds when \(n\gtrsim d+\log(1/\delta)\), and they recover the classical Wilks scale for i.i.d. Gaussian designs.

## Methodology  
The authors adopt a combinatorial‑probabilistic approach, treating the log‑likelihood ratio as a sum of independent contributions from each observation. They employ concentration inequalities that are valid uniformly over all possible design vectors, then use a worst‑case analysis to eliminate dependence on the specific configuration. The treatment is careful: they first bound the tail probability for any fixed target parameter and then maximise over the admissible set of designs, yielding a universal constant‑free expression.

## Results  
The main theoretical results are the three quantile formulas above and the sharp bound \(d+\log(1/\delta)\) under the condition \(n\gtrsim d+\log(1/\delta)\). The low‑dimensional cases are explicitly characterized, showing that the usual Wilks scaling breaks down. For i.i.d. Gaussian designs the classical Wilks χ²\(_d\) distribution is recovered exactly in the limit.

## Significance  
This work provides a nonasymptotic framework for logistic regression inference that does not require regularity or asymptotic normality, offering exact finite‑sample guarantees usable in low dimensions and with arbitrary target functions. By eliminating dependence on the design matrix, it makes the analysis applicable to a broader class of problems where traditional asymptotics fail.

## Related Concepts  
Wilks χ²\(_d\), log‑likelihood ratio statistic, asymptotic normality, concentration inequalities, uniform convergence, finite‑sample inference, nonasymptotic bounds.
