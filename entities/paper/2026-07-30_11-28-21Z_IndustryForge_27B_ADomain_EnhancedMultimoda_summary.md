# Summary: 2026-07-30_11-28-21Z_IndustryForge_27B_ADomain_EnhancedMultimodalFounda.md
Saved: 2026-07-30 20:34
Source: 2026-07-30_11-28-21Z_IndustryForge_27B_ADomain_EnhancedMultimodalFounda.md
Model: None

---

## Summary  
The paper introduces **IndustryForge‑27B**, a domain‑enhanced multimodal foundation model built on Qwen3.5‑VL‑27B to automate industrial CAD tasks ranging from single parts to full assemblies, including drawing interpretation, parametric script generation, and Windows COM API coding. By curating six specialized sub‑corpora that cover visual questions, code generation, and software operation, the authors create a unified multi‑task fine‑tuning recipe that yields significant gains over the base model while preserving general capabilities.

## Key Contributions  
- **Finding 1:** IndustryForge‑27B lifts the performance of Qwen3.5‑VL‑27B by an average of **+33.65 pp** across four CAD‑domain benchmarks, demonstrating strong domain adaptation.  
- **Finding 2:** The model outperforms the closed‑source state‑of‑the‑art GPT‑5.4 on all four benchmarks, showing that a fine‑tuned foundation can surpass proprietary systems in specialized industrial tasks.  
- **Finding 3:** Across eleven general‑capability benchmarks, IndustryForge‑27B retains and slightly improves the base model’s score (+1.56 pp mean) without catastrophic forgetting.

## Methodology  
The authors curated six industrial‑CAD sub‑corpora—CAD Visual QA (CAD‑VQA), parametric CAD code generation (text2cadquery), assembly‑level CAD code generation (text2cadquery‑assembly), and three COM API corpora for Inventor/SolidWorks (com_2d, com_3d, com_assembly)—collecting roughly 52 k multimodal samples. These were integrated into a single multi‑task supervised fine‑tuning pipeline on top of Qwen3.5‑VL‑27B, enabling the model to handle diverse calls from upper‑layer agents in one training recipe.

## Results  
On four CAD‑domain benchmarks, IndustryForge‑27B improves the base model by **+33.65 pp** on average and beats GPT‑5.4 on every task. On eleven general‑capability benchmarks it maintains performance with a **+1.56 pp** mean increase, indicating no loss of broad reasoning ability. The training also avoids catastrophic forgetting, preserving the model’s original capabilities.

## Significance  
IndustryForge‑27B provides a unified substrate for downstream industrial‑agent projects that span CAD design, software operation, parts‑to‑assembly workflows, single‑shot generation, and closed‑loop self‑improvement. By delivering strong domain performance while retaining general reasoning, it lowers the barrier to building full‑stack automated manufacturing agents.

## Related Concepts  
- Multimodal foundation models  
- Domain adaptation / fine‑tuning  
- Multi‑task supervised learning (SFT)  
- CAD visual QA (CAD‑VQA)  
- Parametric CAD code generation (text2cadquery, text2cadquery‑assembly)  
- Windows COM API integration (com_2d/com_3d/com_assembly)  
- Catastrophic forgetting mitigation
