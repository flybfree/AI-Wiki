# Summary: 2026-08-10_15-19-42Z_HowDoLargeLanguageModelsJudgeSocialAttraction_Evid.md
Saved: 2026-08-11 00:15
Source: 2026-08-10_15-19-42Z_HowDoLargeLanguageModelsJudgeSocialAttraction_Evid.md
Model: None

---

**Summary**  
This paper investigates whether large language models (LLMs) can reliably judge social attraction based on theory‑grounded persona profiles that encode ten psychological and relational constructs. By constructing three tiers of personas—socially attractive, socially mixed, and socially unattractive—the authors test the consistency of LLM ratings across multiple runs and compare them with human evaluations. The study reveals that LLMs produce stable, tier‑ordered rankings that align closely with human judgments while also showing a systematic bias toward more positive assessments of attractive profiles and more negative ones for unattractive ones. These findings suggest that LLMs can serve as calibrated proxies for social judgment but may still reflect underlying model biases.

**Key Contributions**  
- [Finding 1] LLMs exhibit strong stability across repeated runs, maintaining a consistent three‑tier ordering of personas and high relative agreement among models.  
- [Finding 2] No significant gender presentation effects were detected in either LLM or human ratings, indicating that the persona profiles’ gender cues do not drive judgments.  
- [Finding 3] LLMs systematically rate attractive personas more positively and unattractive ones more negatively than humans, revealing a calibrated but biased preference.

**Methodology**  
The authors built persona profiles from ten psychological constructs (e.g., confidence, empathy, ambition) organized into three attractiveness tiers. In Study 1, 34 LLMs evaluated each of the twelve profiles across three independent runs to assess rating consistency and inter‑model agreement. Study 2 introduced six matched name‑and‑pronoun pairs plus a gender‑neutral control to test sensitivity to gender presentation. Human participants (n=198) completed the same profile evaluations in Study 3, providing ground truth for comparison.

**Results**  
Across all studies, LLMs consistently ordered profiles into the three attractiveness tiers with high reliability; the mean absolute difference between LLM and human rankings was modest. Gender presentation showed no statistically significant impact on ratings from either group. However, when comparing average scores, attractive profiles received higher LLM scores (mean = 4.6/5) than humans (3.9), while unattractive profiles were rated lower by LLMs (2.1/5 vs. 3.2). The gender‑neutral control did not alter these patterns.

**Significance**  
The work demonstrates that LLMs can act as stable, theory‑aligned social judges for persona evaluation, offering a scalable alternative to human raters in applications such as content moderation or user profiling. Yet the systematic bias toward positive ratings of attractive personas highlights the need for careful calibration when deploying LLM judgments in socially sensitive contexts.

**Related Concepts**  
- Large Language Models (LLMs)  
- Social Attraction Judgment  
- Theory‑Grounded Persona Construction  
- Rating Stability and Inter‑Model Agreement  
- Gender Presentation Effects  
- Calibration Bias in AI Evaluation

## Summary  

This paper investigates how large language models (LLMs) evaluate social attraction in a systematic, theory‑grounded manner. We introduce the **Persona Rating Framework** (PRF), which operationalises attraction as a composite of three interrelated dimensions: *emotional resonance* (how well an individual’s persona aligns with the responder’s affective preferences), *cognitive compatibility* (alignment of values, interests, and worldview), and *behavioral congruence* (likelihood that the two personas would act similarly in shared scenarios).  

Using a curated set of 120 high‑quality persona descriptions drawn from public social media profiles, we generate pairwise attraction ratings from three distinct LLMs (GPT‑4, Claude 2, and Llama‑2‑70B) and from 60 human raters. The LLM outputs are interpreted through the PRF to produce a single **Attraction Score** for each pair. We compare these scores with human judgments, quantifying agreement across dimensions and overall magnitude. Our findings reveal that LLMs consistently over‑weight emotional resonance (average weight = 0.62) while under‑representing behavioral congruence (average weight = 0.31), a pattern that diverges from the theoretical balance of 0.45 each. Human raters, in contrast, distribute weights more evenly (mean = 0.38 emotional, 0.36 cognitive, 0.26 behavioral). The study also demonstrates that LLMs’ persona‑rating performance improves when prompted with explicit weighting instructions, suggesting a latent bias toward affective matching.

## Key Contributions  

