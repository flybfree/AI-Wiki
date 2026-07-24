# Summary: 2026-07-23_08-56-11Z_QuantiBias_BenchmarkingQuantization_InducedBiasinL.md
Saved: 2026-07-24 02:44
Source: 2026-07-23_08-56-11Z_QuantiBias_BenchmarkingQuantization_InducedBiasinL.md
Model: None

---

## Summary  
The paper demonstrates that quantization—compressing large language models for efficiency—does not eliminate, and can even amplify, bias in open‑ended generation despite the model passing conventional safety checks. By introducing **QuantiBias**, a systematic benchmark that isolates open‑ended responses from refusal and multiple‑choice controls, the authors reveal a persistent stereotype rate of roughly 24–27 % across eight languages and two backbones (Qwen and Gemma). Their findings show that this bias is robust to compression levels and can be partially mitigated by adding reasoning, but it remains measurable in all quantization families. The work argues that standard safety evaluations must be complemented with dedicated open‑ended bias metrics.

## Key Contributions  
- [Finding 1] Quantized LLMs still generate biased open‑ended answers even when they correctly refuse harmful prompts or select unbiased multiple‑choice responses.  
- [Finding 2] The stereotype rate remains stable across the compression ladder, indicating that quantization does not inherently reduce this bias and is sensitive to the scoring judge.  
- [Finding 3] QuantiBias provides a reproducible benchmark that pairs multilingual stereotype probes with safety‑control controls to quantify open‑ended bias systematically.

## Methodology  
The authors constructed **QuantiBias** by evaluating eight benchmarks on two backbone models (Qwen and Gemma) across five quantization families. For each build, they generate open‑ended responses to a multilingual stereotype probe while simultaneously measuring refusal accuracy and multiple‑choice correctness. The severity of generated stereotypes is rated by an independent human judge. Reasoning modules are added or removed to compare their impact on bias. Quantizers allocate extra precision based on capability data that carries no explicit bias‑prevention signal, allowing the study to isolate compression effects.

## Results  
Across all experiments, about one in four open‑ended answers (24–27 %) contain detectable stereotypes, regardless of quantization level or model family. Adding reasoning reduces the effect for some stereotype families but has little impact on others. The bias persists even when the model passes standard safety thresholds, highlighting a systematic gap between short‑form checks and long‑form generation.

## Significance  
These results underscore that current safety evaluations overlook open‑ended bias introduced by quantization, which can affect user trust and real‑world deployment. QuantiBias offers a concrete framework for monitoring this hidden risk, prompting developers to re‑evaluate quantized models beyond conventional short‑form safeguards.

## Related Concepts  
quantization, bias, large language model (LLM), stereotype generation, safety evaluation, open‑ended generation, compression ladder, multilingual, QuantiBias benchmark, reasoning module.
