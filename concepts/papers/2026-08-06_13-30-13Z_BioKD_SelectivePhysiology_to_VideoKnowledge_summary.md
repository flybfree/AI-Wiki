# Summary: 2026-08-06_13-30-13Z_BioKD_SelectivePhysiology_to_VideoKnowledgeDistill.md
Saved: 2026-08-06 22:17
Source: 2026-08-06_13-30-13Z_BioKD_SelectivePhysiology_to_VideoKnowledgeDistill.md
Model: None

---

## Summary  
BioKD addresses the challenge of video-based emotion recognition by leveraging physiological signals as a reliable, non-intrusive training signal while maintaining deployment simplicity through single-video inference. The framework introduces a reliability-aware distillation mechanism that selectively transfers knowledge from noisy physiological teacher supervision to a video-only student model, mitigating errors caused by inter-subject variability and temporal inconsistencies. By integrating progressive distillation with a sample-wise gating strategy, BioKD enhances cross-modal alignment without requiring multimodal synchronization or additional hardware at inference time.

## Key Contributions  
- [Finding 1] The reliability gate dynamically adjusts knowledge transfer strength based on physiological signal confidence, reducing negative transfer from unreliable teacher supervision.  
- [Finding 2] Progressive distillation enables stable learning by first aligning low-level video features before gradually incorporating higher-level affective representations guided by physiology.  
- [Finding 3] BioKD achieves superior performance in both trial-wise and subject-wise evaluation settings on DEAP and AMIGOS, outperforming baseline models that rely solely on video or use unreliable weighting strategies.

## Methodology  
BioKD operates within a video-only inference pipeline while using physiological signals—such as heart rate variability (HRV) and skin conductance—as auxiliary supervision during training. The reliability gate evaluates each sample’s physiological signal quality by detecting anomalies, temporal drift, or inter-subject differences, assigning lower weight to samples with poor signal consistency. Knowledge distillation proceeds in stages: initial video-to-video alignment is followed by cross-modal refinement where reliable physiological cues selectively influence the student model’s affective embeddings. This progressive approach ensures that only high-confidence teacher signals contribute to learning.

## Results  
BioKD consistently outperforms baseline models on both DEAP and AMIGOS datasets, achieving 68.01% accuracy in trial-wise arousal recognition and 65.29% under subject-wise evaluation—demonstrating robustness across diverse individuals. Compared to entropy-only weighting strategies, BioKD reduces overconfidence from teacher errors by suppressing low-confidence physiological inputs. Critically, BioKD incurs no additional inference-time overhead relative to the video student model and eliminates the need for physiological sensors or synchronized data streams.

## Significance  
This work advances emotion recognition systems toward more reliable, deployable solutions by decoupling training from real-world sensing constraints. By making teacher supervision more robust through reliability modeling, BioKD enables high-accuracy affective analysis without compromising privacy or accessibility. The framework’s efficiency and effectiveness position it as a scalable alternative to multimodal approaches in applications requiring continuous video-only operation.

## Related Concepts  
Knowledge distillation, physiological signal processing, cross-modal learning, reliability gating, progressive training, emotion recognition, affective computing, DEAP dataset, AMIGOS dataset.
