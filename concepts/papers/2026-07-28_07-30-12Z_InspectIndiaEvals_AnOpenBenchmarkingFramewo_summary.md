# Summary: 2026-07-28_07-30-12Z_InspectIndiaEvals_AnOpenBenchmarkingFrameworkforEv.md
Saved: 2026-07-28 22:33
Source: 2026-07-28_07-30-12Z_InspectIndiaEvals_AnOpenBenchmarkingFrameworkforEv.md
Model: None

---

## Summary  
Inspect India Evals is an open‑source benchmarking framework designed to evaluate large language models against Indian linguistic, cultural, and safety challenges that are overlooked by existing English‑centric benchmarks. It addresses the gap between global fairness metrics and local context‑specific failures in digital public infrastructure (DPI) and social bias. The framework comprises six benchmarks covering multilingual knowledge, social bias, DPI safety, harmful prompt responses, jailbreak resistance, and cultural knowledge judged via LLM‑as‑judge rubrics. By testing open‑weight models from 8B to 32B parameters, it demonstrates that Indian‑focused LLMs can outperform larger Western models on local fairness indices.  

## Key Contributions  
- Inspect India Evals provides the first comprehensive, multilingual benchmark suite tailored to India’s linguistic diversity and cultural nuances.  
- The framework identifies a significant gap in existing benchmarks by showing that DPI safety compliance varies widely across Indian LLMs, with some achieving 100% refusal on harmful prompts while others fail at 20%.  
- Experimental results reveal that open‑weight models such as Sarvam‑M 24B and Gemma 2 27B achieve the highest scores (80%) on the composite India Fairness Index, outperforming larger 32B models in cultural knowledge and DPI safety.  

## Methodology  
The authors built Inspect India Evals on top of UK AISI’s Inspect AI platform, integrating six benchmarks: Multilingual MMLU across sixteen Indian languages, BharatBBQ for social bias detection, a Digital Public Infrastructure (DPI) safety test, multilingual harmful‑prompt safety evaluation, multi‑turn jailbreak resistance, and an Indian cultural knowledge benchmark scored via LLM‑as‑judge rubrics. They evaluated five open‑weight LLMs with parameter counts ranging from 8B to 32B.  

## Results  
All models passed the Multilingual Safety test with 100% refusal rates. DPI safety compliance ranged from 20% to 100%, indicating uneven handling of Indian‑specific risks. The composite India Fairness Index scores placed Sarvam‑M 24B and Gemma 2 27B at the top, both scoring 80%. These models also outperformed larger 32B models on cultural knowledge and DPI safety tasks.  

## Significance  
This work matters because it demonstrates that global LLM benchmarks are insufficient for real‑world deployment in India’s diverse linguistic landscape. By quantifying failures unique to Indian contexts, Inspect India Evals guides developers toward safer, more culturally aware AI systems, especially those integrated into Digital Public Infrastructure that serve millions.  

## Related Concepts  
- Large Language Models (LLMs)  
- Multilingual MMLU benchmark  
- Digital Public Infrastructure (DPI) safety  
- LLM‑as‑judge rubrics  
- Open‑weight model evaluation  
- UK AISI Inspect AI platform
