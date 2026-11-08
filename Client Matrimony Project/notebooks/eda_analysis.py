import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization aesthetics
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.family': 'sans-serif'})

print("=========================================================")
print("ACC CLIENT PROJECT: MATRIMONY INDUSTRY EDA PIPELINE")
print("=========================================================\n")

# 1. Load the fully formatted master dataset
df = pd.read_csv('master_matrimony_formatted_15k.csv')
print(f"Master Dataset Loaded Successfully! Total Rows: {len(df)}")

# 2. Executive App-Level Aggregations (Client Metrics)
print("\n--- 1. App-Level Benchmark Metrics ---")
app_metrics = df.groupby('app_source').agg(
    total_reviews=('reviewId', 'count'),
    mean_rating=('score', 'mean'),
    scam_allegation_pct=('is_scam', lambda x: x.mean() * 100),
    billing_friction_pct=('is_billing', lambda x: x.mean() * 100),
    telecaller_harassment_pct=('is_call_harassment', lambda x: x.mean() * 100),
    tech_issues_pct=('is_tech_issue', lambda x: x.mean() * 100),
    ignored_grievance_pct=('has_support_reply', lambda x: (1 - x.mean()) * 100)
).reset_index()

# Map package IDs to readable app names
app_names = {
    'com.betterhalf': 'Betterhalf.ai',
    'com.bharatmatrimony': 'BharatMatrimony',
    'com.jeevansathi.android': 'Jeevansathi',
    'com.shaadi.android': 'Shaadi.com'
}
app_metrics['app_name'] = app_metrics['app_source'].map(app_names)
print(app_metrics[['app_name', 'total_reviews', 'mean_rating', 'scam_allegation_pct', 'billing_friction_pct', 'ignored_grievance_pct']].to_string(index=False))

# 3. Sentiment & Pain-Point Breakdown
print("\n--- 2. Overall Sentiment Breakdown ---")
sentiment_summary = df['sentiment_category'].value_counts(normalize=True) * 100
print(sentiment_summary.to_string())

# 4. Generate & Save High-Resolution Charts for Client Report
print("\n--- 3. Generating Analytical Charts for Client Deck ---")
fig, axes = plt.subplots(2, 2, figsize=(15, 11))

# Chart A: Sentiment Distribution across Platforms
sns.countplot(data=df, x='app_source', hue='sentiment_category', ax=axes[0,0], palette='Set2')
axes[0,0].set_title('A. Customer Sentiment Distribution by Platform', fontsize=12, fontweight='bold')
axes[0,0].set_xticklabels(['Betterhalf', 'BharatMatrimony', 'Jeevansathi', 'Shaadi'], rotation=0)
axes[0,0].set_xlabel('')
axes[0,0].set_ylabel('Review Count')

# Chart B: Business Pain-Point Penetration (%)
pain_points = df.groupby('app_source')[['is_scam', 'is_billing', 'is_call_harassment', 'is_tech_issue']].mean() * 100
pain_points.index = ['Betterhalf', 'BharatMatrimony', 'Jeevansathi', 'Shaadi']
pain_points.plot(kind='bar', ax=axes[0,1], colormap='tab10')
axes[0,1].set_title('B. Key Customer Pain-Point Penetration (%)', fontsize=12, fontweight='bold')
axes[0,1].set_ylabel('Percentage of Negative Reviews (%)')
axes[0,1].set_xticklabels(pain_points.index, rotation=0)
axes[0,1].legend(['Scams/Fake Profiles', 'Billing Friction', 'Telecaller Harassment', 'Technical Bugs'])

# Chart C: Mean Rating Comparison
sns.barplot(data=app_metrics, x='app_name', y='mean_rating', ax=axes[1,0], palette='Blues_d')
axes[1,0].set_title('C. Average User Rating (Scale 1-5)', fontsize=12, fontweight='bold')
axes[1,0].set_ylabel('Mean Rating Score')
axes[1,0].set_xlabel('')

# Chart D: Customer Support Neglect Rate (%)
sns.barplot(data=app_metrics, x='app_name', y='ignored_grievance_pct', ax=axes[1,1], palette='Reds_d')
axes[1,1].set_title('D. Ignored Customer Grievance Rate (%)', fontsize=12, fontweight='bold')
axes[1,1].set_ylabel('Unanswered Reviews (%)')
axes[1,1].set_xlabel('')

plt.tight_layout()
plt.savefig('matrimony_eda_summary_charts.png', dpi=300)
print("Saved executive charts to 'matrimony_eda_summary_charts.png'!")

# 5. Export Summary Table for Presentation
app_metrics.to_csv('client_executive_summary_metrics.csv', index=False)
print("Saved summary metrics to 'client_executive_summary_metrics.csv'!")