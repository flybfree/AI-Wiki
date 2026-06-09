# Summary: 2026-04-24_16-45-51Z_ThinkingWithoutWords_EfficientLatentReasoningwithA.md
Saved: 2026-04-29 02:53
Source: 2026-04-24_16-45-51Z_ThinkingWithoutWords_EfficientLatentReasoningwithA.md
Model: qwen3.6:35b

---

## Summary
This paper addresses the computational inefficiency of generating long, explicit chains-of-thought (CoT) while maintaining high reasoning performance. The authors propose $\textbf{Abstract Chain-of-Thought}$ (Abstract-CoT), a novel post-training mechanism that replaces natural language CoTs with a short sequence of discrete latent tokens from a reserved vocabulary. This approach significantly reduces inference cost by enabling efficient, non-verbal reasoning without sacrificing the quality achieved by verbose textual explanations.

## Key Contributions
1. **Abstract Chain-of-Thought (Abstract-CoT):** Introduction of a discrete latent reasoning mechanism that uses an abstract token vocabulary to represent complex reasoning steps, drastically reducing generation length compared to natural language CoTs.
2. **Efficient Warm-up Strategy:** Development of a policy iteration warm-up loop combining supervised fine-tuning (
