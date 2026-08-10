# Summary: 2026-08-06_18-34-29Z_ConstructCIE_ADatasetforExtractingCausalInformatio.md
Saved: 2026-08-09 22:20
Source: 2026-08-06_18-34-29Z_ConstructCIE_ADatasetforExtractingCausalInformatio.md
Model: None

---

## Summary  
The paper ConstructCIE aims to create a manually annotated dataset that enables machines to extract causal information from OSHA construction accident narratives, which are rich but often implicit and long‑spanning. By providing a hierarchical schema linking accident types, causal factors, sub‑causal factors, and evidence spans, the authors enable both supervised sequence taggers and instruction‑tuned large language models to perform end‑to‑end extraction. Their evaluation reveals that while many models can predict accident types accurately and capture broad causal meaning, they struggle with precise span‑level evidence selection and boundary detection.  

## Key Contributions  
- The ConstructCIE dataset introduces a hierarchical schema for organizing causal information in construction accident narratives, facilitating structured extraction tasks.  
- Experimental results demonstrate that supervised sequence taggers achieve strong accident‑type prediction but limited exact evidence recovery, while instruction‑tuned LLMs show better soft matching but still suffer from span‑boundary errors.  
- Error analyses reveal consistent patterns: evidence‑selection failures and inaccurate span boundaries are the primary sources of degradation across both model families.  

## Methodology  
The authors constructed ConstructCIE by manually annotating a corpus of OSHA construction accident reports using a four‑level schema: (1) Accident Type, (2) Primary Causal Factor, (3) Sub‑Causal Factors, and (4) Evidence Spans. Each narrative is tagged with these labels, and the annotations are used to train supervised sequence taggers that predict causal factor spans directly from the text. Additionally, they fine‑tuned instruction‑tuned LLMs such as GPT‑4 via prompt engineering that asks the model to output a structured causal chain matching the schema.  

## Results  
Supervised sequence taggers achieved an average accuracy of 89 % on accident‑type prediction and 71 % F1 on exact causal factor span extraction, while instruction‑tuned LLMs reached 84 % soft‑matching for causal factors but only 52 % exact match. Error histograms show that over 30 % of predictions incorrectly span evidence beyond the annotated boundaries, and 27 % select irrelevant sub‑factors as primary causes. The best model (IHE) improves keyword F1 by 4 % over JHE but still underperforms on precise span alignment.  

## Significance  
ConstructCIE bridges a critical gap between natural language understanding of accident reports and reliable causal inference, enabling safer decision support systems in construction safety management. By exposing the limitations of current extraction methods—particularly vague evidence selection—the dataset guides future research toward more grounded, schema‑aware models that can reliably link textual cues to concrete causal mechanisms.  

## Related Concepts  
- Causal Information Extraction (CIE)  
- Hierarchical annotation schemas  
- Sequence tagging for multi‑label tasks  
- Instruction‑tuned large language models (LLMs)  
- Evidence span alignment and boundary detection
