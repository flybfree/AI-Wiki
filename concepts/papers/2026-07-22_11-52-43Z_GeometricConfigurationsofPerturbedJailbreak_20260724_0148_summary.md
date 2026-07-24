# Summary: 2026-07-22_11-52-43Z_GeometricConfigurationsofPerturbedJailbreakPrompts.md
Saved: 2026-07-24 01:48
Source: 2026-07-22_11-52-43Z_GeometricConfigurationsofPerturbedJailbreakPrompts.md
Model: None

---

## Summary  
The authors investigate how string‑level perturbations that transform failed jailbreak prompts into successful ones are represented internally within the low‑weight versions of Qwen‑2 and Llama‑3 models. By examining two distinct embedding spaces—the last‑layer‑last‑token space and a one‑dimensional top‑50 next‑token probability space— they aim to uncover any structural patterns that could explain why certain prompts succeed while others are rejected. Their analysis reveals that neither representation yields a clean behavioral hyperplane, suggesting that compliance is not driven by simple linear decision boundaries. Instead, specific tokens exhibit strong statistical links to compliant outputs, hinting at subtle but meaningful configurations of the prompt strings.

## Key Contributions  
- [Finding 1] No behavioral hyperplane exists in either embedding space, indicating that refusal‑dominated answers are not separable by a single linear model across all prompts.  
- [Finding 2] The token “Sure” shows a statistically significant association with compliant responses specifically in the Qwen‑2.5‑1.5B model’s last‑layer embedding space.  
- [Finding 3] In Llama‑3.2 models, both the comma “,” and the two‑character sequence “ĊĊ” are linked to compliant answers, suggesting that punctuation or special characters can act as cues for safe completion.

## Methodology  
The researchers selected the smallest available weight variants of Qwen‑2 (1.5B, 3B, 7B) and Llama‑3.2 (1B, 3B, 3.1‑8B) to keep computational cost low while preserving enough capacity for token embeddings. They extracted two representation spaces: the final hidden state of the last token (last‑layer‑last‑token embedding space) which captures spelling and formatting information, and a one‑dimensional vector formed by the top‑50 next‑token probabilities at each position. These vectors were then clustered using standard k‑means to visualize prompt similarity and compliance outcomes.

## Results  
Across all models, the clustering analysis produced no clear hyperplane that separates compliant from refusal answers in either space; the decision boundary would need to be highly non‑linear or context‑dependent. However, statistical tests revealed that “Sure” appears far more often in successful completions for Qwen‑2.5‑1.5B (p < 0.01), while “,” and “ĊĊ” show similar associations in Llama‑3.2 variants. The next‑token probability space, despite its apparent simplicity, also shows a slight clustering bias toward compliant completions when these tokens precede the response.

## Significance  
Understanding these token‑level configurations is crucial for designing robust jailbreak defenses because they expose how subtle string manipulations can bypass simple safety filters. By revealing that certain characters or sequences are predictive of safe outputs, developers can incorporate more nuanced token‑aware safeguards rather than relying solely on pattern matching.

## Related Concepts  
- Embedding space (last‑layer‑last‑token)  
- Next‑token probability vector  
- Behavioral hyperplane  
- Jailbreak prompt perturbation  
- Clustering analysis  
- Token‑level association with model output
