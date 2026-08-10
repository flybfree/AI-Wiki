# Summary: 2026-08-06_21-34-51Z_Pre_InferenceRoutingforCost_EfficientDocumentField.md
Saved: 2026-08-09 22:25
Source: 2026-08-06_21-34-51Z_Pre_InferenceRoutingforCost_EfficientDocumentField.md
Model: None

---

## Summary  
The paper proposes a pre‑inference routing technique that selects between a low‑cost and a high‑capacity document extraction model based on an estimated difficulty signal, aiming to cut inference expense while preserving quality. It demonstrates that routing is beneficial only when the cheap model fails frequently enough to make it worthwhile and when those failures can be inferred from visible cues such as image quality or layout. The authors apply this routing across five document genres, achieving substantial cost reductions with minimal F1 loss. A simple bag‑of‑words router suffices, indicating that genre‑specific difficulty—not router design—is the primary limitation.

## Key Contributions  
- [Finding 1] Routing reduces extraction cost by 31–33 % on receipts and 77 % on degraded ad‑buy forms while keeping F1 within 0.02 of the strong model’s performance.  
- [Finding 2] A small labeled pilot can correctly predict whether routing will be useful, validating that cheap prediction signals are feasible.  
- [Finding 3] The router’s effectiveness is limited by genre; a bag‑of‑words approach works as well as engineered features, and router design does not transfer across datasets.

## Methodology  
The authors first gather inexpensive document‑level signals—such as image quality and layout cues—to train a binary classifier that estimates extraction difficulty. They then implement a routing layer that routes each incoming document to either the low‑cost extractor or the high‑capacity one based on this prediction. Experiments compare two model pairs with cost ratios of 5× and 3× across five genres, measuring both F1 scores and computational cost.

## Results  
In receipts, routing cuts cost by roughly 32 % without dropping F1; on degraded ad‑buy forms it reduces cost by about 77 %. The router is only effective when both conditions hold: frequent cheap‑model failures and detectable failure signals. When either condition fails (e.g., clean digital invoices), routing yields no benefit. A simple bag‑of‑words router matches engineered feature performance, confirming that genre difficulty dominates.

## Significance  
This work shows that intelligent model selection can dramatically lower inference expense in document extraction pipelines while preserving accuracy, offering a scalable cost‑saving strategy for real‑world applications where data diversity varies.

## Related Concepts  
- Pre‑inference routing  
- Cost‑effective model selection  
- F1 score  
- Bag‑of‑words features  
- Genre‑specific difficulty  
- Interpretability of routing signals
