# Summary: 2026-08-01_08-43-26Z_UnleashingthePowerofText_Text_GuidedFlowMatchingfo.md
Saved: 2026-08-03 21:26
Source: 2026-08-01_08-43-26Z_UnleashingthePowerofText_Text_GuidedFlowMatchingfo.md
Model: None

---

## Summary  
The paper tackles infrared‑visible image fusion under realistic degradation conditions, where only a limited amount of modality‑specific information is available from the corrupted inputs. Existing approaches inject fixed global text representations into visual features, which cannot adapt to spatially varying degradations or local structures. To overcome this limitation, we propose TGFusion, a text‑guided latent‑space flow matching framework that unifies degradation suppression with cross‑modal fusion using structured prompts. Our contribution is a Prompt‑conditioned Multi‑stream Joint Flow Transformer that treats text as an independent semantic stream and enables token‑level bidirectional interaction among visual, infrared, and textual streams.

## Key Contributions  
- [Finding 1] Provide a unified framework for degradation suppression and cross‑modal fusion guided by structured text prompts.  
- [Finding 2] Introduce a Prompt‑conditioned Multi‑stream Joint Flow Transformer that represents text as an independent semantic stream with token‑level bidirectional attention.  
- [Finding 3] Achieve superior perceptual quality, image naturalness, structural‑detail preservation, and infrared‑saliency retention across diverse single and compound degradations.

## Methodology  
The authors encode task, degradation, and generation cues into structured prompts that serve as conditioning signals for the fusion process. They design a joint flow transformer architecture that processes three streams simultaneously: visible, infrared, and text. Joint attention mechanisms allow token‑level bidirectional interaction between these streams, while layer‑wise updating enables dynamic selection of reliable information from each modality and guided generation of the fused latent representation.

## Results  
Experiments on public benchmarks and extensive testing under complex degradation scenarios demonstrate that TGFusion outperforms prior methods in perceptual quality, naturalness, structural‑detail preservation, and infrared‑saliency retention. The model remains robust across a wide range of single and compound degradations, showing consistent improvements over baseline approaches.

## Significance  
This work matters because it enables reliable image fusion when only limited, degraded information is available, allowing text to act as a prior that guides both information selection and latent generation. By integrating textual guidance with flow‑based fusion in a multi‑stream transformer, the method opens new possibilities for applications such as medical imaging, remote sensing, and augmented reality where degradation is inevitable.

## Related Concepts  
latent‑space flow matching, multi‑stream joint flow transformer, prompt conditioning, token‑level bidirectional attention, degradation suppression, cross‑modal fusion, infrared‑saliency retention.
