# Summary: 2026-08-12_07-07-57Z_Harness_IF_EvaluatingInstructionFollowingAcrossIns.md
Saved: 2026-08-12 21:30
Source: 2026-08-12_07-07-57Z_Harness_IF_EvaluatingInstructionFollowingAcrossIns.md
Model: None

---

## Summary  
The paper introduces **Harness‑IF**, a framework that evaluates how coding agents obey operational rules across the various surfaces they read (user turn, system prompt, project file, tool description, skill description). By scoring each rule individually from execution evidence rather than relying on final task success, Harness‑IF separates genuine compliance from random chance. The authors also propose **Against‑Prior Accuracy (AP‑Acc)**, a metric that measures only rules whose default behavior is opposite to the unprompted rule and only when those defaults are observed across multiple probe builds. This work provides a systematic way to assess instruction following beyond aggregate success rates.

## Key Contributions  
- [Finding 1] Harness‑IF introduces **Against‑Prior Accuracy (AP‑Acc)**, which scores rules that contradict the unprompted default, thereby isolating compliance from coincidence.  
- [Finding 2] Across twelve frontier models, AP‑Acc ranges from 66.1 % to 78.6 %, and every model performs worse on against‑prior rules than on prompt‑aligned ones (average drop of ~5.8 points).  
- [Finding 3] Aggregate compliance scores systematically overstate true rule adherence; the direction of the performance gap survives a common‑support analysis, indicating that higher aggregate scores are inflated by model‑specific margins rather than deeper understanding.

## Methodology  
The authors constructed **60 realistic multi‑turn coding items** drawn from a library of 642 operational rules. Each item places a single rule on one of five configurable surfaces (user turn, system prompt, project file, tool description, skill description) and records the agent’s execution evidence. To compute AP‑Acc, tasks are re‑run with the rule held out across **nine probe builds**, allowing the measurement of how often the opposite default is observed. This approach evaluates each rule in isolation while controlling for build‑specific biases.

## Results  
The experimental results show that model accuracy on aligned rules spans **72.1 % to 85.9 %**, while AP‑Acc ranges from **66.1 % to 78.6 %**. Every model is consistently worse on against‑prior rules, with a mean performance gap of **3.6–7.4 points** (average 5.81). A common‑support analysis confirms that this direction holds across all models and does not depend on the specific rule cluster. Importantly, aggregate compliance scores overstate true adherence by a model‑specific margin: prior control leaves the top build unchanged but swaps three adjacent rank pairs.

## Significance  
Harness‑IF matters because it provides the first systematic metric that distinguishes genuine rule following from mere coincidence in multi‑turn coding agents. By measuring against‑prior accuracy, the framework uncovers hidden biases and overestimation of compliance, enabling more honest benchmarking and better calibration of instruction‑following capabilities.

## Related Concepts  
- Instruction following  
- Rule compliance  
- Against‑Prior Accuracy (AP‑Acc)  
- Multi‑turn coding tasks  
- Prompt surfaces (user turn, system prompt, project file, tool description, skill description)  
- Benchmarking of AI agents  
- Common‑support analysis

## Original Paper Reference

- [Read the original paper](http://arxiv.org/abs/2608.11727v1)
