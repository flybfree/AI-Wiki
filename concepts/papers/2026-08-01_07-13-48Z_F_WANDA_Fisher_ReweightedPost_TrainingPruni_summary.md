# Summary: 2026-08-01_07-13-48Z_F_WANDA_Fisher_ReweightedPost_TrainingPruningforSu.md
Saved: 2026-08-03 20:22
Source: 2026-08-01_07-13-48Z_F_WANDA_Fisher_ReweightedPost_TrainingPruningforSu.md
Model: None

---

## Summary  
The paper tackles the challenge of compressing large language models (LLMs) with minimal loss in performance, highlighting that one‑shot post‑training pruning methods such as WANDA and SPARSEGPT each excel in a single dimension—WANDA preserves fluency while SPARSEGPT reduces compute cost. By introducing Fisher‑Reweighted Post‑Training Pruning (F‑WANDA), the authors achieve a Pareto‑optimal trade‑off: they retain WANDA’s quality metrics while cutting wall‑clock and energy consumption to one‑third of SPARSEGPT, all without extra calibration data or fine‑tuning. The approach is demonstrated on LLAMA‑2‑7B at 50 % unstructured sparsity, delivering a WikiText‑2 perplexity of 6.85 that matches WANDA’s fluency and improving MMLU scores by +1.6 pp over WANDA and +1.1 pp over SPARSEGPT.  

## Key Contributions  
- **Fisher‑Reweighted Budget Allocation**: F‑WANDA reallocates the per‑row keep budget across output neurons proportionally to the empirical Fisher information of pre‑activations, enabling a more efficient use of sparsity resources.  
- **Single‑Pass Fisher Signal Collection**: The method gathers the Fisher signal in one additional backward pass over the calibration corpus already used by WANDA, avoiding weight updates or new training passes.  
- **Pareto‑Frontier Performance**: F‑WANDA simultaneously matches WANDA’s quality (perplexity 6.85) and improves downstream tasks (+1.6 pp MMLU over WANDA), while incurring only one‑third of SPARSEGPT’s computational cost, thus lying on the Pareto frontier of quality versus pruning cost.  

## Methodology  
F‑WANDA is a drop‑in modification of the original WANDA algorithm that computes Fisher information for each output neuron during a single backward pass over the calibration dataset. The Fisher score quantifies how much variance an output neuron contributes to the loss signal, guiding which neurons should be kept or pruned. The algorithm then redistributes the fixed keep budget across neurons according to this score, ensuring that high‑information neurons are retained while low‑impact ones are removed. No model weights are altered; only the sparsity pattern is adjusted, preserving the original pre‑training knowledge.  

## Results  
On LLAMA‑2‑7B with 50 % unstructured sparsity, F‑WANDA achieves a WikiText‑2 perplexity of 6.85, identical to WANDA’s best result, indicating no degradation in fluency. Benchmarking on MMLU (5‑shot), the model scores +1.6 percentage points above WANDA and +1.1 pp above SPARSEGPT. Computationally, F‑WANDA requires only one additional backward pass over the calibration corpus, reducing wall‑clock time to roughly one‑third of SPARSEGPT’s pruning cost while using comparable energy. These results demonstrate that quality can be preserved and even enhanced when computational resources are limited.  

## Significance  
By offering a method that simultaneously maximizes linguistic quality and minimizes deployment cost, F‑WANDA addresses the sustainability concerns surrounding large language model compression. It enables organizations to deploy LLMs on edge devices or in low‑power environments without sacrificing user experience, thereby reducing carbon footprints associated with massive inference workloads. The approach also provides a principled way to allocate sparsity resources based on empirical signal rather than heuristic thresholds, potentially improving both efficiency and robustness across diverse tasks.  

## Related Concepts  
- Post‑training pruning (one‑shot)  
- Unstructured sparsity  
- Fisher information theory  
- WANDA algorithm  
- SPARSEGPT  
- Pareto frontier optimization
