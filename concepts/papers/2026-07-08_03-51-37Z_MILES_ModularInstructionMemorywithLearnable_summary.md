# Summary: 2026-07-08_03-51-37Z_MILES_ModularInstructionMemorywithLearnableSelecti.md
Saved: 2026-07-23 23:37
Source: 2026-07-08_03-51-37Z_MILES_ModularInstructionMemorywithLearnableSelecti.md
Model: None

---

## Summary  
The paper proposes **MILES**, a framework that enables large language models to improve their reasoning by dynamically expanding and selecting modular memory units during test‑time execution. By treating each problem as a sequence of sub‑goals, MILES stores asymmetric pairs of embeddings and instructions in a modular structure, allowing the model to collect supervision from confident samples while handling uncertain ones with learned selection heads. The coarse level expands memory and trains these heads, whereas the fine stage applies them to rerank candidates and guide final reasoning. This approach yields a self‑improving LLM that can adapt without requiring large labeled datasets or fixed action spaces.

## Key Contributions  
- **Finding 1:** MILES introduces modular instruction memory units composed of asymmetric sub‑goal embeddings paired with sub‑instructions, each linked to a learnable selection head.  
- **Finding 2:** The framework employs a correctness‑optimized selection mechanism that learns from confident test samples and applies it to rerank uncertain candidates in a coarse‑to‑fine retrieval process.  
- **Finding 3:** MILES achieves superior accuracy‑efficiency tradeoffs, consistently matching or surpassing prior methods while operating under realistic incremental memory expansion.

## Methodology  
MILES maintains a dynamic memory that grows step‑wise as new problems are encountered. Each step creates a modular unit containing an embedding of the sub‑goal and its corresponding instruction; these units are stored asymmetrically to preserve order information. A learnable selection head is trained on confident samples collected at the coarse level, enabling it to rank candidate memories for both certain and uncertain reasoning tasks. During inference, the model first uses the coarse memory expansion strategy to gather supervision, then applies the fine‑tuned heads to rerank candidates and steer the LLM toward a correct final answer.

## Results  
Extensive experiments across multiple benchmark datasets show that MILES consistently matches or exceeds prior state‑of‑the‑art methods in reasoning accuracy while using fewer memory resources. The framework demonstrates robust performance under test‑time constraints, with improved efficiency measured by lower latency and reduced token consumption. Moreover, MILES transfers well to novel problem sets, indicating strong generalization.

## Significance  
MILES addresses a critical limitation of existing memory‑based LLMs: reliance on large labeled corpora and fixed action spaces that hinder real‑world deployment. By enabling incremental, correctness‑driven memory expansion and selection, the model can improve reasoning autonomously during inference, offering a path toward truly self‑improving AI systems without extensive pre‑training.

## Related Concepts  
- Memory‑based retrieval  
- Modular architecture  
- Selection head (learnable policy)  
- Coarse‑to‑fine learning  
- Sub‑goal embeddings and instructions  
- Test‑time adaptation  
- Instruction memory
