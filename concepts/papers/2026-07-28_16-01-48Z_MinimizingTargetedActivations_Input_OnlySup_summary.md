# Summary: 2026-07-28_16-01-48Z_MinimizingTargetedActivations_Input_OnlySuppressio.md
Saved: 2026-07-28 22:55
Source: 2026-07-28_16-01-48Z_MinimizingTargetedActivations_Input_OnlySuppressio.md
Model: None

---

## Summary  
The paper investigates an input‑only counterpart to activation steering: the ability to suppress a specific internal latent by optimizing only the prompt, without ever accessing the model’s inference weights. The target is an “evaluation‑awareness” latent that can be read and steered in prior work, and its suppression would undermine safety evaluations if it altered model behavior when the model detects being tested. By combining GCG‑style token optimization with a self‑cross‑entropy fluency regularizer (Fluent Dreaming/EPO), the authors achieve robust suppression of five distinct latent constructions—including a CAA direction, an SAE feature, and a single MLP neuron—on Llama‑3.2‑3B and Llama‑3.1‑8B models.  

## Key Contributions  
- **Finding 1:** Input‑only optimization can drive the evaluation‑awareness latent to near‑zero (z≈‑7) while preserving overall fluency through a negated feature term and a self‑cross‑entropy regularizer.  
- **Finding 2:** The suppression is robust, but the CAA direction behaves like a placebo: it is suppressed as hard as a random direction and causes behavior shifts comparable to those of genuine steering, indicating that activation‑readability does not imply behavioral controllability.  
- **Finding 3:** A single MLP neuron is correlated with evaluation judgments at both scales, yet it is not causally responsible; scanning the real Pile corpus yields a natural‑text baseline that competes well with the optimizer for controlling the internal direction.  

## Methodology  
The authors employ activation steering techniques that operate solely on the input side. They use Fluent Dreaming/EPO as a base, inserting a negated feature term and sweeping a fluency weight to balance suppression against output quality. The optimization is performed by modifying only the prompt tokens; no inference‑time access to model weights or activations is allowed. This approach enables the study of how prompt engineering can influence hidden representations without compromising model integrity.  

## Results  
Latent values are reduced to approximately –7, a strong suppression level. When the CAA direction is targeted, its suppression mirrors that of a random direction, and the model’s behavior changes only marginally, suggesting the effect is largely epistemic rather than causal. Including a real evaluation passage in context while optimizing only a prefix leads to an unexpected increase in the model’s evaluation judgment, highlighting the fragility of safety assessments when latent steering is applied. The single MLP neuron shows strong correlation with evaluation scores but no causal link; using the Pile corpus as a baseline yields performance on par with the optimizer for controlling that direction. A positive control validates an erasure detector, leaving open whether suppression constitutes erasure or rotation.  

## Significance  
The work demonstrates that activation‑readability does not guarantee behavioral controllability, raising concerns about the reliability of safety evaluations that rely on latent manipulation. Robust input‑only suppression can be achieved with minimal impact on model output quality, offering a powerful tool for probing internal representations while preserving utility. However, the findings caution against assuming that steering a specific latent will reliably change observable behavior, which is crucial for trustworthy AI safety testing.  

## Related Concepts  
Activation steering, Fluent Dreaming/EPO, GCG token optimization, self‑cross‑entropy fluency regularizer, evaluation‑awareness latent, CAA direction, SAE feature, MLP neuron, erasure detector, activation‑readability vs controllability.
