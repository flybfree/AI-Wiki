# Summary: 2026-08-09_20-31-52Z_FromRecoverytoDrop_off_HowActionPost_trainingReduc.md
Saved: 2026-08-10 23:29
Source: 2026-08-09_20-31-52Z_FromRecoverytoDrop_off_HowActionPost_trainingReduc.md
Model: None

---

## Summary  
The paper investigates how action post‑training degrades a vision‑language model’s (VLM) ability to decode depth, a primitive of spatiogeometric understanding. By examining every decoder layer of two weight‑matched pairs—Molmo2‑ER (the base VLM) and MolmoAct2‑LIBERO (the VLA)—the authors discover that the VLA consistently underperforms the base model, creating a “floor” in early layers but an additional “cliff” in later layers. The cliff is localized to late‑layer MLP interference, and its removal largely restores depth decodability. This work reveals a systematic trade‑off between preserving early‑layer representations and sacrificing late‑layer spatiogeometric capabilities during action post‑training.

## Key Contributions  
- [Finding 1] The VLA exhibits a persistent depth‑decodability floor across all layers, indicating that action post‑training harms the model’s overall spatial understanding.  
- [Finding 2] The degradation is non‑uniform: while the base VLM’s depth decodability improves in its final layers, the VLA experiences an additional late‑layer drop called the “cliff.”  
- [Finding 3] Causal analysis shows that ablating the late‑layer MLP recovers most of the terminal cliff, whereas matched‑attention ablations or intervening the same module in the weight‑matched base VLM do not produce comparable recovery.  

## Methodology  
The authors probe depth perception by measuring how well each decoder layer can reconstruct depth from visual inputs for both the VLM and its action‑post‑trained counterpart. They compare Molmo2‑ER (base) with MolmoAct2‑LIBERO (VLA), ensuring identical weights except for the action module. By varying which components are removed—late‑layer MLP, attention heads, or applying the same intervention to the base model—they isolate the source of the cliff and confirm that only late‑layer MLP interference drives the loss.

## Results  
Across all layers, the VLA’s depth decodability is lower than the base VLM’s, forming a floor. The base VLM’s terminal layers actually improve over earlier ones, whereas the VLA’s performance collapses in those same later layers, producing the cliff. Removing the late‑layer MLP in the VLA restores roughly 80 % of the lost depth recaptability, while muting matched attention or applying the intervention to the base model yields negligible gains.

## Significance  
These findings demonstrate that action post‑training, intended to enhance multimodal control, inadvertently erodes spatiogeometric reasoning in VLA. The identified cliff highlights a critical vulnerability: late‑layer MLP accumulation can become detrimental when actions are added, underscoring the need for regularization strategies that protect depth perception.

## Related Concepts  
- Vision‑language model (VLM) and vision‑language‑action model (VLA)  
- Action post‑training as a training paradigm for multimodal control  
- Depth perception and spatiogeometric understanding in visual systems  
- Decoder layer analysis and layer‑wise performance metrics  
- MLP writes, accumulated MLP writes, floor effect, cliff effect
