# Summary: 2026-07-24_05-27-49Z_AnalysingSelf_HarmRepresentationsinLanguageModels_.md
Saved: 2026-07-26 21:38
Source: 2026-07-24_05-27-49Z_AnalysingSelf_HarmRepresentationsinLanguageModels_.md
Model: None

---

## Summary  
The paper investigates how large language models encode self‑harm related text, aiming to improve detection and intervention systems. It trains linear probes on two datasets (X‑Sensitive, SH‑Detection) across four LLMs and examines where self‑harm information is encoded in the network layers. Contrastive probing reveals that Gemma‑3‑4B encodes a more intricate representation of self‑harm direction than other models. Findings suggest that self‑harm representations concentrate near the output layer and are not always linearly separable.  

## Key Contributions  
- [Finding 1] Self‑harm information crystallizes in the final 3–7% of network layers (93 to 97% depth) across all datasets.  
- [Finding 2] The most accurate linear probes correspond to contrastive self‑harm directions, not merely linearly separable features; Gemma‑3‑4B encodes this direction more intricately.  
- [Finding 3] Cross‑architecture analysis shows that representation quality varies by model architecture, with Gemma‑3‑4B outperforming others in capturing nuanced self‑harm semantics.  

## Methodology  
The authors trained linear probe classifiers on top of each layer of the four models (Gemma‑3‑4B, LLaMA‑2‑70B, Mistral‑7B, and Falcon‑180B) using two self‑harm datasets: X‑Sensitive and SH‑Detection. They performed contrastive probing by extracting directional embeddings for pairs of self‑harm sentences, normalizing them, and evaluating probe accuracy per layer to locate where semantic information is retained.  

## Results  
Across all models and datasets, probe performance peaked in the last 3–7% of layers, indicating that self‑harm semantics are compressed near the output. Gemma‑3‑4B achieved the highest probe accuracy for contrastive probing, suggesting a more refined representation. Linear separability was not required; probes based on contrastive direction were most effective.  

## Significance  
Accurate detection of self‑harm content is critical for safety interventions; understanding where and how LLMs encode such language can inform model governance, risk mitigation, and the design of intervention triggers.  

## Related Concepts  
- Large Language Models (LLMs)  
- Linear probing  
- Contrastive probing  
- Self‑harm detection  
- Model depth analysis  
- Representation learning
