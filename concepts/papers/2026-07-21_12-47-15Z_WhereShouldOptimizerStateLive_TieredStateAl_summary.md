# Summary: 2026-07-21_12-47-15Z_WhereShouldOptimizerStateLive_TieredStateAllocatio.md
Saved: 2026-07-24 00:49
Source: 2026-07-21_12-47-15Z_WhereShouldOptimizerStateLive_TieredStateAllocatio.md
Model: None

---

## Summary  
Mixture-of-experts (MoE) models face a severe memory bottleneck due to the large optimizer state required by standard optimizers like AdamW, which stores both first and second moments for all parameters. This paper introduces SkewAdam, a tiered optimizer that allocates optimizer states differently across three parameter populations in MoE systems—the dense backbone, expert modules, and router—to reduce memory usage without sacrificing training accuracy. By leveraging the distinct gradient statistics of these components, SkewAdam achieves significantly lower memory consumption while maintaining or improving validation performance compared to baseline optimizers.

## Key Contributions  
- [Finding 1] The optimizer state in MoE training is dominated by second moment storage, and this can be reduced through tiered allocation based on parameter population size and gradient behavior.  
- [Finding 2] SkewAdam’s tiered state allocation—using factored second moments for experts and router, and exact second moments with momentum for the backbone—reduces memory usage to just 1.29 GB, a 60% reduction from AdamW’s 50.6 GB.  
- [Finding 3] Despite using far less state than AdamW (2.6% of its size), SkewAdam achieves superior validation perplexity and balanced router load, demonstrating that state allocation strategy matters as much as state volume.

## Methodology  
The authors designed SkewAdam by analyzing the three distinct parameter groups in an MoE: the dense backbone (5% of parameters), expert modules (95%), and the router (less than 0.01%). They observed that the backend and experts have different gradient magnitudes, while the router has negligible gradients due to sparse activation. SkewAdam therefore allocates memory-efficient estimators accordingly: a factored second moment for most parameters, an exact second moment with float32 momentum only for the backbone, and no state for the router. This tiered approach minimizes memory footprint while preserving adaptive learning dynamics.

## Results  
In experiments over 82 million tokens on a 6.78B-parameter MoE model, SkewAdam achieved validation perplexity of 108.4, outperforming AdamW (126.8), Muon (120.2), and Lion (393.7). Crucially, the memory usage dropped from 81.4 GB to 31.3 GB—well within a 40 GB accelerator’s budget. Ablation studies confirmed that reducing state size further via tiered allocation does not degrade accuracy: matching AdamW’s 50.6 GB of state with SkewAdam’s 1.29 GB yields the same perplexity. Additionally, Adafactor (which uses factored second moments but lacks momentum) lagged by 40 points, highlighting that momentum is essential for performance. Learning rate tuning narrowed but did not close the gap between AdamW and tuned Adafactor.

## Significance  
This work demonstrates that optimizer state allocation can be optimized as much as its size to improve training efficiency in MoE systems. By decoupling memory usage from accuracy loss through intelligent tiering, SkewAdam enables deployment on resource-constrained hardware without sacrificing performance. The findings suggest that how optimizer state is structured—rather than just how much there is—is a critical factor in scalable AI training.

## Related Concepts  
Mixture-of-experts (MoE), AdamW, second moment methods, factored estimators, learning rate adaptation, memory-efficient training, tensor parallelism, and sparse computation.
