# Summary: 2026-08-10_08-42-06Z_AccuratebutNatural_DiagnosingGrammaticalandIdiomat.md
Saved: 2026-08-10 23:59
Source: 2026-08-10_08-42-06Z_AccuratebutNatural_DiagnosingGrammaticalandIdiomat.md
Model: None

---

## Summary  
This paper aims to separate grammatical accuracy from idiomaticity in Japanese EFL writing, which automated evaluation often conflates. It introduces a layered LLM‑correction pipeline that produces both literal error corrections and natural‑sounding revisions for 3,830 samples written by 120 junior high students. The study quantifies two diagnostic measures—accuracy gaps (structures attempted but produced incorrectly) and idiomatic gaps (grammatically correct structures used unusually little or too much). By mapping these gaps onto a typology of error types, the work offers teachers a nuanced view of learner difficulties.

## Key Contributions  
- Accuracy gaps are pronounced for definite articles, third‑person singular –s, and modals such as would/could.  
- Idiomatic underuse is most evident in -ing forms and hypothetical modals like would, while overuse occurs with simple present verbs, subject‑verb‑object patterns, and modal can.  
- A two‑dimensional typology links error rates to idiomatic gaps, distinguishing accurate but overused grammar from error‑prone or avoided complex forms.

## Methodology  
The authors employed a regex‑based CEFR‑J grammar extractor to automatically identify structural errors in the corpus. For each sample they generated two types of corrections: literal (grammatically correct) and idiomatic (natural). The pipeline produced accuracy gaps by counting structures that were attempted but output incorrectly, and idiomatic gaps by measuring deviation from native usage norms. These measures were then plotted on a 2‑D typology to classify error patterns.

## Results  
Empirical analysis revealed distinct clusters: definite articles, third‑person singular –s, and modals showed high accuracy gaps; -ing forms and hypothetical modals exhibited the largest idiomatic underuse; simple present verbs, S‑V‑O structures, and modal can displayed the greatest overuse. The typology confirmed that some learners produce accurate but unnatural language (overused grammar), while others avoid complex forms altogether.

## Significance  
The findings advance pedagogical feedback by allowing teachers to diagnose whether a learner’s difficulty stems from inaccurate execution, structural avoidance, or L1‑mapped overreliance. This evidence‑based typology supports targeted production practice rather than blanket correction, improving the relevance of automated writing evaluation tools for Japanese EFL contexts.

## Related Concepts  
- Grammatical accuracy vs. idiomaticity  
- LLM‑correction pipeline  
- CEFR‑J grammar extractor (regex‑based)  
- Accuracy gaps and idiomatic gaps as diagnostic measures  
- Two‑dimensional typology of writing errors  
- EFL writing evaluation for Japanese learners
