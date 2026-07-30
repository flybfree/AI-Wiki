# Summary: 2026-07-29_13-15-23Z_Hearsay_Vision_LanguageMedicalDiagnosesWithoutanIm.md
Saved: 2026-07-29 20:34
Source: 2026-07-29_13-15-23Z_Hearsay_Vision_LanguageMedicalDiagnosesWithoutanIm.md
Model: None

---

## Summary  
The paper demonstrates that frontier vision‑language models generate plausible but incorrect medical diagnoses when only demographic descriptors are supplied and no image is attached, indicating systematic confabulation rather than random output. It shows that the nature of this confabulation varies across demographic groups, diagnostic categories, and even model architectures, revealing distinct failure modes such as a “hedged regime” where prose acknowledges the missing data while still naming a disease. The authors argue that trustworthy deployment in clinical pipelines requires direct auditing of the structured diagnosis channel and treating probe‑word sensitivity as a primary evaluation metric.

## Key Contributions  
- **Finding 1:** Confabulation correlates with patient demographic descriptors; for example, a 65‑year‑old white man asking about a skin mole receives “Melanoma” in nearly every response, while a 32‑year‑old Black woman asked about her chest X‑ray gets “Sarcoidosis,” with reasoning that reads “suspected, based on demographics and classic pattern.”  
- **Finding 2:** Two structural failure modes are observed: (i) the hedged regime, where the model’s prose explicitly notes the absence of an image yet still produces a structured diagnosis field; and (ii) the dermatology effect collapse, which disappears when “skin mole” is swapped for the more generic term “skin lesion,” indicating that the mirage phenomenon is not monolithic.  
- **Finding 3:** Probe‑word sensitivity differs across models: Claude Opus‑4.7 shows sharp, demographic‑specific confabulations, whereas GPT‑5.4 fabricates diagnoses across all tested demographic cells, most conspicuously naming sarcoidosis for young Black patients on chest X‑ray.

## Methodology  
The authors query three state‑of‑the‑art vision‑language medical models—Claude Opus‑4.7, GPT‑5.4, and Gemini‑3.1‑Pro—using only demographic descriptors (age, race, gender) and a symptom description without any associated medical image. They systematically vary the patient’s age, ethnicity, and the exact wording of the query across chest X‑ray, brain MRI, and dermatology scenarios to observe how each model constructs its output.

## Results  
Claude exhibits a pronounced demographic bias: a white male receives melanoma for “skin mole,” while a Black female receives sarcoidosis for her chest X‑ray. GPT‑5.4’s effect is broader, producing sarcoidosis diagnoses for young Black patients on chest X‑ray across all conditions tested. Both models generate a structured diagnosis field alongside hedged prose that acknowledges the missing image. The dermatology confabulation collapses when “skin mole” is replaced by “skin lesion,” confirming distinct failure modes rather than a single phenomenon.

## Significance  
This work reveals that medical VLM diagnoses without images are not random hallucinations but systematic, demographic‑driven confabulations that can mislead clinical decision‑making. By highlighting the need to audit structured output channels and to evaluate probe‑word sensitivity as a core metric, the study underscores a critical gap in current safety assessments of vision‑language systems deployed in healthcare.

## Related Concepts  
- Vision‑language models (VLMs)  
- Confabulation / hallucination in multimodal AI  
- Demographic bias and fairness in AI  
- Structured vs. unstructured output channels  
- Probe‑word sensitivity evaluation  
- Hedged regime in language generation  
- Medical diagnosis hallucination
