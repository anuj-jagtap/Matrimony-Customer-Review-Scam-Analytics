# Data Dictionary: Matrimony Industry Customer Review Dataset

This document defines the schema, data types, descriptions, and feature engineering logic for the master dataset (`master_matrimony_formatted_15k.csv`) used in the Matrimony Market Intelligence & Customer Review Analysis project.

---

## 1. Raw Scraped Attributes (`google-play-scraper`)

These fields represent raw data scraped directly from the Google Play Store across four targeted matrimony applications (`com.shaadi.android`, `com.bharatmatrimony`, `com.jeevansathi.android`, and `com.betterhalf`).

| Column Name | Data Type | Example Value | Description |
| :--- | :--- | :--- | :--- |
| `reviewId` | `string` | `gp:AOqpTOE...` | Unique global identifier for each app store review (Primary Key). |
| `userName` | `string` | `Rahul Sharma` | Display name of the reviewer. Set to `'Anonymous User'` if missing. |
| `userImage` | `string` | `https://play-lh.googleusercontent.com/...` | URL pointing to the user's profile avatar. |
| `content` | `string` | `"Totally waste of money. Fake profiles asking for money..."` | Unprocessed raw review text submitted by the user. |
| `score` | `integer` | `1` | Numerical rating given by the user on a 1 to 5 star scale. |
| `thumbsUpCount` | `integer` | `14` | Total number of other users who marked the review as helpful. |
| `reviewCreatedVersion` | `string` | `4.8.2` | App version installed on the user's device when writing the review (`'Unknown'` if null). |
| `at` | `datetime` | `2025-08-14 10:22:15` | Timestamp indicating when the review was originally posted. |
| `replyContent` | `string` | `"Hi Rahul, please write to us at support@..."` | Official response text provided by the platform's customer support team. |
| `repliedAt` | `datetime` | `2025-08-15 14:05:00` | Timestamp indicating when customer support posted their response. |
| `app_source` | `string` | `com.shaadi.android` | Target application package identifier (`com.shaadi.android`, `com.bharatmatrimony`, `com.jeevansathi.android`, `com.betterhalf`). |

---

## 2. Preprocessed & Engineered Features

These attributes were generated during the preprocessing and feature engineering pipeline (`preprocess.py`) to quantify sentiment, customer friction points, trust deficits, and support SLAs.

| Column Name | Data Type | Range / Values | Engineering Logic & Description |
| :--- | :--- | :--- | :--- |
| `clean_text` | `string` | Text string | Preprocessed review text (lowercase, special characters stripped, normalized whitespace). |
| `review_length` | `integer` | `1` to `1500+` | Total character count of `clean_text`. Used in econometric correlation modeling ($r = -0.155$). |
| `sentiment_category` | `string` | `Negative`, `Neutral`, `Positive` | Categorical classification based on rating score:<br>• `1`–`2` stars = `Negative`<br>• `3` stars = `Neutral`<br>• `4`–`5` stars = `Positive` |
| `is_scam` | `boolean / int` | `0` or `1` | **Trust & Security Flag:** Regex match on `clean_text` for terms: *scam, fake, fraud, bot, cheat, blackmail, money lost, money ask*. |
| `is_billing` | `boolean / int` | `0` or `1` | **Monetization Friction Flag:** Regex match on `clean_text` for terms: *billing, auto-debit, payment, refund, subscription, expensive, lock-in, price*. |
| `is_call_harassment`| `boolean / int` | `0` or `1` | **Sales Pressure Flag:** Regex match on `clean_text` for terms: *telecaller, call, harass, executive, force, agent, pressure, spam call*. |
| `is_tech_issue` | `boolean / int` | `0` or `1` | **App Reliability Flag:** Regex match on `clean_text` for terms: *bug, crash, otp, login, error, freeze, update, server*. |
| `is_contact_issue` | `boolean / int` | `0` or `1` | **Communication Paywall Flag:** Regex match on `clean_text` for terms: *contact, number, chat, view profile, message limit, paywall*. |
| `has_support_reply` | `boolean / int` | `0` or `1` | Binary indicator set to `1` if `replyContent` is present and non-null; otherwise `0`. |
| `support_latency_hours`| `float` | `0.0` to `500.0+` | Calculated resolution latency: $(\text{repliedAt} - \text{at})$ converted into total hours. Null if `has_support_reply` is `0` or if negative (edited reviews). |

---

## 3. Executive KPI Aggregations (Summary Schema)

Schema for the aggregated metrics file (`client_master_summary_metrics.csv`):

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `App_Name` | `string` | Readable app name (*Betterhalf.ai, BharatMatrimony, Jeevansathi, Shaadi.com*). |
| `Total_Reviews` | `integer` | Total review sample size evaluated for the platform. |
| `Mean_Rating` | `float` | Average user rating score (1.00 to 5.00). |
| `Scam_Rate_Pct` | `float` | Percentage of reviews flagged with trust/scam allegations (`is_scam == 1`). |
| `Billing_Friction_Pct`| `float` | Percentage of reviews flagged with billing/subscription friction (`is_billing == 1`). |
| `Unanswered_Support_Pct`| `float` | Percentage of customer reviews completely ignored by platform support (`has_support_reply == 0`). |