# Resume-JD Matcher

## Project Description

The Resume-JD Matcher is an NLP-powered tool designed to automate the initial screening phase of recruitment. By analyzing the semantic structure of candidate resumes and comparing them against specific Job Descriptions (JDs), the tool assigns a percentage-based relevance score. This assists HR professionals in prioritizing high-potential candidates and reducing the time spent on manual resume review.

## Input → Output

- **Input:**

  - **Resume:** A document file (PDF or DOCX) containing the candidate's profile.
  - **Job Description:** A raw text string or file outlining the role requirements.

- **Output:**

  - **Similarity Score:** A value between 0 and 1 (or 0-100%) indicating the match quality.

  - **Keyword Analysis:** (Optional) A list of matched vs. missing critical skills.

## Why Similarity Scoring?

Traditional keyword matching often fails because it looks for exact word replication. We utilize **Similarity Scoring** (specifically Cosine Similarity on text vectors) to measure the distance between the Job Description and the Resume in a multi-dimensional space.

- **Quantifiable Results:** It turns subjective "fit" into a mathematical score.
- **Contextual Matching:** It helps rank resumes even if they don't have the exact same phrasing, provided the vector space captures the domain terminology effectively.

## Problem Statement

In the modern hiring landscape, recruiters are inundated with hundreds of applications for every open position. Manually reviewing every resume is:

1. **Inefficient:** Takes hours of valuable time.
2. **Error-Prone:** Fatigue can lead to missed candidates.
3. **Inconsistent:** Human bias can affect screening quality.
    This project aims to solve the **volume** and **consistency** problem by providing an automated, objective first-pass filter.

## Approach (High-Level)

The project follows a standard NLP pipeline:

1. **Data Ingestion:** Using libraries (like `PyPDF2` or `docx2txt`) to extract raw text from uploaded documents.
2. **Preprocessing:** Cleaning the text by removing special characters, stop words, and applying lemmatization to standardize words.
3. **Vectorization:** Converting the cleaned text into numerical representation.
    - _Note: Currently using [TF-IDF / CountVectorizer / BERT] to create vectors._
4. **Similarity Calculation:** Computing the **Cosine Similarity** between the JD vector and the Resume vector.
    - Formula: $Cosine(\mathbf{A}, \mathbf{B}) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$

## Initial Scope

- **Supported Formats:** PDF, DOCX, TXT.
- **Language:** English only.
- **Logic:** Text-based similarity (does not currently account for formatting or layout).
- **Constraint:** _[Optional: Mention your instruction type constraint here, e.g., "2 bits are currently used to determine the instruction type logic in the processing pipeline."]_
