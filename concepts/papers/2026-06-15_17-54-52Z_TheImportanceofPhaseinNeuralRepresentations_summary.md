# Summary: 2026-06-15_17-54-52Z_TheImportanceofPhaseinNeuralRepresentations_AnInte.md
Saved: 2026-06-15 23:14
Source: 2026-06-15_17-54-52Z_TheImportanceofPhaseinNeuralRepresentations_AnInte.md
Model: qwen3.8-flash-next-iq3_xxs

---

## Summary
This paper investigates whether trained image classifiers internalize the classic Oppenheim-Lim finding that phase information in Fourier transforms carries more semantic identity than magnitude information. The author conducts causal interventions on the hidden layers of various neural network architectures, including PRISM2D, GFNet, ViT-B/16, and ResNet-50, to determine if predictions follow the phase or sign of transplanted features. The study reveals that most architectures rely heavily on phase or sign codes for identity recognition, while image-specific magnitude is largely dispensable for the final readout. However, the manifestation of this phase dependence varies significantly across architectures due to differences in rectification mechanisms and readout geometries, providing a mechanistic explanation for the observed texture-versus-shape biases in CNNs versus attention models.

## Key Contributions
- **Causal Validation of Phase Dependence**: The paper demonstrates that in architectures like PRISM2D, GFNet, and ViT-B/16, transplanting the phase of one image onto the magnitude of another causes the classifier’s prediction to follow the phase donor, confirming that identity is encoded in phase rather than magnitude.
- **Dispensability of Magnitude**: The study shows that deleting all image-specific magnitude information from hidden layers barely affects classification accuracy, suggesting that magnitude serves a secondary or non-essential role in the final decision-making process for these models.
- **Architectural Nuance in ResNet-50**: The author identifies a critical distinction in ResNet-50, where post-ReLU sign transplants appear ineffective. However, by intervening before the ReLU activation, a strong latent sign code is revealed in late blocks, showing that the phase dependence is masked by the architecture's rectification layers.
- **Mechanistic Explanation for Texture-Shape Gap**: The paper provides a unified mechanistic account explaining why CNNs and attention models exhibit different biases toward texture versus shape, attributing these differences to how phase/sign codes are exposed or hidden by specific architectural components like ReLUs and readout geometries.

## Methodology
The authors employ a causal intervention strategy inspired by the Oppenheim-Lim test, adapted for neural network internals. For pairs of images, the phase (or sign) of one image is transplanted onto the magnitude of the other at specific hidden layers within the network. The classifier’s output is then analyzed to determine which image’s identity dominates the prediction. The study tests multiple architectures, including PRISM2D, GFNet, ViT-B/16, and ResNet-50. To ensure robustness, the authors implement controls to rule out trivial cases where magnitude might simply stop depending on the image. For ResNet-50, specific interventions are performed both before and after ReLU activations to isolate the effect of rectification on the visibility of phase information. Additionally, a DC-only control is used to analyze how the readout consumes spatial averages.

## Results
The experiments show that for PRISM2D, GFNet, and ViT-B/16, predictions consistently follow the phase or sign donor, and removing image-specific magnitude has negligible impact on accuracy. This confirms that identity rides on phase in these models. In contrast, ResNet-50 initially appears to break this pattern because transplanting sign after ReLU layers has no effect. However, when the intervention is moved to before the ReLU, a strong latent sign code is detected in the late blocks. The DC-only control further reveals that the readout in ResNet-50 consumes a channel-wise spatial average. These results demonstrate that while all tested architectures share a phase/sign identity code, they expose it in different bases determined by their specific rectification and readout structures.

## Significance
This research provides a deeper mechanistic understanding of how modern image classifiers process visual information, bridging classical signal processing theory with deep learning interpretability. By showing that phase carries semantic identity across diverse architectures, it challenges the assumption that magnitude is equally important for classification. The findings offer a concrete explanation for the long-standing observation that CNNs are more texture-biased while attention models are more shape-biased, attributing this to architectural differences in how phase information is handled. This insight is crucial for developing more robust, interpretable, and generalizable vision models, as it highlights the importance of phase preservation and the potential pitfalls of rectification layers in hiding semantic information.

## Related Concepts
- Oppenheim-Lim Test
- Fourier Phase and Magnitude
- Neural Network Interpretability
- Causal Interventions in Deep Learning
- Texture vs. Shape Bias
- ReLU Rectification
- Attention Models (ViT, GFNet)
- Convolutional Neural Networks (ResNet)
- Semantic Identity in Representations
