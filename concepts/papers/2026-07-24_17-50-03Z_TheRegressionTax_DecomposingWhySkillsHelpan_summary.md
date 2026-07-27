# Summary: 2026-07-24_17-50-03Z_TheRegressionTax_DecomposingWhySkillsHelpandHurtLL.md
Saved: 2026-07-26 21:56
Source: 2026-07-24_17-50-03Z_TheRegressionTax_DecomposingWhySkillsHelpandHurtLL.md
Model: None

---

## Summary  
The paper introduces the “Regression Tax” framework to dissect why adding procedural skills to LLM agents can both improve and degrade performance, arguing that aggregate task‑success metrics hide a critical cost. By comparing agents with and without skills across thousands of runs on two office‑automation benchmarks and three model harnesses, the authors separate regressions—failures that appear only after skills are introduced—from residual failures that persist regardless of skill presence. Their analysis reveals three distinct regression mechanisms: skill description osmosis, grounding displacement, and verification displacement. The study shows that many regressions can be remedied by improving grounding and verification rather than by selecting a different procedural skill.

## Key Contributions  
- [Finding 1] Regressions are substantial enough that the best‑performing skills outperform others primarily by regressing less, not by gaining more task success.  
- [Finding 2] The three regression modes identified are (i) skill description osmosis—a skill changes behavior merely by being present in context; (ii) grounding displacement—where a prescribed procedure overrides the agent’s input interpretation; and (iii) verification displacement—where the procedure suppresses checks the agent would otherwise perform.  
- [Finding 3] Persistent failures exhibit the same underlying pattern, indicating that existing evaluation artifacts overemphasize procedural guidance while under‑estimating grounding and verification as dominant failure sources.

## Methodology  
The authors performed a large‑scale experimental study involving nearly 6,000 runs across two office‑automation benchmarks (e.g., “Office Assistant” tasks) and three model harness stacks. For each run they evaluated agents both with and without the same procedural skill, recording task success rates to compute regression (failure only after skills) versus residual failure rates. They then traced execution traces to pinpoint where agent behavior diverged from expected outcomes, allowing them to attribute regressions to specific mechanisms.

## Results  
Regressions were found in a significant minority of runs; the most effective skill improvements correlated with lower regression counts rather than higher success gains. Persistent failures (residuals) consistently stemmed from grounding and verification issues, not from procedural content. Moreover, many regressions could be recovered by enhancing grounding—ensuring the agent correctly interprets inputs—and verification—preventing suppression of necessary checks.

## Significance  
Evaluating LLM agents should decompose skill effects into gains versus regressions rather than relying on aggregate improvement scores. This insight shifts focus from choosing “better” procedural skills to improving grounding and verification mechanisms, which are the primary sources of remaining errors.

## Related Concepts  
- Regression tax (the hidden cost of adding skills)  
- Regression modes: skill description osmosis, grounding displacement, verification displacement  
- Residual failures (failures independent of skill presence)  
- Procedural skills in LLM agents  
- Evaluation artifacts and trace analysis
