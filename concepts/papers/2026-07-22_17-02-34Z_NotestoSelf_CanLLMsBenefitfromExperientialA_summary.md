# Summary: 2026-07-22_17-02-34Z_NotestoSelf_CanLLMsBenefitfromExperientialAbstract.md
Saved: 2026-07-24 02:09
Source: 2026-07-22_17-02-34Z_NotestoSelf_CanLLMsBenefitfromExperientialAbstract.md
Model: None

---

## Summary  
The paper investigates whether large language models can benefit from experiential abstractions—human‑like distilled knowledge such as strategies and reminders—and tests this hypothesis on mathematical reasoning tasks. It extracts natural‑language abstractions from LLM solution traces, then evaluates two usage modes: retrieval at inference time and reinforcement learning with abstraction‑augmented prompts. The study shows that these abstractions improve performance across math and logic benchmarks.

## Key Contributions  
- Learned experiential abstractions can be extracted automatically from LLM reasoning traces.  
- Both teacher‑extracted and self‑extracted abstractions enhance LLM performance on MATH and logical tasks.  
- The abstraction usage framework is transferable to other datasets and models.

## Methodology  
The authors analyze solution traces of LLMs on the MATH dataset, identify recurring patterns as natural‑language abstractions, store them in a library, and then evaluate retrieval during inference or incorporate them into reinforcement learning training prompts. They compare performance with and without abstractions, and also compare teacher‑extracted vs self‑extracted abstractions.

## Results  
Retrieval improves accuracy by a significant margin across the MATH benchmark, while abstraction‑augmented RL yields comparable gains to teacher‑distilled models. The framework transfers successfully to other reasoning datasets, demonstrating robustness beyond the original training set.

## Significance  
This work demonstrates that LLMs can learn from distilled experience much as humans do, offering a path to more robust and efficient reasoning without requiring massive retraining or additional data.

## Related Concepts  
Experiential abstraction, teacher‑student distillation, reinforcement learning with prompts, retrieval augmentation, MATH benchmark.
