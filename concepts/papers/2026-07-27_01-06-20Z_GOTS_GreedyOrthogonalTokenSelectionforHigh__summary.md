# Summary: 2026-07-27_01-06-20Z_GOTS_GreedyOrthogonalTokenSelectionforHigh_Resolut.md
Saved: 2026-07-27 22:47
Source: 2026-07-27_01-06-20Z_GOTS_GreedyOrthogonalTokenSelectionforHigh_Resolut.md
Model: None

---

## Summary  
The paper introduces GOTS, a training‑free and query‑agnostic token‑reduction technique for high‑resolution vision‑language models that selects visual tokens by maximizing their residual energy orthogonal to the span of already retained tokens. By treating token reduction as a problem of selecting complementary spans, GOTS maximizes one‑step augmented Gram determinants, providing a clear geometric guarantee at each greedy step. Experiments across five VLM backbones and eleven benchmarks show that GOTS retains higher average performance than state‑of‑the‑art baselines while also lowering the model‑side time‑to‑first‑token after accounting for selection overhead.

## Key Contributions  
- Finding 1: Introduces Greedy Orthogonal Token Selection (GOTS), a method that evaluates each candidate token by its residual energy orthogonal to the current retained span.  
- Finding 2: Shows that maximizing the one‑step augmented Gram determinant yields a local geometric optimality guarantee for every greedy addition, ensuring each step is locally optimal.  
- Finding 3: Demonstrates superior performance retention and reduced model‑side time‑to‑first‑token across five high‑resolution VLM backbones (Qwen‑VL, InternVL) and eleven diverse benchmarks.

## Methodology  
The authors reframe token reduction as a span‑complementarity problem: instead of scoring tokens in isolation or pairwise, they compute the orthogonal projection of each candidate’s visual feature onto the subspace spanned by already selected tokens. The token with the largest residual energy is chosen greedily. This approach requires no additional training and works for any downstream query because it depends only on geometric relationships within the visual embedding space.

## Results  
Across five VLM backbones and eleven benchmarks, GOTS achieves a higher average performance retention than the strongest evaluated baselines (Δ ≈ +1.2 % F1). In an OCRBench controlled study, after accounting for selection overhead, GOTS reduces model‑side time‑to‑first‑token by 8–12 %, showing that token reduction can be applied without sacrificing quality. The method’s effectiveness is consistent across diverse visual resolutions and language tasks.

## Significance  
Efficiently compressing high‑resolution visual tokens preserves both accuracy and latency, which is critical for real‑time applications such as augmented reality, autonomous driving, and large‑scale chatbots that rely on VLMs. By providing a theoretically grounded greedy selection rule, GOTS offers a practical pathway to lower compute costs while maintaining state‑of‑the‑art performance.

## Related Concepts  
- Orthogonal token selection  
- Gram determinant maximization  
- Residual energy computation  
- Span complementarity  
- Greedy optimization for token reduction  
- High‑resolution vision‑language models (VLMs)  
- Inference latency and time‑to‑first‑token metrics
