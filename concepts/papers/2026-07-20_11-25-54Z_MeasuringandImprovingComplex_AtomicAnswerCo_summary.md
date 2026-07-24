# Summary: 2026-07-20_11-25-54Z_MeasuringandImprovingComplex_AtomicAnswerConsisten.md
Saved: 2026-07-24 00:19
Source: 2026-07-20_11-25-54Z_MeasuringandImprovingComplex_AtomicAnswerConsisten.md
Model: None

---

## Summary  
The paper tackles a persistent problem in endoscopic visual question answering (VQA): complex answers that are scored correct despite underlying atomic questions being answered incorrectly, leading to inconsistent model performance. To address this gap, the authors introduce EndoCA, a paired benchmark that evaluates both complex‑answer accuracy and its consistency with atomic answers, and propose a training‑free Atomic‑Support Reconciliation (ASR) mechanism that either revises or selectively abstains from answering when atomic support is weak.

## Key Contributions  
- [Finding 1] Complex endoscopic VQA answers can be judged correct even when the model fails on individual atomic questions.  
- [Finding 2] EndoCA provides a structured benchmark with two suites (Core and Diagnostic) to systematically measure complex‑atomic consistency across varying question complexities.  
- [Finding 3] ASR introduces a training‑free reconciliation strategy that uses model‑generated atomic answers as contextual premises for answer revision or selective answering.

## Methodology  
The authors evaluate eleven vision language models—open, medical, endoscopy‑adapted, and closed‑source—on the EndoCA benchmark. First, they compute complex‑answer accuracy and atomic‑answer accuracy separately to highlight inconsistencies. Then, they apply ASR in two modes: ASR‑Revise revises complex answers using atomic support as a premise, while ASR‑Selective allows abstention when atomic confidence is low. This training‑free approach avoids fine‑tuning the models and instead leverages the generated answer set for consistency guidance.

## Results  
On four publicly available models, ASR‑Revise modestly improves paired complex‑atomic correctness without a large drop in overall complex‑answer accuracy. ASR‑Selective yields higher answered rates by skipping low‑confidence cases. Overall, the combination of EndoCA and ASR demonstrates that consistency can be enhanced with minimal impact on performance.

## Significance  
Providing a consistency‑aware benchmark (EndoCA) and a training‑free reconciliation tool (ASR) equips researchers and practitioners with tools to detect and mitigate hidden inconsistencies in complex VQA answers, especially important for medical endoscopic applications where reliability is critical.

## Related Concepts  
- Endoscopic visual question answering (VQA)  
- Complex vs. atomic answer decomposition  
- Answer consistency evaluation  
- Model‑generated answer reconciliation  
- Selective answering / abstention strategies
