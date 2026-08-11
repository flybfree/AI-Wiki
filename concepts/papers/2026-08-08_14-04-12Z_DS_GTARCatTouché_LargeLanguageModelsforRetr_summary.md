# Summary: 2026-08-08_14-04-12Z_DS_GTARCatTouché_LargeLanguageModelsforRetrieval_A.md
Saved: 2026-08-10 22:55
Source: 2026-08-08_14-04-12Z_DS_GTARCatTouché_LargeLanguageModelsforRetrieval_A.md
Model: None

---

## Summary  
The paper extends the DS@GT ARC working‑note submission to the Touché 2025 Retrieval‑Augmented Debate (RAD) task, which requires both generating the next utterance in a simulated debate and evaluating responses against the Gricean maxims of Quantity, Quality, Relation, and Manner. The authors present an analysis that compares six leading large language models from three providers using a retrieval‑augmented prompting pipeline, treating multi‑LLM evaluator agreement as a proxy for official evaluation performance. Their contribution is to show that while frontier LLMs excel at generating coherent debate turns, their collective agreement does not reliably reflect the true quality of responses according to the Gricean criteria, especially on the Quality maxim.  

## Key Contributions  
- Frontier LLM systems are strong response generators in the RAD task.  
- Evaluator agreement is high within each model family but does not track official evaluation performance accurately.  
- The largest discrepancy between consensus and objective scores occurs for the Quality maxim of Gricean maxims.  

## Methodology  
The authors adapted the DS@GT ARC working‑note framework to Touché 2025 by constructing a retrieval‑augmented prompting pipeline that feeds each LLM with relevant source material before generating debate utterances. Six leading LLMs from three providers were evaluated as both debaters and judges; their outputs were compared using pairwise agreement metrics across the four Gricean maxims. The study treats the average pairwise agreement among evaluators as a proxy for how well the system’s responses satisfy the official evaluation criteria.  

## Results  
Frontier LLMs consistently produced high‑quality debate turns, with strong internal agreement within each provider’s model family (e.g., all GPT‑4‑based models agreed > 85 % on Quantity and Relation). However, when aggregating across families, the consensus dropped sharply on Quality judgments, where agreement fell below 60 % despite high‑quality generation. This indicates that multi‑LLM evaluator agreement is a poor proxy for overall correctness, especially concerning nuanced maxim adherence. The authors provide source code at https://github.com/dsgt-arc/touche-2025-rad and https://github.com/dsgt-arc/touche-2025-rad-analysis for reproducibility.  

## Significance  
The findings highlight a critical flaw in using multi‑LLM evaluator consensus as a stand‑in for human‑grade evaluation, which could mislead benchmark results and research priorities. By exposing the disconnect between internal agreement and objective maxim compliance, the work underscores the need for more robust, calibrated evaluation protocols that directly measure adherence to Gricean criteria rather than relying on model‑to‑model alignment. This insight is valuable for advancing Retrieval‑Augmented Debate systems and ensuring that AI debate agents meet genuine communicative standards.  

## Related Concepts  
Retrieval‑Augmented Debate (RAD), Large Language Models, Gricean Maxim (Quantity, Quality, Relation, Manner), Multi‑LLM evaluation, DS@GT ARC working note, Touché 2025 task, Retrieval‑augmented prompting pipeline.
