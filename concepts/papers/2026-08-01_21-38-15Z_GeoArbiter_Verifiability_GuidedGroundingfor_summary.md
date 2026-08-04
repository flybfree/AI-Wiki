# Summary: 2026-08-01_21-38-15Z_GeoArbiter_Verifiability_GuidedGroundingforRemote_.md
Saved: 2026-08-03 20:32
Source: 2026-08-01_21-38-15Z_GeoArbiter_Verifiability_GuidedGroundingforRemote_.md
Model: None

---

## Summary  
This paper addresses the problem of remote‑sensing multimodal large language models (MLLMs) that generate geographic claims which may contradict visible imagery. It proposes GeoArbiter, a verifiability‑guided grounding pipeline that selects only image‑unverifiable facts to improve accuracy while reducing hallucinations.

## Key Contributions  
- The authors demonstrate that source trust should be based on cross‑modal verifiability: records are most useful for attributes the image cannot verify and most dangerous when they dispute visual evidence.  
- GeoArbiter, a training‑free pipeline, injects only such unverifiable geographic facts, preserving most of the full‑retrieval accuracy gain while reducing claim‑level hallucination.  
- The method improves robustness to conflicting records across three open remote‑sensing multimodal LLMs.

## Methodology  
The authors propose a content‑level filtering approach that distinguishes between verifiable and non‑verifiable attributes in retrieved geographic records. Instead of using arbitration prompts that leak information, they filter out records that could contradict visible evidence, thereby preserving the benefits of retrieval without introducing bias.

## Results  
Experimental evaluation on three open remote‑sensing multimodal LLMs shows a 12.06–17.19 point increase in fMoW land‑use accuracy when using GeoArbiter. The pipeline retains 84.69–87.15% of the full‑retrieval accuracy gain, reduces hallucination by 9.58–26.34%, and maintains robustness across conflicting records.

## Significance  
This work provides a simple yet effective mechanism for grounding MLLMs in fallible geographic knowledge, mitigating hallucinations caused by unreliable source data. By operationalizing verifiability, it offers a scalable solution to improve factuality in remote‑sensing applications.

## Related Concepts  
- Remote‑sensing multimodal large language models (MLLMs)  
- Grounding and fact verification  
- Cross‑modal verifiability  
- Content‑level filtering  
- Retrieval augmentation
