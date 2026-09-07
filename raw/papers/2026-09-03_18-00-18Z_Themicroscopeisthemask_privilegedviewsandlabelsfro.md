---
title: The microscope is the mask: privileged views and labels from a cryo-ET forward model
published: 2026-09-03T18:00:18Z
authors: Bogdan Toader, Kiarash Jamali, Tanmay A. M. Bharat, Sjors H. W. Scheres
url: http://arxiv.org/abs/2609.04325v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The microscope is the mask: privileged views and labels from a cryo-ET forward model

## Abstract
We explore the use of simulated data for training a model for protein annotation in crowded cryo-electron tomography volumes reconstructed from images collected at limited tilt angles and severely corrupted by the measurement operator. Firstly, we leverage the corruptions imposed by the forward model to generate domain-specific augmented paired views of the exact same scene for an invariance objective integrated into the LeJEPA self-supervised training framework. Secondly, we use additional information from the simulation pipeline such as the positions and identity of proteins in the simulated volumes to inform the architecture of the model and the loss function, so that semantic information is localised at protein positions in the resulting dense feature volume. The resulting model, CARNIVAL, is evaluated without finetuning on classification and detection tasks in real tomograms, using a benchmark dataset containing multiple protein types and two tomogram processing types. We show that CARNIVAL outperforms a state-of-the-art model trained using a contrastive objective on simulated data but without forward model-based paired views or privileged information.

## Metadata
- **Published**: 2026-09-03T18:00:18Z
- **Authors**: Bogdan Toader, Kiarash Jamali, Tanmay A. M. Bharat, Sjors H. W. Scheres
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04325v1)