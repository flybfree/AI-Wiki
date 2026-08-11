# Summary: 2026-08-10_15-11-22Z_Inputconvexneuralnetworksassurrogatesinmathematica.md
Saved: 2026-08-11 00:15
Source: 2026-08-10_15-11-22Z_Inputconvexneuralnetworksassurrogatesinmathematica.md
Model: None

---

## Summary  
The paper proposes using input convex neural networks (ICNNs) as surrogates in mathematical optimisation problems, arguing they are superior to traditional feedforward ReLU networks. ICNNs exploit the approximate convexity of the underlying response to provide tighter linear programming relaxations and avoid integrality gaps. The authors develop a branch‑and‑bound algorithm that builds a continuous relaxation based on the epigraph and concave envelope of the network, branching directly on inputs. Experiments show ICNN surrogates match FNN accuracy while improving solve time and scalability.

## Key Contributions  
- [Finding 1] Input convex neural networks are identified as structurally superior surrogates for approximately convex or concave functions.  
- [Finding 2] The ICNN‑MIP formulation yields a tighter linear programming relaxation than the FNN‑MIP counterpart with no integrality gap in favourable instances.  
- [Finding 3] A branch‑and‑bound algorithm is introduced that constructs the strongest continuous relaxation via epigraph and concave envelope, enabling early termination when the embedding holds.

## Methodology  
The authors approach the problem by first formulating the optimisation as an MIP using the ICNN surrogate. They then derive a continuous relaxation by representing ReLU activations with epigraph constraints and bounding the network output between its epigraph and concave envelope. This relaxation is built at each branch‑and‑bound node, allowing direct branching on input variables rather than intermediate ones, and termination occurs when the epigraph embedding holds.

## Results  
Experimental case studies in humanitarian food aid, oil well routing, and wine blending confirm that ICNN surrogates achieve FNN‑level accuracy while reducing solve time by up to 40 % and enabling scalable solutions for larger instances. Theoretical analysis shows the LP relaxation of the ICNN‑MIP formulation has an integrality gap of zero when the underlying function is convex or concave.

## Significance  
This work bridges neural network surrogate modeling with exact optimisation, offering a practical alternative to computationally heavy MIP reformulations. By leveraging input convexity, it reduces problem size and improves robustness, making high‑precision optimisation feasible in real‑world applications.

## Related Concepts  
- Input convex neural networks (ICNN)  
- Feedforward ReLU networks (FNN)  
- Mixed‑integer programming (MIP) reformulation  
- Linear programming relaxation  
- Epigraph representation of ReLU activations  
- Concave envelope  
- Branch‑and‑bound algorithm
