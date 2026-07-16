# Summary: 2026-07-15_17-12-37Z_Multi_ExpertRoutingforMulti_DomainLow_ResourceOCR_.md
Saved: 2026-07-15 21:01
Source: 2026-07-15_17-12-37Z_Multi_ExpertRoutingforMulti_DomainLow_ResourceOCR_.md
Model: None

---

## Summary  
The paper presents a multi‑expert routing framework designed to improve OCR performance on the Manchu script, which contains three visually distinct writing styles (regular script, running script, and semi‑cursive chancery hand) despite scarce labeled examples. By reusing checkpoints from an iterative fine‑tuning process as domain specialists and employing a lightweight page‑level image classifier to dispatch each page to the most appropriate expert, the system can achieve high accuracy without retraining large models for every style. The router either selects an existing specialist or quickly trains a new one when none is suitable. This approach yields state‑of‑the‑art results on three frozen test sets while keeping computational overhead low.

## Key Contributions  
- [Finding 1] A multi‑expert routing pipeline reuses checkpoints from iterative fine‑tuning as reusable domain specialists, enabling efficient sharing of knowledge across writing styles.  
- [Finding 2] The lightweight page classifier achieves two‑decimal precision dispatching (0.30 % CER on regular script, 1.57 % on memorials, 4.83 % on running script), matching the domain‑label oracle at that level.  
- [Finding 3] Only one expert needs to be trained per final domain; two specialists were not specifically fine‑tuned for their assigned style, demonstrating strong generalization.

## Methodology  
The authors first performed iterative fine‑tuning on each writing style, producing a set of checkpoints that serve as “experts.” A simple CNN classifier processes the raw page image to predict which expert is most likely to handle it. If the classifier’s confidence falls below a threshold, an additional expert is trained for that specific domain using only the few available examples. The router then routes each page to its assigned expert and aggregates predictions, producing per‑page OCR outputs.

## Results  
On three frozen test sets the routed system matches the selected specialist for each style at two‑decimal precision: 0.30 % CER on regular script, 1.57 % on memorials, and 4.83 % on running script. The router achieves a page‑level domain accuracy of 99.3 %, which equals the performance of the domain‑label oracle. Notably, two of the three experts were not fine‑tuned for their final domain; only the running‑script expert was trained with that target.

## Significance  
This work demonstrates that multi‑expert routing can dramatically reduce data requirements and computational cost for low‑resource OCR tasks across heterogeneous visual domains. By reusing checkpoints and training minimal additional models, the approach scales to new writing styles without extensive fine‑tuning, offering a practical path toward high‑quality OCR in historical or niche scripts.

## Related Concepts  
- Multi‑expert routing  
- Domain adaptation via checkpoint reuse  
- Iterative fine‑tuning  
- Lightweight image classifier  
- Character Error Rate (CER)  
- Page‑level accuracy  
- Fine‑tuned domain specialists
