# Summary: 2026-08-09_23-38-12Z_ReadingisnotReasoning_BridgingtheAgenticPolicyGapi.md
Saved: 2026-08-10 23:31
Source: 2026-08-09_23-38-12Z_ReadingisnotReasoning_BridgingtheAgenticPolicyGapi.md
Model: None

---

## Summary  
The paper investigates why vision‑text compression creates an agentic policy gap, where visual‑history agents perform worse than their text‑history counterparts despite identical OCR quality. It introduces CAPS, a two‑stage cross‑modal self‑distillation framework that transfers successful text‑policy behavior to the visual‑history model via offline trajectory distillation and online reinforcement learning supervision. Experiments on SearchQA and ALFWorld demonstrate substantial gains in accuracy and efficiency compared with baseline AgentOCR models. The work shows that explicit cross‑modal policy transfer can preserve capability under modality shift, reducing memory‑context costs dramatically.

## Key Contributions  
- [Finding 1] Visual‑history agents exhibit systematic drift in action selection, query formulation, stopping criteria, and evidence use beyond OCR errors.  
- [Finding 2] CAPS, a two‑stage cross‑modal self‑distillation framework, transfers text‑policy success to visual‑history inputs using both offline trajectory distillation and online policy supervision.  
- [Finding 3] CAPS improves SearchQA by 5.0 % (3B) and 3.4 % (7B) and ALFWorld by 15.6 % (3B) and 14.5 % (7B), while cutting average memory‑context cost up to 63.3 %.

## Methodology  
The authors first analyze the gap through controlled evaluations of history recovery, matched‑state decisions, and full trajectories on two datasets. They then design CAPS: an offline stage where a strong text‑history policy self‑distills into a visual‑history model using trajectory data; an online stage where the visual‑history agent receives dense supervision from its own reinforcement learning loop, aligning its policy with the text‑policy’s decisions. This dual approach ensures both initial alignment and continual refinement.

## Results  
CAPS outperforms AgentOCR on SearchQA (5.0 % / 3.4 %) and ALFWorld (15.6 % / 14.5 %) for models of 3B and 7B parameters, respectively. Memory‑context cost is reduced by up to 63.3 % on average and 83.4 % at peak, indicating both higher efficiency and better performance.

## Significance  
By bridging the agentic policy gap through cross‑modal self‑distillation, CAPS enables vision‑text compression to retain the reasoning capabilities of text‑only agents while dramatically lowering computational overhead, paving the way for scalable multimodal AI systems.

## Related Concepts  
- Vision‑text compression  
- Agentic policy gap  
- Cross‑modal self‑distillation  
- Offline trajectory distillation  
- Online reinforcement learning supervision
