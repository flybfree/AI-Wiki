# Summary: 2026-08-10_15-11-22Z_Inputconvexneuralnetworksassurrogatesinmathematica.md
Saved: 2026-08-10 23:52
Source: 2026-08-10_15-11-22Z_Inputconvexneuralnetworksassurrogatesinmathematica.md
Model: None

---

## Summary  
The paper proposes using input convex neural networks (ICNNs) as surrogates in mathematical optimisation problems, arguing that they outperform traditional feedforward ReLU networks when the underlying response is approximately convex or concave. By exploiting the structural properties of ICNNs—particularly their ability to be represented via epigraph constraints—the authors develop a branch‑and‑bound algorithm that builds tighter linear programming relaxations than the usual mixed‑integer programming (MIP) reformulation of FNNs. Experimental case studies on humanitarian food aid, oil well routing, and wine blending demonstrate that ICNN surrogates match FNN accuracy while delivering substantial gains in solve time and scalability.  

## Key Contributions  
- [Finding 1] The ICNN‑MIP formulation yields a tighter linear programming relaxation than the conventional FNN‑MIP counterpart, with no integrality gap in favourable instances.  
- [Finding 2] ICNNs admit an LP‑based reformulation via epigraph representations of ReLU activations; when this embedding is not exact we construct the strongest continuous relaxation as the convex hull of the ICNN graph, bounded below by the epigraph and above by its concave envelope.  
- [Finding 3] A branch‑and‑bound algorithm builds this relaxation at each node, branches directly on input variables rather than intermediate ones, and terminates early when the epigraph embedding is valid.  

## Methodology  
The authors approached the problem by first analysing the exact MIP reformulation of feedforward ReLU networks, which becomes computationally intractable as network depth grows. They then introduced ICNNs, whose piecewise‑linear structure allows an LP‑based epigraph formulation that is exact only under input convexity. To handle imperfect embeddings they defined a tractable relaxation: the convex hull of the ICNN graph, bounded by the epigraph and the concave envelope. The branch‑and‑bound algorithm evaluates this relaxation at each node, branching on input variables, and stops early when the epigraph constraint is satisfied, thereby avoiding unnecessary integer decisions.  

## Results  
Experimental results across three domains show that ICNN surrogates achieve FNN accuracy within a few percent while reducing solve time by up to 70 % and improving scalability for larger instances. Theoretical analysis confirms that the LP relaxation derived from the convex hull has an integrality gap of zero when the underlying function is convex, and a bounded gap otherwise.  

## Significance  
This work matters because it provides a theoretically grounded alternative to MIP‑based FNN surrogates, offering faster, more scalable optimisation for problems where response functions are convex or concave. By leveraging ICNNs’ structural properties, the method reduces computational overhead and enables practical use in large‑scale operations research applications such as humanitarian logistics, resource routing, and supply‑chain planning.  

## Related Concepts  
input convex neural networks (ICNN), epigraph representation of ReLU activations, linear programming relaxation, mixed‑integer programming (MIP) reformulation, branch‑and‑bound algorithm, convex hull of a graph, concave envelope, input convexity, surrogate modeling.
