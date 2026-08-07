# Summary: 2026-08-05_19-40-06Z_CounterfactualAnalysisviaLargeLanguageModels.md
Saved: 2026-08-06 21:49
Source: 2026-08-05_19-40-06Z_CounterfactualAnalysisviaLargeLanguageModels.md
Model: None

---

## Summary  
The paper proposes using large language models (LLMs), specifically GPT‑3.5, for counterfactual analysis in online lending to predict ROI under alternative interest rates. It evaluates the model’s predictive performance against traditional machine‑learning methods and demonstrates that prompt engineering can boost its R² from 1.97% to 2.84%, nearing the 3.48% of gradient‑boosted regression. The authors also show that GPT generates coherent, logically consistent counterfactual ROI values for various interest‑rate scenarios. This work highlights LLMs as viable tools for decision‑making in lending.

## Key Contributions  
- Finding 1: Prompt engineering significantly improves GPT’s predictive R², moving from 1.97% to 2.84%, close to the best traditional algorithm.  
- Finding 2: GPT can generate logical and causally coherent counterfactual ROI predictions for alternative interest rates.  
- Finding 3: The study demonstrates that LLMs can rival advanced machine‑learning models in this specific task.

## Methodology  
The authors constructed a dataset of online lending transactions with known ROI outcomes. They compared GPT‑3.5’s ability to predict ROI under hypothetical interest‑rate changes against gradient‑boosted regression and other ML baselines. Prompt engineering was applied by formulating detailed instructions that specify the scenario, variables, and desired output format.

## Results  
The R² for GPT with prompts is 2.84%, exceeding its unprompted baseline of 1.97% and approaching the 3.48% achieved by gradient‑boosted regression. Additionally, manual inspection confirmed that GPT’s counterfactual ROI values were internally consistent and aligned with expected economic logic across multiple interest‑rate variations.

## Significance  
By showing that LLMs can achieve near‑state‑of‑the‑art predictive performance in a real‑world financial context, the paper expands the applicability of LLMs beyond pure text generation to structured decision support. It suggests that prompt engineering can unlock quantitative reasoning capabilities, offering a low‑cost alternative to complex model training pipelines.

## Related Concepts  
- Counterfactual analysis  
- Large language models (LLMs)  
- Prompt engineering  
- Gradient‑boosted regression  
- Return on investment (ROI) prediction  
- Online lending
