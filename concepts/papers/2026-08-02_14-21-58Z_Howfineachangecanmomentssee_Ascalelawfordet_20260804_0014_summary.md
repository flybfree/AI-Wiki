# Summary: 2026-08-02_14-21-58Z_Howfineachangecanmomentssee_Ascalelawfordetectingd.md
Saved: 2026-08-04 00:14
Source: 2026-08-02_14-21-58Z_Howfineachangecanmomentssee_Ascalelawfordetectingd.md
Model: None

---

## Summary  
This paper introduces a scale law that quantifies the minimal detectable change in high-dimensional embedding streams, specifically focusing on moment-based detection methods. The authors establish a theoretical constraint linking the precision of observed moments to the statistical power of detecting distribution shifts, revealing that only changes at scales finer than a certain threshold can be reliably captured by polynomial tests. They also develop a practical calibration rule derived from kernel theory, which predicts optimal bandwidths for mean-moment distance (MMD) and related detectors based on feature fineness rather than dimensionality. The work contrasts moment-based approaches with topological ones like persistent homology, demonstrating that while the latter suffer from inconsistent performance across scales, the former offers a more consistent and cost-effective alternative.

## Key Contributions  
- [Finding 1] A scale law is derived that constrains any moment-based change detection method: certifying a feature of spatial scale ε carrying mass fraction f requires polynomial tests of degree N* ≥ log(1/f)/(2ε), proven via the Chebyshev extremal problem. This law shows that statistical power depends on how finely changes occur, not on the number of moments observed.  
- [Finding 2] The authors construct a Gauss-quadrature-based lower bound, showing N* ≥ 4b−1 for a b-scale topology, confirming that cost is driven by feature fineness rather than feature count. This establishes a theoretical foundation for bandwidth selection in kernel-based detectors.  
- [Finding 3] A practical calibration rule is proposed: Gaussian test functions and the RKHS witness of an RBF kernel achieve this bound, so MMD tests should use bandwidth equal to the feature scale. The law also reveals a one-sided nature—topological summaries like persistence can be fooled by distributions with identical moments but different topology.

## Methodology  
The authors begin by framing distribution shift detection in terms of changes in spatial scales within high-dimensional embeddings, focusing on moment-based statistics such as mean, covariance, and higher-order moments. They formulate the problem as a Chebyshev extremal optimization to derive necessary conditions for detecting small-scale shifts. Using Gauss-quadrature, they construct lower bounds on test degrees required by scale. The calibration rule is derived from kernel theory, where Gaussian functions are identified as optimal witnesses for RBF kernels. Experiments compare these theoretical predictions against real embedding streams and adversarial attacks targeting moment-based detectors.

## Results  
On real embedding streams across three settings and scales, the median σ*/ε ratio is 1.12 with IQR 1.01–1.52, indicating tight alignment between feature scale and detectable change magnitude. A data-driven bandwidth aligned to this law achieves AUC ≥ 0.95 in shift detection. Against adversarial attacks optimizing against mean, covariance, k-NN, and kurtosis, only a kernel test with bandwidth matching the feature scale remains effective. Persistent homology shows mixed results: total persistence has recall 0.75 at FPR 1%, but its first persistence landscape attains 0.00, highlighting inconsistency in topological summaries.

## Significance  
This work provides a theoretical and practical framework for robustly detecting distribution shifts in high-dimensional data streams using moment-based methods. By establishing a scale law grounded in kernel theory and Chebyshev optimization, it clarifies the limitations of traditional moment statistics and offers a scalable calibration rule that outperforms both polynomial tests and topological summaries on this task.

## Related Concepts  
- Distribution shift detection  
- Moment-based statistics (mean, covariance, kurtosis)  
- Mean-moment distance (MMD)  
- Kernel theory and RKHS  
- Gaussian test functions  
- Persistent homology  
- Chebyshev extremal problem  
- Gauss-quadrature construction
