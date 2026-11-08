# 💍 Matrimony Industry Market Intelligence & Scam Analysis

## Executive Summary
An end-to-end data analytics and market research project executed for a client entering the digital matrimony space. Analyzing over **15,000 authentic customer reviews** extracted from the Google Play Store, this project uncovers hidden consumer friction points, quantifies scam and fake profile allegations, evaluates monetization bottlenecks, and delivers actionable business recommendations to build a high-trust matrimonial platform.

---

## Tech Stack & Libraries
* **Data Extraction:** Python (`google-play-scraper`)
* **Data Processing & Cleaning:** Pandas, NumPy
* **Text Processing & Feature Engineering:** Regular Expressions (`re`), String manipulation for deduplication and sentiment categorization
* **Visualization & Reporting:** Power BI / Matplotlib / Seaborn

---

## Project Workflow

1. **Domain Research & Pivot:** Initially evaluated official web success stories, which lacked critical friction data. Pivoted to user-generated app reviews on the Google Play Store to capture unvarnished customer feedback.
2. **Automated Data Extraction (`scraper.py`):** Developed a custom Python extraction pipeline targeting major matrimony applications, successfully pulling 15,000+ raw review records.
3. **Data Hygiene & Preprocessing (`preprocessing.py`):** 
   * Handled missing values and removed duplicate entries.
   * Standardized date-time formats and rating scales.
   * Engineered categorical flags to isolate reviews mentioning *fake profiles, financial fraud, subscription friction,* and *customer support failures*.
4. **Exploratory Data Analysis (EDA):** Quantified rating distributions, common complaint keywords, and pricing-tier dissatisfaction.
5. **Strategic Recommendations:** Translated technical findings into a business roadmap for the client's upcoming platform launch.

---

## Key Findings & Business Insights

* **Trust & Verification Gap:** Over 35% of low-rating reviews cite encounters with fake profiles or unverified accounts, highlighting an urgent market demand for mandatory government ID or selfie-verification onboarding.
* **Monetization Friction:** Users expressed high dissatisfaction with aggressive paywalls that lock basic messaging features after registration, driving churn to competitors with more transparent trial models.
* **Customer Support Bottlenecks:** Delayed dispute resolution for fraudulent profiles was the primary driver of negative app churn.

---

## How to Run the Scripts

1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/Matrimony-Customer-Review-Scam-Analytics.git](https://github.com/YourUsername/Matrimony-Customer-Review-Scam-Analytics.git)
