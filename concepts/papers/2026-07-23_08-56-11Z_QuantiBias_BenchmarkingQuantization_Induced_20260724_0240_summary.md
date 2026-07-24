# Summary: 2026-07-23_08-56-11Z_QuantiBias_BenchmarkingQuantization_InducedBiasinL.md
Saved: 2026-07-24 02:40
Source: 2026-07-23_08-56-11Z_QuantiBias_BenchmarkingQuantization_InducedBiasinL.md
Model: None

---

## Summary  
This paper investigates how quantization of large language models (LLMs) introduces subtle biases that evade conventional safety evaluations. It demonstrates that while quantized models still refuse harmful prompts and answer multiple‑choice questions unbiasedly, they generate stereotypical content in open‑ended queries across eight languages. The authors introduce QuantiBias, a benchmark to quantify this bias systematically. Their work shows that standard safeguards are insufficient for detecting these hidden prejudices.  

## Key Contributions  
- The quantized model retains refusal and MCQ performance but introduces measurable stereotype generation in open‑ended answers, with ~24–27% of responses flagged as biased by independent judges across the compression ladder.  
- A robust selective gap exists between short‑form safety checks and long‑form bias, indicating that standard evaluation misses a critical failure mode.  
- QuantiBias provides a paired benchmark combining multilingual stereotype probes with refusal and MCQ controls to isolate open‑ended generation while rating severity.  

## Methodology  
The authors held the base model (Qwen or Gemma), its training data, and prompts constant, then applied five quantization families ranging from full precision to low‑bit integer. For each build they generated responses to a multilingual stereotype prompt and evaluated them with human judges using a calibrated severity scale. They also measured refusal rates on harmful queries and multiple‑choice answer correctness, separating open‑ended generation from short‑form tasks.  

## Results  
Across two backbones, eight benchmarks, and five quantizers, the authors found that open‑ended bias increased roughly one in four times (24–27%) relative to full‑precision models. Reasoning before answering reduced the effect for some stereotype families by about half but had no impact on others. The magnitude of bias varied with quantization level, confirming a systematic degradation as precision is allocated to capability data that does not contain bias‑prevention signals.  

## Significance  
This work reveals that quantization can amplify hidden biases in LLMs, undermining claims of safety when only short‑form checks are used. By exposing the gap between standard evaluations and long‑form generation, QuantiBias urges developers to re‑evaluate open‑ended outputs, especially as models become more compressed for deployment.  

## Related Concepts  
- Quantization  
- Bias in language models  
- Open‑ended generation  
- Safety evaluation  
- Multilingual bias detection
