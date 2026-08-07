# Summary: 2026-08-06_11-39-19Z_CourseGraph_FindingoverlapsanddifferencesinCompute.md
Saved: 2026-08-06 22:13
Source: 2026-08-06_11-39-19Z_CourseGraph_FindingoverlapsanddifferencesinCompute.md
Model: None

---

## Summary  
The paper introduces **CourseGraph**, a framework that automatically detects whether an external computer‑science course taken abroad overlaps with a student’s home curriculum, thereby preventing redundant or conflicting coursework. By leveraging natural‑language processing and machine‑learning classification, CourseGraph extracts structured information from university webpages and evaluates it against existing degree requirements. The authors demonstrate the system on two real‑world datasets: the Eindhoven University of Technology CS program (where overlaps are known) and six approved international programs at Lund University (with administrator decisions). This work bridges curriculum administration challenges with scalable, AI‑driven analysis for student mobility initiatives such as Erasmus+.

## Key Contributions  
- **Finding 1:** CourseGraph can automatically extract course titles, descriptions, and learning outcomes from webpages using a BERT‑based language model.  
- **Finding 2:** The system computes pairwise semantic similarity between courses and feeds this into a Random Forest classifier to predict overlap probability with the home curriculum.  
- **Finding 3:** Experimental evaluation shows that CourseGraph correctly identifies overlapping courses in both test sets, outperforming manual inspection for large‑scale programs.

## Methodology  
The authors first scrape each course’s webpage to obtain raw textual content. A pre‑trained BERT model converts this text into dense vector representations, capturing semantic meaning of titles and descriptions. These vectors are then used to compute cosine similarity between every pair of courses. The similarity scores serve as features for a Random Forest classifier trained on labeled examples (overlap vs. no overlap) derived from administrator decisions at Lund University. The classifier outputs a binary prediction indicating whether the external course constitutes an overlap with any course in the student’s home curriculum.

## Results  
In the Eindhoven dataset, CourseGraph correctly classified 96 % of courses as overlapping when compared to the official curriculum, and it identified all true overlaps (100 %). For the Lund dataset, the classifier achieved a precision of 0.94 and recall of 0.89, meaning that most flagged courses were indeed overlaps while only a few legitimate non‑overlaps were mistakenly flagged. The system processed over 200 course pairs per second on a single GPU, demonstrating scalability.

## Significance  
CourseGraph addresses a critical pain point for students participating in international programs: the risk of enrolling in courses that duplicate or conflict with their home degree requirements. By automating this evaluation, universities can provide clearer guidance to Erasmus+ participants and reduce administrative workload. The approach also offers a reusable template for other disciplines where curriculum alignment matters.

## Related Concepts  
- Curriculum alignment / degree requirements  
- Student mobility programs (e.g., Erasmus+)  
- Natural language processing with BERT embeddings  
- Semantic similarity computation  
- Random Forest classification for binary prediction  
- Course webpage scraping and data extraction
