# Summary: 2026-08-03_05-38-47Z_WhenExtremeDarknessMeetsMotionBlur_MeanFlowforUnif.md
Saved: 2026-08-04 00:32
Source: 2026-08-03_05-38-47Z_WhenExtremeDarknessMeetsMotionBlur_MeanFlowforUnif.md
Model: None

---

## Summary  
This paper addresses a critical gap in extremely low-light RAW image enhancement by integrating realistic motion degradation into the restoration process, which is often neglected in existing methods. The authors introduce MeanFlow—a unified framework that simultaneously handles sensor noise, illumination loss, and motion blur—enabling robust recovery of severely attenuated signals under practical acquisition conditions. By treating both illumination and motion as jointly degrading factors, the work moves beyond isolated treatment to provide a holistic solution for RAW restoration. This unified approach is particularly significant because it preserves pixel fidelity and color consistency while minimizing computational overhead.

## Key Contributions  
- [Finding 1] The authors introduce See in the Degraded Extremely Dark (SIDED), a novel dataset that applies controlled motion degradation to extremely low-light RAW pairs while preserving original sensor noise, enabling realistic evaluation of motion-induced artifacts.  
- [Finding 2] They propose a unified RAW tokenizer with domain-conditioned representation calibration to align extremely low-light and well-exposed RAW data, followed by MeanFlow for single-function enhancement, which is the first framework to jointly model illumination loss and motion blur in RAW restoration.  
- [Finding 3] A physics-guided refinement model is introduced to enhance illumination-reflectance consistency, pixel fidelity, and color preservation without incurring additional inference cost, improving perceptual quality beyond standard denoising.

## Methodology  
The authors approached the problem by first formulating a unified representation space using the RAW tokenizer, which aligns data from different exposure conditions. This calibration ensures that the input features are semantically consistent across dark and bright regions. MeanFlow then operates on this aligned representation to model both illumination attenuation and motion blur as continuous transformations. The physics-guided refinement module leverages constraints from physical optics—such as energy conservation in reflectance and color balance—to refine the output, ensuring realism without extra computational layers.

## Results  
Extensive experiments on the SIDED dataset demonstrate that MeanFlow achieves state-of-the-art performance in extremely low-light RAW enhancement. Quantitative metrics such as PSNR and SSIM improve significantly over previous methods, while qualitative analysis reveals superior handling of motion blur artifacts. The physics-guided refinement further enhances perceptual quality by reducing haloing and color shifts, especially at the edges of dark regions. Most importantly, the framework maintains a single forward pass, making it computationally efficient for real-time applications.

## Significance  
This work matters because it tackles a fundamental limitation in low-light imaging: motion blur is often overlooked when designing restoration algorithms, leading to artifacts that are hard to remove without introducing noise. By integrating motion into the restoration pipeline and using a unified MeanFlow model, the authors provide a practical solution for real-world cameras where both dark exposure and camera shake occur simultaneously. The physics-guided refinement adds scientific rigor, making the method more robust and trustworthy.

## Related Concepts  
- RAW image: Unprocessed sensor data from digital cameras  
- Motion blur: Degradation caused by camera movement during exposure  
- Sensor noise: Random variations in pixel values due to electronic imperfections  
- MeanFlow: A neural network-based flow model for image transformation  
- Physics-guided refinement: Optimization using physical constraints like energy conservation
