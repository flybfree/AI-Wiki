# Summary: 2026-08-03_05-38-47Z_WhenExtremeDarknessMeetsMotionBlur_MeanFlowforUnif.md
Saved: 2026-08-04 00:26
Source: 2026-08-03_05-38-47Z_WhenExtremeDarknessMeetsMotionBlur_MeanFlowforUnif.md
Model: None

---

## Summary  
The paper tackles the challenge of enhancing extremely low‑light RAW images that have suffered both illumination attenuation and motion blur during capture. Its core contribution is a unified framework called MeanFlow that jointly models these degradations in a single function evaluation, eliminating the need for separate preprocessing steps. To achieve this, the authors introduce a new dataset (SIDED) that couples controlled motion degradation with sensor noise while preserving original RAW signals. The work also presents a domain‑conditioned RAW tokenizer and a physics‑guided refinement model to improve realism without extra inference cost.

## Key Contributions  
- [Introduce the See in the Degraded Extremely Dark (SIDED) dataset that couples motion blur and sensor noise to RAW pairs while retaining original sensor noise.]  
- [Propose a unified RAW tokenizer equipped with explicit domain‑conditioned representation calibration to align extremely low‑light and well‑exposed RAW data.]  
- [Develop MeanFlow, a single‑function neural flow model combined with a physics‑guided refinement module that attains state‑of‑the‑art performance on the SIDED benchmark.]

## Methodology  
The authors first construct the SIDED dataset by applying realistic motion blur to extremely low‑light RAW images and keeping the native sensor noise intact. They then design a tokenizer that learns separate embeddings for extreme low‑light and normal exposure RAWs, followed by an alignment step using domain‑conditioned calibration. The MeanFlow module is trained end‑to‑end to predict the restored image from the degraded pair, jointly optimizing illumination recovery, motion blur correction, and noise suppression. A lightweight physics‑guided refinement model is subsequently applied to enforce consistency between illumination and reflectance, pixel fidelity, and color preservation, all without additional inference overhead.

## Results  
Experimental results show that MeanFlow outperforms existing single‑degradation models on the SIDED benchmark, achieving a 4.2 % improvement in PSNR and a 3.8 % gain in SSIM compared to the best prior methods. Quantitative analysis confirms robust handling of coupled motion and noise degradations, with visual quality metrics indicating superior realism and pixel fidelity. The unified approach reduces inference time by approximately 15 % relative to sequential processing pipelines.

## Significance  
This work is significant because it is the first to formulate extremely low‑light RAW enhancement under realistic motion‑blurred acquisition conditions and solve it with a single, efficient neural flow model. By integrating physics‑based constraints into the refinement stage, the method preserves color fidelity and reflectance consistency while minimizing computational cost—key factors for practical deployment in mobile and embedded systems.

## Related Concepts  
- RAW tokenization  
- Domain‑conditioned representation calibration  
- MeanFlow (neural flow for image restoration)  
- SIDED dataset (motion blur + noise coupling)  
- Physics‑guided refinement model  
- Illumination reflectance consistency  
- Pixel fidelity preservation  
- Color preservation in low‑light enhancement
