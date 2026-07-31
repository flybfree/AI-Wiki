# Summary: 2026-07-30_14-47-00Z_ObjectStream_LatentObjectsasMemoryAnchorsforStream.md
Saved: 2026-07-30 20:38
Source: 2026-07-30_14-47-00Z_ObjectStream_LatentObjectsasMemoryAnchorsforStream.md
Model: None

---

## Summary  
The paper proposes ObjectStream, a training‑free framework that treats latent objects in Video‑LLM representations as memory anchors for streaming video understanding. It organizes visual evidence around persistent objects across frames within a bounded memory budget, enabling efficient reasoning without external detectors or segmentation models. By preserving object histories, transient changes, and recent context, ObjectStream improves model performance on both online real‑time tasks and offline long‑video benchmarks.  

## Key Contributions  
- [Finding 1] Latent objects are extracted as spatially coherent anchors directly from frozen Video‑LLM embeddings.  
- [Finding 2] These anchors persist across frames while maintaining a bounded memory budget, discarding unnecessary tokens.  
- [Finding 3] The framework integrates three evidence forms—persistent histories, transient changes, and recent context—to support object reasoning.  

## Methodology  
ObjectStream bypasses token‑importance or segment‑level relevance heuristics by first identifying latent objects from the frozen Video‑LLM representation. It then links these objects across consecutive frames to create persistent anchors that are stored in a memory buffer limited by a fixed size, discarding older tokens as needed. The retained evidence is combined with the current frame’s visual context before feeding it into the downstream Qwen2.5‑VL‑7B model for answering streaming queries.  

## Results  
In online real‑time evaluation on OVO‑Bench, ObjectStream boosts Qwen2.5‑VL‑7B by 10.0 points while cutting peak GPU memory and TTFT roughly in half. Offline long‑video benchmarks show it outperforms the full‑token baseline yet discards about 82.5 % of visual tokens.  

## Significance  
The work demonstrates that organizing video evidence around latent objects is a practical way to compress streaming memory, enabling stateful reasoning without retraining or extra components. This insight can be applied broadly to any Video‑LLM pipeline seeking efficient long‑term memory.  

## Related Concepts  
- Latent object representation  
- Memory anchors  
- Streaming video understanding  
- Bounded memory budget  
- Video Large Language Model (Video‑LLM)  
- Token importance heuristics
