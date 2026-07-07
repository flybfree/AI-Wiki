# Summary: 2026-07-06_17-59-59Z_FromFixedtoFreeCameras_Calibration_FreeView_Robust.md
Saved: 2026-07-06 23:31
Source: 2026-07-06_17-59-59Z_FromFixedtoFreeCameras_Calibration_FreeView_Robust.md
Model: None

---

## Summary  
This paper introduces CamVLA, a calibration-free vision-language-action (VLA) model designed to enable robots to perform tasks reliably despite significant camera repositioning or remounting in real-world environments. Unlike prior view-robust VLA policies that require explicit camera extrinsics for geometric grounding, CamVLA autonomously learns both the local action and the hand-eye transformation without relying on extrinsic data. The model decouples manipulation control from camera geometry, allowing it to generate pose-independent actions while maintaining visual consistency through a learned 6-DoF hand-eye matrix. This approach enables deployment with only a single monocular RGB image and task instruction, eliminating the need for depth sensors or precise calibration.

## Key Contributions  
- [Finding 1] CamVLA decouples camera-centric action generation from geometric grounding by predicting both a camera-frame end-effector action and a 6-DoF hand-eye matrix.  
- [Finding 2] The model achieves calibration-free, depth-free, single-view operation using only monocular RGB input and task instructions at deployment.  
- [Finding 3] CamVLA consistently improves success rates across diverse unseen viewpoints in both simulation and real-world robot data.

## Methodology  
The authors approach the problem by treating camera geometry as a learnable variable rather than a fixed extrinsic parameter. They train the model to predict two components: first, an action expressed entirely within the local camera frame (camera-centric), which is independent of the camera’s position in the world; second, a 6-DoF transformation matrix that maps the robot base frame to the camera frame. These predictions are composed using a deterministic geometric transform to produce a final action in the robot base frame. This disentanglement allows the model to learn how to move (action) and where to look (geometric grounding) separately, enabling robustness to camera changes.

## Results  
CamVLA demonstrates superior performance compared to baseline VLA models across multiple benchmarks. In simulation tasks involving object manipulation under varying viewpoints, CamVLA achieves up to 25% higher success rates than previous methods. Real-world evaluations on a mobile robot with a single RGB camera show consistent task completion even when the camera is repositioned by over 45 degrees. The model requires no depth input or calibration data, and its performance remains stable across different lighting conditions and viewpoints.

## Significance  
CamVLA represents a significant step toward practical, deployment-ready VLA systems that can operate in unstructured environments without relying on precise camera setup. By removing the need for extrinsic calibration and multi-sensor fusion, it enables broader adoption of vision-based robotic manipulation in real-world settings where cameras are often fixed or repositioned dynamically.

## Related Concepts  
- Vision-Language-Action (VLA) models: systems that integrate visual input, natural language commands, and motor actions.  
- Hand-eye calibration: the process of aligning camera views with robot joint states.  
- Calibration-free perception: achieving robustness without precomputed extrinsic parameters.  
- Camera-centric action: generating actions in a frame-independent or local coordinate system.
