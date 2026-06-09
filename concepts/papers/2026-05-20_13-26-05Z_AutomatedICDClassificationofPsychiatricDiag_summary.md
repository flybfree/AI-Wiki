# Summary: 2026-05-20_13-26-05Z_AutomatedICDClassificationofPsychiatricDiagnoses_F.md
Saved: 2026-05-20 21:04
Source: 2026-05-20_13-26-05Z_AutomatedICDClassificationofPsychiatricDiagnoses_F.md
Model: None

---

## Summary
This research addresses the critical challenge of automating the coding of psychiatric diagnoses by mapping free-text clinical descriptions to the International Classification of Diseases (ICD) standard. The authors evaluate a spectrum of Natural Language Processing (NLP) techniques, ranging from traditional frequency-based models to advanced Large Language Models (LLMs), using a specialized dataset of over 145,000 Spanish psychiatric records. The primary goal is to determine which text representation paradigms most effectively handle the semantic complexity and ambiguity inherent in mental health documentation. The study demonstrates that transformer-based embeddings significantly outperform classical methods, with the e5_large model achieving superior performance through end-to-end fine-tuning.

## Key Contributions
- The study provides a comprehensive comparative analysis of classical NLP techniques versus state-of-the-art LLMs specifically tailored for the domain of psychiatric diagnostic coding, highlighting the limitations of traditional methods in capturing nuanced medical terminology.
- It identifies the e5_large model as the most effective approach for this specific task, achieving a high $F1_{micro}$ score of 0.866, thereby establishing a new benchmark for automated ICD classification in Spanish psychiatric contexts.
- The research underscores the necessity of adapting LLMs to specific clinical nomenclatures to overcome the challenges posed by "long-tail" label distributions and the inherent ambiguity of psychiatric discourse, offering a pathway for reducing administrative burdens in global mental health care.

## Methodology
The authors utilized a specialized dataset comprising 145,513 Spanish psychiatric descriptions to train and evaluate various text representation paradigms. The experimental framework included classical frequency-based models such as Bag-of-Words (BoW) and Term Frequency-Inverse Document Frequency (TF-IDF) as baseline comparisons. These were contrasted with modern transformer-based embeddings, including e5_large, BioLORD, and the Llama-3-8B model. The methodology involved mapping these free-text descriptions to ICD codes, with a specific focus on end-to-end fine-tuning strategies to enhance the models' ability to capture implicit semantic cues and nuanced medical terminology.

## Results
The experimental results clearly indicate that transformer-based embeddings consistently outperform traditional frequency-based methods. The e5_large model, when subjected to end-to-end fine-tuning, achieved the highest performance metrics, recording an $F1_{micro}$ score of 0.866. This superior performance is attributed to the model's capacity to capture implicit semantic cues and handle the complex, often ambiguous language found in psychiatric discourse. In contrast, classical models struggled with the long-tail distribution of diagnostic labels and failed to adequately represent the subtle distinctions required for accurate ICD coding.

## Significance
This research is significant because it demonstrates that automating psychiatric diagnostic coding is feasible and accurate when leveraging advanced LLMs. By reducing the administrative burden associated with manual coding, this approach can streamline clinical workflows and improve data quality in mental health records. The findings suggest that adapting LLMs to specific clinical domains is essential for overcoming the unique linguistic challenges of psychiatric care, ultimately supporting more efficient and scalable global mental health initiatives.

## Related Concepts
- Automated ICD Classification
- Psychiatric Diagnosis Coding
- Large Language Models (LLMs)
- Natural Language Processing (NLP)
- Transformer-based Embeddings
- e5_large Model
- Long-tail Label Distributions
- Clinical Nomenclature Adaptation
- Spanish Medical Text Analysis

[[Automated ICD Classification of Psychiatric Diagnoses: From Classical NLP to Large Language Models]]