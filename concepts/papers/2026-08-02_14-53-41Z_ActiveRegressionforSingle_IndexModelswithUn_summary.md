# Summary: 2026-08-02_14-53-41Z_ActiveRegressionforSingle_IndexModelswithUnknownLi.md
Saved: 2026-08-04 00:11
Source: 2026-08-02_14-53-41Z_ActiveRegressionforSingle_IndexModelswithUnknownLi.md
Model: None

---

## Summary  
The paper tackles active regression for single‑index models when the link function is unknown and only a $1$‑Lipschitz function $f$ is assumed. It formulates the problem as minimizing $\|f(Ax)-b\|_p^p$ with full access to matrix $A$ but query‑only access to vector $b$, extending prior work that handled known link functions or limited loss norms. The authors present a non‑adaptive sampling algorithm achieving $(1+\varepsilon)$‑approximation for any $p\ge 1$ and prove nearly tight lower bounds for the case $p>2$. This work bridges the remaining gap in active $\ell_p$‑regression for single‑index settings.

## Key Contributions  
- [Finding 1] A non‑adaptive sampling algorithm that attains $(1+\varepsilon)$‑approximation for unknown link functions and general $p\ge 1$, with query complexity $O(d^{p/2\vee 1}/ε^{p\vee 2}\operatorname{poly}\log(n/ε))$.  
- [Finding 2] Nearly tight lower bounds for the problem when $p>2$, showing that any algorithm must make at least $\Omega(d^{p/2}/ε^2)$ queries.  
- [Finding 3] Extension of earlier results to all loss norms $p\ge 1$ and unknown link functions, closing a significant portion of the theoretical gap in active regression.

## Methodology  
The authors adopt a combinatorial optimization viewpoint: they treat the unknown link function as part of the optimization variable alongside $x$, leveraging the Lipschitz constraint to bound possible values. By constructing a set of carefully chosen query points that maximize information gain about both $f$ and $b$, they derive an explicit sampling schedule independent of prior knowledge of $A$ or $f$. The algorithm is analyzed using concentration inequalities for high‑dimensional vectors, ensuring the $(1+\varepsilon)$ guarantee holds with high probability.

## Results  
The theoretical analysis yields a query bound that scales as $O(d^{p/2\vee 1}/ε^{p\vee 2}\operatorname{poly}\log(n/ε))$, which is optimal up to polynomial factors for $p>2$ and matches known bounds for $p=2$. The lower‑bound matching demonstrates that the algorithm cannot be substantially improved without additional assumptions. No empirical experiments are reported because the problem is purely theoretical; all results are derived from rigorous analysis.

## Significance  
This work provides a unified framework for active regression under unknown link functions, enabling practical applications in compressed sensing and learning where only limited access to data is available. By establishing both an upper‑bound algorithm and matching lower bounds, it clarifies the inherent complexity of the problem and guides future research toward more efficient sampling strategies.

## Related Concepts  
- Active (non‑adaptive) regression: selecting a subset of queries that maximize information gain.  
- Single‑index models: regression where only one linear combination $Ax$ is observed.  
- $\ell_p$-loss with unknown link function: loss norm depends on an unconstrained Lipschitz map $f$.  
- $(1+\varepsilon)$ approximation: algorithmic guarantee within a factor of the optimum.  
- Non‑adaptive sampling: queries are fixed in advance, not adaptively chosen based on previous answers.
