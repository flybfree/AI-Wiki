# Summary: 2026-08-05_06-20-57Z_Energy_andMemory_EfficientPEFTMethodsforPersonaliz.md
Saved: 2026-08-05 20:30
Source: 2026-08-05_06-20-57Z_Energy_andMemory_EfficientPEFTMethodsforPersonaliz.md
Model: None

---

## Summary  
The paper investigates how parameter‑efficient fine‑tuning (PEFT) techniques can be used to personalize small language models on consumer GPUs while minimizing both energy consumption and memory usage. By benchmarking five PEFT methods—Full Fine‑Tuning, LoRA, LoRA+, QLoRA, and BitFit—across four SLMs from two architectures and multiple GLUE/LaMP tasks, the authors provide an energy‑first selection criterion that balances NetScore‑E (energy) and NetScore‑M (memory). The study demonstrates that LoRA+ dominates on energy efficiency, while QLoRA excels in VRAM reduction for Transformer models, highlighting a trade‑off between these constraints.

## Key Contributions  
- Finding 1: LoRA+ achieves the highest NetScore‑E in 19 of 24 configurations and is selected as the optimal method in 18 of 24 cases.  
- Finding 2: QLoRA cuts peak finetuning VRAM by up to 3.9× for Transformer models, giving it the best NetScore‑M in five Transformer configurations, though its de‑quantization overhead limits selection in most cases.  
- Finding 3: BitFit and full fine‑tuning are rarely competitive on either NetScore‑E or NetScore‑M; TinyLlama‑1.1B leads energy‑focused metrics on five benchmarks.

## Methodology  
The authors systematically compare the five PEFT methods across four SLMs (TinyLlama‑1.1B, Qwen3‑1.7B, Mamba‑1.4B, Mamba‑2‑1.3B) using three GLUE tasks and three LaMP personalization tasks. For each configuration they compute NetScore‑E and NetScore‑M, applying a strict rule: the method with the highest NetScore‑E is preferred; ties are resolved by higher NetScore‑M. This energy‑first approach ensures that memory constraints only act as secondary criteria.

## Results  
LoRA+ dominates on energy efficiency, attaining the top NetScore‑E in 19/24 settings and being selected in 18/24 overall. QLoRA, limited to Transformer models, reduces VRAM by up to 3.9× but suffers from de‑quantization overhead; it wins NetScore‑M in five Transformer configurations yet is only selected once energy dominates. BitFit and full fine‑tuning are consistently sub‑optimal across all metrics. TinyLlama‑1.1B leads both NetScore‑E on five benchmarks and NetScore‑M on four, underscoring its suitability for constrained devices.

## Significance  
These findings provide a practical, energy‑aware pathway to personalized on‑device deployment of small language models, showing that compact architectures combined with PEFT can meet real‑world constraints. By quantifying the impact of each method under both energy and memory lenses, the work guides developers toward the most efficient configuration for consumer hardware.

## Related Concepts  
- Parameter‑Efficient Fine‑Tuning (PEFT)  
- LoRA+, QLoRA, BitFit fine‑tuning strategies  
- NetScore‑E (energy‑focused evaluation metric) and NetScore‑M (memory‑focused evaluation metric)  
- VRAM constraints on consumer GPUs  
- Personalization tasks such as LaMP‑1/2/3  
- Small Language Models (SLMs) and their trade‑offs between size, performance, and resource usage.
