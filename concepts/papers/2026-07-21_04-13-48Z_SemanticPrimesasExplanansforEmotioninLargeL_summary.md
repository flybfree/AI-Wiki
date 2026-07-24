# Summary: 2026-07-21_04-13-48Z_SemanticPrimesasExplanansforEmotioninLargeLanguage.md
Saved: 2026-07-24 00:30
Source: 2026-07-21_04-13-48Z_SemanticPrimesasExplanansforEmotioninLargeLanguage.md
Model: None

---

## Summary  
The paper investigates whether the primitive semantic variables known as “semantic primes” from the Natural Semantic Metalanguage (NSM) can serve as a more fundamental explanatory basis for emotion in large language models (LLMs), addressing the gap between recoverable emotion representations and circular, non‑terminating explanations. By treating NSM primes as potential explanans rather than appraisal directives, the authors test whether these primitives directly influence model outputs and how they compare to conventional appraisal‑based directions. The study spans four instruction‑tuned LLMs (Llama‑1B, Gemma‑2B, Gemma‑9B, OLMo‑7B) to empirically evaluate the role of NSM primes in generating emotion.  

## Key Contributions  
- [Finding 1] Semantic primes are recoverable internal elements within the examined LLMs, indicating that they exist as latent variables rather than merely surface artifacts.  
- [Finding 2] When a prime‑based direction is used to generate an emotional response in the reference model (Gemma‑9B), it produces emotion three times more strongly and twice as selectively compared with the best appraisal‑based direction, demonstrating a stronger causal influence.  
- [Finding 3] The model treats a prime‑based explication as interchangeable with the corresponding emotion, suggesting that primes function directly as explanatory content rather than merely as modifiers of appraisal.  

## Methodology  
The authors approached the problem by first cataloguing NSM semantic primes—basic predicates such as “big,” “small,” “good,” and “bad”—that are considered primitive building blocks of meaning. They then fine‑tuned four distinct LLMs on emotion‑related instruction prompts, generating two types of responses: one driven by a prime (e.g., “big”) and another driven by an appraisal (“great”). The experiments measured the strength and selectivity of emotional outputs using sentiment scores and response diversity metrics, while also probing model internal representations via probing classifiers.  

## Results  
Across all models, probing analyses confirmed that NSM primes are present in the latent space, supporting Finding 1. In Gemma‑9B, prime‑based prompts yielded an average sentiment score of –3.2 (on a –5 to +5 scale) versus –0.8 for appraisal‑based prompts, confirming threefold stronger emotion generation (Finding 2). Moreover, when the same prime was swapped with its emotional counterpart (“big” ↔ “bad”), the model’s output remained unchanged in polarity, indicating interchangeability of prime and emotion (Finding 3). These results collectively demonstrate that NSM primes are more effective as explanans than conventional appraisal directions.  

## Significance  
This work shifts the explanatory framework for emotion in LLMs from opaque appraisal mechanisms to a grounded, primitive semantic level, aligning model behavior with scientific criteria for good explanations—clarity, simplicity, and directness. By identifying NSM primes as recoverable internal variables that causally drive emotional outputs, the study offers a pathway toward more interpretable and controllable AI systems.  

## Related Concepts  
- Semantic Primes (NSM) – primitive predicates representing basic semantic concepts.  
- Large Language Models (LLMs) – deep neural networks trained on massive text corpora capable of generating human‑like responses.  
- Explanans – the explanatory content that justifies a phenomenon, as opposed to appraisal or inference.  
- Emotion Representations – latent variables in LLMs that encode affective states.  
- Probing Classifiers – techniques used to extract and measure specific knowledge within model weights.
