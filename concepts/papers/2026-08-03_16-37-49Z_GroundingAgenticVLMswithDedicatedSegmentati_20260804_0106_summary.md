# Summary: 2026-08-03_16-37-49Z_GroundingAgenticVLMswithDedicatedSegmentationforFi.md
Saved: 2026-08-04 01:06
Source: 2026-08-03_16-37-49Z_GroundingAgenticVLMswithDedicatedSegmentationforFi.md
Model: None

---

## Summary  
Vision‑language models (VLMs) excel at semantic reasoning but struggle with precise spatial grounding for fine‑grained vehicle damage, leading to hallucinations. This paper introduces TinyDamage, a hybrid architecture that couples the VLM with a dedicated segmentation model to improve detection of tiny defects like scratches and hairline cracks. The approach reduces report hallucination from 92 % to 31 % on human‑verified data.

## Key Contributions  
- The authors demonstrate that state‑of‑the‑art VLMs are systematically ungrounded for fine‑grained damage, producing hallucinated locations and missing elongated scratches.  
- They find focal loss collapses tiny‑damage detection to zero due to class imbalance, while a supervised contrastive objective improves separability.  
- They integrate segmentation into a LangGraph agent pipeline, achieving 31 % hallucination rate and introduce DET_l for evaluating tiny‑object grounding under class imbalance.

## Methodology  
The authors address the grounding gap by building TinyDamage: a VLM (Qwen‑VL) handles semantic reasoning and report generation, while a multi‑task segmentation model performs spatial detection using contrastive loss; they embed this segmentation output into a LangGraph agent that grounds each VLM step. The pipeline processes images through segmentation first, then feeds results to the VLM for contextual reporting.

## Results  
On 100 human‑verified reports, TinyDamage reduces hallucination from 92 % (text‑only) and 78 % (image‑only) to 31 %, with DET_l showing high recall on tiny objects. The pipeline runs at sub‑second latency per vehicle image. Semantic accuracy remains 87.3%.

## Significance  
This work bridges the semantic‑vision gap in autonomous driving safety, enabling reliable detection of minute defects that could affect roadworthiness. By decoupling spatial grounding from language generation, it offers a scalable framework for other fine‑grained visual tasks.

## Related Concepts  
- Vision‑language models (VLMs)  
- Multi‑task segmentation  
- Contrastive loss  
- LangGraph agent pipelines  
- Focal loss  
- Detection at low resolution (DET_l)
