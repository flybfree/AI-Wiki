# Summary: 2026-07-23_10-35-38Z_V_DEAL_DiagnosingVideoSafetyDe_CalibrationasanUnde.md
Saved: 2026-07-24 02:47
Source: 2026-07-23_10-35-38Z_V_DEAL_DiagnosingVideoSafetyDe_CalibrationasanUnde.md
Model: None

---

## Summary  
The paper V‑DEAL investigates why Video Large Language Models (VLLMs) exhibit higher attack success rates when harmful videos are paired with benign queries rather than with explicitly harmful queries. It proposes a three‑level diagnostic framework that separates perception errors from internal refusal mechanisms, quantifying how visual understanding and textual comprehension interact to produce safety de‑calibration. By systematically ruling out simple perception failures and measuring the model’s hidden‑state refusal tendency, V‑DEAL identifies a coupling failure between visual input and textual response generation. The study also introduces a prompt‑injection intervention that mitigates attacks without requiring extensive fine‑tuning.

## Key Contributions  
- [Finding 1] Harmful videos paired with benign queries achieve an average attack success rate of 48.33 %, higher than when the same videos are paired with harmful queries.  
- [Finding 2] V‑DEAL’s three‑level framework isolates perception failure, internal refusal tendency, and their coupling as distinct diagnostic dimensions.  
- [Finding 3] Hidden‑state analysis reveals that visual understanding activates a weaker refusal tendency than textual understanding.

## Methodology  
The authors evaluate six Video LLMs on three public benchmarks (e.g., VideoQA, VREC). They first measure detection accuracy, which exceeds 81 % across models. Then they compute attack success rates under two query conditions: benign and harmful queries paired with the same harmful video. To probe internal mechanisms, they conduct hidden‑state probing to compare activation patterns triggered by visual versus textual inputs. Finally, they implement a prompt‑injection technique that rewrites the model’s response generation to reduce unsafe outputs.

## Results  
Detection accuracy is consistently above 81 % across all six models. The average attack success rate with benign queries is 48.33 %, indicating persistent safety de‑calibration despite correct visual detection. Hidden‑state analysis confirms that visual inputs produce weaker refusal signals than textual ones. The prompt‑injection intervention reduces the average attack success by 48.24 percentage points, bringing it to a level comparable with prior fine‑tuning‑based mitigations.

## Significance  
This work provides a diagnostic lens for safety de‑calibration in multimodal LLMs, moving beyond superficial fixes like data augmentation toward targeted interventions that address the underlying understanding‑refusal coupling. By quantifying how visual and textual components interact, V‑DEAL enables researchers to design more effective mitigations such as prompt injection, which can be deployed quickly without large retraining efforts.

## Related Concepts  
Video Large Language Models, safety alignment, understanding‑refusal coupling, perception failure, hidden‑state analysis, prompt injection, fine‑tuning, multimodal reasoning.
