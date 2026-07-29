# Summary: 2026-07-27_20-46-29Z_SimilarModelsLearnDifferently_Final_WindowPretrain.md
Saved: 2026-07-28 22:24
Source: 2026-07-27_20-46-29Z_SimilarModelsLearnDifferently_Final_WindowPretrain.md
Model: None

---

## Summary  
The paper investigates whether the final window of pretraining—data that precedes supervised fine‑tuning (SFT)—leaves a hidden imprint on a model’s behavior that is invisible after SFT. By varying this last window across six distinct data sources and then applying identical post‑training procedures, the authors show that two checkpoints can be indistinguishable in benchmark performance yet diverge dramatically under further alignment training. The key insight is that what a model has been trained on *last* determines how it responds to subsequent instruction‑following or preference‑optimization updates. Consequently, checkpoint evaluation must consider pretraining order, not just post‑SFT metrics.

## Key Contributions  
- [Finding 1] A final‑window imprint creates a latent difference that no SFT benchmark can detect but influences downstream alignment outcomes.  
- [Finding 2] When safety text occupies the last window, it yields selective protection against harmful requests—loss of refusal is minimal compared with earlier windows or other data sources.  
- [Finding 3] Checkpoint evaluation should report the content and order of the final pretraining window because it shapes how a model reacts to post‑SFT training.

## Methodology  
The authors construct six branches from a single partially pretrained checkpoint, each differing only in the last 500 million tokens (≈0.1–1 % of total pretraining). Each branch is trained on a distinct data source: generic web text, filtered web text, normative discourse, safety text, mathematical text, or synthetic educational text. After this window, all branches undergo identical supervised fine‑tuning and subsequent preference‑optimization or reinforcement learning with a verifiable reward. The experiment measures refusal behavior on harmful prompts before and after post‑training to quantify the imprint.

## Results  
After SFT, all six checkpoints perform within ~1 point of each other across instruction following, refusal, and capability benchmarks, making them appear interchangeable. However, under post‑SFT preference optimization or RL reward updates, the safety‑text branch retains its refusal ability far better than the web‑text branch, while the other four branches gain little to no protection. The protective effect appears only when safety text is placed last; earlier placement yields weaker outcomes. These results replicate on a second model family, confirming robustness.

## Significance  
The study reveals that pretraining order matters for alignment and safety, challenging the common practice of judging checkpoints solely by post‑SFT performance. Reporting the final window’s content enables researchers to understand and mitigate unintended behavioral drift, improving reproducibility and trust in model deployment.

## Related Concepts  
- Final window of pretraining (last data before instruction tuning)  
- Supervised fine‑tuning (SFT)  
- Preference optimization / reinforcement learning with verifiable rewards  
- Instruction following and refusal behavior  
- Alignment training  
- Pretraining imprint / latent bias
