# Summary: 2026-07-22_14-37-25Z_HalluTruthQA_AFine_GrainedBenchmarkforHallucinatio.md
Saved: 2026-07-24 02:01
Source: 2026-07-22_14-37-25Z_HalluTruthQA_AFine_GrainedBenchmarkforHallucinatio.md
Model: None

---

## Summary  
HalluTruthQA introduces a fine‑grained benchmark for detecting hallucinations in Arabic question answering, providing detailed annotations such as erroneous character spans and human explanations. The dataset contains 2 400 expert‑curated examples across Islamic knowledge, history, science, and geography, each paired with model answers, reference answers, binary labels, candidate answers, and macro/micro hallucination types. Experiments evaluate four open‑source LLMs in a zero‑shot setting across detection, span‑level localization, factual verification, and explanation tasks, showing that no single model dominates all metrics. These results demonstrate that moving beyond simple detection is essential for granular evaluation of Arabic language models.

## Key Contributions  
- HalluTruthQA provides a fine‑grained benchmark with expert‑curated examples across four knowledge‑intensive domains in Arabic.  
- The dataset includes character‑level erroneous spans and human‑written explanations for hallucinated answers, enabling precise localization and explanation evaluation.  
- Experiments reveal that detection (0.880 Macro‑F1), span‑level localization (0.516 F1‑Sp), factual verification (0.852 LO‑Score) and explanation scoring (0.644 final score) are distinct abilities with varying model performance.

## Methodology  
The authors constructed 2 400 examples from Islamic knowledge, history, science, and geography. For each example they supply an Arabic question, a model‑generated answer, the verified reference answer, a binary hallucination label, six candidate factual answers, character‑level erroneous spans (when applicable), human explanations, and macro/micro hallucination type labels. Evaluation is performed in a zero‑shot manner across four open‑source LLMs—Allam, Falcon‑H1, Qwen32, and Silma—using detection F1, span‑level F1, LO‑Score verification, and explanation evaluation.

## Results  
The best scores achieved are 0.880 Macro‑F1 for detection, 0.516 F1‑Sp for span‑level localization, 0.852 LO‑Score for factual verification, and 0.644 final score for explanation evaluation. No single model excels across all tasks; performance varies significantly depending on the granularity of the task.

## Significance  
HalluTruthQA shifts Arabic hallucination assessment from binary detection to fine‑grained analysis that localizes errors, verifies factual content, and explains mistakes. This granular approach enables targeted improvements for knowledge‑intensive domains where precise answer accuracy is critical.

## Related Concepts  
- Hallucination (generation of false or fabricated information)  
- Fine‑grained benchmarking  
- Arabic question answering  
- Macro and micro hallucination types  
- Span‑level localization  
- LO‑Score factual verification metric  
- Explanation evaluation
