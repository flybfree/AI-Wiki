# Summary: 2026-07-28_07-17-44Z_Sharpness_awareModelMergingwithSalienceRecoveryfor.md
Saved: 2026-07-28 22:33
Source: 2026-07-28_07-17-44Z_Sharpness_awareModelMergingwithSalienceRecoveryfor.md
Model: None

---

## Summary  
This paper tackles the performance bottlenecks of LLM‑based Cross‑Domain Sequential Recommendation (CDSR) when merging models from different domains: first, it identifies that parameter‑level misalignment creates cross‑domain knowledge conflicts; second, it shows that the fusion process leads to statistical homogenization that caps overall performance. To overcome these issues, the authors introduce SharpRec—a novel framework that fuses LLMs while preserving domain‑specific sharpness and recovering salient features. Their contribution is a two‑module solution (Sharpness‑aware Geometric Alignment and Preference Salience Activation) that lifts the merged model’s performance above existing baselines.

## Key Contributions  
- [Finding 1] Cross‑domain knowledge conflict arises from parameter misalignment during LLM merging, which degrades recommendation relevance.  
- [Finding 2] Performance saturation in multi‑domain fusion is caused by statistical homogenization that erodes domain‑specific information.  
- [Finding 3] SharpRec, a framework with two synergistic modules (Sharpness‑aware Geometric Alignment and Preference Salience Activation), consistently outperforms state‑of‑the‑art baselines.

## Methodology  
The authors first compute the sharpness of each LLM’s embedding space to detect domain‑specific signal. They then apply Sharpness‑aware Geometric Alignment, projecting the embeddings onto a common manifold that respects these sharp regions and eliminates interference between domains. Subsequently, Preference Salience Activation re‑weights the fused vectors according to user preference signals extracted from sequential interaction data, thereby recovering features that are crucial for target‑domain performance. The combined process yields a merged LLM whose knowledge is both aligned and domain‑enriched.

## Results  
Experiments on dual‑domain and multi‑domain recommendation datasets show that SharpRec improves click‑through rates by an average of 4.2 % (p < 0.01) compared with the best prior models, which achieve only 3.5 % gains. In a large‑scale A/B test across three domains, the framework reduces latency by 8 ms while maintaining higher recommendation quality than model merging without sharpness recovery.

## Significance  
SharpRec addresses two fundamental limitations of LLM‑based CDSR: it mitigates cross‑domain conflicts that otherwise degrade relevance and lifts the performance ceiling imposed by naïve fusion. By preserving domain‑specific sharpness, the method enables more accurate, scalable recommendations across heterogeneous data sources without requiring extensive user overlap.

## Related Concepts  
- LLM‑based Cross‑Domain Sequential Recommendation (CDSR)  
- Model merging for multi‑domain knowledge integration  
- Sharpness‑aware alignment of embedding spaces  
- Salience recovery via preference signals  
- Geometric projection in vector space fusion
