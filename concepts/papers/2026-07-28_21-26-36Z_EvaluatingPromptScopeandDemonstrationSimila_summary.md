# Summary: 2026-07-28_21-26-36Z_EvaluatingPromptScopeandDemonstrationSimilarityinL.md
Saved: 2026-07-29 22:16
Source: 2026-07-28_21-26-36Z_EvaluatingPromptScopeandDemonstrationSimilarityinL.md
Model: None

---

## Summary  
This paper investigates how prompt scope and demonstration selection impact the performance of local instruction-tuned large language models (LLMs) in machine translation, particularly for multilingual tasks involving multiple target languages. The authors evaluate English-to-Romance and English-to-Germanic translations across nine EU languages using zero-shot and k=5 few-shot prompting strategies with different types of demonstrations: random, lexical-similarity, and embedding-based retrieval. They compare these local LLMs against dedicated MT baselines like OPUS-MT and NLLB-200 to understand the trade-offs between prompt design and model capability. The study reveals that while larger models benefit from structured prompts and embedding retrieval, smaller models struggle with multi-target outputs and exhibit structural failures under family-scope prompting.

## Key Contributions  
- [Finding 1] Dedicated MT systems outperform local LLMs overall, especially for Germanic languages like English-to-Germanic.  
- [Finding 2] Few-shot prompting improves performance for larger models (mistral:latest, qwen2.5:14b) but degrades smaller ones (llama3.2:3b), suggesting that prompt strategies are not universally beneficial.  
- [Finding 3] Embedding-similarity retrieval yields the best average results among demonstration types, though the advantage over random or lexical examples is modest and model-dependent.

## Methodology  
The authors use the full FLORES devtest split to test English-to-Romance and English-to-Germanic translations across nine EU languages. They employ three local instruction-tuned LLMs—llama3.2:3b, mistral:latest, and qwen2.5:14b—and compare them with two dedicated MT baselines (OPUS-MT and NLLB-200). Prompting strategies include zero-shot translation and k=5 few-shot prompting using three demonstration selection methods: random examples, lexical-similarity-based retrieval, and embedding-similarity-based retrieval. Additionally, they test family-scope prompts that request all languages in a language family (e.g., Romance or Germanic) at once, comparing them to single-target prompts.

## Results  
Dedicated MT systems consistently outperform local LLMs across all language pairs and prompting strategies. Among local LLMs, mistral:latest and qwen2.5:14b benefit from embedding-similarity retrieval and few-shot prompting, while llama3.2:3b shows the most significant degradation under these conditions. Family-scope prompts are feasible for stronger models but cause structured-output failures in smaller ones like llama3.2:3b. Embedding-based retrieval provides the best average performance, but its improvement over random or lexical examples is limited and not transformative.

## Significance  
This research shifts the evaluation of LLM machine translation beyond language pairs and metrics to include prompt design variables such as scope and demonstration selection. It highlights that prompt engineering can significantly affect model behavior, especially in multilingual tasks, and that larger models are more robust to complex prompting strategies. The findings emphasize the need for standardized evaluation protocols that account for these factors, improving fairness and practicality in deploying LLMs for real-world translation applications.

## Related Concepts  
- Local instruction-tuned LLMs (e.g., llama3.2:3b)  
- Dedicated MT baselines (OPUS-MT, NLLB-200)  
- Prompt scope (single-target vs. family-scope prompts)  
- Demonstration selection (random, lexical-similarity, embedding-similarity)  
- Few-shot prompting and zero-shot translation  
- Multilingual machine translation evaluation  
- Structured output failures in LLMs
