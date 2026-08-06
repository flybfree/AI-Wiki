# Summary: 2026-08-05_06-49-49Z_CARVE_Cross_SliceAnisotropicReallocationofVisualEv.md
Saved: 2026-08-05 20:31
Source: 2026-08-05_06-49-49Z_CARVE_Cross_SliceAnisotropicReallocationofVisualEv.md
Model: None

---

## Summary  
The paper introduces CARVE, a training‑free compression framework that reduces the visual token budget in slice‑based 3D medical language models without sacrificing performance. By reallocating tokens across depth slices according to cross‑slice evidence density, CARVE creates a more efficient visual representation than simply enlarging the token count or applying generic 2D/ video‑style compressions. The approach treats token reduction as a budget‑constrained 2.5‑dimensional allocation problem, enabling selective retention of high‑value evidence while discarding redundant slices. This selective reallocation yields significant gains across multiple medical VQA benchmarks.

## Key Contributions  
- [Finding 1] Slice‑wise token budgets exhibit diminishing returns; improving in‑plane resolution is more effective than adding more slices at comparable computational cost.  
- [Finding 2] CARVE partitions the depth axis into coherent windows and allocates tokens non‑uniformly based on normalized cross‑slice evidence, constructing spatial anchors that retrieve locally varying evidence from the full volume.  
- [Finding 3] Under an 80 % token reduction on Hulu‑Med‑7B, CARVE outperforms all compression baselines on AMOS‑MM report‑generation metrics, achieving a 6.2‑point higher retention of full‑token quality and preserving 98.1 % of performance across three VQA benchmarks.

## Methodology  
CARVE treats visual token reduction as a budget‑constrained allocation problem in 2.5 dimensions (slices × rows × columns). First, the depth axis is divided into windows that capture coherent visual contexts. For each window, a set of spatial anchors is selected on representative slices; these anchors serve as high‑value tokens. The framework then retrieves evidence from adjacent slices and merges it into the nearest anchor within the same window, effectively compressing redundant or low‑information tokens while preserving essential information. This process is performed without retraining any encoder or decoder, making CARVE a training‑free inference‑time compression method.

## Results  
Experiments on Hulu‑Med‑7B and two additional 3D medical VQA datasets demonstrate that CARVE removes roughly 80 % of visual tokens while maintaining high performance. The model achieves the highest scores across all AMOS‑MM report‑generation metrics, with a 6.2‑point advantage over the strongest baseline. Moreover, full‑token quality is retained at 98.1 % on three VQA benchmarks, confirming that token compression does not degrade downstream reasoning ability.

## Significance  
CARVE addresses a critical bottleneck in slice‑based 3D medical language models: excessive visual tokens inflate computational load without proportional gains in understanding. By reallocating tokens based on cross‑slice evidence density, CARVE offers a scalable, training‑free solution that can be applied to any existing model architecture. This not only reduces inference latency and memory usage but also enables more efficient deployment of 3D medical AI systems in clinical settings.

## Related Concepts  
- Slice‑based MLLMs (multimodal language models)  
- Visual token budgeting and compression  
- Cross‑slice evidence density  
- Budget‑constrained allocation problems  
- 2.5‑dimensional representation  
- Spatial anchors in volumetric data
