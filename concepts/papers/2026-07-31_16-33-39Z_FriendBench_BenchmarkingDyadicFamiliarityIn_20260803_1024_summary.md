# Summary: 2026-07-31_16-33-39Z_FriendBench_BenchmarkingDyadicFamiliarityInference.md
Saved: 2026-08-03 10:24
Source: 2026-07-31_16-33-39Z_FriendBench_BenchmarkingDyadicFamiliarityInference.md
Model: None

---

## Summary
This paper introduces FriendBench, a novel benchmark designed to evaluate the ability of both humans and Multimodal Large Language Models (MLLMs) to infer dyadic familiarity from short video clips of social interactions. The core challenge involves determining whether two individuals are already acquainted or meeting as strangers based solely on their non-verbal and verbal cues during a 20-second ice-breaker conversation. By controlling for the content of the dialogue, the benchmark isolates the manner of interaction as the primary signal for inference. The study compares performance across text, audio, and video modalities, revealing that while top-tier models match human accuracy, they exhibit distinct biases in their decision-making processes compared to human observers.

## Key Contributions
- **Introduction of FriendBench**: The authors create a rigorous benchmark dataset comprising 96 balanced dyadic interactions, providing stimuli, human ratings, and model predictions to standardize the evaluation of social familiarity inference.
- **Performance Parity with Behavioral Divergence**: The study demonstrates that the best-performing multimodal models achieve statistical parity with human crowds in accuracy across all modalities, yet they differ fundamentally in their underlying priors, specifically leaning toward classifying pairs as "strangers."
- **Modality-Specific Human Advantage**: While richer channels (video) improve performance for both humans and machines, only humans derive a significant additional benefit from visible behavioral cues beyond speech, highlighting a unique aspect of human social cognition that current models lack.

## Methodology
The researchers constructed FriendBench by collecting 20-second video clips of dyadic ice-breaker conversations where every pair answered identical prompts. This design ensures that the semantic content of the conversation is constant, forcing the inference to rely entirely on paralinguistic and non-verbal cues such as tone, gaze, and body language. They evaluated 26 models from seven different companies alongside matched human panels. The evaluation was conducted across three distinct modalities: text (transcripts), audio (speech only), and video (full multimodal input). The dataset includes 96 balanced dyads to ensure equal representation of familiar and stranger pairs, allowing for a fair comparison of accuracy and bias metrics.

## Results
The experimental results show that the highest-performing models are statistically indistinguishable from human crowds in terms of raw accuracy across text, audio, and video modalities. However, a deeper analysis reveals a critical difference in effective priors: while humans maintain a balanced distribution between predicting "familiar" and "stranger," the strongest models exhibit a systematic bias toward predicting "stranger." Furthermore, the study finds that adding richer sensory channels improves performance for both groups, but the magnitude of improvement varies. Crucially, humans gain a unique advantage from visible behavioral cues in the video modality that is not fully replicated by current multimodal architectures, suggesting that human social inference relies on visual integration in ways that models do not yet emulate.

## Significance
This work is significant because it moves beyond simple accuracy metrics to expose hidden biases in how AI systems process social information. By demonstrating that models can match human performance while holding different priors, the paper highlights a potential gap in social alignment and fairness in AI systems. It provides a crucial tool for researchers to diagnose these biases and develop more nuanced multimodal models that better reflect human social cognition, particularly in applications requiring sensitive interpersonal understanding.

## Related Concepts
- Multimodal Large Language Models (MLLMs)
- Dyadic Familiarity Inference
- Social Signal Processing
- Human-AI Comparison
- Bias in AI Decision Making
- Non-verbal Communication Analysis
