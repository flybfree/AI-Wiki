# Summary: 2026-08-31_15-47-23Z_FaithfulnessIsNotFree_AuditingOfflineKV_CacheQuant.md
Saved: 2026-08-31 23:09
Source: 2026-08-31_15-47-23Z_FaithfulnessIsNotFree_AuditingOfflineKV_CacheQuant.md
Model: None

---

## Summary  
Retrieval‑augmented generation (RAG) systems often pre‑compute and store key‑value caches of retrieved documents to avoid re‑encoding context at each query. The authors investigate whether quantizing these offline caches—especially with INT8 and INT4—preserves the faithfulness of generated answers, i.e., whether the model still produces responses that are fully supported by the evidence it was given. Their work shows that while INT8 quantization is near lossless for both accuracy and faithfulness, INT4 introduces a severe regression: many correct‑looking answers become factually unsupported, and the compression harms faithfulness even when accuracy metrics remain unchanged.

## Key Contributions  
- [Finding 1] Quantizing offline KV‑cache content with INT8 retains near‑lossless performance on both accuracy and faithfulness.  
- [Finding 2] INT4 quantization degrades factual correctness, causing over 90 % of the remaining accurate answers to lose their evidential grounding.  
- [Finding 3] The negative impact on faithfulness is amplified under noisy retrieval and when more retrieved chunks are present.

## Methodology  
The authors evaluate Qwen2.5‑7B‑Instruct under INT8 and INT4 quantization across two datasets (RGB and HotpotQA). For each setting they compute standard accuracy scores, then assess factual correctness using a hallucination detector, NLI entailment checks, and an LLM judge that rates faithfulness. They also vary retrieval quality and the number of retrieved chunks to isolate confounding factors.

## Results  
INT8 quantization yields negligible drops in both accuracy (≈0.2 % absolute) and faithfulness (≈1 % relative). INT4 reduces overall accuracy by ~3 % but, more critically, 90 % of the answers that remain factually correct lose their evidential support, as measured by the hallucination detector and NLI entailment scores. The effect is strongest when retrieval is noisy or when many chunks are retrieved.

## Significance  
This study reveals a hidden cost of compressing offline caches: faithfulness—essential for trustworthy AI—can be sacrificed without detection by conventional accuracy metrics. Deploying compressed caches in production RAG systems would risk generating misleading answers that appear correct but are unsupported, prompting the need for explicit auditing before compression.

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Key‑value cache storage  
- Quantization (INT8, INT4)  
- Hallucination detection and NLI entailment  
- Fairness vs. accuracy trade‑offs in AI systems
