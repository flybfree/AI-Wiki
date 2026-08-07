# Summary: 2026-08-05_18-17-59Z_RectifyingGeometricMisalignment_OnlineSource_FreeA.md
Saved: 2026-08-06 21:49
Source: 2026-08-05_18-17-59Z_RectifyingGeometricMisalignment_OnlineSource_FreeA.md
Model: None

---

## Summary  
The paper addresses the challenge of online source‑free adaptation for class‑imbalanced EEG data in BCI, where standard Riemannian alignment methods like RCT assume balanced label priors and fail to correct geometric misalignment caused by dynamic label shifts. OSPDIM (Online SPD manifold information maximization) introduces a manifold‑constrained bias parameter that is optimized via information maximization to rectify this skew on the tangent space. The method operates online, continuously updating its mapping without requiring offline batch statistics or explicit class balancing. By doing so, it provides a robust, plug‑and‑play solution for real‑world BCI applications.  

## Key Contributions  
- OSPDIM formulates label shift as a geometric misalignment on the Riemannian SPD manifold and corrects it with an online bias parameter.  
- The framework maximizes information about the source manifold in the tangent space to estimate and adjust the alignment, rather than relying on global batch statistics.  
- Extensive experiments demonstrate that OSPDIM outperforms standard Riemannian baselines under severe class imbalance, especially in online adaptation scenarios.  

## Methodology  
The authors model EEG data as points on a 2‑D SPD manifold and compute their tangent vectors. They introduce a bias vector β that is constrained to lie within the source manifold’s tangent space. The mapping from target to source is expressed as T = A + β, where A is the Riemannian centering transformation. Using information maximization, they estimate β by maximizing the mutual information between the transformed data and the source distribution while keeping β on the SPD manifold. This online estimation allows continuous correction of geometric skew without batch re‑training.  

## Results  
Simulations on synthetic 2‑D SPD matrices show that OSPDIM eliminates residual misalignment where RCT leaves a systematic offset, achieving near‑zero Euclidean distance between aligned data sets. On real motor imagery datasets (e.g., MEGA, BCI‑EEG), OSPDIM reduces classification error by up to 12 % compared with RCT and improves adaptation speed in online settings, especially when one class is underrepresented.  

## Significance  
By decoupling label distribution shifts from the alignment problem, OSPDIM enables reliable source‑free adaptation even when class priors are highly imbalanced. This makes BCI systems more robust to real‑world variability, reducing the need for costly offline calibration and supporting scalable deployment across subjects and sessions.  

## Related Concepts  
- Riemannian manifold  
- SPD (positive definite symmetric) manifold  
- Tangent space  
- Riemannian centering transformation (RCT)  
- Unsupervised domain adaptation (UDA)  
- Information maximization  
- Online learning
