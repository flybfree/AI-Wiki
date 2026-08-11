# Summary: 2026-07-28_17-59-31Z_π_mathbf_R__2__ReactiveReal_timeFlowPolicies.md
Saved: 2026-07-28 23:03
Source: 2026-07-28_17-59-31Z_π_mathbf_R__2__ReactiveReal_timeFlowPolicies.md
Model: None

---

## Summary  
Generalist manipulation policies built from large pretrained backbones suffer from latency because their perception‑to‑action pipeline cannot react to sensory input that arrives mid‑execution, limiting closed‑loop control. The authors introduce **πR²**, a framework that makes these flow policies reactive and real‑time while preserving expressive multi‑modal capabilities. πR² achieves this by decoupling conditioning into a fast proprioceptive channel and a slower vision‑language channel, and by treating in‑flight actions as inpainting conditions within a latency‑adaptive flow schedule. The method can be fine‑tuned from existing pretrained policies with minimal architectural changes.

## Semantic links
- [[concepts/papers/2026-08-04_00-24-06Z_TQLite_Multi_LLMJuryGuidedDistillationforRe_summary.md|Summary: 2026-08-04_00-24-06Z_TQLite_Multi_LLMJuryGuidedDistillationforReal_time.md]] — 4 title terms overlap; 9 summary/topic terms overlap; semantic match 0.04
- [[concepts/papers/2026-07-21_17-13-49Z_Real_timeoptimalcontrolwithshallowrecurrent_summary.md|Summary: 2026-07-21_17-13-49Z_Real_timeoptimalcontrolwithshallowrecurrentdecoder.md]] — 3 title terms overlap; 14 summary/topic terms overlap; semantic match 0.12

## Key Contributions  
- [Finding 1] Splits conditioning into a fast proprioception stream (updated every tick) and a slower vision‑language stream, enabling reactions to fresh proprioceptive data within each action chunk while tolerating stale visual features.  
- [Finding 2] Implements a latency‑adaptive flow schedule that treats in‑flight actions as inpainting conditioning, emitting one denoising step per call so the policy can adapt to varying hardware latencies.  
- [Finding 3] Provides a minimal‑modification fine‑tuning path from pretrained policies (e.g., GR00T‑N1.7) that retains multi‑action prediction and large‑backbone expressiveness.

## Methodology  
The authors leverage the per‑position noise schedule of diffusion forcing to structure their policy’s conditioning pipeline. By separating fast and slow conditioning streams, each chunk can be processed with a single denoising step corresponding to one latency tick, eliminating the need for repeated replanning. The flow schedule is designed to accept in‑flight actions as conditioning inputs, allowing the model to emit new actions on demand without waiting for full denoising cycles.

## Results  
On an xArm6+XHand platform equipped with an A5000 GPU, πR² replans closed‑loop at roughly 25 Hz, four times faster than the baseline (~10 Hz). Across both simulation and real‑world manipulation tasks, the method improves success rates by up to 23 % in simulation and 30 % over the strongest baseline. These gains demonstrate that latency‑aware conditioning can be integrated into large flow policies without sacrificing performance.

## Significance  
πR² bridges the gap between expressive deep‑learning manipulation policies and real‑time closed‑loop control, showing that large backbones need not be sacrificed for reactivity. By reducing replanning frequency and enabling per‑tick actuation, it opens the door to higher‑rate, safer robotic interactions in both simulated and physical environments.

## Related Concepts  
- Flow policy  
- Diffusion forcing noise schedule  
- Latency adaptation  
- Inpainting conditioning  
- Proprioception channel  
- Vision‑language features  
- Multi‑modal policy  
- Action chunking
