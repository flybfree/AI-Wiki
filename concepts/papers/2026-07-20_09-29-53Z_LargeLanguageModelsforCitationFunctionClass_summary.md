# Summary: 2026-07-20_09-29-53Z_LargeLanguageModelsforCitationFunctionClassificati.md
Saved: 2026-07-24 00:14
Source: 2026-07-20_09-29-53Z_LargeLanguageModelsforCitationFunctionClassificati.md
Model: None

---

## Summary  
The paper aims to evaluate large language models’ ability to classify citation functions across zero‑shot, few‑shot, and fine‑tuned settings on the ACL‑ARC dataset, achieving state‑of‑the‑art performance. It introduces AC3, a new seven‑category annotation scheme that distinguishes neutral acknowledgments from explicit evaluative stances such as criticism, complimenting, or contradiction. The study systematically compares five models—Mistral 7B, Orca 2‑7B, LLaMA 3.1‑8B, Falcon 7B, and SciBERT—to determine which approach yields the highest macro F1 score.  

## Key Contributions  
- [Finding 1] Fine‑tuned Falcon 7B reaches a 73.3% macro F1 on ACL‑ARC, surpassing prior methods.  
- [Finding 2] AC3 provides a granular seven‑category citation function taxonomy with four context extraction variants.  
- [Finding 3] The work is the first comprehensive model comparison for citation function classification, filling a gap in recent surveys.  

## Methodology  
The authors adopt a multi‑task experimental framework that tests each LLM under three prompting strategies (zero‑shot, few‑shot, fine‑tuning) and across four context extraction configurations defined by AC3. Model outputs are tokenized, then classified using a lightweight classifier trained on the annotated dataset; macro F1 is computed per model and configuration.  

## Results  
The best performance is achieved with the fine‑tuned Falcon 7B (73.3% macro F1). Zero‑shot models like Mistral 7B score around 68%, while few‑shot variants improve modestly. AC3’s four context variants show that broader context extraction yields higher accuracy, especially for opinion‑oriented citations.  

## Significance  
This study advances bibliometric NLP by demonstrating LLMs’ utility in fine‑grained citation analysis and provides a benchmark (AC3) for future research. It also clarifies the trade‑offs between model size, prompting strategy, and contextual scope.  

## Related Concepts  
- Large language models  
- Citation function classification  
- Zero‑shot vs few‑shot learning  
- Macro F1 metric  
- ACL‑ARC dataset  
- Fine‑tuning  
- Context extraction  
- Neutral acknowledgments  
- Evaluative citations (criticizing/complimenting/contradicting)
