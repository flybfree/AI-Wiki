# Summary: 2026-08-03_10-12-15Z_MANGO_Grasp_MahalanobisFieldsoverGeometry_Oriented.md
Saved: 2026-08-03 23:52
Source: 2026-08-03_10-12-15Z_MANGO_Grasp_MahalanobisFieldsoverGeometry_Oriented.md
Model: None

---

## Summary  
Cross‑embodiment dexterous grasping seeks to generate stable grasps that work across diverse multi‑fingered hands without requiring extensive embodiment‑specific tuning. The paper proposes MANGO‑Grasp, which treats objects as geometry‑oriented 3D Gaussian primitives and robot hands as surface keypoints encoded into morpho‑kinematic descriptors. By using Mahalanobis fields over keypoint–primitive pairs to guide interaction prediction and grasp optimization, the method achieves a shared optimization formulation that works across all hands. The approach improves both simulated and real‑world performance compared with strong baselines.

## Key Contributions  
- **Mahalanobis Fields as Interaction Targets:** The authors introduce Mahalanobis fields derived from keypoint–primitive pairs to capture the anisotropic interaction between a robot hand surface point and an object’s local geometry, serving both as training loss signals and inference guidance.  
- **Geometry‑Oriented 3D Gaussians for Objects:** Objects are represented by Gaussian primitives whose shape aligns with the surface normal, encoding local curvature; this representation is adaptively allocated based on geometric complexity.  
- **Morpho‑Kinematic Descriptor Fusion:** The robot hand’s keypoints are fused into a single morpho‑kinematic descriptor that simultaneously encodes morphology and kinematics, enabling a unified optimization across heterogeneous hands.

## Methodology  
The authors first compute the surface normal at each keypoint on the robot hand and align it with the nearest Gaussian primitive of the object. The Mahalanobis field is then constructed as the covariance matrix between the keypoint vector and the primitive’s parameters, highlighting directions where contact strength should be high (along normals) versus low (within tangents). During training, this field drives a loss that balances grasp stability with minimal deformation. At inference, the same field guides an optimization problem that jointly minimizes contact force variance and maximizes surface alignment, using a single formulation and hyperparameter set for all hands.

## Results  
On the CMAP benchmark, MANGO‑Grasp surpasses the strongest seen‑hand baseline by 8.24 percentage points in success rate. It also achieves zero‑shot transfer to the unseen SharpaWave hand, improving over its best zero‑shot baseline by 16.57 percentage points. In real‑world experiments, the method reaches an 86 % grasp success rate, demonstrating robust performance across simulated and physical environments.

## Significance  
MANGO‑Grasp advances cross‑embodiment dexterous manipulation by unifying object geometry representation with robot morpho‑kinematic descriptors through a principled Mahalanobis interaction framework. Its shared optimization eliminates the need for per‑hand hyperparameter tuning, making it scalable to new hands and improving both simulation and real‑world grasp reliability.

## Related Concepts  
- Mahalanobis fields (covariance‑based interaction metrics)  
- Geometry‑oriented 3D Gaussians (surface‑aligned Gaussian primitives)  
- Morpho‑kinematic descriptors (fusion of morphology and kinematics)  
- Cross‑embodiment dexterous grasping (multi‑hand, multi‑environment manipulation)
