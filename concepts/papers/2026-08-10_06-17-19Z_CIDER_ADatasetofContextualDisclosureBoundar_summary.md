# Summary: 2026-08-10_06-17-19Z_CIDER_ADatasetofContextualDisclosureBoundariesforP.md
Saved: 2026-08-10 23:38
Source: 2026-08-10_06-17-19Z_CIDER_ADatasetofContextualDisclosureBoundariesforP.md
Model: None

---

## Summary  
The paper introduces CIDER, a dataset of 14,850 human annotations that capture users’ nuanced disclosure boundaries across 169 individuals and 60 interpersonal communication scenarios. Each scenario presents nine sharing variants under different AI‑mediated conditions, forming 1,650 contextual boundary sets per user. The core contribution is a task in which large language models must predict a user’s disclosure decision from limited historical examples while receiving varying amounts of contextual information. By evaluating this task across twelve open and proprietary models, the authors demonstrate that personalization can boost prediction accuracy by up to 11.41 percentage points using only six examples.

## Key Contributions  
- [Finding 1] CIDER provides a richly annotated dataset of user‑specific disclosure boundaries spanning multiple communication roles and AI conditions, enabling systematic study of privacy preference alignment.  
- [Finding 2] In‑context personalization improves model performance by roughly eleven point four percent with just six historical examples, showing that few‑shot adaptation can capture fine‑grained user preferences.  
- [Finding 3] Larger, more capable models such as GPT‑5.4 and Claude Sonnet 4.6 leverage semantic context effectively, whereas smaller models tend to rely on coarse heuristics about disclosure granularity and identifiability; only Claude Sonnet 4.6 achieves balanced gains in both false‑positive and false‑negative rates.

## Methodology  
The authors assembled CIDER by having each of the 169 users evaluate nine sharing variants within a scenario, recording their decision to disclose or withhold information under six distinct AI‑mediated conditions (e.g., no AI assistance, partial assistance). For every user, role, and condition they generated a boundary set that records the observed disclosure pattern. The evaluation task then asks models to predict a user’s future decision based on a small number of such historical boundaries while providing additional contextual cues. This setup isolates the impact of personalization versus model capability.

## Results  
Across twelve language models, baseline accuracy ranges from 68 % to 79 %. When six boundary examples are supplied and the model is prompted with full context, average accuracy rises to 80.5 %, an improvement of up to 11.41 percentage points over the best non‑personalized baseline. GPT‑5.4 (medium reasoning effort) reaches 83.2 % accuracy, while Claude Sonnet 4.6 attains 84.7 %. Smaller models such as LLaMA‑2‑7B plateau around 79.1 %, indicating reliance on structural heuristics rather than semantic understanding. Notably, personalization often shifts the false‑positive rate up while lowering the false‑negative rate, creating imbalances; only Claude Sonnet 4.6 shows a balanced improvement in both metrics.

## Significance  
CIDER bridges the gap between abstract privacy norms and concrete user behavior, providing a benchmark for evaluating how LLMs respect individual disclosure boundaries. The findings highlight that inference‑time personalization holds promise but is not universally beneficial; larger models can exploit context better yet may introduce trade‑offs in error distribution. This dataset thus serves as a critical resource for advancing personalized privacy alignment in conversational AI.

## Related Concepts  
- In‑context learning  
- Privacy preference modeling  
- Disclosure boundaries  
- Contextual information  
- Model interpretability  
- False positive / false negative rates
