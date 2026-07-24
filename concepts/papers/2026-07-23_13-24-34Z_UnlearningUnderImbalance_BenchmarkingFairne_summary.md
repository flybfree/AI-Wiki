# Summary: 2026-07-23_13-24-34Z_UnlearningUnderImbalance_BenchmarkingFairnessinMul.md
Saved: 2026-07-24 02:45
Source: 2026-07-23_13-24-34Z_UnlearningUnderImbalance_BenchmarkingFairnessinMul.md
Model: None

---

## Summary  
Machine unlearning aims to erase personal data from large language models, but most existing benchmarks assume a uniform distribution of identities and do not reflect real‑world demographic imbalances. This paper introduces FAIRGET, the first Visual Question Answering benchmark that evaluates unlearning under unbalanced, realistic forget requests, and FAUN, an algorithm that unlearns identities while preserving fairness. The study demonstrates that standard unlearning can produce biased behavior when certain groups are over‑ or under‑represented in removal data. By addressing these imbalances, the authors achieve superior unlearning quality together with fairer model outputs.

## Key Contributions  
- [Finding 1] FAIRGET provides a benchmark for visual question answering that includes diverse, realistically imbalanced forget requests across demographic groups, enabling systematic evaluation of fairness‑aware unlearning.  
- [Finding 2] FAUN introduces a bias‑aware activation steering mechanism that selectively removes identity information while compensating for uneven request frequencies to maintain model fairness.  
- [Finding 3] Experiments on FAIRGET and the established FIUBench show that FAUN outperforms baseline unlearning methods in both quantitative unlearning accuracy and qualitative fairness metrics.

## Methodology  
The authors first generate synthetic multimodal data where each image‑text pair is tagged with a demographic identifier. They then create forget requests that vary in frequency, mimicking real user behavior. The unlearning process employs FAUN’s bias‑aware activation steering: during fine‑tuning, the algorithm adjusts layer activations to suppress the influence of over‑represented groups while preserving correct representation for under‑represented ones. Fairness is measured by downstream visual question answering performance across all demographic slices.

## Results  
On FAIRGET, models using FAUN achieve a 4.2 % higher accuracy on average than baselines that ignore imbalance (e.g., standard fine‑tuning). Fairness metrics such as demographic parity and equalized odds improve by up to 15 % relative to baseline scores. The FIUBench comparison confirms that FAUN’s unlearning quality is comparable or better while maintaining fairness, validating the method’s robustness across tasks.

## Significance  
This work bridges a critical gap in AI regulation compliance: unlearning must not only erase data but also respect demographic equity. By providing a benchmark and an algorithm that handles imbalance, FAIRGET and FAUN enable developers to build responsible multimodal LLMs that comply with emerging fairness standards without sacrificing performance.

## Related Concepts  
- Machine unlearning (removing personal data from models)  
- Multimodal large language model (MLLM) fine‑tuning  
- Visual Question Answering (VQA) benchmarking  
- Demographic imbalance and bias in training data  
- Fairness metrics: demographic parity, equalized odds  
- Bias‑aware activation steering for selective memory erasure
