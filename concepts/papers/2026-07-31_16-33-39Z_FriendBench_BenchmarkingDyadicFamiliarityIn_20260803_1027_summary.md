# Summary: 2026-07-31_16-33-39Z_FriendBench_BenchmarkingDyadicFamiliarityInference.md
Saved: 2026-08-03 10:27
Source: 2026-07-31_16-33-39Z_FriendBench_BenchmarkingDyadicFamiliarityInference.md
Model: None

---

## Summary
This paper introduces FriendBench, a novel benchmark designed to evaluate the ability of both humans and multimodal large language models (MLLMs) to infer dyadic familiarity from short social interactions. The authors construct a dataset of 96 balanced dyads featuring ice-breaker conversations, where participants answer identical prompts, thereby isolating behavioral cues from linguistic content as the primary source of information for determining prior acquaintance. By comparing performance across text, audio, and video modalities, the study reveals that while top-tier models can match human accuracy in identifying familiar versus stranger pairs, they exhibit a distinct bias toward predicting "stranger" status. This research highlights critical differences in how artificial systems and humans process social signals, emphasizing that richer sensory channels benefit humans more significantly than machines.

## Key Contributions
- **Introduction of FriendBench**: The authors present the first comprehensive benchmark specifically tailored for dyadic familiarity inference, providing a standardized dataset of 96 balanced video clips with synchronized text, audio, and visual data to facilitate fair comparisons between human cognition and AI models.
- **Discovery of Prior Bias in Models**: A significant finding is that while state-of-the-art multimodal models achieve accuracy levels statistically indistinguishable from human crowds, they do so by leaning heavily toward a "stranger" prior, whereas humans maintain a balanced distribution of predictions, suggesting fundamental differences in decision-making strategies.
- **Modality-Specific Human Advantage**: The study demonstrates that while additional modalities (audio and video) improve performance for both groups, only humans derive a significant accuracy boost from visible behavioral cues beyond speech, indicating that current models fail to fully integrate non-verbal visual information effectively.

## Methodology
The researchers collected 96 dyadic interactions where pairs engaged in ice-breaker conversations for 20 seconds. Crucially, every pair received the same type of prompt, ensuring that any difference in inferred familiarity must stem from behavioral mannerisms rather than conversational content. The dataset includes synchronized text transcripts, audio recordings, and video footage. The authors then evaluated 26 different models from seven major technology companies across these three modalities. Simultaneously, they gathered human ratings from matched panels to serve as a ground truth baseline. The experimental design ensured that the task was purely inferential based on interaction style, allowing for a clean assessment of multimodal integration capabilities in both biological and artificial agents.

## Results
The experimental results show that the best-performing multimodal models achieve accuracy rates that are statistically indistinguishable from human participants across all modalities (text, audio, and video). However, a deeper analysis reveals that humans and models reach this parity through different mechanisms. Humans maintain a balanced prior probability for both "familiar" and "stranger" outcomes, whereas the strongest models exhibit a systematic bias toward predicting "stranger." Furthermore, the addition of visual data significantly boosts human performance but provides diminishing returns for models, suggesting that current architectures do not effectively leverage non-verbal visual cues to the same extent as humans.

## Significance
This work is significant because it moves beyond simple accuracy metrics to expose underlying biases and modality integration failures in current multimodal AI systems. It underscores that matching human performance on a binary classification task does not imply equivalent cognitive processing or robustness. The findings suggest that future research must focus on how models weight different sensory inputs and manage priors, rather than just optimizing for final accuracy scores. This benchmark provides a crucial tool for diagnosing these subtle but critical deficiencies in social AI.

## Related Concepts
- Multimodal Large Language Models (MLLMs)
- Dyadic Familiarity Inference
- Social Signal Processing
- Non-verbal Communication Analysis
- Bias in Artificial Intelligence
- Human-AI Comparison Benchmarks
