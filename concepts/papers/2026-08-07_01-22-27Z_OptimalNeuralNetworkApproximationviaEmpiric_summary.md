# Summary: 2026-08-07_01-22-27Z_OptimalNeuralNetworkApproximationviaEmpiricalLeast.md
Saved: 2026-08-09 22:34
Source: 2026-08-07_01-22-27Z_OptimalNeuralNetworkApproximationviaEmpiricalLeast.md
Model: None

---

## Summary  
The paper introduces a rigorous discrete residual least‑squares framework for approximating solutions of elliptic spectral equations on the sphere using linearized ReLU$^k$ neural networks with deterministic collocation points. It proves that, under antipodally quasi‑uniform parameter sets and sufficiently many points, the approximation error in the Hölder space $\mathcal H^{\beta}(\mathbb S^{d})$ is bounded by a constant times the residual norm in $L^{2}$, with an explicit rate of $n^{-r/d}$. The analysis also yields high‑probability residual estimates for random collocation points and introduces a Bernstein inequality that links network smoothness to Hölder norms.

## Key Contributions  
- [Finding 1] A precise error bound $\|u-u_{n,m}\|_{H^{\beta}(\mathbb S^{d})}\eqsim\|f-\mathfrak L_{\beta}u_{n,m}\|_{L^{2}(\mathbb S^{d})}$ with the rate $n^{-r/d}$, valid for $k>\frac{d-1}{2}+\beta$ and quasi‑uniform parameter sets.  
- [Finding 2] A high‑probability residual estimate that holds uniformly over i.i.d. uniform collocation points, up to a logarithmic factor and an arbitrarily small smoothness loss.  
- [Finding 3] The Bernstein inequality $\|v_n\|_{H^{r}(\mathbb S^{d})}\lesssim\underline h^{-(r-s)}\|v_n\|_{H^{s}(\mathbb S^{d})}$ for $0\le s<r<k+\tfrac12$, which connects network parameter separation to smoothness.

## Methodology  
The authors formulate the problem as a discrete least‑squares minimization over the linearized ReLU$^k$ network space $L_n^k(\Theta_n)$, using collocation points $\{η_i^*\}_{i=1}^m$. They employ deterministic parameter sets that are antipodally quasi‑uniform and assume $m\gtrsim n$, then apply a Bernstein inequality to control the Hölder norm of the approximating function. The theoretical analysis proceeds by comparing the discrete residual with the continuous solution, leveraging interpolation theory between $L^{2}$ and Hölder spaces.

## Results  
The main result is that for any $r$ satisfying $\frac{d}{p}<r\le\frac{d}{2}$ (with $p>2$) or $r>\frac{d}{2}$, the approximation error scales as $n^{-r/d}$. The bound holds with constants depending only on $d$, $k$, and the parameter separation $\underline h$. Additionally, when collocation points are i.i.d. uniform, the residual norm is bounded by a high‑probability quantity that includes a logarithmic factor and can be made arbitrarily small in smoothness.

## Significance  
This work bridges deep learning with classical spectral analysis on manifolds, providing a mathematically rigorous guarantee for neural network approximations of elliptic problems. The derived error rates and high‑probability estimates offer concrete tools for designing training schemes where deterministic collocation points are used, potentially improving convergence compared to stochastic or random point choices.

## Related Concepts  
- Elliptic spectral equations $\mathfrak L_{\beta}u = f$ on the sphere  
- Linearized ReLU$^k$ neural networks and their function spaces $L_n^k(\Theta_n)$  
- Discrete residual least‑squares approximation  
- Hölder space $\mathcal H^{\beta}(\mathbb S^{d})$ and its embedding into $L^{2}$  
- Bernstein inequality for smooth functions on manifolds  
- Antipodal quasi‑uniform parameter sets and collocation points
