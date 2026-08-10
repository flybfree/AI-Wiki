# Summary: 2026-08-04_DeepSeekV4FlashonaSingleAMDMI300X.md
Saved: 2026-08-04 09:01
Source: 2026-08-04_DeepSeekV4FlashonaSingleAMDMI300X.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
The article describes a production‑grade setup that runs DeepSeek V4‑Flash‑0731 on a single AMD MI300X using the vLLM ROCm nightly stack with custom patches. The configuration achieves up to 8.5 K tokens per second in prefill and 168 tokens/s for decode, handling 2–8 concurrent streams and bursts of 64 streams without OOM or engine errors. All model weights (≈157 GiB) reside in HBM3 with no additional quantization or off‑load.

## Semantic links
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson4_AgentFrameworks.md|Lesson 4 — Agent Frameworks: The Loop Engine]] — 2 title terms overlap, 3 topic terms overlap, same area: home
- [[concepts/ai-foundations/ai-ml-foundations-lesson-14-choosing-the-right-architecture-for-the-task.md|AI/ML Foundations Lesson 14 - Choosing the Right Architecture for the Task]] — 2 title terms overlap, 3 topic terms overlap, same area: home
- [[concepts/llm-models/OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 2 title terms overlap, 2 topic terms overlap, same area: home

## Key Takeaways  
- [The entire 304 B checkpoint fits entirely within the MI300X’s 192 GB HBM3, eliminating PCIe streaming and layer off‑load.]  
- [Correctness of AMD/Graphcore FP8 implementation is paramount; a kernel that assumes OCP semantics can be wrong by a factor of two in scale.]  
- [Custom ROCm kernels for gfx942 shapes and an OGS geometry override are required to achieve peak performance on this GPU architecture.]

## Context  
The MI300X (CDNA3) offers 192 GB HBM3 and 5.3 TB/s memory bandwidth, roughly double that of the H100 SXM5. While AMD’s newer GPUs such as MI325X/MI355X support OCP‑standard FP8, the MI300X uses a Graphcore‑based variant (E4M3) that demands special handling. The official vLLM recipe targets NVIDIA hardware and newer AMD cards with 4K context, leaving the single‑GPU case for 0731 unaddressed.

## Implications  
This configuration demonstrates that large language models can be served cost‑effectively on a single high‑memory GPU, potentially reshaping cloud AI pricing. It also highlights the need for architecture‑specific kernel tuning and correctness fixes when deploying state‑of‑the‑art models on heterogeneous hardware, encouraging broader adoption of AMD’s MI300X in production inference pipelines.
