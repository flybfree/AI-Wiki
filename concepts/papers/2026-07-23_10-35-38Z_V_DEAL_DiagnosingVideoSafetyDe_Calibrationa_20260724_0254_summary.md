# Summary: 2026-07-23_10-35-38Z_V_DEAL_DiagnosingVideoSafetyDe_CalibrationasanUnde.md
Saved: 2026-07-24 02:54
Source: 2026-07-23_10-35-38Z_V_DEAL_DiagnosingVideoSafetyDe_CalibrationasanUnde.md
Model: None

---

## Summary  
The paper introduces **V‑DEAL**, a three‑level diagnostic framework that investigates why Video Large Language Models (Video LLMs) exhibit higher attack success when harmful videos are paired with benign queries rather than explicitly harmful ones. By separating perception failures from internal refusal tendencies, V‑DEAL reveals an “understanding‑refusal coupling” failure as the root cause of this vulnerability. The authors present a systematic diagnostic pipeline that progressively rules out visual misperception and quantifies how textual versus visual understanding drives model behavior. Their work therefore offers a novel analytical lens for safety alignment in video‑aware LLMs.

## Key Contributions  
- [Finding 1] Harmful videos paired with benign queries achieve an average attack success rate of **48.33 %**, which is substantially higher than when the same videos are paired with explicitly harmful queries, indicating a decoupling between visual understanding and safety refusal.  
- [Finding 2] V‑DEAL’s three‑level framework—(i) perception check, (ii) internal refusal quantification, (iii) coupling analysis—identifies that textual understanding activates a stronger refusal tendency than visual understanding, exposing the underlying “understanding‑refusal” failure.  
- [Finding 3] A prompt‑injection intervention reduces attack success by an average of **48.24 percentage points**, achieving performance comparable to prior fine‑tuning‑based safety mitigations.

## Methodology  
V‑DEAL proceeds in three stages: first, the authors rule out any visual perception errors by confirming that models correctly detect harmful content with >81 % accuracy across six Video LLMs and three public benchmarks. Next, they perform hidden‑state analysis to measure the model’s internal refusal propensity when processing video versus text cues. Finally, they evaluate a lightweight prompt‑injection technique that injects safety constraints into the generation process, thereby weakening the coupling between visual input and unsafe output.

## Results  
The experimental results show that while models correctly recognize harmful videos with **81 %+ accuracy**, the overall attack success remains elevated at **48.33 %** under benign‑query pairing. The prompt‑injection method lowers this figure to roughly 0 %, matching the efficacy of existing fine‑tuning approaches. These findings demonstrate that safety de‑calibration stems from an imbalance between visual and textual understanding rather than outright failure.

## Significance  
Understanding why Video LLMs are vulnerable to prompt attacks is crucial for building robust, real‑world deployments where safety must be preserved without sacrificing performance. V‑DEAL provides a diagnostic tool that can pinpoint the specific stage of the model’s reasoning pipeline where the coupling breaks down, enabling targeted interventions rather than broad retraining.

## Related Concepts  
- Video Large Language Models (Video LLMs)  
- Safety alignment / alignment failure  
- Understanding‑refusal coupling  
- Perception vs. internal representation failures  
- Hidden‑state analysis of model behavior  
- Prompt injection for safety mitigation  
- Refusal tendency quantification
