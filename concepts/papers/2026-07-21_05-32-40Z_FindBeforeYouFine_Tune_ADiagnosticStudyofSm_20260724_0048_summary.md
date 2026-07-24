# Summary: 2026-07-21_05-32-40Z_FindBeforeYouFine_Tune_ADiagnosticStudyofSmallLLMs.md
Saved: 2026-07-24 00:48
Source: 2026-07-21_05-32-40Z_FindBeforeYouFine_Tune_ADiagnosticStudyofSmallLLMs.md
Model: None

---

## Summary  
The paper aims to develop a diagnostic framework for selecting small LLMs suitable for cybersecurity QA before fine‑tuning, and evaluate its impact on model capabilities. It introduces FiT (Find before Fine‑Tune) which assesses three key abilities—vocabulary recognition, parametric knowledge, and contextualization of retrieved information—and shows that fine‑tuning harms these abilities in a regime‑dependent way. The study compares five 7B open‑weight models under instruction‑focused vs. knowledge‑focused tuning regimes. By using FiT scores to predict post‑tuning changes, it demonstrates that task‑oriented diagnosis can prevent unnecessary adaptation and mitigate risk.  

## Key Contributions  
- [Finding 1] Fine‑tuning consistently degrades vocabulary recognition and parametric knowledge in small LLMs across both tuning regimes.  
- [Finding 2] The two fine‑tuning regimes trade off differently; knowledge‑focused tuning causes moderate, rank‑preserving degradation while instruction‑focused tuning induces abstention that collapses measured knowledge, inverting the ranking.  
- [Finding 3] Pre‑fine‑tuning FiT scores reliably anticipate the direction of post‑tuning change, enabling a diagnostic screen for unsuitable models.  

## Methodology  
The authors built FiT by measuring three capabilities on benchmark cybersecurity QA tasks using prompts that isolate vocabulary recall, parametric fact retrieval, and contextual integration. They selected five 7B open‑weight LLMs (e.g., Mistral, LLaMA‑2‑7B) and performed two fine‑tuning regimes: knowledge‑focused (continual learning on factual QA pairs) and instruction‑focused (instruction following with cybersecurity prompts). After each regime, they re‑ran FiT assessments to capture performance shifts.  

## Results  
Experimental results show that vocabulary scores drop sharply after both regimes, parametric knowledge declines modestly under knowledge‑focused tuning but collapses under instruction‑focused tuning. Contextualization remains stable in the latter. Rank‑correlation analysis reveals a strong positive correlation between pre‑tuning FiT and post‑tuning degradation magnitude, confirming predictive power.  

## Significance  
These findings highlight that fine‑tuning small LLMs for cybersecurity QA can unintentionally erode critical capabilities, potentially leading to unsafe or inaccurate answers. By providing an objective diagnostic (FiT) before adaptation, organizations can avoid costly retraining and preserve model reliability in high‑stakes domains.  

## Related Concepts  
- Fine‑tuning  
- Knowledge vs instruction fine‑tuning regimes  
- Hallucination  
- Instruction following  
- Retrieval‑grounded contextualization  
- Rank correlation analysis  
- Diagnostic screening
