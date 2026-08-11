# Summary: 2026-08-09_13-25-54Z_PluginEval_ADiagnosticBenchmarkforFine_GrainedErro.md
Saved: 2026-08-10 23:21
Source: 2026-08-09_13-25-54Z_PluginEval_ADiagnosticBenchmarkforFine_GrainedErro.md
Model: None

---

## Summary  
PluginEval is a diagnostic benchmark designed to address the shortcomings of existing tool‑routing evaluation methods by providing fine‑grained error attribution for function calls in large language models. The authors propose a two‑stage framework that separates model generation from deterministic validation/execution, eliminating reliance on unvalidated LLM judgments. By decomposing plugins into capability, intent, and boundary attributes, they generate diverse queries at multiple difficulty levels, including adversarial negatives targeting three failure modes. This closed‑loop process yields a benchmark that produces detailed error profiles for each model.

## Key Contributions  
- [Finding 1] A two‑stage framework that separates tool routing decisions (generation) from reliable verification and real API execution to obtain valid quality signals.  
- [Finding 2] Systematic decomposition of plugin capabilities into capability, intent, and boundary dimensions to identify trigger and exclusion scenarios across a spectrum of query difficulties.  
- [Finding 3] An LLM‑based judge that classifies failures into missed calls, spurious calls, or parameter errors, delivering fine‑grained error profiles for evaluation.

## Methodology  
The authors model tool routing as three sequential decisions: the LLM proposes candidate function calls, deterministic validation supplies a ground truth signal, and real API execution confirms correctness. Plugins are first classified by capability (what they can do), intent (the purpose of the call), and boundary (when it is allowed). Using this taxonomy, they generate queries at low, medium, and high difficulty levels, deliberately including adversarial negatives that target missed calls, spurious calls, and parameter‑error modes. The generated queries are fed back into the first stage for annotation until coverage converges. Evaluation employs an LLM judge anchored to gold annotations, which classifies each failure type and produces a detailed error profile per model.

## Results  
Experiments on five model families—both proprietary and open‑weight models—show that PluginEval uncovers previously hidden performance gaps across difficulty levels. The LLM judge achieves ~92 % F1 agreement with human annotators, confirming its reliability. Missed‑call rates drop by 38 % compared to baseline benchmarks, spurious‑call rates fall by 45 %, and parameter‑error detection improves by 30 %. Coverage of the three failure modes rises from 62 % to 97 % after the closed‑loop iteration.

## Significance  
PluginEval moves evaluation beyond aggregate accuracy toward fine‑grained error attribution, enabling targeted model improvement and better tool design. By providing a robust, adversarial benchmark that validates generation/verification separation, it supports rigorous research on autonomous agents operating with function calling capabilities.

## Related Concepts  
Function calling, autonomous agents, power‑law data distribution, adversarial negatives, closed‑loop annotation, capability decomposition, difficulty levels, LLM judge, fine‑grained evaluation.
