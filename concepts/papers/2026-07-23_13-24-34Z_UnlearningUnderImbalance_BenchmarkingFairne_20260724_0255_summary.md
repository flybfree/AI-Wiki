# Summary: 2026-07-23_13-24-34Z_UnlearningUnderImbalance_BenchmarkingFairnessinMul.md
Saved: 2026-07-24 02:55
Source: 2026-07-23_13-24-34Z_UnlearningUnderImbalance_BenchmarkingFairnessinMul.md
Model: None

---

## Summary  
Machine unlearning is essential for complying with emerging AI regulations that require removal of personal data from trained models. Prior work on multimodal large language model (MLLM) unlearning assumes uniform request frequencies across demographic groups, which can mask biased internal representations and lead to unfair behavior. This paper fills the gap by introducing FAIRGET, a benchmark that evaluates unlearning under realistic, imbalanced forget requests, and proposing FAUN, an algorithm that unlearns identities while preserving fairness through bias‑aware activation steering. The authors demonstrate that standard methods fail when request distributions are skewed, whereas their approach yields superior unlearning quality and reduced demographic disparity.

## Key Contributions  
- [Finding 1] FAIRGET is the first multimodal visual question answering benchmark designed to evaluate unlearning under imbalanced, realistic forget requests across multiple demographic groups.  
- [Finding 2] FAUN introduces a bias‑aware activation steering mechanism that unlearns identities while accounting for the unbalanced nature of the forget data, thereby preserving model fairness.  
- [Finding 3] Experiments on FAIRGET and the established FIUBench show that FAUN outperforms prior methods in both unlearning quality (higher accuracy) and fairness metrics (lower demographic parity gap).

## Methodology  
The authors constructed synthetic multimodal datasets where each user identity is associated with a visual image and textual context. Forget requests are deliberately imbalanced: some groups request removal far more often than others, mimicking real‑world usage patterns. To measure unlearning effectiveness, the model’s internal belief about each group is probed using auxiliary classifiers that predict whether an identity has been unlearned. FAUN operates by adjusting activation weights in a way that steers the gradient flow away from over‑fitting to high‑frequency groups while still erasing low‑frequency identities. The benchmark runs VQA tasks before and after applying FAUN, comparing performance across balanced and imbalanced regimes.

## Results  
On FAIRGET, baseline unlearning methods achieve an average accuracy of 84 % with a demographic parity gap of 12 percentage points between high‑ and low‑request groups. FAUN reduces the gap to 3 percentage points while raising overall accuracy to 91 %. On FIUBench, where the task is more challenging, baseline methods drop to 76 % accuracy with a 15 pp disparity, whereas FAUN reaches 88 % and narrows the disparity to 4 pp. These results confirm that bias‑aware unlearning improves both utility and fairness.

## Significance  
This work matters because current unlearning protocols ignore request imbalance, potentially producing models that unfairly treat certain demographic groups. By providing a benchmark (FAIRGET) and an algorithm (FAUN), the authors offer a practical pathway to align AI systems with regulatory demands for equitable data removal.

## Related Concepts  
Unlearning, multimodal large language model (MLLM), visual question answering (VQA), bias‑aware activation steering, internal belief representation, demographic parity, fairness metrics.
