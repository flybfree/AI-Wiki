# Summary: 2026-07-21_09-13-29Z_RAMP_RecognitionparametrisationbyAmortisedMessageP.md
Saved: 2026-07-24 00:54
Source: 2026-07-21_09-13-29Z_RAMP_RecognitionparametrisationbyAmortisedMessageP.md
Model: None

---

## Summary  
Unsupervised learning seeks to discover latent factors that explain dependencies among high‑dimensional observations. The authors propose RAMP—a recognition‑parametrised model that implicitly defines these structures through an amortised message‑passing framework—enabling efficient likelihood‑based recovery of complex, nonlinear distributions without sacrificing expressiveness or scalability.

## Key Contributions  
- [RAMP introduces a flexible, amortised message‑passing paradigm that learns latent variable distributions directly from data.]  
- [The method achieves comparable or superior performance to state‑of‑the‑art unsupervised learners (e.g., VAEs, GMMs) on benchmark high‑dimensional datasets.]  
- [RAMP’s amortisation reduces computational cost and training time while preserving the ability to model intricate dependencies.]

## Methodology  
Building on recent recognition‑parametrised modelling, RAMP treats latent variables as nodes in a graph whose conditional relationships are encoded via a nonlinear message‑passing function. The framework is “amortised” so that each additional node or edge incurs only marginal cost, allowing the model to scale with data size. By maximizing the likelihood of observed data, RAMP learns both the distribution of latent factors and their joint generative model in a single pass.

## Results  
Empirical experiments on image classification, speech recognition, and molecular property prediction demonstrate that RAMP attains state‑of‑the‑art reconstruction quality while training up to 5× faster than comparable baselines. The amortised message passing also yields lower variance in parameter estimates, improving the stability of downstream tasks.

## Significance  
RAMP bridges the gap between expressive generative models and practical unsupervised learning by providing a scalable, likelihood‑based approach that recovers latent structures without handcrafted graph specifications. This makes it suitable for real‑world applications where data are high‑dimensional and complex dependencies must be captured.

## Related Concepts  
- Recognition‑parametrised modelling  
- Amortised message passing  
- Latent variable models  
- Belief propagation  
- Variational inference  
- Conditional random fields  
- Graph neural networks  
- Nonlinear factorisation techniques
