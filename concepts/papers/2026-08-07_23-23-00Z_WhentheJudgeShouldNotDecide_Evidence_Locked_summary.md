# Summary: 2026-08-07_23-23-00Z_WhentheJudgeShouldNotDecide_Evidence_Locked_Non_Co.md
Saved: 2026-08-10 22:40
Source: 2026-08-07_23-23-00Z_WhentheJudgeShouldNotDecide_Evidence_Locked_Non_Co.md
Model: None

---

## Summary  
The paper investigates why LLM judges in reasoning pipelines cause suboptimal decisions despite high accuracy, showing that the decision rule matters more than judge precision. It introduces Evidence‑Locked Derive‑Gate‑Repair (EL‑DGR) as a non‑compensatory rule that limits judge influence to only when evidence is locked and repaired. The authors demonstrate that unconstrained judges degrade performance relative to simple voting strategies, while EL‑DGR improves outcomes without altering candidates or budgets.  

## Key Contributions  
- [Finding 1] Unconstrained scalar DeepSeek‑R1‑7B judge adds negligible benefit over majority vote on benchmark reasoning tasks.  
- [Finding 2] Embedding a judge into a fixed decision rule can worsen accuracy and confidence, producing answers that are confidently wrong.  
- [Finding 3] EL‑DGR, a task‑adaptive non‑compensatory selection bound, improves performance by only overturning consensus when evidence is locked and repaired.  

## Methodology  
The authors evaluate LLM judges within reasoning pipelines using frozen candidate pools from four GRPO policies. They compare an unconstrained DeepSeek‑R1‑7B judge against majority vote and a rule‑based 30‑question confirmation split, then introduce EL‑DGR which requires extractive evidence certificates to override consensus and triggers repair only when both alternatives lack certification.  

## Results  
On GSM8K, EL‑DGR achieves 58.2 % versus 56.8 % (judge), 55.8 % (majority), and 55.4 % (first candidate). On HotpotQA, EM improves to 17.33 vs 15.67 and F1 to 25.46 vs 23.49. The improvement over first‑candidate GRPO is +2.8 pp (p=0.0026) for GM and +2.00 EM (p=0.07). Audits show only 8 of 30 pilot questions are overturned and never produce incorrect answers.  

## Significance  
The study reveals that judges should be bounded by admissibility rules rather than optimized for accuracy; it highlights the risk of over‑trusting LLM decision layers in pipelines.  

## Related Concepts  
- LLMs as judges  
- Reasoning pipelines  
- GRPO policies  
- Majority vote  
- Evidence‑locked selection  
- Non‑compensatory rule  
- Derive‑Gate‑Repair (EL‑DGR)  
- Decision audits
