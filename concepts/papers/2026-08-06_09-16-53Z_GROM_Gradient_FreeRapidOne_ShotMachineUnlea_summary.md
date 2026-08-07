# Summary: 2026-08-06_09-16-53Z_GROM_Gradient_FreeRapidOne_ShotMachineUnlearning.md
Saved: 2026-08-06 22:10
Source: 2026-08-06_09-16-53Z_GROM_Gradient_FreeRapidOne_ShotMachineUnlearning.md
Model: None

---

## Summary  
The paper introduces GROM (Gradient‑Free Rapid One‑Shot Machine Unlearning), a method that removes targeted knowledge from large language models in a single forward pass without any iterative optimization or back‑propagation. By treating unlearning as a ridge‑regularized least‑squares problem, GROM derives an exact additive update to the model’s weight matrices that suppresses unwanted content while preserving retained behavior. The approach is both fast and robust against low‑bit quantization attacks that typically recover erased information in gradient‑based baselines.

## Key Contributions  
- [Finding 1] GROM provides a closed‑form, gradient‑free solution for one‑shot unlearning that requires no iterative optimization or back‑propagation.  
- [Finding 2] The method applies an exact additive weight edit to the targeted layer, forcing suppression of unwanted knowledge while strictly preserving behavior on retained data.  
- [Finding 3] GROM’s update is resilient to low‑bit quantization attacks that can recover unlearned content in conventional fine‑tuning approaches.

## Methodology  
The authors model the unlearning task as a ridge‑regularized least‑squares problem: minimize the squared error between the desired output and the current model output, subject to a regularization term on the target weight matrix. Because only forward passes are needed to compute the necessary statistics (e.g., activation patterns), the solution is obtained analytically via matrix inversion. The resulting update is additive—i.e., it adds a small correction to the original weights rather than overwriting them. This gradient‑free procedure eliminates the need for parameter‑efficient fine‑tuning such as LoRA, and the computation completes in seconds.

## Results  
GROM achieves state‑of‑the‑art forgetting‑utility trade‑offs on benchmark suites including TOFU‑5%, TOFU‑10%, MUSE‑Books, MUSE‑News, and WMDP. Compared to gradient‑based baselines, GROM reduces computational overhead by orders of magnitude while maintaining or improving utility scores. Crucially, the method’s weight edit is not merely masked; it actually removes the targeted content from the model’s parameters, which makes it immune to low‑bit quantization attacks that typically recover erased knowledge in fine‑tuned models.

## Significance  
GROM enables safe, privacy‑preserving removal of sensitive information from LLMs without costly fine‑tuning cycles. Its rapid, exact update makes it practical for real‑time or embedded systems where training time is a constraint. By guaranteeing that the unlearned knowledge is truly excised rather than hidden, GROM addresses a longstanding limitation of gradient‑based unlearning and opens new avenues for trustworthy AI.

## Related Concepts  
One‑shot machine unlearning, model forgetting, ridge regularization, least squares optimization, gradient‑free optimization, additive weight editing, low‑bit quantization attacks, LoRA (low‑rank adaptation), parameter‑efficient fine‑tuning.
