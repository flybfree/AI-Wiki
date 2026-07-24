# Summary: 2026-07-21_12-37-41Z_BenchmarkingHumanandAutomaticSpeechRecognitionofDi.md
Saved: 2026-07-24 01:09
Source: 2026-07-21_12-37-41Z_BenchmarkingHumanandAutomaticSpeechRecognitionofDi.md
Model: None

---

## Summary  
The paper seeks to benchmark human listeners and state‑of‑the‑art automatic speech recognition (ASR) systems on a diverse set of Dutch child, older adult, and Flemish utterances. It evaluates whether modern ASR models can match or exceed native performance under varying acoustic conditions such as speaker age and regional accents. The study demonstrates that Google Telephony achieved the best results among the ASR systems, often matching human listeners in accuracy. Future work will focus on improving robustness to these demographic variations.

## Key Contributions  
- State‑of‑the‑art ASR models, especially Google Telephony, reach performance comparable to human listeners on diverse speech.  
- Performance differences between humans and ASR are modest and stem from speaker age, regional accents, and utterance length.  
- The specific test set used (Jasmin‑CGN versus the test stimuli) significantly influences the conclusions about benchmarking human vs. ASR performance.

## Methodology  
The authors assembled a dataset containing natural recordings of Dutch child speech, older adult speech, and Flemish utterances recorded under controlled conditions to capture typical acoustic variability. Both human listeners and ASR systems were evaluated using standard word‑error‑rate (WER) metrics on the same stimuli. The comparison was performed across multiple test sets to assess consistency and potential bias.

## Results  
Google Telephony outperformed other ASR systems, achieving a WER of about 95 %, which is near human levels. Human listeners scored an average WER of 88 %, while some ASR models even surpassed this figure. Age‑related variation caused the largest discrepancies: older adult speech produced higher WER for both humans and ASR, whereas child speech was most challenging for humans but also for ASR. Regional accents (Flemish vs. Dutch) introduced moderate error increases.

## Significance  
This work shows that human listeners are not an infallible benchmark; modern ASR can match or exceed them under certain conditions. It highlights the need for ASR systems to be robust to demographic and regional variations, informing future training data collection and model design.

## Related Concepts  
- Automatic Speech Recognition (ASR)  
- Human listener performance  
- Word Error Rate (WER)  
- Speaker age effects  
- Regional accents (Dutch vs. Flemish)  
- Test‑set bias in benchmarking
