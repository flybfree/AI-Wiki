# Summary: 2026-08-07_10-16-56Z_DocMemo_DynamicEvidenceDiscoveryviaProbabilisticMe.md
Saved: 2026-08-09 22:53
Source: 2026-08-07_10-16-56Z_DocMemo_DynamicEvidenceDiscoveryviaProbabilisticMe.md
Model: None

---

## Summary  
Long‑document understanding requires locating sparse, heterogeneous evidence across many pages while avoiding the fragility of static retrieval. The authors introduce DocMemo, a memory‑guided framework that treats reasoning as a dynamic exploration process rather than a fixed top‑k selection. By maintaining three levels of memory—Document Schema Memory, Page Belief Memory, and Question Episodic Memory—the system continuously updates page relevance through Bayesian updating with Thompson sampling, spatial proximity propagation, and structure‑aware evidence access. Experiments on three benchmarks demonstrate that this approach yields state‑of‑the‑art performance.

## Key Contributions  
- [Finding 1] The tri‑level memory architecture (schema, belief, episodic) enables systematic tracking of cross‑round page relevance.  
- [Finding 2] Thompson sampling coupled with Bayesian belief updating provides a principled mechanism for adaptive evidence discovery.  
- [Finding 3] Structural propagation and fine‑grained visual region integration improve robustness to early retrieval errors.

## Methodology  
DocMemo formulates long‑document reasoning as a dynamic evidence exploration problem. The framework maintains three memory components: Document Schema Memory stores structural priors, Page Belief Memory holds probabilistic relevance estimates for each page, and Question Episodic Memory records the evolving reasoning trajectory. During inference, the system updates these beliefs via Thompson sampling, propagates spatial proximity information to guide neighbor selection, and accesses evidence with adaptive granularity that respects document structure while incorporating fine‑grained visual regions.

## Results  
On three benchmark datasets—DocQA, Multi‑Modal QA, and Long‑Document Retrieval—the proposed DocMemo achieves higher F1 scores than prior state‑of‑the‑art methods. The improvement is attributed to the dynamic belief updating that recovers from early retrieval mistakes and better leverages multimodal evidence.

## Significance  
DocMemo addresses a critical limitation of existing long‑document systems: static, error‑prone retrieval that cannot adapt after initial mistakes. By integrating structured memory and probabilistic reasoning, it offers a scalable solution for real‑world applications where locating relevant evidence across hundreds of pages is essential.

## Related Concepts  
- Dynamic evidence discovery  
- Probabilistic memory‑guided retrieval  
- Thompson sampling in belief updating  
- Cross‑round state propagation  
- Structural awareness in document understanding
