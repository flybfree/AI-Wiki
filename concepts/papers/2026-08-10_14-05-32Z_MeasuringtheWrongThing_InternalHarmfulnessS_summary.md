# Summary: 2026-08-10_14-05-32Z_MeasuringtheWrongThing_InternalHarmfulnessScoresAn.md
Saved: 2026-08-10 23:50
Source: 2026-08-10_14-05-32Z_MeasuringtheWrongThing_InternalHarmfulnessScoresAn.md
Model: None

---

## Summary  
The paper critiques the way internal safety scores are used to detect jailbreak attacks, arguing that these scores measure the wrong quantity: they assess prompt‑level harmful intent while ignoring how a model actually responds. By introducing **Active Attention Probing**, the authors provide a fixed, content‑independent measurement coordinate that isolates the score from the prompt’s wording. Their experiments show that wrapping harmful prompts into a “plain” wrapper raises actual harmful generation but makes those prompts appear less risky to the score, causing false negatives in jailbreak detection. The findings reveal a systematic misalignment between internal safety judgments and real‑world attack outcomes.

## Key Contributions  
- **Finding 1:** Wrapping harmful prompts increases harmful generation (0.05 → 0.27) while the safe‑intent AUROC drops from 0.936 to 0.803, indicating that the score’s false‑positive budget is spent on attacks that would have failed anyway.  
- **Finding 2:** Among wrapped harmful prompts, the outcome AUROC is 0.220, meaning successful attacks are ranked below failed ones, a reversal of the expected ordering.  
- **Finding 3:** This reversal persists across three target models, seven attack families, and two independent judges; distribution shift later degrades calibration and threshold transfer before it harms ranking.

## Methodology  
The authors audit the inference pipeline that produces internal safety scores. They employ **Active Attention Probing**, which supplies a fixed content‑independent measurement coordinate so that the score is evaluated at the same position regardless of prompt wrapping. For each base goal they generate two versions: a plain prompt and its wrapped counterpart, then feed both to the target model to obtain completions. The study compares harmful‑intent AUROC (how well the score separates benign vs. malicious prompts) with outcome AUROC (whether successful attacks are correctly identified). This paired design isolates the effect of wrapper manipulation on both the internal judgment and the actual attack result.

## Results  
Wrapping a harmful prompt raises its generation toxicity from 0.05 to 0.27, yet the safe‑intent AUROC falls sharply to 0.803, showing that the safety filter’s false‑positive budget is misallocated. The outcome AUROC for wrapped prompts is only 0.220, indicating that successful attacks are now below failed ones—a clear ranking reversal. These effects hold across three target models (Llama, etc.), seven distinct attack families, and two judges, confirming a robust phenomenon. Subsequent distribution shift degrades calibration and threshold transfer before it further impairs the ranking order.

## Significance  
The paper demonstrates that internal safety scores built on prompt‑dependent attention can systematically misclassify jailbreak attacks, leading to false negatives and eroding trust in automated moderation systems. By introducing a content‑independent probing method, the authors highlight the need for calibration‑aware evaluation and suggest that current “one‑size‑fits‑all” safety filters may be fundamentally flawed.

## Related Concepts  
- Internal safety scores  
- Jailbreak detection  
- AUROC (Area Under the ROC Curve)  
- Active Attention Probing  
- Distribution shift  
- Calibration and threshold transfer  
- Prompt wrapping  
- Malicious intent vs. harmful generation
