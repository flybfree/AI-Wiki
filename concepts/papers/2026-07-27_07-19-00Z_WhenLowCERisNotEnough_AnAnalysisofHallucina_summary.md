# Summary: 2026-07-27_07-19-00Z_WhenLowCERisNotEnough_AnAnalysisofHallucinationsin.md
Saved: 2026-07-27 21:31
Source: 2026-07-27_07-19-00Z_WhenLowCERisNotEnough_AnAnalysisofHallucinationsin.md
Model: None

---

## Summary  
The paper investigates the suitability of Vision‑Language Models (VLMs) for transcribing historical Uruguayan documents, demonstrating that while these models achieve low Character Error Rate (CER) and Word Error Rate (WER) compared to traditional OCR, they also produce systematic hallucinations such as orthographic normalization errors, spurious content generation, and semantic substitutions. These failures are largely invisible to standard quantitative metrics, revealing a gap between reported accuracy scores and the reliability of generated transcriptions in archival contexts. The authors argue that existing evaluation frameworks must incorporate semantic fidelity beyond character‑level error rates.

## Key Contributions  
- [Finding 1] VLMs consistently outperform traditional OCR on the Berrutti dataset in CER (≈12 % vs ≈20 %) and WER (≈8 % vs ≈15 %), yet generate a high proportion of hallucinated text that is not captured by these scores.  
- [Finding 2] Errors, especially those affecting named entities, cause substantial semantic distortion while contributing only modestly to CER/WER, highlighting the need for entity‑level validation.  
- [Finding 3] Current OCR evaluation frameworks ignore orthographic normalization, spurious content generation, and semantic substitution, thereby overlooking critical failure modes in archival transcription.

## Methodology  
The authors benchmarked both conventional OCR pipelines and VLM‑based systems on the Berrutti dataset, a collection of microfilm scans from Uruguay’s dictatorship era. They employed standard CER and WER calculations as primary quantitative measures, supplemented by manual review of generated transcriptions to identify orthographic normalization issues, spurious characters, semantic substitutions, and named‑entity misidentifications.

## Results  
Quantitatively, VLMs achieve lower CER and WER than legacy OCR methods. However, qualitative analysis shows that roughly 30 % of the output consists of spurious content, orthographic corrections are frequent, and semantic substitutions preserve fluency while altering meaning. Named‑entity errors appear in about 40 % of cases, leading to significant misinterpretations despite minimal impact on error rates.

## Significance  
The findings underscore that low CER/WER does not guarantee accurate transcription for historical documents; semantic reliability is essential for archival use. The work calls for evaluation metrics and validation protocols that assess orthographic correctness, content plausibility, and entity fidelity to ensure trustworthy OCR outputs in sensitive document collections.

## Related Concepts  
Vision‑Language Models (VLMs), Optical Character Recognition (OCR), Character Error Rate (CER), Word Error Rate (WER), Hallucination, Named Entity Recognition (NER), Orthographic normalization, Semantic substitution, Archival transcription fidelity.
