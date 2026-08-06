# Summary: 2026-08-04_20-26-12Z_Attention_OnlyWhite_BoxTransformerviaLeJEPA_BasedS.md
Saved: 2026-08-06 00:06
Source: 2026-08-04_20-26-12Z_Attention_OnlyWhite_BoxTransformerviaLeJEPA_BasedS.md
Model: None

---

## Summary  
This paper proposes an Attention‑Only White‑Box Transformer that is jointly optimized with a LeJEPA‑based self‑supervised paradigm. By treating the isotropic Gaussian embedding distribution from LeJEPA as equivalent to the sparse rate reduction term \(R(Z)\) in white‑box optimization, the authors derive the full objective and solve it via ADMM, yielding an attention‑only architecture that discards ISTA structures and MLP layers. The resulting model achieves competitive classification performance while cutting its parameter count by roughly 31 %. A follow‑up analysis shows that replacing all MLP blocks in standard Vision Transformers with ReLU activations through knowledge distillation can further reduce parameters by about 66 % without sacrificing accuracy.

## Key Contributions  
- [Finding 1] The LeJEPA self‑supervised framework defines an isotropic Gaussian embedding distribution that is conceptually equivalent to the sparse rate reduction term \(R(Z)\) in white‑box Transformer optimization.  
- [Finding 2] Joint ADMM‑based optimization of \(R^{c}(Z|U_{[K]}) + \lambda\|Z\|_0\) produces an attention‑only Transformer that eliminates ISTA and MLP components, reducing the model size by ~31 % while preserving performance.  
- [Finding 3] Knowledge distillation that substitutes ReLU activations for MLP layers in ViTs cuts parameter count by ~66 % and maintains competitive accuracy.

## Methodology  
The authors reconceptualize white‑box network generation as a joint problem: the LeJEPA paradigm supplies an embedding distribution, and the sparse rate reduction term \(R(Z)\) guides optimization. They formulate the full objective as \(R^{c}(Z|U_{[K]}) + \lambda\|Z\|_0\) and solve it iteratively with ADMM. The solution yields a Transformer that relies solely on attention mechanisms—no ISTA or MLP layers are required. Experiments compare this attention‑only model to the original CRATE white‑box Transformer, both trained under the LeJEPA self‑supervised paradigm.

## Results  
On CIFAR‑10, the attention‑only White‑Box Transformer attains 88.88 % accuracy versus 89.18 % for CRATE; on CIFAR‑100 it reaches 63.54 % compared to 63.56 %. The new model uses about 31 % fewer parameters than the original design. Knowledge distillation that replaces all MLP blocks with ReLU activations reduces parameter count by roughly 66 % while keeping accuracy within a similar range.

## Significance  
The work demonstrates that aligning self‑supervised learning objectives with white‑box optimization can yield more efficient architectures without sacrificing performance, highlighting the redundancy of certain components in standard ViTs. This insight encourages future research into parameter‑lightening strategies for transformer‑based models.

## Related Concepts  
- White‑box networks  
- Self‑supervised learning  
- LeJEPA (Least‑Energy Joint Embedding Pre‑training)  
- Sparse rate reduction term \(R(Z)\)  
- Alternating Direction Method of Multipliers (ADMM)  
- Attention‑only Transformer  
- Knowledge distillation  
- MLP layers in Vision Transformers
