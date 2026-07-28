# Summary: 2026-07-27_16-49-36Z_EvidenceAttributioninVisualDocumentUnderstandingwi.md
Saved: 2026-07-27 23:06
Source: 2026-07-27_16-49-36Z_EvidenceAttributioninVisualDocumentUnderstandingwi.md
Model: None

---

## Summary  
The paper investigates why vision‑language models often generate “attribution hallucinations” when they are required to link answers to the exact evidence regions in a document. It shows that this failure is partly due to the limited expressive power of a coordinate interface, which only returns bounding‑box coordinates. By replacing coordinates with a language‑only output—verbatim quotations—and a multimodal retriever that locates each quote via a layout parser, the authors demonstrate a substantial improvement in evidence recall and a reduction in hallucinations while preserving answer quality. The study also introduces a gradient‑policy optimization (GRPO) training scaffold that enables models to learn better quoting without any region labels at all.

## Key Contributions  
- [Finding 1] The coordinate interface is insufficient for reliable attribution, limiting evidence recall to at most eight points and inflating hallucination rates.  
- [Finding 2] A quote‑and‑retrieve pipeline that couples text output with a layout‑parser‑based location retrieval raises evidence recall from ≤8 to between 26–47 and halves the hallucination rate, without degrading answer quality.  
- [Finding 3] Using GRPO on an 8B backbone, the model learns to quote more appropriate evidence, raising strict attributed accuracy from 22.4 % to 33.8 %.

## Methodology  
The authors first benchmark six open vision‑language models on a verified bilingual CiteVQA subset under two interfaces: (1) coordinate output and (2) language output plus retrieval of page regions via a layout parser that extracts tables, figures, and captions as quote locations. The second part builds a training scaffold where the same quote‑and‑retrieve loop is used to train the model; the reward for GRPO is defined by a judge’s reading of the gold answer together with the retrieved region crops. No explicit region labels are required because the parser supplies them implicitly.

## Results  
Evidence recall improves dramatically: from ≤8 points under coordinates to 26–47 points under quoting, an increase of roughly eight points. The hallucination rate drops by about half. Strict attributed accuracy for the GRPO‑trained model rises from 22.4 % to 33.8 %, a gain of over eleven percentage points, while overall answer quality remains unchanged.

## Significance  
These findings provide a practical pathway to improve evidence attribution in visual document understanding without relying on costly coordinate annotations or expensive region‑level supervision. By leveraging language quotations and automated layout parsing, the approach reduces annotation burden and mitigates hallucinations, making attribution more robust for long documents.

## Related Concepts  
- Visual Document Understanding (VDU)  
- Evidence Attribution / Answer Verification  
- Attribution Hallucination  
- Multimodal Retrieval  
- Layout Parsing (tables, figures, captions)  
- Gradient Policy Optimization (GRPO)  
- Coordinate Interface vs. Language‑Only Interface
