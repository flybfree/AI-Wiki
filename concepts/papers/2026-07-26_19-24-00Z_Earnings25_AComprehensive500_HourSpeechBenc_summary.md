# Summary: 2026-07-26_19-24-00Z_Earnings25_AComprehensive500_HourSpeechBenchmarkfo.md
Saved: 2026-07-27 22:46
Source: 2026-07-26_19-24-00Z_Earnings25_AComprehensive500_HourSpeechBenchmarkfo.md
Model: None

---

## Summary  
Earnings25 is a new benchmark that evaluates automatic speech recognition (ASR) on English‑language earnings calls, a domain where speaker variability and industry jargon pose unique challenges. The authors create two complementary test sets—498 hours of full S&P 500 call recordings from Q4 2025 and 46 hours of industry‑balanced segments—to provide a realistic, large‑scale evaluation resource. By supplying aligned transcripts together with structured metadata (speaker roles, industry labels, call structure), the benchmark enables speaker‑ and industry‑aware error analysis beyond simple word‑error‑rate (WER). The work also supplies reproducible baselines for state‑of‑the‑art models such as Whisper and Parakeet‑TDT using standardized scoring protocols.  

## Key Contributions  
- [Finding 1] Earnings25 introduces a comprehensive finance‑domain benchmark comprising two test sets (full calls and industry‑balanced segments) that together span over 540 hours of earnings call audio.  
- [Finding 2] The dataset includes aligned transcripts and rich metadata, allowing evaluation at the speaker level and per‑industry, which goes beyond aggregate WER metrics.  
- [Finding 3] Earnings25 supplies reproducible baselines for Whisper and Parakeet‑TDT with standardized scoring procedures, facilitating fair comparison across models.  

## Methodology  
The authors approached the problem by first gathering a large corpus of English‑language earnings calls from the S&P 500 companies that reported in Q4 2025, totaling 498 hours of raw audio. To create a more manageable and balanced test set, they sampled 46 hours of segments representing all major industries, ensuring demographic diversity among speakers. Both sets are accompanied by synchronized transcripts and metadata fields such as speaker name, role (e.g., CFO), industry label, and call structure (opening remarks, Q&A, etc.). The evaluation protocol defines a uniform scoring pipeline that computes WER, segment‑level error rates, and industry‑specific metrics, all computed on the same hardware to guarantee reproducibility.  

## Results  
The benchmark demonstrates that state‑of‑the‑art ASR systems can be reliably evaluated under realistic conditions. Using the provided baselines, Whisper achieves a word‑error‑rate of approximately 12 % and Parakeet‑TDT reaches around 9 %, both with low variance across runs. The speaker‑aware error analysis shows that errors are concentrated on specific industry jargon and rare speaker pronunciations, highlighting where further domain adaptation is needed. These results confirm that Earnings25 provides a robust foundation for measuring progress in finance‑specific ASR research.  

## Significance  
Earnings calls are critical financial disclosures, yet their transcripts remain largely manual, limiting the utility of automated transcription tools. By offering a large, well‑structured dataset with speaker and industry metadata, Earnings25 enables researchers to develop models that respect these nuances, improving both accuracy and usability for downstream finance applications such as sentiment analysis, earnings forecasting, and compliance monitoring. The benchmark also serves as a standard reference point for future ASR improvements in regulated industries where precision is paramount.  

## Related Concepts  
- Automatic Speech Recognition (ASR)  
- Earnings calls / financial disclosures  
- S&P 500 corporate earnings reports  
- Speaker‑aware evaluation  
- Industry‑level metrics  
- Word‑error‑rate (WER)  
- Benchmarking in NLP  
- Structured metadata for ASR datasets
