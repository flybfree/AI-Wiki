# Summary: 2026-07-22_06-03-20Z_AMulticlassQuantumAlignedCentroidKernel.md
Saved: 2026-07-24 01:27
Source: 2026-07-22_06-03-20Z_AMulticlassQuantumAlignedCentroidKernel.md
Model: None

---

## Summary  
The paper proposes a trainable quantum kernel called McQuack that tackles three long‑standing problems in kernel methods: quadratic scaling, non‑trainable kernels, and the lack of an intrinsic multiclass formulation. By replacing the full training‑set Gram matrix with a trainable sample‑to‑class‑centroid fidelity matrix, McQuack achieves linear dependence on the number of samples. The authors demonstrate that both simulated and hardware‑based (IBM 124‑qubit) evaluations outperform existing quantum baselines and match the performance of an RBF kernel without any training overhead.  

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 6 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A trainable quantum kernel that scales linearly with training data by using a fidelity matrix between samples and class centroids rather than a full Gram matrix.  
- [Finding 2] Hardware inference on IBM devices yields results comparable to an RBF kernel, showing practical relevance of the algorithm without training.  
- [Finding 3] Experiments up to 13 qubits reveal no barren‑plateau behavior, highlighting that careful parameter initialization is crucial for successful optimization.  

## Methodology  
The authors construct a quantum circuit where each class is represented by a centroid state; the kernel computes fidelity between training samples and these centroids. This trainable matrix replaces the O(N²) Gram matrix, enabling gradient‑based learning of the kernel parameters. The method is applied to multiclass classification tasks, with optimization performed via standard gradient descent on simulated data and on real IBM Q hardware.  

## Results  
In simulation, McQuack consistently outperformed pure quantum kernels such as the variational circuit baseline. When deployed on 124 qubits of two IBM devices, inference without training achieved performance within a few percent of an RBF kernel’s accuracy across more than 150 datasets. The model remained trainable up to 13 qubits with no signs of barren plateaus, provided the initial parameters were initialized appropriately.  

## Significance  
McQuack addresses the scalability bottleneck of full‑Gram kernels and introduces a fully trainable quantum algorithm that can be used on near‑term NISQ hardware. By providing linear scaling and comparable performance to classical RBF kernels, it opens a pathway for scalable multiclass classification in the era of limited qubits.  

## Related Concepts  
- Kernel methods (Gram matrix, RBF kernel)  
- Quantum computing and quantum kernels  
- Trainable quantum algorithms  
- Class‑centroid representation  
- Barren plateaus  
- Parameter initialization strategies
