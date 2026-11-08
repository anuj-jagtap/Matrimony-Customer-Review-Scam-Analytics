from google_play_scraper import reviews, Sort
import pandas as pd

# Expanded targets
expanded_targets = {
    'com.shaadi.android': 4500,          
    'com.bharatmatrimony': 4500,        
    'com.jeevansathi.android': 4000,     
    'com.betterhalf': 2000               
}

all_raw_data = []


for package_id, target_count in expanded_targets.items():
    print(f"Scraping up to {target_count} reviews for {package_id}...")
    try:
        result, _ = reviews(
            package_id,
            lang='en',
            country='in',
            sort=Sort.MOST_RELEVANT,
            count=target_count
        )
        df_app = pd.DataFrame(result)
        df_app['app_source'] = package_id
        all_raw_data.append(df_app)
        print(f"Successfully scraped {len(df_app)} reviews for {package_id}.")
    except Exception as e:
        print(f"Error scraping {package_id}: {e}")

# Combine into a master raw dataset
master_raw_df = pd.concat(all_raw_data, ignore_index=True)
print(f"\nExpanded Raw Master Dataset Ready! Total Rows: {len(master_raw_df)}")

# Save directly to project folder
master_raw_df.to_csv('master_matrimony_expanded_raw_reviews.csv', index=False)
print("Saved successfully to master_matrimony_expanded_raw_reviews.csv")