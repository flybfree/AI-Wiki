# Summary: 2026-08-05_04-56-53Z_ACounterexampletoFourierAlignmentinSingle_NeuronMo.md
Saved: 2026-08-05 22:24
Source: 2026-08-05_04-56-53Z_ACounterexampletoFourierAlignmentinSingle_NeuronMo.md
Model: None

---

## Summary  
The paper provides a counterexample showing that Fourier alignment does not hold for single‑neuron modular addition, demonstrating that an initially active ReLU neuron can become completely inactive while its Fourier energy remains uniformly distributed among all frequencies. This negative solution to MAIS‑O60 challenges the assumption that training leads to such alignment. The construction applies to an open set of initial conditions, implying positive probability under Gaussian initialization.

## Key Contributions  
- [Finding 1] Construction of a finite‑time dead neuron with equal Fourier energy distribution.  
- [Finding 2] Verification that the failure occurs for every Clarke trajectory from an open set of initial conditions under smooth ReLU approximations and fixed‑step gradient descent.  
- [Finding 3] Demonstration that single‑frequency alignment is not a general consequence of training a single neuron on modular addition.

## Methodology  
The authors approach the problem theoretically by analyzing the dynamics of a single ReLU neuron in a modular addition setting. They construct a specific initial condition where the neuron’s activation decays to zero, then remains at a limit state whose Fourier transform exhibits uniform energy across all nonzero frequencies. This is done analytically using properties of ReLU and its derivative conventions.

## Results  
The counterexample holds on an open set of initial conditions, confirming that with positive probability under Gaussian initialization the neuron will exhibit this behavior. The appendix shows that the same phenomenon persists for every Clarke trajectory from such a set, reinforcing the generality of the failure. Thus, Fourier alignment is not guaranteed in single‑neuron modular addition.

## Significance  
This result matters because it undermines the belief that training simple neural modules leads to frequency‑wise energy equilibration, which has been used as a diagnostic for learning stability. By providing a concrete counterexample, the paper highlights the need for more careful analysis of activation dynamics beyond Fourier assumptions.

## Related Concepts  
- ReLU neuron  
- Modular addition  
- Fourier alignment / energy distribution  
- MAIS‑O60 conjecture  
- Clarke trajectories  
- Gaussian initialization  
- Fixed‑step gradient descent
