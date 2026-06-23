# Summary: 2026-06-21_17-24-31Z_Sub_Billion_Super_Frontier_SmallLanguageModelsRiva.md
Saved: 2026-06-22 22:01
Source: 2026-06-21_17-24-31Z_Sub_Billion_Super_Frontier_SmallLanguageModelsRiva.md
Model: None

---


## Summary  
The paper investigates whether small language models (SLMs) can match the performance of zero‑shot frontier LLMs on relation extraction tasks across both general‑domain and literary texts. By fine‑tuning compact 360 M–3 B parameter models on pooled data, the authors demonstrate that task‑specific adaptation yields micro‑F1 scores comparable to or exceeding those of large generative systems when deployed on a single consumer GPU. The results also reveal that the advantage stems from targeted training rather than sheer model size, and that an in‑domain RoBERTa baseline can surpass frontier models without any generative decoding.  

## Key Contributions  
- [Finding 1] Small language models (up to 0.5 B parameters) achieve a general‑domain positive‑class micro‑F1 of 0.83, outperforming GPT‑5.4 (0.69) and Claude Sonnet 4.6 (0.66) evaluated zero‑shot.  
- [Finding 2] Within‑family scale comparisons show only marginal improvement for SLMs versus larger models, indicating that performance gains are driven by task adaptation rather than model capacity alone.  
- [Finding 3] An in‑domain RoBERTa baseline also exceeds both GPT‑5.4 and Claude Sonnet 4.6 on literary RE benchmarks (0.92 vs 0.83/0.833), proving that task‑specific adaptation yields superior results over generic generative decoding.  

## Methodology  
The authors evaluate five SLMs ranging from 360 M to 3 B parameters across three domain‑composition regimes and two prompt‑conditioned tuning styles, generating 30 configurations total. They compare these models against zero‑shot frontier LLMs (GPT‑5.4, Claude Sonnet 4.6) and a discriminative RoBERTa baseline on nine relation‑extraction benchmarks that span general‑domain and literary texts. The evaluation focuses on micro‑F1 scores for positive‑class extraction to quantify performance.  

## Results  
The best‑performing SLM, Qwen2.5‑0.5B fine‑tuned on pooled general‑domain data, reaches a micro‑F1 of 0.83 in the general domain, surpassing both GPT‑5.4 (0.69) and Claude Sonnet 4.6 (0.66). On literary RE, tuned SLMs achieve 0.92 on the human‑annotated Biographical benchmark versus 0.83 for GPT‑5.4 and an average of 0.833/0.578 across two literary benchmarks. A clean within‑family scale comparison reveals only marginal improvement, confirming that adaptation outweighs size differences.  

## Significance  
These findings demonstrate that compact, task‑adapted models can deliver accurate, private, and hardware‑efficient relation extraction, enabling deployment in resource‑constrained or privacy‑sensitive environments where large frontier LLMs are impractical. The work underscores the importance of targeted fine‑tuning over raw model scaling for high‑quality downstream tasks.  

## Related Concepts  
Relation extraction (RE), zero‑shot frontier LLMs, small language models, fine‑tuning, domain adaptation, RoBERTa baseline, micro‑F1 score, generative decoding, parameter efficiency.
