# Summary: 2026-07-29_14-15-55Z_ProgressiveMultimodalAlignmentforContinualInstruct.md
Saved: 2026-07-29 20:35
Source: 2026-07-29_14-15-55Z_ProgressiveMultimodalAlignmentforContinualInstruct.md
Model: None

---

## Summary  
The paper addresses projector‑level forgetting in Multimodal Continual Instruction Tuning (MCIT), where visual distributions shift and instruction semantics evolve, causing the shared alignment projector to drift. To mitigate this, they propose Progressive Multimodal Alignment (PMA), a framework that adaptively expands projector experts only when needed while retaining the original pretrained projector as an anchor. PMA uses a lightweight descriptor to detect distribution shifts and an expandable router to integrate expert outputs, achieving sub‑linear parameter growth. The method is designed as a method‑agnostic add‑on that works across various MLLM backbones.  

## Key Contributions  
- [Finding 1] PMA identifies multimodal distribution shifts via a lightweight representation descriptor and prevents projector forgetting.  
- [Finding 2] It progressively expands projector experts only when necessary, preserving previously learned alignment.  
- [Finding 3] The approach achieves sub‑linear parameter growth and is method‑agnostic across MLLM backbones.  

## Methodology  
The authors treat the projector as a trainable component that can be incrementally updated. First, they compute a lightweight descriptor from multimodal features to detect shifts; when a shift is detected, an expandable router triggers the addition of new expert modules while the original pretrained projector remains active as a stable anchor. This progressive mechanism balances stability and plasticity while limiting parameter overhead.  

## Results  
Experiments on two recent MCIT benchmarks show that PMA mitigates projector‑level forgetting, yielding consistent gains over prior state‑of‑the‑art methods when combined with PMA. Moreover, the framework scales across diverse MLLM backbones, demonstrating robust performance without significant extra compute or memory.  

## Significance  
By addressing a previously overlooked issue of projector forgetting, PMA improves continual instruction tuning reliability and adaptability. Its sub‑linear parameter growth makes it practical for deployment in resource‑constrained settings, and its method‑agnostic design encourages broader adoption across the MLLM community.  

## Related Concepts  
Projector‑level forgetting, Multimodal Continual Instruction Tuning (MCIT), projector experts, lightweight representation descriptor, expandable router, sub‑linear parameter growth, method‑agnostic add‑on, alignment anchor.
