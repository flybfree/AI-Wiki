# Summary: 2026-05-09_2005.14165-language-models-are-few-shot-learners.md
Saved: 2026-05-09 23:00
Source: 2026-05-09_2005.14165-language-models-are-few-shot-learners.md
Model: None

---


## Summary  
The paper “Language Models Are Few‑Shot Learners” (GPT‑3) argues that simply enlarging a language model—both in parameter count and the amount of text it is trained on—creates a system capable of performing many downstream tasks with only a handful of examples given at inference time. By training a 175 billion‑parameter decoder‑only transformer on 45 TB of raw text, GPT‑3 demonstrates that prompting with task‑specific examples can replace traditional fine‑tuning, achieving performance comparable to or better than state‑of‑the‑art models trained for each specific task. The contribution is a paradigm shift from task‑specific training to a single universal model that adapts at inference time through the prompt.

## Key Contributions  
- **Finding 1:** Model quality improves smoothly with scale; larger models exhibit emergent capabilities such as code generation, multi‑turn dialogue and reasoning that were not present in smaller architectures.  
- **Finding 2:** A single decoder‑only transformer can be prompted with zero‑shot or few‑shot examples to execute diverse tasks without any task‑specific training data.  
- **Finding 3:** The prompt functions as a programmatic instruction set, turning the model into a general‑purpose tool that “learns” by showing examples rather than by weight updates.

## Methodology  
The authors trained GPT‑3 using a standard autoregressive objective on a massive corpus (≈45 TB of text) with 175 billion parameters, employing the decoder stack of the Transformer architecture. Evaluation was performed by feeding the model prompts that contained task instructions and examples (zero‑shot, one‑shot, few‑shot). The performance was compared to fine‑tuned models trained specifically on each target task.

## Results  
Empirical results show a monotonic increase in accuracy as both parameter count and training data volume grow. GPT‑3 consistently outperformed the best fine‑tuned baselines across translation, question answering, reading comprehension, code generation and simple logical reasoning tasks. In many few‑shot settings it achieved zero‑shot or one‑shot performance that matched or exceeded prior state‑of‑the‑art results, confirming the “few‑shot” claim.

## Significance  
GPT‑3 introduced the concept of a *foundation model*—a single, broadly trained system that can be adapted to many downstream tasks via prompting. This unified paradigm underlies all subsequent large language models (e.g., ChatGPT, Claude, GPT‑4, Gemini) and reshaped research agendas toward scaling rather than task‑specific fine‑tuning.

## Related Concepts  
- Few‑shot learning: performing a task with only a few examples.  
- Prompt engineering: crafting prompts to guide model behavior.  
- Decoder‑only transformer architecture: the backbone of GPT‑3 and its successors.  
- Foundation models: large, general‑purpose models trained on diverse data.  
- Scaling laws: empirical relationships between model size, data, compute and performance.

[[2026-05-09_2005.14165-language-models-are-few-shot-learners.md]]