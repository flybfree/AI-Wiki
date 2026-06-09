# Summary: 2026-05-09_2203.15556-chinchilla-compute-optimal.md
Saved: 2026-05-10 00:00
Source: 2026-05-09_2203.15556-chinchilla-compute-optimal.md
Model: None

---


## Summary  
The paper investigates how to train a transformer language model under a fixed compute budget, revealing that current large‑language models are severely undertrained. By comparing GPT‑3 (175 B parameters, 300 B tokens) with Chinchilla (70 B parameters, 400 B tokens), the authors show that a smaller model trained on much more data outperforms a larger one trained on less data despite using only four times less compute. The study introduces an optimal token‑per‑parameter ratio and a concrete scaling rule for balancing model size and dataset.

## Key Contributions  
- **Finding 1:** Chinchilla (70 B parameters, 400 B tokens) beats GPT‑3 (175 B parameters, 300 B tokens) with only ~20 FLOPs per parameter versus ~1.7 for GPT‑3.  
- **Finding 2:** The optimal token‑per‑parameter ratio is around 20; Chinchilla’s ratio (~5.7) is closer to this sweet spot than GPT‑3’s.  
- **Finding 3:** A practical “double‑both” training strategy: increasing compute by a factor *k* requires multiplying both model parameters and training tokens roughly by √k (e.g., 8× compute → double each).

## Methodology  
The authors built on Kaplan et al.’s scaling laws, keeping GPT‑3’s total FLOPs constant but redistributing them between model size and token count. They trained two models at different sizes on the same dataset, measured performance across standard benchmarks, and derived the token‑per‑parameter sweet spot. The “double‑both” rule was inferred from observed scaling patterns.

## Results  
Chinchilla achieved lower perplexity and higher scores than GPT‑3 while using only 4× less compute (≈20 FLOPs per parameter vs ≈1.7). Its token‑per‑parameter ratio (~5.7) is nearer the theoretical optimum (~20), whereas GPT‑3’s ratio was far below it. The scaling rule holds: for an 8× increase in compute, both model size and data amount should be quadrupled.

## Significance  
This work overturns the “bigger is better” mindset, proving that data quality and quantity are the primary constraints in large‑language‑model scaling. It supplies a concrete recipe for efficient training, directly influencing subsequent models such as PaLM, LLaMA, Mistral, Qwen, and DeepSeek. The paper clarifies why coordination between model size and dataset is essential, turning theoretical scaling laws into actionable practice.

## Related Concepts  
- Scaling laws (Kaplan et al., 2020) – relationship among parameters, data, and compute.  
- Token‑per‑parameter ratio – the optimal balance of model capacity and training data.  
- “Double‑both” rule – proportional increase in both model size and dataset with compute scaling.  
- Data curation and deduplication – importance of high‑quality, non‑redundant data.
