---

title: "Summary: Gender-Dependent Diagnostic Substitution in LLM Medical Triage: Same Symptoms, Unequal Urgency"
url: http://arxiv.org/abs/2606.03641v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-02_13-35-12Z_Gender_DependentDiagnosticSubstitutioninLLMMedical.md
generated_at: "2026-06-11 10:51"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper tests whether large language models give different emergency‑room referral rates for identical neurological symptoms depending on patient gender and age. It finds that young women are referred far less often than men, even though severity scores are comparable.

## Key Takeaways
- Young women receive significantly lower ER referral rates (Gemini 0% vs 23.3%, Claude 6.7% vs 96.7%, GPT‑5.4‑mini 6.7% vs 66.7%) compared with age‑matched men, all p < 0.001.
- The disparity vanishes at age 65 for all models, suggesting the bias is tied to younger female patients.
- Models substitute a gender‑linked diagnosis (idiopathic intracranial hypertension) for women while assigning generic space‑occupying lesions to men, causing lower urgency.

## Context
Large language models are increasingly used in clinical decision support, yet they inherit biases from training data and statistical priors. This study reveals that such priors can override symptom severity, producing inequitable triage outcomes.

## Implications
If AI triage systems continue to rely on epidemiological assumptions, they may systematically deprioritize urgent care for vulnerable groups. Practitioners must audit models for gender‑dependent substitution and design safeguards that prioritize clinical urgency over demographic cues.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.03641v1)
