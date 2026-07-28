# Summary: 2026-07-25_02-23-34Z_Real2Sim2RealforVision_Language_ActionManipulation.md
Saved: 2026-07-27 23:34
Source: 2026-07-25_02-23-34Z_Real2Sim2RealforVision_Language_ActionManipulation.md
Model: None

---

## Summary  
This paper introduces Real2Sim2Real, an end-to-end AMD ROCm-based pipeline for vision-language-action (VLA) manipulation that enables embodied AI to operate seamlessly between simulated and real-world environments without relying on CUDA. The system integrates large-scale VLA models with physical robotic agents, leveraging AMD’s Radeon PRO GPUs and Ryzen AI edge compute through the open-source ROCm software stack. By unifying data-center training silicon (RDNA4), simulation/rendering GPUs (Radeon AI PRO R9700), and edge compute (RDNA3.5), the pipeline supports full-stack training, deployment, and inference across diverse hardware platforms. The work addresses a critical gap in Physical AI by providing a reproducible, AMD-accelerated framework for VLA-based manipulation tasks.

## Key Contributions  
- [Finding 1] A fully AMD-accelerated ROCm-based pipeline that replaces CUDA dependency, enabling VLA model training and deployment on Radeon PRO GPUs (R9700) and RDNA3.5 hardware without GPU compute limitations.  
- [Finding 2] The integration of SmolVLA with a physical Franka robot to perform semantic object selection tasks in real-world environments, demonstrating end-to-end vision-language-action control from simulation to physical action.  
- [Finding 3] A synthetic data generation pipeline combining 3D Gaussian Splatting (3DGS) reconstructions with Genesis physics engine to create high-fidelity Sim2Real datasets for training manipulation policies.

## Methodology  
The authors approached the problem by designing a modular, hardware-agnostic pipeline that decouples simulation and real-world execution. Training is performed on AMD ROCm-enabled GPUs using PyTorch, while deployment leverages Radeon AI PRO’s low-latency compute and RDNA3.5 edge modules for real-time inference. The Sim2Real pipeline generates synthetic scenes by fusing 3DGS point clouds with Genesis physics, preserving semantic object properties for VLA models to learn from. Reinforcement learning is applied across quadruped and humanoid platforms, with performance benchmarked on both R9700 and W7900 hardware.

## Results  
The pipeline achieved state-of-the-art results in Sim2Real manipulation tasks, including accurate object selection (one-of-three) and smooth physical execution by the Franka arm. Synthetic data generation produced 10,000+ high-resolution scenes with consistent physics and semantics. Reinforcement learning models demonstrated stable locomotion on both humanoid robots, with latency under 50ms on RDNA3.5 edge hardware. All experiments were reproducible via the free Radeon Cloud Platform.

## Significance  
Real2Sim2Real is a landmark contribution to Physical AI by eliminating CUDA dependency and enabling large-scale VLA training at scale using AMD’s ROCm stack. It proves that high-performance, real-world-ready AI can be achieved without NVIDIA-centric infrastructure, accelerating the adoption of embodied AI in robotics and smart environments.

## Related Concepts  
Vision-Language-Action (VLA) models, 3D Gaussian Splatting (3DGS), Genesis physics engine, ROCm software stack, Radeon PRO GPUs, RDNA4/RDNA3.5 architecture, Embodied AI, Sim-to-Real transfer learning, Reinforcement Learning for robotics
