# Summary: 2026-07-27_04-39-13Z_SyRuP_EnhancingSystem_PromptFollowingviaReward_Gui.md
Saved: 2026-07-27 22:54
Source: 2026-07-27_04-39-13Z_SyRuP_EnhancingSystem_PromptFollowingviaReward_Gui.md
Model: None

---

## Summary  
Large Language Models (LLMs) increasingly rely on system prompts to guide behavior, but these prompts are often followed implicitly through in-context learning, which can be unreliable for complex or compositional instructions. This paper introduces SyRuP—a decoding-time framework that enhances system-prompt adherence without retraining the base model—by training a reward-guided cross-attention head from preference pairs conditioned on the system prompt. At inference, SyRuP reranks the model’s top-k token candidates using a learned signal that captures both direct and contrastive effects of the system prompt, enabling more reliable and consistent output generation.

## Key Contributions  
- [Finding 1] SyRuP introduces a reward-guided cross-attention mechanism that produces token-level adherence scores from system-prompt-conditioned preference pairs, allowing explicit guidance during decoding.  
- [Finding 2] The framework integrates an optional contrastive signal to detect and amplify shifts in base logits caused by the system prompt, improving reranking precision.  
- [Finding 3] SyRuP achieves consistent improvements over prompting and decoding-time baselines across multiple system-prompt following benchmarks with only moderate inference overhead.

## Methodology  
The authors address the limitation of implicit prompt following by treating the system prompt as a separate memory source. They train a reward head using preference pairs where each pair consists of two responses generated under identical base prompts but different system prompts. The reward head learns to predict token-level adherence by cross-attending to the system prompt and generating scores that reflect how well each token aligns with the intended behavior. At inference, these scores are combined with the base model’s logits via a weighted sum, producing a refined probability distribution. An optional contrastive component is added to detect and amplify differences in logit shifts caused by the system prompt, enhancing reranking effectiveness.

## Results  
Experiments on standard system-prompt following benchmarks—such as those evaluating instruction-following, role adherence, and safety compliance—demonstrate that SyRuP significantly outperforms prompting (e.g., few-shot or chain-of-thought) and decoding-time baselines like top-k sampling with reranking. The improvement is measured in both accuracy and consistency, with SyRuP reducing deviation from the intended prompt by up to 30% on average. Notably, the model remains frozen, requiring only a lightweight inference-time augmentation that adds minimal latency.

## Significance  
This work provides a practical solution for reliable system-prompt control without retraining or post-processing, which is crucial for real-world applications where inference efficiency and consistency are paramount. By enabling explicit token-level guidance, SyRuP bridges the gap between prompt engineering and model behavior, offering a scalable approach to improving LLM reliability in production systems.

## Related Concepts  
- In-context learning  
- System prompts  
- Decoding-time control  
- Preference modeling  
- Cross-attention mechanisms  
- Contrastive reinforcement learning  
- Logit shifting  
- Reranking  
- Token-level guidance
