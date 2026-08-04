# Summary: 2026-08-03_09-58-20Z_TALSC_Timeliness_AwareLarge_SmallVLMCollaborationf.md
Saved: 2026-08-04 00:41
Source: 2026-08-03_09-58-20Z_TALSC_Timeliness_AwareLarge_SmallVLMCollaborationf.md
Model: None

---

## Summary  
The paper addresses the challenge of integrating large vision‑language models (LVLMs) with small on‑board VLMs in autonomous driving, focusing on timeliness. It proposes a Timeliness‑Aware Large‑Small VLM Collaboration (TALSC) framework that models Age of Information and schedules tasks accordingly. The contribution is a general timeliness metric and an online scheduling algorithm using Lyapunov drift‑plus‑estimated‑penalty for guaranteed performance. This work is motivated by the need for safety‑critical real‑time decisions.  

## Key Contributions  
- Derivation of a general timeliness metric linking Age of Information, token length, and task performance.  
- Design of a Lyapunov drift‑plus‑estimated‑penalty scheduling algorithm that guarantees timeliness despite unknown output tokens.  
- Empirical demonstration on nuScenes showing up to 12.6 % normalized Micro‑F1 gain under various communication/computing settings.  

## Methodology  
The authors first characterize how the Age of Information evolves during VLM inference, establishing its dependence on token count and downstream task accuracy; our scheduling algorithm minimizes a Lyapunov drift term while penalizing estimated latency to ensure long‑term performance. The Age of Information is defined as the time elapsed between sensor capture and inference completion. Our online scheduling algorithm estimates future token length using drift analysis and incorporates a penalty term based on estimated latency, ensuring that scheduling decisions improve overall timeliness.  

## Results  
Simulations on nuScenes show TALSC outperforms baseline strategies such as static batching and greedy token selection. The normalized Micro‑F1 score improves by up to 12.6 % relative to the best baseline, confirming both accuracy gains and timeliness preservation. These gains are consistent across different bandwidth scenarios, indicating robustness to network variability.  

## Significance  
This work bridges the gap between large model capabilities and real‑time autonomous driving requirements, enabling practical deployment of LVLMs without sacrificing safety‑critical latency. By providing a theoretically grounded scheduling method, TALSC offers a scalable solution for future infrastructure‑assisted AD systems that must balance accuracy with strict timing constraints.  

## Related Concepts  
- Age of Information  
- Vision‑Language Models (VLMs)  
- Large‑Small VLM Collaboration  
- Lyapunov drift  
- Online scheduling  
- Micro‑F1 score  
- nuScenes dataset  
- Edge servers  
- Timeliness metric
