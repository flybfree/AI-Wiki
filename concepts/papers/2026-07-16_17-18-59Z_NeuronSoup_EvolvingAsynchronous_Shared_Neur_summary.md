# Summary: 2026-07-16_17-18-59Z_NeuronSoup_EvolvingAsynchronous_Shared_NeuronTempo.md
Saved: 2026-07-23 23:47
Source: 2026-07-16_17-18-59Z_NeuronSoup_EvolvingAsynchronous_Shared_NeuronTempo.md
Model: None

---

## Summary  
NeuronSoup proposes an architecture that replaces the conventional synchronous, layer‑by‑layer processing of deep networks with asynchronous signal propagation through a shared pool of neurons. By allowing each input to travel along independent paths that may share intermediate hidden neurons, the system creates constructive or destructive interference based on arrival timing and polarity without requiring any back‑propagation. The topology, weights, delays, and connectivity are co‑evolved by a genetic algorithm operating on a flat real‑valued genome of 14 602 genes, yielding a network that adapts its depth per sample. This approach achieves strong performance on MNIST classification while occupying only 115 KB of memory.

## Key Contributions  
- [Finding 1] The architecture eliminates the need for a differentiable computation graph by using asynchronous, shared‑neuron temporal graphs where signal interference is naturally induced.  
- [Finding 2] A genetic algorithm co‑evolves a flat genome of 14 602 genes to design topology, weights, delays, and connectivity, outperforming CMA‑ES at this scale.  
- [Finding 3] The evolved network attains 85.9 % test accuracy on MNIST with 204 active paths through 266 hidden neurons (156 shared across multiple paths), occupying a compact 115 KB footprint.

## Methodology  
The authors treat the neural computation as an evolutionary optimization problem: each individual in the population is represented by a flat real‑valued genome encoding connectivity, weight magnitudes, and inter‑neuron delays. The fitness function measures classification accuracy on frozen ResNet18 features. CMA‑ES was ruled out because it cannot handle the high‑dimensional, non‑convex landscape of 14 602 genes; instead a custom genetic algorithm with crossover, mutation, and selection is employed for thousands of generations. The network’s dynamic depth per sample is controlled by the number of active paths selected at inference time.

## Results  
After 10 000 generations the evolved system processes each MNIST digit through up to 204 parallel paths that share a common pool of 266 hidden neurons, with one neuron participating in eleven distinct paths. The model reaches 85.9 % test accuracy while occupying only 115 KB of storage—significantly smaller than comparable deep networks.

## Significance  
NeuronSoup demonstrates that deep learning can be replaced by a biologically inspired, non‑differentiable architecture that automatically discovers lateral interactions between processing pathways. By co‑evolving topology and dynamics without gradients, the method sidesteps gradient vanishing issues, enables per‑sample depth adaptation, and produces compact, interpretable models suitable for resource‑constrained domains.

## Related Concepts  
- Genetic algorithms (GA) as optimization tools for high‑dimensional design spaces.  
- CMA‑ES (Covariance Matrix Adaptation Evolution Strategy), a stochastic local search method unsuitable here due to scale.  
- Temporal graphs and shared neurons that enable asynchronous signal interference.  
- Flat real‑valued genomes representing topology, weights, delays, and connectivity.  
- Lateral interactions between processing pathways discovered implicitly rather than engineered explicitly.
