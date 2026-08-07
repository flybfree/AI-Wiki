# Summary: 2026-08-06_09-52-09Z_DecomposedEntailmentforFactualityCheckingandHalluc.md
Saved: 2026-08-06 20:35
Source: 2026-08-06_09-52-09Z_DecomposedEntailmentforFactualityCheckingandHalluc.md
Model: None

---

## Summary  
This paper introduces HallDetect, a lightweight, reference‑free and black‑box framework for detecting hallucinations in Large Language Model (LLM) outputs across various generation tasks. The core idea is to decompose the generated text into atomic claims that are independently verified by a compact encoder‑based entailment model using contrastive learning over a multi‑scale library of source chunks. An asymmetric score aggregates these claims, and any single confidently contradicted claim triggers a false‑positive flag while also providing a claim‑to‑span audit trail that pinpoints the erroneous portion. The approach is evaluated under strict 4‑bit quantized backbones and consumer‑grade hardware constraints.

## Key Contributions  
- HallDetect provides a reference‑free, black‑box hallucination detection system that works without access to source material or explicit grounding.  
- It decomposes generated content into atomic claims verified by contrastive entailment models on multi‑scale source chunks, enabling fine‑grained error localization.  
- The framework yields an asymmetric score and a claim‑to‑span audit trail, allowing single‑claim false positives to reliably flag hallucinations.

## Methodology  
HallDetect builds on decomposition‑based factuality evaluation: the model first splits the generated response into discrete claims. Each claim is encoded by a compact encoder that learns to distinguish between entailed and non‑entailed statements using contrastive learning over a curated set of source chunks at multiple scales (e.g., short sentences, paragraphs). The encoder’s output is compared against a set of positive/negative pairs, producing an entailment score. These scores are aggregated asymmetrically—only when a claim receives a high confidence in contradiction does it flag the response as hallucinatory. The system also records which span corresponds to each claim, creating an audit trail that localizes errors without requiring the source text.

## Results  
HallDetect outperforms comparably resourced generative and embedding‑based baselines on three of four benchmark suites while maintaining stability across different backbone families. Experiments were conducted with 4‑bit quantized models running on consumer‑grade hardware, ensuring low computational overhead. The model’s claim‑to‑span audit trail correctly identifies the erroneous portion in each hallucinated output, improving traceability compared to black‑box scores alone.

## Significance  
By offering a scalable, resource‑efficient detection mechanism that does not rely on external source access or complex grounding procedures, HallDetect enhances the reliability of LLMs in real‑world applications. The decomposition and contrastive verification strategy provides transparent error localization, which is crucial for trustworthy AI systems where hallucinations can have serious consequences.

## Related Concepts  
- Hallucination detection  
- Factuality checking  
- Entailment models  
- Contrastive learning  
- Multi‑scale chunking  
- Asymmetric scoring  
- Black‑box evaluation
