# Summary: 2026-08-02_03-53-30Z_MindtheGap_Zero_QueryJailbreaksviaFilter_Generator.md
Saved: 2026-08-03 21:30
Source: 2026-08-02_03-53-30Z_MindtheGap_Zero_QueryJailbreaksviaFilter_Generator.md
Model: None

---

## Summary  
The paper investigates why text‑to‑image (T2I) safety filters can be bypassed by malicious prompts that are crafted offline without ever querying the target model, a phenomenon known as a zero‑query jailbreak. By exposing a systematic mismatch between how the filter and generator interpret a prompt—the Filter‑Generator Discrepancy (FGD)—the authors propose an entirely offline attack framework that exploits this gap to generate safe‑looking but unsafe images. Their method screens perturbations using tokenization and semantic rules, then runs a surrogate‑ensemble evolutionary search, achieving higher success rates than comparable baselines.

## Key Contributions  
- [Finding 1] The Filter‑Generator Discrepancy (FGD) is identified as the core vulnerability that allows a prompt to appear low‑risk to the filter while still preserving the visual concept required by the generator.  
- [Finding 2] A zero‑query jailbreak framework is introduced, which uses observable discrepancy rules at tokenization and semantic stages to prune the search space into high‑potential candidates without any access to the target model.  
- [Finding 3] The surrogate‑ensemble evolutionary search is demonstrated as an effective offline optimization strategy that maximizes attack success while keeping computational cost low.

## Methodology  
The authors first characterize how filters and generators process a prompt: the filter evaluates risk based on token patterns, whereas the generator focuses on semantic content. They define FGD as any deviation between these two evaluations. Using this definition, they generate perturbations that lower the filter’s perceived risk (e.g., by masking or re‑ordering tokens) while keeping the underlying image concept intact. These perturbations are then evaluated with a surrogate model trained offline; the best‑performing ones are selected iteratively through an evolutionary algorithm that combines crossover and mutation operators. No interaction with the target T2I pipeline occurs during this process.

## Results  
Experiments were conducted on six black‑box pipelines and one commercial online service (Q16). The proposed method achieved an average attack success rate of 29.2 % for MHSC and 33.3 % for Q16, surpassing the strongest baselines by roughly 8–12 percentage points. This improvement is consistent across all tested systems, indicating robustness to different filter‑generator architectures.

## Significance  
Understanding FGD provides a new lens on how safety mechanisms can be circumvented without direct model probing, which is crucial for designing more resilient T2I deployments. The zero‑query approach offers a practical way to stress‑test filters offline, reducing reliance on costly adversarial testing that requires live model access.

## Related Concepts  
- Text‑to‑image (T2I) systems  
- Prompt‑level safety filters  
- Jailbreak prompts and attacks  
- Adversarial prompt engineering  
- Surrogate modeling and evolutionary search  
- Tokenization and semantic similarity analysis
