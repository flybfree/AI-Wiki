---
title: Biologically Informed Representation Learning for Robust Cross-Center Generalization of MALDI-TOF Mass Spectrometry
published: 2026-08-08T15:19:53Z
authors: Alejandro L. García-Navarro, Carlos Sevilla-Salcedo, Belén Rodríguez-Sánchez, Vanessa Gómez-Verdejo
url: http://arxiv.org/abs/2608.08182v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Biologically Informed Representation Learning for Robust Cross-Center Generalization of MALDI-TOF Mass Spectrometry

## Abstract
Machine learning models for MALDI-TOF mass spectrometry have shown considerable promise for clinical microbiology tasks such as microbial identification and antimicrobial resistance prediction. However, their deployment across institutions remains limited by domain shift, as acquisition-specific variability often leads models to capture technical artifacts rather than transferable biological information. Existing representation learning approaches primarily address this problem through statistical domain alignment while largely overlooking the biological supervision naturally available in microbiology datasets. We introduce DALMA, a probabilistic representation learning framework that jointly models acquisition-specific variability and biological supervision to learn biologically structured latent representations. By combining domain-specific reconstruction with biologically guided representation learning, DALMA learns transferable representations that generalize across heterogeneous clinical centers without requiring institution-specific components at inference, enabling zero-shot deployment on previously unseen sites. We evaluate DALMA on a multi-center benchmark comprising seven datasets from three countries. DALMA consistently achieves state-of-the-art zero-shot microbial identification across two held-out clinical centers, while the learned representations also transfer effectively to antimicrobial resistance prediction. Furthermore, latent-space novelty estimation enables reliable selective prediction under previously unseen domain shifts. These results demonstrate that biologically informed representation learning provides an effective strategy for robust and transferable ML in clinical microbiology.

## Metadata
- **Published**: 2026-08-08T15:19:53Z
- **Authors**: Alejandro L. García-Navarro, Carlos Sevilla-Salcedo, Belén Rodríguez-Sánchez, Vanessa Gómez-Verdejo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08182v1)