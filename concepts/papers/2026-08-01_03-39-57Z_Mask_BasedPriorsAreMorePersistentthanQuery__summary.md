# Summary: 2026-08-01_03-39-57Z_Mask_BasedPriorsAreMorePersistentthanQuery_KeyInit.md
Saved: 2026-08-03 23:50
Source: 2026-08-01_03-39-57Z_Mask_BasedPriorsAreMorePersistentthanQuery_KeyInit.md
Model: None

---

## Summary  
The paper investigates why Transformers generalize poorly on Boolean extrapolation tasks and whether explicit structural priors can remedy this failure mode. It argues that existing query‑key (QK) initialization methods cannot persist during training, while a simple additive attention mask initialized from task structure does so effectively. The authors propose a learnable mask that encodes the interaction pattern of the Boolean problem as a fixed bias on attention logits, thereby separating structural constraints from content‑dependent scores. Experiments demonstrate that this mask yields near‑perfect extrapolation performance, outperforming both vanilla and QK‑initialized models.

## Key Contributions  
- [Finding 1] Query‑key initializations are rapidly overwritten during training on Boolean reasoning tasks, leaving the model trapped by its default inductive bias.  
- [Finding 2] A finite, learnable additive attention mask that is initialized from the task’s interaction structure can encode a persistent structural prior throughout optimization.  
- [Finding 3] This mask improves low‑data arithmetic accuracy and remains competitive on vision and language benchmarks without altering the Transformer architecture.

## Methodology  
The authors compare three variants of Transformers: (1) vanilla models trained with random QK projections, (2) models that receive a hard attention mask enforcing locality or causality, and (3) models whose additive masks are initialized from the Boolean task’s interaction matrix. The mask is added to each attention logit as a learnable bias term, keeping it separate from the content‑dependent scores computed by QK similarity. Experiments run on standard Boolean reasoning benchmarks, low‑data arithmetic datasets, and downstream vision/language tasks such as ImageNet classification and GLUE.

## Results  
Mask‑initialized models achieve 98 % correct predictions on the hardest Boolean extrapolation problems, compared with ~70 % for vanilla Transformers and ~65 % for QK‑initialized ones. Low‑data arithmetic accuracy rises from 42 % to 58 %, while ImageNet classification scores are within 1–2 % of state‑of‑the‑art baselines. The mask does not degrade performance on standard vision or language benchmarks, indicating its utility beyond Boolean tasks.

## Significance  
The work shows that attention masks can serve as a lightweight substrate for encoding persistent inductive bias, offering a simple way to guide learning without modifying the core Transformer architecture. This approach is especially valuable in low‑resource settings where explicit task priors are needed, and it provides a principled alternative to more complex initialization schemes.

## Related Concepts  
- Transformer inductive bias  
- Minimum‑degree interpolator (the default extrapolation rule)  
- Query‑key (QK) initialization  
- Additive attention mask  
- Structural priors  
- Generalization on unseen Boolean data
