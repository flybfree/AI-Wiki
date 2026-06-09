# Summary: 2026-04-26_14-53-48Z_SFT_then_RLOutperformsMixed_PolicyMethodsforLLMRea.md
Saved: 2026-04-29 03:08
Source: 2026-04-26_14-53-48Z_SFT_then_RLOutperformsMixed_PolicyMethodsforLLMRea.md
Model: qwen3.6:35b

---

## Summary
This paper challenges the prevailing assumption that mixed-policy optimization methods are superior to the standard Supervised Fine-Tuning (SFT)-then-Reinforcement Learning (RL) pipeline for enhancing LLM reasoning. The authors demonstrate that many recent improvements reported in the literature rely on faulty baselines caused by implementation bugs, specifically an optimizer bug in DeepSpeed and a loss aggregation error in OpenRLHF. After correcting these foundational issues, the standard SFT-then-RL approach significantly outperforms all evaluated mixed-policy methods across multiple math benchmarks using models like Qwen2.5 and Llama-3.1.

## Key Contributions
1. **Validation of Standard Pipeline:** The authors conclusively prove that the traditional SFT-then-RL pipeline remains highly effective for improving LLM reasoning, surpassing complex mixed-policy alternatives.
2. **Identification of Critical Bugs:** They pinpoint two major implementation flaws—a CPU-offloaded optimizer bug in DeepSpeed and a loss aggregation bug in OpenRLHF—that artificially suppress SFT performance across the research community.
3. **Efficiency Benchmark:** The study shows that even a highly truncated RL variant (only 50 steps) can outperform mixed-policy methods while drastically reducing computational overhead (FLOPs).

## Methodology
The authors benchmarked various LLM fine-tuning strategies, including standard SFT-then-RL and several state-of-the-art mixed-policy optimization techniques. A core part of the methodology involved debugging and correcting common infrastructure bugs within popular deep learning frameworks (DeepSpeed, OpenRLHF) that were used to train these models.

## Results
After correcting the identified DeepSpeed optimizer bug and the OpenRL
