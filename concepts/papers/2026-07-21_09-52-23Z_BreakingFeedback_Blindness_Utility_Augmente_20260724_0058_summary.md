# Summary: 2026-07-21_09-52-23Z_BreakingFeedback_Blindness_Utility_AugmentedTransf.md
Saved: 2026-07-24 00:58
Source: 2026-07-21_09-52-23Z_BreakingFeedback_Blindness_Utility_AugmentedTransf.md
Model: None

---

## Summary  
This paper addresses a critical limitation in Transformer-based sequential decision-making models: feedback-blind retrieval, where the model cannot distinguish between observation-equivalent histories with different action-reward outcomes due to attention mechanisms relying solely on input observations. To overcome this, the authors introduce the Utility-Augmented Transformer (UAT), a novel architecture that integrates utility information directly into the attention computation via a compact utility state. UAT enables feedback-informative tasks by allowing action-reward histories to dynamically influence context retrieval during forward passes, thereby breaking the structural bottleneck of standard Transformers in non-stationary environments.

## Key Contributions  
- [Finding 1] The paper formalizes feedback-blindness as a structural limitation in observation-only attention mechanisms, proving that any attention mechanism constrained by observation similarity cannot distinguish between action-reward histories with identical observations but different outcomes.  
- [Finding 2] UAT is proposed as a utility-augmented retrieval architecture where a compact utility state modulates query, key, and value projections, enabling direct influence of action-reward history on context retrieval without modifying the Transformer’s core structure.  
- [Finding 3] The model exhibits an exact zero-gate degradation property: when feedback is uninformative (i.e., utility state is constant), UAT reduces to a vanilla Transformer, preserving its original behavior and ensuring no performance loss in blind settings.

## Methodology  
The authors address the problem by redefining attention as a feedback-conditioned process rather than purely observation-driven. They introduce a compact utility state that encodes action-reward history, which is linearly combined with the query, key, and value projections before applying attention. This modification allows the model to dynamically adjust context retrieval based on past actions and rewards. The architecture maintains finite-horizon compactness and Lipschitz continuity under standard assumptions, ensuring theoretical robustness. Crucially, UAT’s utility state acts as a gate that only activates when feedback is informative, preserving compatibility with observation-only contexts.

## Results  
UAT consistently outperforms baseline models across four non-stationary benchmarks: synthetic navigation with hidden goal shifts, non-stationary sepsis treatment, cross-market portfolio allocation, and delayed-feedback recommendation. In all cases, UAT improves performance over observation-only Transformers, test-time adaptation methods, and input-level feedback baselines. The gains are especially pronounced in noisy regimes requiring strong adaptation, where standard models fail to adapt effectively. Theoretical analysis confirms that UAT strictly enlarges the class of feasible decision maps beyond observation-only Transformers.

## Significance  
This work resolves a fundamental mismatch between model design and task requirements in sequential decision-making: while feedback is available, attention mechanisms remain blind to it. By integrating utility into retrieval, UAT enables models to learn from action-reward histories without sacrificing generalization or efficiency. The zero-gate property ensures that the model remains effective even when feedback is unavailable, making it a robust and practical solution for real-world applications where adaptation is critical.

## Related Concepts  
- Feedback-blindness: inability of attention mechanisms to distinguish between observation-equivalent histories with different outcomes.  
- Utility state: a compact representation encoding action-reward history that modulates attention computation.  
- Zero-gate degradation: the property that UAT reverts to vanilla Transformer when feedback is uninformative.  
- Non-stationary environments: settings where underlying dynamics change over time, requiring adaptive decision-making.
