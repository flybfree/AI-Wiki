# Summary: 2026-08-03_04-04-56Z_SharpRootAnti_ConcentrationviaProjectiveIncidencea.md
Saved: 2026-08-04 00:25
Source: 2026-08-03_04-04-56Z_SharpRootAnti_ConcentrationviaProjectiveIncidencea.md
Model: None

---

## Summary  
The paper resolves the one‑dimensional local root anti‑concentration problem that arose in the online optimization of piecewise‑Lipschitz functions with a homogeneous feature curve and coefficients whose density relative to the uniform law on a symmetric convex body \(K\) is bounded by a constant \(A\). It shows that the worst‑case interval‑hitting constant equals \(A\) times a section‑averaged projective incidence speed, which is equivalent up to universal constants to the projective Lipschitz constant of the curve. This yields a sharp, dimension‑free characterization and eliminates the previous \(\sqrt N\) loss. Moreover, for monic degree‑\(d\) polynomials under arbitrary coefficient laws it proves that the interval‑hitting constant is finite if and only if the ordered real‑root laws have bounded densities, with a factor‑\(d\) comparison that is sharp. The authors also provide verifiable area formulas and two‑chart certificates for dependent or singular coefficient spaces and illustrate their utility in graph‑learning applications.

## Key Contributions  
- [Finding 1] A sharp root anti‑concentration bound: the interval‑hitting constant equals \(A\) times a section‑averaged projective incidence speed, which is essentially the projective Lipschitz constant, giving a dimension‑free, optimal characterization.  
- [Finding 2] Finite interval‑hitting constant for monic degree‑\(d\) polynomials iff ordered real‑root densities are bounded, with a sharp factor‑\(d\) comparison that holds even when coefficient laws are singular.  
- [Finding 3] Verifiable criterion using conditional and joint coefficient‑space area formulas together with a two‑chart certificate, enabling the analysis of dependent or singular coefficient distributions.

## Methodology  
The authors approach the problem by combining projective incidence theory with ordered root laws. They first translate the interval‑hitting constant into a geometric quantity that measures how quickly a curve’s projection intersects intervals, which is bounded by the projective Lipschitz constant. For polynomial coefficients they employ conditional and joint area formulas to characterize when the ordered real‑root law has bounded density, supplemented by a two‑chart certificate that can be checked computationally even for singular coefficient spaces. This framework is then applied to graph‑learning models: a cost‑sensitive Gaussian‑RBF harmonic classifier uses the projective incidence theorem to obtain an expected regret of \(\widetilde O((A n^{2} D e^{BD}/\ell + 1)\sqrt T)\), while a common‑offset polynomial‑kernel model, after rigid translation of ordered roots, achieves \(\widetilde O((qn^{2}\kappa+1)\sqrt T)\) regret despite singular coefficient laws.

## Results  
The worst‑case interval‑hitting constant is exactly \(A\) multiplied by the section‑averaged projective incidence speed; this speed is equivalent to the projective Lipschitz constant up to universal constants, providing a sharp bound that removes the \(\sqrt N\) factor. The finiteness of the interval‑hitting constant for monic degree‑\(d\) polynomials is characterized precisely by bounded densities of ordered real roots, with a comparison factor of \(d\). The area formulas and two‑chart certificates allow verification of these conditions even when coefficient laws are dependent or singular. In graph‑learning settings, the classifier regret scales as \(\widetilde O((A n^{2} D e^{BD}/\ell + 1)\sqrt T)\) and the kernel model regret as \(\widetilde O((qn^{2}\kappa+1)\sqrt T)\).

## Significance  
These results eliminate the previous loss of a factor \(\sqrt N\) in root anti‑concentration, delivering a sharp, dimension‑free bound that works for both dependent and singular coefficient spaces. The verification tools (area formulas and two‑chart certificates) make the theoretical guarantee practical, enabling efficient learning algorithms with provable regret improvements across diverse settings.

## Related Concepts  
- Projective incidence theorem  
- Ordered root laws  
- Interval‑hitting constant  
- Piecewise‑Lipschitz functions  
- Homogeneous feature curves  
- Projective Lipschitz constant  
- Conditional and joint coefficient‑space area formulas  
- Two‑chart certificates  
- Graph learning (transition‑to‑regret chain)  
- Regret analysis for Gaussian‑RBF harmonic classifiers and polynomial kernels
