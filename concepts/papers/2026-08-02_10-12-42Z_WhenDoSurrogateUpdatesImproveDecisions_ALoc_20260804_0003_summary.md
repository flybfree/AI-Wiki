# Summary: 2026-08-02_10-12-42Z_WhenDoSurrogateUpdatesImproveDecisions_ALocalTheor.md
Saved: 2026-08-04 00:03
Source: 2026-08-02_10-12-42Z_WhenDoSurrogateUpdatesImproveDecisions_ALocalTheor.md
Model: None

---

## Summary  
This paper addresses a fundamental mismatch in trajectory-based training: models are updated using surrogate losses derived from training trajectories, yet their decision utility is measured by downstream task rewards. The authors introduce a local theoretical framework to analyze when such updates improve both the population surrogate loss and the model’s actual decision risk. By formalizing trajectory learnability and decision utility, they derive conditions under which one-step updates reduce error in both domains and accumulate benefits over repeated training steps.

## Key Contributions  
- [Finding 1] A theoretical bound separates the discrepancy between surrogate and decision risk into first-order gradient misalignment (due to nonnegative calibration) and second-order curvature effects, with a pathwise extension showing how these errors accumulate across multiple updates.  
- [Finding 2] Universal one-step transfer over any accessible update direction occurs precisely when the surrogate and decision gradients are positively collinear, enabling consistent improvement in decision utility regardless of trajectory choice.  
- [Finding 3] The calibration gap between surrogate loss and decision risk is bounded by learnability-based trajectory selection, with a refined candidate-difference approach that focuses only on directions affecting pairwise rankings to tighten this guarantee.

## Methodology  
The authors fix a model checkpoint and restrict the update space to a specific manifold. They define two key quantities: learnability (the reduction in population surrogate risk) and decision utility (the reduction in decision risk). Using these, they analyze how trajectory-based updates affect both metrics simultaneously. The analysis is formalized through gradient alignment properties and curvature considerations, leading to precise conditions for when surrogate training improves actual decisions.

## Results  
Theoretical results establish that first-order transfer errors are bounded by calibration misalignment and second-order curvature, with accumulation over steps modeled pathwise. Experimentally, in gridworld and LLM post-training settings, the predicted behavior matches observed outcomes: updates improve decision utility when gradients align, and trajectory selection is optimized to minimize calibration gaps. The approximation-calibration trade-off across nested update spaces further supports the theoretical framework.

## Significance  
This work bridges the gap between surrogate loss training and real-world decision performance, offering a principled theory for when and how trajectory updates translate into better outcomes. It provides actionable insights for training algorithms in reinforcement learning and large language models, where downstream utility often lags behind surrogate metrics.

## Related Concepts  
- Trajectory-based training  
- Surrogate loss  
- Decision risk  
- Gradient alignment  
- Calibration gap  
- Pathwise accumulation  
- Pairwise ranking  
- Update space restriction
