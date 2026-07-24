# Summary: 2026-07-21_21-15-55Z_End_to_EndDifferentialPrivacyinTrainingDeepNeuralN.md
Saved: 2026-07-24 01:14
Source: 2026-07-21_21-15-55Z_End_to_EndDifferentialPrivacyinTrainingDeepNeuralN.md
Model: None

---

## Summary  
The paper proposes an end‑to‑end differentially private framework for training deep neural network classifiers where only the input data is protected while labels remain public. It leverages Dirichlet randomization of softmax outputs to enforce DP on inputs and uses Rényi DP to bound privacy loss across repeated epochs. The approach achieves state‑of‑the‑art accuracy on several benchmark datasets under various privacy budgets. This work demonstrates that selective privacy application can preserve model performance without sacrificing utility.

## Key Contributions  
- [Finding 1] Introduces a private training framework that privatizes only the input data, keeping labels public.  
- [Finding 2] Applies Dirichlet mechanism to randomize softmax outputs, providing end‑to‑end DP for inputs.  
- [Finding 3] Formulates tight Rényi DP bounds accounting for label reuse across epochs.

## Methodology  
The authors consider neural networks with softmax output layers that map training inputs onto the unit simplex. During training they replace deterministic softmax outputs with Dirichlet‑distributed values, injecting noise proportional to the privacy parameter ε. They employ Rényi differential privacy to analyze cumulative privacy loss over multiple epochs, ensuring each use of data contributes within the ε budget. Training proceeds as usual but with noisy labels; the model learns from this randomized target while preserving input confidentiality.

## Results  
Experiments on CIFAR10, MNIST, MedMNIST, FashionMNIST, and SVHN show improved accuracy compared to prior DP methods. At (ε=4, δ=1e‑5) they achieve 88.17 % on CIFAR10 versus the prior 78.37 %. Even at ε=1 they reach 82.96 %, surpassing earlier work. These gains are consistent across all datasets and privacy budgets, confirming that selective privacy can boost performance.

## Significance  
By decoupling input privacy from label privacy, the method reduces privacy overhead while preserving model utility. It enables practical deployment of DP in settings where labels are public or safe to share, opening new avenues for privacy‑preserving AI without compromising accuracy.

## Related Concepts  
Differential privacy (DP), Rényi DP, Dirichlet mechanism, softmax layer, unit simplex mapping, end‑to‑end training, privacy budget allocation.
