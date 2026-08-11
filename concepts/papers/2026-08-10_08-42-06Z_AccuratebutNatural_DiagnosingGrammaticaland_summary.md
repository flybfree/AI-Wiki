# Summary: 2026-08-10_08-42-06Z_AccuratebutNatural_DiagnosingGrammaticalandIdiomat.md
Saved: 2026-08-10 23:42
Source: 2026-08-10_08-42-06Z_AccuratebutNatural_DiagnosingGrammaticalandIdiomat.md
Model: None

---

## Summary  
This study aims to separate grammatical accuracy from idiomatic naturalness in Japanese EFL writing, which automated evaluation often blurs. By constructing a layered LLM‑correction pipeline, the authors generate both literal error corrections and idiomatic revisions for 3,830 samples written by 120 junior high students. The analysis quantifies two diagnostic measures—accuracy gaps (incorrectly produced structures) and idiomatic gaps (structures that are underused or overused)—to reveal distinct learner difficulties. Their framework offers teachers a way to diagnose whether problems stem from inaccurate execution, avoidance of complex forms, or L1‑mapped overreliance.

## Key Contributions  
- [Finding 1] Definite articles, third‑person singular -s, and modals such as would/could show significant accuracy gaps.  
- [Finding 2] The -ing form and hypothetical modal would exhibit the largest idiomatic underuse, while simple present verbs and subject‑verb‑object patterns display overuse.  
- [Finding 3] A two‑dimensional typology maps error rates against idiomatic gaps, distinguishing accurate but overused grammar from error‑prone or avoided complex forms.

## Methodology  
The authors employed a regex‑based CEFR‑J grammar extractor to automatically identify structural errors in the corpus. They fed each sample through an LLM that produced two types of corrections: one preserving the original grammatical structure (accuracy correction) and another producing a more idiomatic version. The corrected texts were then scored for accuracy gaps and idiomatic gaps using statistical measures derived from native‑speaker reference data.

## Results  
Quantitative analysis showed that accuracy gaps are highest for definite articles, third‑person singular -s, and modal verbs like would/could, indicating learners struggle to produce these structures correctly. Idiomatic gaps were largest for the -ing form (underuse) and hypothetical modal would (both underuse and overuse), while simple present verbs and S‑V‑O patterns showed overuse. The typology revealed three learner profiles: those with accurate but overused grammar, those avoiding complex forms due to accuracy errors, and those misusing L1 mappings.

## Significance  
By disentangling accuracy from naturalness, the study provides evidence‑based feedback for teachers, allowing them to target interventions precisely—whether to correct structural mistakes, encourage underuse of idiomatic forms, or reduce overreliance on L1 patterns. This contributes to more effective Japanese EFL pedagogy and a clearer understanding of learner writing development.

## Related Concepts  
- Grammatical accuracy vs. idiomatic naturalness  
- CEFR‑J grammar extractor (regex‑based)  
- LLM‑generated literal and idiomatic corrections  
- Accuracy gaps, idiomatic gaps  
- Two‑dimensional typology of learner writing errors
