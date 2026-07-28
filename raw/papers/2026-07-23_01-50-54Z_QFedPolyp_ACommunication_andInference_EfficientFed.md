---
title: QFedPolyp: A Communication- and Inference-Efficient Federated Learning Framework for Polyp Segmentation
published: 2026-07-23T01:50:54Z
authors: Madan Baduwal, Priyanka Paudel
url: http://arxiv.org/abs/2607.22743v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QFedPolyp: A Communication- and Inference-Efficient Federated Learning Framework for Polyp Segmentation

## Abstract
Background and Objective: Automatic polyp segmentation supports computer-aided diagnosis and early colorectal cancer detec- tion. Centralized deep learning requires hospitals to share sensitive medical data, while federated learning preserves privacy but introduces high communication costs through repeated transmission of full-precision model parameters. We propose QFedPolyp, a communication- and inference-efficient federated learning framework for collaborative polyp segmentation.   Methods: QFedPolyp combines quantization-aware training with low-precision model communication. Each hospital locally trains a lightweight U-Net on private data while simulating quantization during training. Clients transmit quantized model parameters to a central server, where they are reconstructed and aggregated using Federated Averaging. Evaluation is performed on Kvasir-SEG, CVC-ClinicVideoDB, PolypGen, and BKAI-IGH NeoPolyp.   Results: Full-precision federated training achieves Dice scores of 0.910 on Kvasir-SEG and 0.930 on CVC-ClinicVideoDB. Uni- form 8-bit communication reduces transmission cost by approximately 4 times while preserving competitive segmentation accuracy. Quantized models also achieve up to 1.5 times faster inference than full-precision models.   Conclusions: QFedPolyp enables privacy-preserving collaborative polyp segmentation with reduced communication overhead and faster inference. The resulting lightweight models are suitable for real-time clinical deployment.

## Metadata
- **Published**: 2026-07-23T01:50:54Z
- **Authors**: Madan Baduwal, Priyanka Paudel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22743v1)