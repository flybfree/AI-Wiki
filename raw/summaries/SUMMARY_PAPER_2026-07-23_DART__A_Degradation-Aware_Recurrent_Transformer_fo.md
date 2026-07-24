---
title: DART: A Degradation-Aware Recurrent Transformer for Archival Film Restoration
url: http://arxiv.org/abs/2607.21219v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_11-34-51Z_DART_ADegradation_AwareRecurrentTransformerforArch.md
generated_at: 2026-07-23 23:19
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper introduces DART, a degradation‑aware recurrent transformer designed to restore archival film footage that suffers from multiple compound artifacts such as scratches, dust, blur and photometric aging. By explicitly modeling a soft defect mask across time, DART guides the restoration process to focus on damage location and severity rather than relying solely on reconstruction loss. Experiments demonstrate that DART achieves higher no‑reference perceptual quality compared with previous methods while maintaining compactness and efficiency.

## Key Takeaways  
- DART predicts a soft defect mask through time, allowing the model to propagate information about where and how severe each artifact is.  
- The predicted mask is used to condition temporal fusion and influence the restoration network’s behavior, making the process explicitly aware of film damage.  
- On real archival benchmarks, DART improves no‑reference perceptual quality over prior architectures without sacrificing model size or computational cost.

## Context  
Restoring historical video often requires models that understand the physical nature of degradation rather than just minimizing reconstruction error. This work advances AI methods for media preservation by integrating explicit artifact awareness into recurrent transformers, a step toward more robust and interpretable restoration pipelines.

## Implications  
For archival institutions and digital heritage projects, DART offers a practical solution to restore fragile film without extensive manual labeling or clean reference data. Practitioners can leverage the compact model to produce cleaner, temporally consistent restorations that preserve visual integrity while reducing computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21219v1)
