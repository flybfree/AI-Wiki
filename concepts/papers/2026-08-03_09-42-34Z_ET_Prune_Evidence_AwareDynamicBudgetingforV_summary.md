# Summary: 2026-08-03_09-42-34Z_ET_Prune_Evidence_AwareDynamicBudgetingforVisualTo.md
Saved: 2026-08-03 23:51
Source: 2026-08-03_09-42-34Z_ET_Prune_Evidence_AwareDynamicBudgetingforVisualTo.md
Model: None

---

## Summary  
The paper introduces ET‑Prune, a training‑free framework for visual token pruning in text‑rich multimodal large language models that adapts the pruning budget based on evidence derived from the question context. It treats pruning as an evidence allocation problem, using decoder‑side partial query‑key blocks to identify relevant textual evidence and safeguarding spatial regions. By converting evidence uncertainty and density into a sample‑specific token floor, ET‑Prune dynamically allocates tokens across middle layers, preserving diffuse or text‑dense evidence while aggressively removing concentrated evidence. The method achieves state‑of‑the‑art performance on OCR benchmarks with roughly half the visual tokens retained.

## Key Contributions  
- [Finding 1] ET‑Prune casts pruning as an evidence allocation problem, using decoder‑side partial query‑key blocks to extract question‑conditioned evidence.  
- [Finding 2] It converts evidence uncertainty and density into a sample‑specific token floor that guides dynamic budgeting across middle layers.  
- [Finding 3] The framework achieves higher OCR accuracy than vanilla pruning while retaining only about half the visual tokens.

## Methodology  
The authors approach the problem by first extracting question‑conditioned evidence from the decoder’s partial query‑key block, which identifies text‑like spatial regions that are semantically relevant. They then compute a token floor based on uncertainty and density of this evidence to set a minimum token count per sample. Three progressive middle‑layer events sequentially allocate tokens: early stages retain diffuse evidence, mid stages prune concentrated evidence aggressively, and the final stage enforces the budget. The process is training‑free and operates deterministically in one pass.

## Results  
Experimental results show ET‑Prune outperforms all six backbone benchmarks at roughly 50 % visual‑token retention, achieving OCRBench‑v2 scores of +1.80 for Qwen3‑VL‑8B and +0.68 for InternVL3.5‑8B compared to strongest pruned baselines. On MMBench v1.1 it reaches 0.8467 circular exact‑matching accuracy versus 0.8437 for Vanilla at 54.45 % average visual‑token retention.

## Significance  
This work demonstrates that evidence‑aware dynamic budgeting can significantly improve inference efficiency without sacrificing critical information in text‑rich multimodal tasks, offering a scalable solution to the token allocation dilemma and highlighting the importance of context‑specific pruning strategies.

## Related Concepts  
visual token pruning, evidence allocation, decoder‑side partial query‑key blocks, token floor, dynamic budgeting, multimodal large language models (MLLMs), OCR benchmarks, circular exact‑matching accuracy.
