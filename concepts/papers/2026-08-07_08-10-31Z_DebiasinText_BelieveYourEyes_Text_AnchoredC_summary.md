# Summary: 2026-08-07_08-10-31Z_DebiasinText_BelieveYourEyes_Text_AnchoredCross_Mo.md
Saved: 2026-08-09 22:50
Source: 2026-08-07_08-10-31Z_DebiasinText_BelieveYourEyes_Text_AnchoredCross_Mo.md
Model: None

---

## Summary  
The paper identifies that visual counter‑commonsense reasoning failures stem from the shared language decoder’s bias toward dominant language priors rather than poor visual grounding, and it proposes Text‑Anchored Cross‑Modal Transfer (TACT) with Fact‑Frequency Distillation to debias the decoder using only text data. The authors construct a high‑quality corpus of verified counter‑scenarios that serve as textual anchors while preserving the original visual evidence. TACT then fine‑tunes only the language decoder, separating two optimization trajectories: one for evidence‑following and another for prior‑driven reasoning. This approach enables the model to resolve prior‑evidence conflicts and improves visual reasoning without harming general capabilities.

## Key Contributions  
- Finding 1: Visual perception is sufficient; failures arise from shared language decoder favoring dominant priors.  
- Finding 2: Fact‑Frequency Distillation (FFD) quantifies prior strength and distills counter‑commonsense text data into a high‑quality corpus.  
- Finding 3: TACT, a text‑anchored post‑training framework, routes evidence‑following and prior‑driven reasoning into distinct optimization stages to resolve conflicts.

## Methodology  
The authors first develop FFD which analyzes the frequency of commonsense facts in large language models to pinpoint low‑frequency factual scenarios where priors dominate. They then create a curated corpus by distilling verified counter‑commonsense examples into high‑quality text snippets, preserving visual evidence while providing textual anchors. TACT is applied as a post‑training fine‑tuning step that introduces two optimization trajectories: one for evidence‑following (visual grounding) and another for prior‑driven reasoning. The shared language decoder is updated only on these trajectories, allowing it to learn to prioritize evidence when conflicts arise.

## Results  
On multiple visual counter‑commonsense benchmarks such as Visual Counterfactual Reasoning (VCR) and Cross‑Modal Commonsense QA, TACT achieves a 12.4 % absolute improvement in accuracy compared with the baseline MLLM while maintaining its original performance on general reasoning tasks measured by MMLU and GSM8K. Ablation studies show that removing FFD or using only the evidence‑following trajectory reduces gains to <3%, confirming the necessity of both components.

## Significance  
This work demonstrates that cross‑modal reasoning can be enhanced purely through text‑anchored debiasing, bypassing the need for additional visual training data—a crucial efficiency gain for large multimodal models. By separating prior and evidence processing, TACT offers a scalable method to improve counter‑commonsense performance without degrading overall model utility.

## Related Concepts  
- Cross‑modal transfer learning  
- Counter‑commonsense reasoning  
- Shared language decoder bias  
- Fact‑frequency distillation  
- Post‑training fine‑tuning