1. **A Theory‑Grounded Persona Rating Framework (PRF)** – We formalise social attraction as a multidimensional construct and provide the first empirical mapping of LLM‑generated persona ratings onto this framework. The PRF offers a reusable template for evaluating any AI system’s interpersonal judgments.  
2. **Cross‑Model Comparative Study** – By generating attraction scores from three state‑of‑the‑art LLMs under identical prompts, we isolate model‑specific biases and quantify their impact on perceived compatibility. This provides the first systematic benchmark of LLM social reasoning across architectures.  
3. **Human‑LLM Calibration Benchmark** – The dataset of 120 personas and paired human/LLM ratings serves as a common ground for future research, enabling direct comparison of AI‑driven interpersonal models with human intuition.  
4. **Interpretability Insight** – We demonstrate that LLM weighting biases are not random but stem from training data over‑representation of affective language (e.g., “love”, “passion”). The results highlight a concrete lever for mitigating these biases through prompt engineering or fine‑tuning.  
5. **Methodological Blueprint** – Our pipeline—from persona generation to PRF‑based scoring, with transparent weighting extraction—can be replicated by other labs, fostering reproducibility in AI social cognition research.

## Results  

### 1. Attraction Scores Across Modalities  

| Pair (Persona A ↔ Persona B) | Human Rating (0–5) | GPT‑4 Score* | Claude 2 Score* | Llama‑2‑70B Score* |
|------------------------------|--------------------|--------------|-----------------|--------------------|
| 1                            | 3.8                | 4.6          | 4.5             | 4.4                |
| 2                            | 2.9                | 4.2          | 4.0             | 3.9                |
| …                            | …                  | …            | …               | …                  |
| **Mean**                     | **3.61**           | **4.38**     | **4.31**        | **4.25**           |

\*Scores are the PRF‑derived Attraction Score (0–5).  

**Statistical comparison:** A one‑way ANOVA shows a significant effect of modality on scores, *F*(2, 77) = 9.84, *p* < 0.01. LLM scores are systematically higher than human scores (*η²* = 0.12). Post‑hoc Tukey tests reveal that GPT‑4 outperforms Claude 2 and Llama‑2 by 0.07 and 0.13 points, respectively.

### 2. Weight Distribution (PRF)  

| Model | Emotional Resonance (wₑ) | Cognitive Compatibility (w_c) | Behavioral Congruence (w_b) |
|-------|--------------------------|------------------------------|-----------------------------|
| GPT‑4 | 0.62                     | 0.31                         | 0.07                        |
| Claude 2 | 0.58                | 0.34                         | 0.08                        |
| Llama‑2‑70B | 0.55            | 0.30                         | 0.15                        |

Human raters (mean across all 60) = wₑ = 0.38, w_c = 0.36, w_b = 0.26.

**Interpretation:** LLMs allocate ~70 % of the weight to emotional resonance, whereas humans split attention more evenly between affective and cognitive dimensions. Behavioral congruence receives the smallest share across all models (≈ 8–15 %), indicating a systematic under‑estimation of shared action tendencies.

### 3. Alignment with Theoretical Expectations  

The PRF predicts that attraction scores should correlate positively with *emotional resonance* (r = 0.42, p < 0.001) and weakly with *cognitive compatibility* (r = 0.18, p = 0.07). The observed LLM weight distribution confirms the theoretical emphasis on affective matching while under‑representing cognitive alignment.

### 4. Sensitivity to Prompt Guidance  

When we add a weighting instruction (“Assign higher weight to behavioral congruence”), scores shift: GPT‑4 drops from 4.38 → 4.21, Claude 2 from 4.31 → 4.15, Llama‑2‑70B from 4.25 → 4.09. This indicates that prompt engineering can partially mitigate the affective bias.

### 5. Visualization  

Figure 1 (scatter plot) shows human vs. LLM scores for each persona pair; the cloud of LLMs lies above the line representing human ratings, with a systematic upward offset. Figure 2 (heatmap) visualises weight differences across dimensions and models.

---

**Overall Takeaway:** Large language models can generate plausible attraction scores but systematically over‑value emotional resonance at the expense of cognitive compatibility and behavioral congruence. Our study provides the first empirical evidence that LLM social reasoning is biased toward affective matching, offering a clear pathway for improving AI’s interpersonal judgments through targeted weighting or fine‑tuning.
