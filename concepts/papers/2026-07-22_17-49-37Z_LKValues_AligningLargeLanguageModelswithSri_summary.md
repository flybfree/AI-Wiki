# Summary: 2026-07-22_17-49-37Z_LKValues_AligningLargeLanguageModelswithSriLankanS.md
Saved: 2026-07-23 00:02
Source: 2026-07-22_17-49-37Z_LKValues_AligningLargeLanguageModelswithSriLankanS.md
Model: None

---

## Summary  
The authors address the problem that large language models (LLMs) are culturally biased toward Western norms and often mishandle local values in multilingual societies such as Sri Lanka, especially in Sinhala. To remedy this gap they introduce **LKValues**, a survey‑grounded resource suite that captures 40 majority‑endorsed societal values from a trilingual questionnaire of 205 respondents and builds two datasets: an instruction corpus (LKvaluesIT) and a value‑sensitive evaluation benchmark (LKvaluesBench). Their experiments fine‑tune three open‑weight models on these resources and show measurable improvements in English and Sinhala outputs while still revealing family‑dependent alignment gaps.  

## Key Contributions  
- [Finding 1] A comprehensive, survey‑derived list of 40 Sri Lankan societal values that reflect local cultural dynamics beyond Western frameworks.  
- [Finding 2] Construction of two novel datasets—LKvaluesIT (≈150 k scenario‑based instruction examples) and LKvaluesBench (1 000 evaluation instances)—to support value‑aligned fine‑tuning and benchmarking.  
- [Finding 3] Fine‑tuned models demonstrate reduced invalid outputs and cross‑lingual disparities, confirming that LKValues can embed local values, though gains vary by model family.  

## Methodology  
The authors conducted a trilingual survey of 205 respondents to blend adapted global value frameworks with locally elicited constructs, yielding the 40 core values. Using these values as a guide, they created **LKvaluesIT**, a Sinhala‑English news‑derived instruction corpus containing 150 k scenario‑based instances, and **LKvaluesBench**, a benchmark of 1 000 value‑sensitive prompts. They evaluated both proprietary and open‑weight LLMs by fine‑tuning three base models—Qwen3.5‑4B‑Base, Qwen3.5‑9B‑Base, and Aya‑Expanse‑8B‑Base—on the instruction corpus and then tested them on the benchmark.  

## Results  
Newer and larger LLMs still exhibit low‑resource cultural value alignment gaps; however, LKValues fine‑tuning improves Qwen‑family models in both English and Sinhala by lowering invalid outputs and narrowing cross‑lingual disparities. The improvement is noticeable but not uniform across model families, indicating that the pipeline works well for certain architectures while remaining dependent on their design.  

## Significance  
LKValues provides a replicable, low‑resource pipeline for embedding Sri Lankan pluralist values into LLMs, offering a concrete dataset (publicly available at https://github.com/NextME14/LKValues) that can be adapted to other multilingual contexts. This work bridges the cultural bias gap and supports responsible AI deployment in South Asian societies.  

## Related Concepts  
value alignment, cultural bias, multilingual LLMs, survey‑grounded resources, instruction tuning, benchmarking, low‑resource adaptation, pluralist values.
