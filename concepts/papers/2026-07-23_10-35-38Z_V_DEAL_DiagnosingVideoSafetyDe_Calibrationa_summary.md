# Summary: 2026-07-23_10-35-38Z_V_DEAL_DiagnosingVideoSafetyDe_CalibrationasanUnde.md
Saved: 2026-07-24 02:38
Source: 2026-07-23_10-35-38Z_V_DEAL_DiagnosingVideoSafetyDe_CalibrationasanUnde.md
Model: None

---

## Summary  
The paper V‑DEAL investigates why Video Large Language Models (VLLMs) are vulnerable to prompt‑injection attacks when harmful videos are paired with benign queries, achieving higher success rates than expected. It proposes a three‑level diagnostic framework that jointly examines model perception, internal refusal mechanisms, and hidden representations to pinpoint the failure as an understanding‑refusal coupling breakdown.

## Key Contributions  
- Finding 1: Models correctly detect harmful video content (>81% accuracy) but still allow attacks when paired with benign queries.  
- Finding 2: Hidden‑state analysis reveals that visual understanding activates a weaker refusal tendency than textual understanding, indicating misaligned internal signals.  
- Finding 3: A prompt‑injection intervention reduces attack success rates by ~48.24 percentage points, matching fine‑tuning approaches.

## Methodology  
The authors employ a three‑level diagnostic framework: (1) perception layer analysis to confirm detection accuracy; (2) quantitative measurement of refusal propensity via internal state extraction; and (3) hidden‑state probing to compare activation patterns between visual and textual modalities. They test six VLLMs on three public benchmarks, applying the framework sequentially.

## Results  
Across experiments, the average attack success rate under benign‑query pairing is 48.33%, while detection accuracy exceeds 81%. Hidden‑state analysis shows lower refusal activation for visual inputs. The intervention method reduces success rates to ~0.09% (comparable to fine‑tuning). Statistical significance is confirmed across all models.

## Significance  
This work uncovers a previously unnoticed coupling failure between understanding and refusal, offering diagnostic tools and practical mitigation strategies that improve safety alignment without heavy retraining. By isolating the specific interaction between visual perception and internal refusal signals, V‑DEAL enables targeted fixes rather than broad model overhauls.

## Related Concepts  
- Video Large Language Models (VLLMs)  
- Prompt injection attacks  
- Understanding‑refusal coupling  
- Hidden‑state analysis  
- Visual vs. textual modality interaction  
- Safety alignment  
- Detection accuracy  
- Internal representation  
- Fine‑tuning interventions
