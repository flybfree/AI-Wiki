# Summary: 2026-04-27_17-17-28Z_ScalableHyperparameter_DivergentEnsembleTrainingwi.md
Saved: 2026-04-29 03:12
Source: 2026-04-27_17-17-28Z_ScalableHyperparameter_DivergentEnsembleTrainingwi.md
Model: qwen3.6:35b

---

## Summary
This paper introduces Hyperparameter-Divergent Ensemble Training (HDET), a novel method designed to efficiently explore the hyperparameter space of large neural models during training. HDET addresses the limitation of standard data-parallel training, which typically uses identical updates across replicas and ignores critical hyperparameters like learning rates. The core contribution is repurposing existing GPU replicas for simultaneous exploration of structured hyperparameter variations (e.g., learning rates). Furthermore, the authors propose an automatic Learning Rate (auto-LR) controller that dynamically optimizes the base schedule using inter-replica loss differences as a meta-gradient signal.

## Key Contributions
1. **Hyperparameter-Divergent Ensemble Training (HDET):** A framework enabling simultaneous exploration of multiple scalar hyperparameters (e.g., learning rate, weight decay) by distributing structured variations across data-parallel replicas.
2. **Automatic Learning Rate Optimization:** Integration of an auto-LR controller that treats the relative training loss across the ensemble as a performance signal, guiding momentum-based meta-updates to improve the base schedule automatically.
3. **Generalization and Efficiency:** The framework is highly generalizable beyond learning rates to any non-architectural scalar hyperparameter, requiring only a fan-out/converge protocol with negligible communication overhead.

## Methodology
HDET operates in alternating phases: a **fan-out stage**, where replicas train independently using distinct hyperparameter settings (e.g., $\text{LR} \pm \delta$), and a **converge stage**, where the parameters are aggregated via AllReduce every $T$ steps. The auto-LR controller utilizes the difference in loss ($\Delta L$) across replicas as a zero-order proxy
