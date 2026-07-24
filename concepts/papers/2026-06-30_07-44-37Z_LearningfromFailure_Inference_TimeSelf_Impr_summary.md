# Summary: 2026-06-30_07-44-37Z_LearningfromFailure_Inference_TimeSelf_Improvement.md
Saved: 2026-07-23 23:36
Source: 2026-06-30_07-44-37Z_LearningfromFailure_Inference_TimeSelf_Improvement.md
Model: None

---

## Summary  
The paper proposes a failure‑driven self‑improvement loop for computer‑use agents that leverages multimodal large language models (MLLMs) to turn discarded failed trajectories into actionable upgrades. By diagnosing why an agent fails, generating inference‑time solutions and lightly verified code patches, the method complements traditional success‑based fine‑tuning without incurring extra training cost or substantial latency. The approach is evaluated on the OSWorld benchmark using the state‑of‑the‑art OpenCUA‑72B model, raising its success rate from 42.3 % to 48.9 %, a gain of six and a half percentage points.

## Key Contributions  
- [Finding 1] A failure‑centric self‑improvement pipeline that extracts valuable information from unsuccessful agent runs.  
- [Finding 2] An LLM‑driven diagnostic system capable of identifying failure modes, proposing inference‑time fixes, and creating verifiable code patches.  
- [Finding 3] Demonstrated improvement on OSWorld with OpenCUA‑72B, achieving a 6.6 percentage‑point boost in task success without additional training.

## Methodology  
The authors place the agent in a verifiable environment where it attempts tasks and records both successful and failed trajectories. The failure data are fed to an LLM that classifies the failure mode (e.g., misinterpreted UI element, incorrect command). Based on this diagnosis, the model proposes an inference‑time solution—often a small code patch—and generates human‑lightly verified patches that can be applied directly during inference. This loop repeats iteratively: each new patch is tested, and any remaining failures are again diagnosed and patched.

## Results  
Experiments on OSWorld show the failure‑driven pipeline raises overall success from 42.3 % to 48.9 %, a relative improvement of about 16 %. The method adds negligible inference overhead because patches are applied at runtime rather than during offline training, and it requires no extra labeled data or additional GPU time for fine‑tuning.

## Significance  
By repurposing the often‑discarded failures that expose model weaknesses, this approach makes self‑improvement more efficient and scalable. It reduces reliance on costly human‑annotated success trajectories while still delivering measurable gains in agent performance, opening a path toward continual learning without large retraining budgets.

## Related Concepts  
- Computer‑use agents (e.g., OpenCUA)  
- Multimodal Large Language Models (MLLMs)  
- Self‑improving loops and reinforcement learning from human feedback  
- Inference‑time code generation and patching  
- Failure analysis in machine learning pipelines
