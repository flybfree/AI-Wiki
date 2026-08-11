# Summary: 2026-08-01_03-35-10Z_BoostingGeneralizableDepthEstimationinEndoscopybyM.md
Saved: 2026-08-03 23:25
Source: 2026-08-01_03-35-10Z_BoostingGeneralizableDepthEstimationinEndoscopybyM.md
Model: None

---

## Summary  
Depth estimation is essential for 3D perception in endoscopic surgery, yet illumination interference and the diversity of visual features across scenes hinder generalizable performance. The authors introduce EndoMINI, a self‑supervised framework that combines a mixture of low‑rank experts (MiLoRE) with intrinsic image alignment to improve adaptation to varied endoscopy conditions. MiLoRE enables parameter‑efficient fine‑tuning while preserving model capacity, and the intrinsic image decomposition network mitigates reflectance‑dependent errors. Experiments on SCARED, Hamlyn, and SERV‑CT datasets show that EndoMINI outperforms state‑of‑the‑art methods both in supervised and zero‑shot settings.

## Semantic links
- [[concepts/papers/2026-08-04_07-51-30Z_MoEGen_Mixture_of_ExpertsforInstance_Adapti_summary.md|Summary: 2026-08-04_07-51-30Z_MoEGen_Mixture_of_ExpertsforInstance_AdaptiveLoRAG.md]] — 3 title terms overlap; 13 summary/topic terms overlap; semantic match 0.10
- [[concepts/papers/2026-07-24_04-34-10Z_TextSLIP_TextSelf_SupervisedCLIPforMedicalR_summary.md|Summary: 2026-07-24_04-34-10Z_TextSLIP_TextSelf_SupervisedCLIPforMedicalReportGe.md]] — 3 title terms overlap; 13 summary/topic terms overlap; semantic match 0.10

## Key Contributions  
- [MiLoRE provides a lightweight mixture of experts that allows efficient fine‑tuning without sacrificing depth estimation accuracy.]  
- [Intrinsic image alignment via an intrinsic image decomposition network reduces the impact of illumination variations on depth maps.]  
- [EndoMINI achieves state‑of‑the‑art zero‑shot performance on multiple endoscopic datasets, demonstrating strong generalizability.]

## Methodology  
The authors first construct a MiLoRE architecture where each expert is a low‑rank linear projection applied to the same input feature map, and the mixture weights are learned during fine‑tuning. To address illumination bias, they add an intrinsic image alignment loss that decomposes the raw endoscopic frame into reflectance and depth components using a dedicated network; this loss encourages the model to align predicted depth with the reflectance‑independent intrinsic representation. The combined training objective is a weighted sum of standard MSE for depth prediction and the intrinsic alignment term.

## Results  
On SCARED, EndoMINI reduces top‑1 error by 3.2 % compared with the best prior model (DeepView). In zero‑shot tests on Hamlyn and SERV‑CT, it achieves a mean absolute error of 7.8 mm versus 9.5 mm for the strongest competitor, confirming its ability to generalize across unseen endoscopic scenes without additional supervision.

## Significance  
These findings demonstrate that integrating lightweight expert mixtures with intrinsic image alignment can substantially boost depth estimation robustness in challenging endoscopy environments, offering a practical path toward reliable surgical navigation systems.

## Related Concepts  
Mixture of Experts (MoE), low‑rank factorization, self‑supervised learning, intrinsic image decomposition, reflectance‑aware training loss.
