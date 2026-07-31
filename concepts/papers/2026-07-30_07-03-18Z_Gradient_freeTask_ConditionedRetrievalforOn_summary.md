# Summary: 2026-07-30_07-03-18Z_Gradient_freeTask_ConditionedRetrievalforOn_Device.md
Saved: 2026-07-30 20:28
Source: 2026-07-30_07-03-18Z_Gradient_freeTask_ConditionedRetrievalforOn_Device.md
Model: None

---

## Summary  
The paper tackles the challenge of on‑device in‑context learning (ICL) by introducing a gradient‑free retrieval mechanism that selects task‑specific demonstrations from local memory while respecting strict computation, memory, and data‑exposure budgets. Its core contribution is Conditional Retrieval Alignment (CoRA), which converts a frozen encoder into a task‑conditioned retriever using only paired candidate inputs and outputs without any fine‑tuning or back‑propagation. CoRA leverages closed‑form ridge regression to align query representations with an output‑derived conditioning space, then compresses the fitted representation via low‑rank factorization for efficient offline index construction. The framework also extends to multimodal exemplar retrieval by incorporating visual features into both conditioning and retrieval spaces.

## Key Contributions  
- Gradient‑free task‑conditioned retrieval that operates without fine‑tuning, backpropagation, or calls to the target model.  
- An exact low‑rank compression of the output‑conditioned fitted representation using a two‑pass streaming construction that never materializes the full matrix.  
- A multimodal extension that jointly conditions and retrieves on visual exemplars alongside textual data.

## Methodology  
CoRA begins by pairing candidate input–output tuples from a frozen encoder. From these pairs it builds an output‑derived conditioning space, then computes the optimal alignment between query inputs and this space via closed‑form ridge regression. The fitted representation is factorized into a low‑rank basis that is constructed in two streaming passes: one to compute the rank‑constrained coefficients offline, and another to produce a compact index used only at query time. Query retrieval therefore requires only the precomputed index and the current input; no additional gradients or model updates are needed.

## Results  
Experiments on ten textual datasets and four multimodal benchmarks (Llama‑3.2‑1B, MobileLLM‑Pro, OpenFlamingo‑3B, Qwen3.5‑2B) show that CoRA achieves state‑of‑the‑art task‑conditioned retrieval performance while using far less memory than full fine‑tuned retrievers. The framework runs end‑to‑end on a Raspberry Pi 5, confirming its feasibility for truly on‑device deployment without requiring target‑model calls or gradient computation.

## Significance  
CoRA enables effective in‑context learning at the edge with minimal computational overhead, opening the door to scalable, privacy‑preserving AI that can adapt to new tasks instantly. By avoiding any form of fine‑tuning and supporting both single‑modal and multimodal retrieval, it addresses a critical bottleneck for real‑world on‑device LLMs.

## Related Concepts  
in‑context learning, retrieval‑based prompting, gradient‑free optimization, ridge regression, low‑rank compression, streaming construction, frozen encoder, task‑conditioned retrieval, multimodal conditioning.
