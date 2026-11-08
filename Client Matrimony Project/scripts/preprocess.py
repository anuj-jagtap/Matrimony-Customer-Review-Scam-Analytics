import pandas as pd
import numpy as np

print("Loading expanded raw dataset...")
df = pd.read_csv('master_matrimony_expanded_raw_reviews.csv')
print(f"Initial raw rows loaded: {len(df)}")

# 1. Handle missing text/content blanks & remove duplicates
df['content'] = df['content'].fillna('').astype(str)
df = df.drop_duplicates(subset=['reviewId'])
print(f"Rows after deduplication: {len(df)}")

# Create lowercase column for keyword matching
df['clean_text'] = df['content'].str.lower()

# 2. Feature Engineering: Define Business Pain-Point Flags (Client Task 4, 5, 6)
print("Applying business pain-point keyword rules...")

scam_kw = r'scam|fraud|cheat|cheating|robber|fake|bot|dummy|extortion|thief|money lost'
billing_kw = r'pay|paid|money|subscription|auto debit|auto-debit|renewal|renew|charge|charged|cost|price|refund|amount|bank'
call_kw = r'call|calling|calls|telecaller|executive|harass|bully|pressure|force|phone'
contact_kw = r'contact|number|mobile|phone number|visible|detail|view'
tech_kw = r'bug|crash|foldable|screen|otp|login|update|app|work|upload|photo'

df['is_scam'] = df['clean_text'].str.contains(scam_kw, regex=True).astype(int)
df['is_billing'] = df['clean_text'].str.contains(billing_kw, regex=True).astype(int)
df['is_call_harassment'] = df['clean_text'].str.contains(call_kw, regex=True).astype(int)
df['is_contact_issue'] = df['clean_text'].str.contains(contact_kw, regex=True).astype(int)
df['is_tech_issue'] = df['clean_text'].str.contains(tech_kw, regex=True).astype(int)

# 3. Operational Support SLA Feature Engineering (Client Task 6)
df['replyContent'] = df['replyContent'].fillna('No Reply')
df['has_support_reply'] = (df['replyContent'] != 'No Reply').astype(int)

df['at'] = pd.to_datetime(df['at'])
df['repliedAt'] = pd.to_datetime(df['repliedAt'], errors='coerce')
df['support_latency_hours'] = (df['repliedAt'] - df['at']).dt.total_seconds() / 3600.0

# 4. New Client-Centric Deliverable Features (Sentiment & Seasonality)
def categorize_sentiment(score):
    if score >= 4:
        return 'Positive'
    elif score == 3:
        return 'Neutral'
    else:
        return 'Negative'

df['sentiment_category'] = df['score'].apply(categorize_sentiment)
df['review_year'] = df['at'].dt.year
df['review_month'] = df['at'].dt.month
df['review_length'] = df['content'].str.len()

# Handle missing version blanks
df['appVersion'] = df['appVersion'].fillna('Unknown')
df['reviewCreatedVersion'] = df['reviewCreatedVersion'].fillna('Unknown')

print(f"Formatting complete! Final Dataset Shape (All 15K Rows Kept): {len(df)}")

# 5. Export Client-Ready Formatted Master File
df.to_csv('master_matrimony_formatted_15k.csv', index=False)
print("Saved successfully to master_matrimony_formatted_15k.csv")