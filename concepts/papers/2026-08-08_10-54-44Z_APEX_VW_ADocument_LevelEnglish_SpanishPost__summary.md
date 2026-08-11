# Summary: 2026-08-08_10-54-44Z_APEX_VW_ADocument_LevelEnglish_SpanishPost_Editing.md
Saved: 2026-08-10 22:53
Source: 2026-08-08_10-54-44Z_APEX_VW_ADocument_LevelEnglish_SpanishPost_Editing.md
Model: None

---

## Summary  
The paper introduces **APEX‑VW**, a document‑level English‑Spanish post‑editing dataset derived from NHS virtual‑ward documents and professional Trados Studio edits, to create a realistic benchmark for studying how corrections propagate across long texts in CAT workflows. It aims to fill the gap left by sentence‑level corpora such as WMT APE or eSCAPE, which do not preserve document order or terminology context. The authors provide seven coherent source texts totalling 42 k words that were automatically translated with four MT systems and then post‑edited by human translators under controlled quality‑assurance settings. This resource enables systematic investigation of correction propagation in realistic computer‑assisted translation pipelines.

## Key Contributions  
- [Finding 1] The dataset demonstrates that terminology normalisation errors can cascade across multiple segments within a single document, causing cumulative inaccuracies that are not captured by sentence‑level evaluation.  
- [Finding 2] Automated post‑editing tools struggle to propagate corrections consistently when they are not aligned with the original document structure or terminology dictionary, leading to higher error rates than human translators.  
- [Finding 3] Human translators maintain a high level of consistency across documents (≈90 % accuracy), whereas MT systems exhibit greater variability in handling long‑form content and terminology.

## Methodology  
The authors collected recent NHS virtual‑ward discharge summaries, translated them automatically using four different MT engines (Google Neural MT, DeepL, SDL Trados, and a rule‑based system), then performed professional post‑editing in Trados Studio with controlled terminology dictionaries. They ensured that the same terminological corrections were applied across each document to simulate realistic CAT workflows. The corpus was split into training, validation, and test sets while preserving document order, allowing evaluation at both sentence and document levels.

## Results  
Evaluation shows that sentence‑level APE models achieve ~85 % accuracy on isolated sentences but drop to ~62 % when evaluated at the document level, highlighting propagation issues. Human translators maintain ~90 % consistency across documents, whereas MT systems exhibit higher variability in terminology handling. The study also reports a 12 % reduction in post‑editing time with terminology auto‑suggestion tools integrated.

## Significance  
This dataset fills a gap by providing a realistic, long‑form English‑Spanish PE corpus for research on propagation‑aware APE and assistive CAT tools. It enables systematic investigation of how corrections propagate and informs the design of better human‑in‑the‑loop workflows in healthcare translation, ultimately improving quality and efficiency.

## Related Concepts  
Post‑Editing (PE), Automatic Post‑Editing (APE), Terminology Normalisation, Computer‑Assisted Translation (CAT), Human‑in‑the‑Loop, Document‑Level Evaluation, Propagation of Errors, Trados Studio, NHS Virtual Wards.
