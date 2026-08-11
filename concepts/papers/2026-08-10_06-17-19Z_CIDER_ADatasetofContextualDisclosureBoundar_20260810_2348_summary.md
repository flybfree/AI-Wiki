# Summary: 2026-08-10_06-17-19Z_CIDER_ADatasetofContextualDisclosureBoundariesforP.md
Saved: 2026-08-10 23:48
Source: 2026-08-10_06-17-19Z_CIDER_ADatasetofContextualDisclosureBoundariesforP.md
Model: None

---

## Summary  
This paper introduces CIDER, a dataset designed to capture the nuanced and context-dependent disclosure boundaries that individuals set in interpersonal communication when sharing information with AI systems. The goal is to align large language models (LLMs) with human privacy preferences by modeling how users decide what to disclose based on specific contexts, roles, and AI-mediated conditions. CIDER provides a richly annotated dataset of 14,850 observations across 60 communication scenarios, enabling evaluation of how well LLMs can predict user-specific disclosure decisions using limited historical examples. The study demonstrates that personalization improves prediction accuracy but often introduces imbalances in error types, highlighting both progress and limitations in inference-time privacy alignment.

## Key Contributions  
- [Finding 1] CIDER is the first dataset to systematically evaluate contextual disclosure boundaries across diverse interpersonal communication scenarios involving AI-mediated information sharing.  
- [Finding 2] In-context personalization improves prediction accuracy by up to 11.41 percentage points using only six historical examples, revealing that models can learn from minimal user-specific context.  
- [Finding 3] Larger models like GPT-5.4 and Claude Sonnet 4.6 better leverage semantic context for accurate predictions, while smaller models rely on structured heuristics based on disclosure granularity and identifiability.

## Methodology  
The authors constructed CIDER by collecting human annotations from 169 users across 60 communication scenarios where privacy norms are violated. Each scenario involves nine sharing variants under different AI conditions (e.g., direct vs. mediated), and each user makes a disclosure decision for each variant, forming a boundary set. The task is to predict these decisions using only six historical examples of the same user’s behavior. Models are evaluated across both open-source and proprietary systems, with performance measured by prediction accuracy and error type distribution.

## Results  
Across 12 models, personalization significantly improves prediction accuracy compared to non-personalized baselines. However, improvements often come at the cost of imbalanced false-positive or false-negative rates. Only Claude Sonnet 4.6 achieves balanced gains in both error types. Larger models with medium reasoning effort perform best, suggesting that semantic understanding and contextual reasoning are critical for accurate privacy preference modeling.

## Significance  
CIDER bridges a key gap between general privacy norms and individual disclosure boundaries, enabling more realistic evaluation of AI systems’ alignment with human values. It demonstrates the potential of inference-time personalization to enhance privacy-aware interactions but also exposes challenges in maintaining balanced performance across error types. The dataset serves as a critical resource for advancing personalized privacy alignment in conversational AI.

## Related Concepts  
Contextual disclosure boundaries, privacy preference alignment, large language models (LLMs), inference-time personalization, false-positive/false-negative rates, interpersonal communication scenarios, human-AI interaction, disclosure granularity, identifiability.
