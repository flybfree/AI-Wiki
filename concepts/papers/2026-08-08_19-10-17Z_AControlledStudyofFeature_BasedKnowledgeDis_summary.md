# Summary: 2026-08-08_19-10-17Z_AControlledStudyofFeature_BasedKnowledgeDistillati.md
Saved: 2026-08-10 23:06
Source: 2026-08-08_19-10-17Z_AControlledStudyofFeature_BasedKnowledgeDistillati.md
Model: None

---

## Summary  
The paper investigates how feature‑based knowledge distillation affects student performance relative to logit‑based distillation, using CIFAR‑100 and a ResNet‑50 teacher across three student architectures (a CustomResNet width sweep, MobileNetV2, and a depth‑w=48 variant). It compares three methods—logit‑KD, Attention Transfer, and FitNets—under identical training conditions to determine which yields the greatest improvement. The study finds that while logit‑KD consistently boosts accuracy, some feature methods either show no clear benefit or even degrade performance depending on student size and depth, and a fixed auxiliary coefficient produces non‑uniform gradient scales across students.

## Key Contributions  
- [Finding 1] Logit knowledge distillation uniformly improves student accuracy over scratch baselines across all tested designs.  
- [Finding 2] Attention Transfer shows no consistent positive effect within the CustomResNet width family but has a net negative average impact there while being positive for MobileNetV2.  
- [Finding 3] FitNets consistently underperforms logit KD in every paired run, with larger gaps for wider students and an exception at depth w=48.

## Methodology  
The authors conduct a controlled experiment where each student model is trained using three distillation methods (logit‑KD, Attention Transfer, FitNets) on the same teacher (ResNet‑50), optimizer settings, learning‑rate schedule, batch size, and random seed. Feature‑based methods share auxiliary coefficients with the teacher’s forward pass, ensuring a matched training condition. The comparison runs are repeated across multiple seeds to assess variance, and student accuracy at test time is evaluated alongside improvement over a scratch baseline.

## Results  
Logit KD yields consistent gains (average +2.1 % accuracy). Attention Transfer improves MobileNetV2 (+0.8 %) but reduces CustomResNet performance by ~0.5 %. FitNets never surpasses logit KD, with an average gap of 1.3 % and widening for w=64/96 students; only at depth w=48 the gap narrows to 0.7 %. Gradient‑scale analysis shows that a fixed coefficient produces varying gradient magnitudes across student architectures.

## Significance  
This work clarifies that feature‑based distillation is not universally superior, highlighting design‑specific trade‑offs and underscoring the importance of matching teacher‑student gradients for stable training in knowledge distillation pipelines.

## Related Concepts  
- Knowledge Distillation  
- Logit Kernel Distance  
- Attention Transfer  
- FitNets (feature‑wise regularization)  
- Cross‑design comparison  
- Gradient scaling  
- Student‑teacher alignment
