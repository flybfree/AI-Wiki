# Summary: 2026-07-31_16-33-39Z_FriendBench_BenchmarkingDyadicFamiliarityInference.md
Saved: 2026-08-03 10:23
Source: 2026-07-31_16-33-39Z_FriendBench_BenchmarkingDyadicFamiliarityInference.md
Model: None

---

## Summary
This paper introduces FriendBench, a novel benchmark designed to evaluate the ability of both humans and multimodal large language models (MLLMs) to infer dyadic familiarity from brief social interactions. The core objective is to determine whether two individuals are already acquainted or meeting as strangers based solely on their non-verbal and verbal behavior during a 20-second ice-breaker conversation, rather than the semantic content of their dialogue. By controlling for prompt type across all pairs, the study isolates the manner of interaction as the primary signal for inference. The research provides a comprehensive comparison of 26 models from seven different companies against matched human panels, offering insights into how various modalities contribute to social cognition in artificial and biological systems.

## Key Contributions
- **Parity in Accuracy:** The study demonstrates that the best-performing multimodal models achieve accuracy levels statistically indistinguishable from human crowds across text, audio, and video modalities, challenging the assumption that AI significantly lags behind humans in basic social inference tasks.
- **Divergent Inference Strategies:** While performance metrics are similar, the underlying mechanisms differ; humans maintain a balanced prior distribution between "familiar" and "stranger" labels, whereas top models exhibit a strong bias toward predicting "stranger," indicating a difference in effective priors rather than discriminative capability.
- **Modality-Specific Human Advantage:** The research reveals that while richer channels (audio and video) improve performance for both humans and machines, only humans derive significant additional benefit from visible behavioral cues beyond speech, highlighting a unique aspect of human social processing.

## Methodology
The authors constructed FriendBench using 96 balanced dyads of participants engaging in standardized ice-breaker conversations. Each pair was presented with the same type of prompt to ensure that differences in interaction style, rather than topic or content, drove the inference task. The dataset includes synchronized text, audio, and video recordings of these 20-second clips. To establish a baseline, human panels rated the familiarity of each dyad. Subsequently, 26 multimodal large language models from seven major technology companies were evaluated on their ability to predict the same labels using the provided stimuli. The study employed rigorous statistical comparisons to analyze accuracy, bias, and modality contributions across both human and model groups.

## Results
Experimental results show that top-tier MLLMs match human crowd performance in accuracy across all tested modalities. However, a critical divergence was found in prediction distributions: models consistently leaned toward labeling pairs as "strangers," whereas humans distributed their predictions more evenly. This suggests models have a different prior belief about social encounters rather than inferior discrimination skills. Furthermore, the analysis of modality impact showed that adding visual data improved model performance but did not provide the same relative boost to human accuracy as it did for speech-only inputs, implying humans integrate visual cues differently or rely on them less exclusively than models might.

## Significance
This work is significant because it establishes a standardized framework for evaluating social intelligence in AI systems, moving beyond semantic understanding to pragmatic and behavioral inference. It highlights that achieving human-level accuracy does not imply human-like reasoning processes, which is crucial for developing transparent and trustworthy AI agents in social contexts. The benchmark also provides valuable data on how multimodal integration affects social perception, guiding future research into more nuanced models of human-AI interaction.

## Related Concepts
- Multimodal Large Language Models (MLLMs)
- Dyadic Familiarity Inference
- Social Cognition in AI
- Non-verbal Communication Analysis
- Benchmarking Human-AI Parity
- Ice-breaker Conversation Dynamics
