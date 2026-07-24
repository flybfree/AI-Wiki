# Summary: 2026-07-17_00-04-53Z_SLAPBench_BenchmarkingMultimodalLargeLanguageModel.md
Saved: 2026-07-23 23:51
Source: 2026-07-17_00-04-53Z_SLAPBench_BenchmarkingMultimodalLargeLanguageModel.md
Model: None

---

## Summary  
The paper introduces SLAPBench, a benchmark for multimodal large language models (MLLMs) to verify identity from four‑finger SLAP fingerprints. It uses the NIST SD302b dataset with 7,832 paired images and evaluates four open‑source MLLMs plus Claude Opus under various prompting strategies. The study demonstrates that prompting can cause model collapse while model capability determines discrimination performance.  

## Key Contributions  
- Finding 1: Prompting governs collapse; task‑description prompts cause near‑perfect false acceptance across most models.  
- Finding 2: Model capability varies widely; Claude Opus achieves lowest FAR (20.2%) and highest AUC (0.953), while InternVL3 is inverted at 0.590 and Qwen2.5 near random.  
- Finding 3: SLAPBench establishes the first SLAP‑specific MLLM baseline and shows that discrimination can be rescued by prompt design.  

## Methodology  
The authors built SLAPBench using NIST SD302b, generating 7,832 paired SLAP images (176 mated, 7,656 non‑mated). They evaluated four open‑source MLLMs (InternVL3‑8B, Qwen2.5‑VL‑7B, Qwen3‑VL‑8B, Gemma‑3‑12B) and Claude Opus 4.8 via zero‑shot, task‑description, and similarity‑scoring prompts. Evaluation measured binary verification (FAR), AUC for similarity scoring, and fairness across gender, race, age.  

## Results  
Task‑description prompting collapsed open‑source models to ~100% FAR; Gemma‑3‑12B also collapsed under zero‑shot. Claude Opus 4.8 avoided collapse with best FAR=20.2%. Similarity scoring showed AUCs: Claude 0.953, Gemma‑3‑12B 0.837, InternVL3 0.590 (inverted), Qwen2.5 0.567 near random; Qwen3‑VL‑8B perfect AUC=1.0 but considered diagnostic due to resolution duplication in SD302b. Fairness probe revealed disparity grows as discrimination weakens.  

## Significance  
SLAPBench provides a standardized benchmark for MLLM fingerprint verification, revealing that prompt engineering is critical and exposing capability gaps among models; it guides developers toward robust multimodal identity systems.  

## Related Concepts  
Four‑finger SLAP fingerprints, multimodal large language models (MLLMs), binary verification (FAR), AUC, prompting strategies (zero‑shot, task‑description, similarity‑scoring), fairness evaluation, NIST SD302b dataset, resolution duplication, cross‑resolution pairs.
