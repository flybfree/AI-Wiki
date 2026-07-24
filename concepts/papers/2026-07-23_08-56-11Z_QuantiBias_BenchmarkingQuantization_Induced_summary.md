# Summary: 2026-07-23_08-56-11Z_QuantiBias_BenchmarkingQuantization_InducedBiasinL.md
Saved: 2026-07-24 02:34
Source: 2026-07-23_08-56-11Z_QuantiBias_BenchmarkingQuantization_InducedBiasinL.md
Model: None

---

## Summary  
The paper investigates how quantization of large language models introduces hidden bias that evades standard safety checks. It demonstrates that quantized models still generate stereotypical content in open‑ended responses despite passing existing tests. To address this, the authors introduce QuantiBias, a benchmark that measures bias across languages and compression levels. The work shows that re‑evaluation of open‑ended generation is necessary for safe deployment.  

## Key Contributions  
- Finding 1: Quantization does not affect short‑form safety (refusals, MCQ) but increases open‑ended stereotype bias across eight languages.  
- Finding 2: Bias persists even as compression proceeds, with rates around 24–27 % of answers containing stereotypes under independent judges.  
- Finding 3: The effect varies by model family and whether reasoning is enabled; some families see ~50 % reduction when reasoning is added.  

## Methodology  
The authors paired a multilingual stereotype probe with refusal and multiple‑choice controls to isolate open‑ended generation, contrasted each build (full‑precision vs quantized) with and without internal reasoning, and scored generated text severity using independent human judges across two backbones (Qwen, Gemma), five quantization families, and eight prompts.  

## Results  
Across the compression ladder, 1 in 4 open‑ended answers contained stereotypical content (24–27 % prevalence). Reasoning before answering roughly halved bias for some stereotype families but left others unchanged. Quantizers allocate extra precision to capability data that carries no bias signal, indicating that the loss is not due to data compression per se.  

## Significance  
This reveals a systematic gap between short‑form safety checks and open‑ended output, prompting developers to re‑evaluate models for hidden bias after quantization. It underscores the need for comprehensive bias testing beyond existing safeguards.  

## Related Concepts  
Quantization, bias mitigation, model compression, stereotype generation, multi‑language evaluation, reasoning augmentation, safety benchmarks.
