# Summary: 2026-08-03_12-28-52Z_BeyondSolution_CentricSearch_AdaptiveInquiryandKno.md
Saved: 2026-08-03 23:54
Source: 2026-08-03_12-28-52Z_BeyondSolution_CentricSearch_AdaptiveInquiryandKno.md
Model: None

---

## Summary  
The paper proposes moving beyond solution‑centric search in autonomous ML engineering, introducing an information paradigm where the system maintains a dynamic knowledge state that guides inquiry. It introduces Iris, an inquiry‑revision loop that acquires epistemic actions and synthesizes observations into revisable task claims. This approach enables efficient use of limited budget while supporting cross‑domain generalization across tasks. The contribution is both conceptual (the information paradigm) and practical (Iris achieving 64.9 % any‑medal on MLE‑Bench).

## Key Contributions  
- Introduces an information paradigm that replaces solution‑centric search with a knowledge‑driven framework.  
- Proposes Iris, an inquiry‑revision loop comprising epistemic actions and claim synthesis for task knowledge management.  
- Demonstrates the highest any‑medal rate among compared systems under a 12‑hour budget.

## Methodology  
The authors designed Iris to operate in a continuous loop: the current information state generates local action plans, each plan uses epistemic queries that probe decision‑critical unknowns without altering retained solutions. Observations are aggregated into task knowledge composed of claims with explicit scope and status; decisions are constructed from raw evidence, structured summaries, or the appropriate level of detailed knowledge.

## Results  
On MLE‑Bench Iris attains a 64.9 % any‑medal rate within a 12‑hour budget, outperforming all other systems examined. It also generalizes across four tasks spanning harness engineering and model post‑training, showing robust cross‑domain performance.

## Significance  
This work shifts autonomous ML engineering toward knowledge management rather than solution optimization, enabling agents to adapt efficiently with limited compute resources. The information paradigm may become a standard for future self‑improving AI systems that must handle long‑horizon tasks.

## Related Concepts  
Information state, epistemic action, task knowledge, revisable claims, inquiry‑revision loop, solution‑centric vs. information‑centric search, MLE‑Bench benchmark.
