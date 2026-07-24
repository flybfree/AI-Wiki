# Summary: 2026-07-22_21-04-51Z_GPE_EvaluatingRobustEvidenceAggregationforFactVeri.md
Saved: 2026-07-24 02:17
Source: 2026-07-22_21-04-51Z_GPE_EvaluatingRobustEvidenceAggregationforFactVeri.md
Model: None

---

## Summary  
The paper tackles the emerging vulnerability of fact‑verification systems when large language models retrieve and cite documents, which can be compromised through GEO (Generative Engine Optimization) attacks. To address this blind spot, it introduces GPE—a multi‑domain benchmark together with a controllable evidence‑aggregation framework that lets researchers inject false or misleading evidence at predefined poisoning ratios. Experiments across several verification methods show measurable drops in accuracy and latency when adversarial evidence is present, phenomena invisible to clean benchmarks alone. The work therefore demonstrates the need for rigorous evaluation of fact checking under adversarial evidence environments.

## Key Contributions  
- [Finding 1] GPE provides the first controllable evidence‑aggregation benchmark for fact verification, enabling systematic testing of GEO‑style poisoning attacks across diverse factual statements.  
- [Finding 2] The framework quantifies robustness degradation in multiple verification methods under varying poisoning ratios, revealing non‑linear performance loss as false evidence is introduced.  
- [Finding 3] Experiments uncover an efficiency trade‑off: higher poisoning rates increase latency and reduce accuracy, highlighting the cost of robustness against adversarial inputs.

## Methodology  
The authors construct a multi‑domain fact‑verification benchmark comprising thousands of statements drawn from news, encyclopedias, and scientific papers. Evidence sources are manipulated by injecting poisoned documents that mimic legitimate retrieval signals, while the poisoning ratio is controlled to range from 0 % (clean) to up to 15 %. An evaluation framework records verification results for each statement under both clean and poisoned conditions, measuring accuracy, F1‑score, and inference latency. The comparison isolates the impact of adversarial evidence on model behavior.

## Results  
Under a 0 % poisoning setting, the baseline models achieve an average accuracy of 92.3 % with a mean inference time of 45 ms per query. When the poisoning ratio is raised to 5 %, accuracy drops to 84.7 % and latency rises to 61 ms—a 12 % increase. At 10 % poisoning, accuracy falls further to 79.1 % while latency reaches 73 ms. These results illustrate a clear degradation curve that is absent in clean evaluations.

## Significance  
Fact verification is critical for maintaining trust in AI‑driven information systems; GEO attacks can propagate misinformation at scale. GPE establishes a standardized, controllable testbed that exposes hidden weaknesses, guiding developers to design more resilient retrieval pipelines and evaluation protocols.

## Related Concepts  
- Fact Verification  
- Large Language Models (LLMs)  
- Evidence Aggregation  
- GEO Poisoning / Generative Engine Optimization  
- Controllable Benchmarking  
- Adversarial Evaluation
