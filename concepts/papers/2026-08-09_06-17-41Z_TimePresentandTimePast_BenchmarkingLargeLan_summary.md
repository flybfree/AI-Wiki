# Summary: 2026-08-09_06-17-41Z_TimePresentandTimePast_BenchmarkingLargeLanguageMo.md
Saved: 2026-08-10 23:13
Source: 2026-08-09_06-17-41Z_TimePresentandTimePast_BenchmarkingLargeLanguageMo.md
Model: None

---

## Summary  
The paper introduces **TIDE**, a benchmark for answering questions about evolving official documents such as customs instruments where the correct answer depends on which version is in force on a given date. By treating time as an active constraint rather than merely an annotation, TIDE tests whether large language models can resolve versions, identify outdated texts, and reject incorrect answers. The study evaluates nine recent LLMs across three access protocols (parametric, gold‑context, retrieval) using a hard‑date gate to separate correct meaning from correct timing. The results show that while macro‑averaged accuracy is modestly high at 68.5 %, the model’s ability to correctly identify the governing version drops sharply when dates are implicit or absent.

## Key Contributions  
- **Finding 1:** The best macro‑averaged accuracy across nine LLMs on TIDE is only 68.5 %.  
- **Finding 2:** Resolving a correct version from an implicitly dated query reaches 59.7 % accuracy, indicating difficulty when the governing date is not explicit.  
- **Finding 3:** Detecting that a supplied version does not govern the query is only 26.7 % accurate, showing models often over‑trust parametric answers.

## Methodology  
The authors constructed TIDE with 3,050 QA pairs drawn from 644 official customs instruments issued between 1969 and 2025 by the Government of Bangladesh. The dataset spans eight task types, includes code‑mixed documents with heterogeneous layouts, and uses two calendars (Bengali and Gregorian). TIDE evaluates nine recent LLMs under a single protocol that combines parametric, gold‑context, and retrieval access modes. A three‑judge LLM council scores each answer, applying a hard date gate to separate correct meaning from correct timing.

## Results  
Macro‑averaged accuracy: 68.5 % (best among the nine models). Version resolution (explicit date): 59.7 %. Detection of non‑governing version: 26.7 %. Models tend to produce confident parametric answers that ignore or override the supplied authoritative text, especially when dates are implicit.

## Significance  
Temporal question answering is critical for legal, tax, and software documentation systems where outdated rules can cause real‑world harm. TIDE provides a rigorous benchmark that exposes the limitations of current LLMs in handling version resolution, prompting research into better date parsing, retrieval mechanisms, and confidence calibration.

## Related Concepts  
- Version resolution (identifying which document version is active on a given date)  
- Temporal QA (question answering with time‑dependent constraints)  
- LLM evaluation protocols (parametric vs. gold‑context vs. retrieval access)  
- Hard date gate (mechanism that separates correct meaning from correct timing)
