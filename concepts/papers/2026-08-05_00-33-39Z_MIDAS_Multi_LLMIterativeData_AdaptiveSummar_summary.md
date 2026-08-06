# Summary: 2026-08-05_00-33-39Z_MIDAS_Multi_LLMIterativeData_AdaptiveSummarization.md
Saved: 2026-08-05 20:27
Source: 2026-08-05_00-33-39Z_MIDAS_Multi_LLMIterativeData_AdaptiveSummarization.md
Model: None

---

## Summary  
The paper introduces MIDAS, a multi‑LLM framework that automatically adapts summarization prompts to diverse enterprise use cases without manual engineering. By leveraging data‑driven pattern learning and iterative critique from multiple large language models, MIDAS tailors outputs to specific formats such as ticket summaries, legal briefs, or incident reports. The approach eliminates the labor‑intensive prompt‑crafting process that current tools require, enabling continuous personalization as requirements evolve. This work demonstrates that data‑adaptive summarization can outperform existing critique‑driven optimization methods across multiple domains.

## Key Contributions  
- A multi‑LLM framework (MIDAS) that learns domain‑specific patterns from training data and iteratively refines prompts.  
- Automatic adaptation to five output formats for enterprise ticket summarization, surpassing state‑of‑the‑art critique‑driven systems like CriSPO and ZERA.  
- Cross‑model and cross‑domain generalization achieved through varied LLM configurations applied to finance‑domain benchmarks.

## Methodology  
MIDAS builds on the critique‑driven optimization paradigm: a primary LLM generates an initial summary, which is then evaluated by a secondary LLM acting as a critic. The feedback loop updates the prompt template using learned patterns from labeled examples across multiple formats. A multi‑LLM ensemble combines diverse model outputs, and the system adapts its prompt through iterative cycles guided by real‑world data, allowing personalization without human intervention.

## Results  
Experimental evaluation on enterprise customer ticket summarization shows MIDAS improves ROUGE‑1 by up to 11.0%, ROUGE‑2 by up to 18.2%, and ROUGE‑L by up to 8.0% compared with CriSPO and ZERA, while consistently raising BERTScore F1 across all formats and output types. The framework also generalizes well when applied to finance‑domain summarization using different LLM models, confirming cross‑model robustness.

## Significance  
MIDAS addresses a critical bottleneck in enterprise AI: the need for manual prompt engineering that hampers scalability and adaptability. By automating adaptation through data‑driven learning, it reduces operational costs, accelerates deployment of summarization services, and ensures compliance with evolving organizational guidelines—making large‑scale, context‑aware summarization feasible.

## Related Concepts  
- Large Language Model (LLM) critique-driven optimization  
- Data‑adaptive summarization  
- Multi‑LLM ensemble frameworks  
- Prompt personalization without manual engineering  
- ROUGE metrics for evaluation  
- BERTScore for semantic quality assessment
