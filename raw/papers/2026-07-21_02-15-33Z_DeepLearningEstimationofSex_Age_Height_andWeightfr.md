---
title: Deep Learning Estimation of Sex, Age, Height, and Weight from CT-derived Digitally Reconstructed Radiographs
published: 2026-07-21T02:15:33Z
authors: Tomohiro Kikuchi, Kohei Yamamoto, Yukihiro Nomura, Yosuke Yamagishi, Takeharu Yoshikawa, Toshiaki Akashi, Jun Kamohara, Hiroyuki Fujii, Harushi Mori
url: http://arxiv.org/abs/2607.18638v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Deep Learning Estimation of Sex, Age, Height, and Weight from CT-derived Digitally Reconstructed Radiographs

## Abstract
Purpose: To develop and validate a deep learning ensemble for estimating adult sex, age, height, and weight from coronal digitally reconstructed radiographs (DRRs) generated from diagnostic CT. Materials and Methods: This retrospective study included 128,621 CT examinations from 80,004 adults at nine institutions in Japan. Three multitask models-ConvNeXt-Base, ViT-Base/16, and MaxViT-Base-were fine-tuned using coronal DRRs and combined by weighted averaging. Data were split by institution into training (114,147 examinations; seven institutions), tuning (4,305; one institution), and test (10,169; one institution) sets; generalizability was assessed on two non-Japanese datasets. Accuracy and mean absolute error (MAE) were used to evaluate sex classification and age, height, and weight regression, respectively. Body surface area (BSA)-corrected heart and liver volume trends were compared using true versus estimated height and weight. Results: In the test set (median age, 69.9 years; 4,899 of 10,169 [48.2%] male), overall sex-classification accuracy was 0.997 (95% CI, 0.996-0.998), and MAEs were 3.57 years (3.51-3.63), 2.59 cm (2.54-2.64), and 3.40 kg (3.34-3.47) for age, height, and weight, respectively. In examinations covering the chest through pelvis, accuracy was 1.000, and MAEs were 3.15 years, 2.28 cm, and 3.18 kg, respectively. BSA calculated from estimated values reproduced age-related heart and liver volume trends obtained using true values. On non-Japanese datasets, height error increased but was reduced by continued fine-tuning. Conclusion: The ensemble estimated adult sex, age, height, and weight from CT-derived DRRs, with generally lower errors in examinations with broader anatomical coverage.

## Metadata
- **Published**: 2026-07-21T02:15:33Z
- **Authors**: Tomohiro Kikuchi, Kohei Yamamoto, Yukihiro Nomura, Yosuke Yamagishi, Takeharu Yoshikawa, Toshiaki Akashi, Jun Kamohara, Hiroyuki Fujii, Harushi Mori
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18638v1)