# Summary: 2026-07-28_03-20-26Z_Neurai_VNBenchmark_StandardizedMachineLearningMode.md
Saved: 2026-07-28 22:29
Source: 2026-07-28_03-20-26Z_Neurai_VNBenchmark_StandardizedMachineLearningMode.md
Model: None

---

## Summary  
This paper introduces Neurai‑VN, a reproducible benchmark for evaluating machine learning models that classify mental health conditions using multimodal data from smartphones and wearables. The benchmark standardizes preprocessing, feature extraction, and evaluation across four binary classification tasks to enable fair comparison of baseline algorithms. By applying subject‑wise cross‑validation on a high‑resolution dataset collected from 100 Vietnamese adults over two weeks, the authors demonstrate that well‑trained models can achieve consistent performance. The results provide clear, reproducible baselines for future research in digital phenotyping.

## Semantic links
- [[concepts/papers/2026-07-30_08-05-26Z_SignLanguageQuestionAnswering_ANewTask_Benc_summary.md|Summary: 2026-07-30_08-05-26Z_SignLanguageQuestionAnswering_ANewTask_Benchmark_a.md]] — 4 title terms overlap; 14 summary/topic terms overlap; semantic match 0.07
- [[concepts/ai-foundations/ai-ml-foundations-lesson-03-data-as-the-foundation-of-learning.md|AI/ML Foundations Lesson 03 - Data as the Foundation of Learning]] — 3 title terms overlap; 5 backlinks; 4 summary/topic terms overlap
- [[concepts/ai-foundations/ai-ml-foundations-lesson-01-ai-machine-learning-and-deep-learning.md|AI/ML Foundations Lesson 01 - AI, Machine Learning, and Deep Learning]] — 3 title terms overlap; 5 backlinks; 4 summary/topic terms overlap

## Key Contributions  
- Founding a standardized multimodal digital phenotyping benchmark (Neurai‑VN) with unified preprocessing and feature pipelines.  
- Defining four clinically relevant binary classification tasks evaluated via subject‑wise cross‑validation to isolate task‑specific performance.  
- Reporting mean subject‑level F1 scores across five folds for each task, establishing reproducible baseline metrics.

## Methodology  
The authors assembled Neurai‑VN by integrating passive sensing (e.g., heart rate variability, sleep patterns) and active assessment (self‑reported mood scales) from wearable and smartphone devices. Data were collected from 100 Vietnamese adults over a two‑week period, yielding richly correlated multimodal streams. Feature configurations were predefined to capture physiological, behavioral, and temporal patterns. Linear regression, random forests, and convolutional neural networks were trained using subject‑wise k‑fold cross‑validation, ensuring that each model learns from the same individual’s data across folds.

## Results  
Mean subject‑level F1 scores reached 0.71 for Healthy Control vs. Depression and Healthy Control vs. Clinical tasks, while Healthy Control vs. Anxiety yielded 0.69 and Depression vs. Anxiety scored 0.56. These figures were obtained across five cross‑validation folds, indicating stable performance even with limited data per subject.

## Significance  
By delivering a reproducible benchmark with clear task definitions and quantitative baselines, Neurai‑VN enables researchers to compare new multimodal models objectively, accelerating progress in mental health classification without the pitfalls of heterogeneous datasets. The study also highlights the importance of subject‑wise validation in DP applications where individual variability is high.

## Related Concepts  
digital phenotyping, multimodal data integration, machine learning baselines, cross‑validation, F1 score, wearable sensing, smartphone monitoring, mental health classification, benchmarking.
