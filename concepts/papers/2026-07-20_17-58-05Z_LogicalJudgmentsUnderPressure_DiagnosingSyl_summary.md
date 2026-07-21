# Summary: 2026-07-20_17-58-05Z_LogicalJudgmentsUnderPressure_DiagnosingSyllogisti.md
Saved: 2026-07-20 22:01
Source: 2026-07-20_17-58-05Z_LogicalJudgmentsUnderPressure_DiagnosingSyllogisti.md
Model: None

---

## Summary  
The paper investigates how correct logical judgments respond when a learned, opaque soft prefix is prepended to an exactly labeled syllogistic reasoning benchmark while the model remains fixed. By varying the logical form and interface, the authors characterize which prefixes succeed in inducing bias and how that bias generalizes across unseen tasks. The study reveals that successful soft prefixes can override correct answers, exposing limits in a model’s logical stability under contextual pressure. These findings demonstrate that learned context can systematically shift responses toward one answer meaning, regardless of the underlying symbolic structure.

## Key Contributions  
- [Finding 1] Soft prefixes cause a broad preference for one answer meaning, overriding correct judgments and persisting across different logical forms and interfaces.  
- [Finding 2] Learned prefixes remain effective even when the logical form or interface is unseen, outperforming paired random controls by 37 to 99 percentage points in all model‑direction‑split comparisons.  
- [Finding 3] The dominant effect is a general answer bias; the residual response varies by model, with Qwen models showing score‑model predictability while Gemma’s overall output aligns closely with those predictions.

## Methodology  
The authors prepend soft prefix vectors—continuous, opaque representations—to an exactly labeled syllogistic reasoning benchmark. The model architecture is held constant, and only the prefix changes. They systematically vary the logical form (e.g., premise content, conclusion structure) and interface (e.g., prompt wording, output format). For each combination they measure the flip rate of correct answers between learned prefixes and matched random controls. Experiments are conducted across three models: Qwen3.6‑35B‑A3B MoE, Qwen3‑8B, and Gemma 4 31B, using paired model–direction–split comparisons.

## Results  
Learned prefixes redirect many correct answers, with flip rates for Qwen3.6‑MoE ranging from 72% to 90%. In all 16 model‑direction‑split tests the learned prefix beats random controls by 37 pp to 99 pp. Gemma’s validity prefixes retain a 54–56 % flip rate, compared with less than 1 % for matched random prefixes. Diagnostic tests show that the primary bias is a preference for one answer meaning rather than fixed‑symbol forcing or a reliable logical operation; Qwen models’ responses can be approximated by simple score models, whereas Gemma’s overall response matches those predictions.

## Significance  
These results highlight that learned contextual pressure can degrade logical stability across diverse models and settings, providing diagnostic evidence of systematic answer bias. The findings suggest that external influences—such as soft prefixes—can systematically shift reasoning outcomes, which is a critical concern for reliable AI systems where correctness must be preserved under changing prompts.

## Related Concepts  
- Soft prefixes (continuous vectors injected at the start of input)  
- Syllogistic reasoning benchmark  
- Logical stability (resistance to answer flips)  
- Answer bias / preference effect  
- Model‑specific behavior in MoE architectures  
- Paired random control comparison  
- Contextual pressure on AI reasoning
