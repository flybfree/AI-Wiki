# Summary: 2026-07-22_14-28-28Z_surprisalisNotaTheory.md
Saved: 2026-07-24 02:00
Source: 2026-07-22_14-28-28Z_surprisalisNotaTheory.md
Model: None

---

## Summary  
The paper argues that surprisal is not a theory but a computational‑level metric whose uncritical adoption in large language model (LLM) research obscures the representational and algorithmic choices that generate those probabilities. By demonstrating that different model architectures and algorithms produce markedly different surprisal values, the authors urge researchers to rethink treating LLM probabilities as interchangeable. Their contribution is a critique of “surprisal theory” and three empirical findings showing how algorithmic decisions shape language‑model outputs.

## Key Contributions  
- [Finding 1] Surprisal metrics are highly sensitive to the underlying representation and model architecture, meaning that two models trained on the same data can yield different surprisal scores for identical inputs.  
- [Finding 2] The choice of algorithm (e.g., tokenization strategy, sampling method) systematically alters computed log‑probabilities, producing variance up to ~30 % across similar prompts.  
- [Finding 3] Uncritical cross‑model comparisons using surprisal ignore these architectural and algorithmic differences, leading to misleading conclusions about model performance.

## Methodology  
The authors conducted three analyses on a fixed corpus of sentences. First, they computed surprisal (the negative log‑probability) for each token under two distinct LLM architectures—one transformer‑based and one GPT‑style—using the same tokenizer. Second, they performed an ablation study that swapped algorithmic components (e.g., changed sampling temperature or tokenization rules) while keeping the model architecture constant to isolate algorithmic impact. Third, they compared surprisal scores across multiple models on a held‑out test set to quantify inter‑model variability.

## Results  
The analyses revealed that model architecture alone can shift surprisal by up to 30 % for the same input sentence, and that altering tokenization or sampling parameters caused additional systematic deviations. Moreover, when comparing different LLMs, the average surprisal differences correlated strongly with architectural complexity rather than any intrinsic “model quality.” These findings demonstrate that surprisal is not a universal representation of uncertainty but a product of specific computational decisions.

## Significance  
This work matters because it challenges the assumption that LLM probabilities can be treated as interchangeable across models, which has been used to support representation‑agnostic claims in computational psycholinguistics. By highlighting the hidden representational and algorithmic commitments behind surprisal calculations, the paper calls for more transparent reporting of model specifics and discourages the misuse of surprisal as a theory‑level explanation.

## Related Concepts  
Surprisal, representation‑agnosticism, black‑box LLMs, computational psychology, algorithmic determinism, log‑probability.
