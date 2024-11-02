import gdelt
import pandas as pd
from datetime import datetime


def download_gdelt_gkg(start_date, end_date, keywords=None, themes=None):
    """
    Download GDELT GKG data with filtering conditions

    Parameters:
    - start_date (str): Start date in 'YYYY-MM-DD' format
    - end_date (str): End date in 'YYYY-MM-DD' format
    - keywords (list): List of keywords to filter articles
    - themes (list): List of GDELT themes to filter

    Returns:
    - pandas DataFrame containing the filtered GKG data
    """
    try:
        # Initialize GDELT (version 2)
        gd = gdelt.gdelt(version=2)

        # Format dates for GDELT query
        date_range = [start_date, end_date]

        # Download GKG data
        results = gd.Search(
            date_range,
            table="gkg",  # Specify GKG table
            coverage=True,  # Get all 15-min intervals
            output="pandas",
        )  # Return as pandas DataFrame

        # Apply filters if provided
        if keywords:
            # Filter by keywords in article text
            keyword_filter = "|".join(keywords).lower()
            results = results[
                results["V2Persons"].str.lower().str.contains(keyword_filter, na=False)
            ]

        if themes:
            # Filter by GDELT themes
            theme_filter = "|".join(themes)
            results = results[results["V2Themes"].str.contains(theme_filter, na=False)]

        return results

    except Exception as e:
        print(f"Error downloading GDELT data: {str(e)}")
        return None


def analyze_gkg_data(df):
    """
    Basic analysis of GKG data

    Parameters:
    - df: pandas DataFrame containing GKG data
    """
    if df is not None and not df.empty:
        print(f"\nTotal articles: {len(df)}")

        # Analyze themes
        if "V2Themes" in df.columns:
            themes = df["V2Themes"].str.split(";").explode().value_counts().head(10)
            print("\nTop 10 Themes:")
            print(themes)

        # Analyze persons mentioned
        if "V2Persons" in df.columns:
            persons = df["V2Persons"].str.split(";").explode().value_counts().head(10)
            print("\nTop 10 Persons Mentioned:")
            print(persons)


# Example usage
if __name__ == "__main__":
    # Define search parameters
    start_date = "2024-01-01"
    end_date = "2024-01-02"
    keywords = ["AI", "artificial intelligence"]
    themes = ["TECHNOLOGY", "INNOVATION"]

    # Download data
    print("Downloading GDELT GKG data...")
    gkg_data = download_gdelt_gkg(
        start_date=start_date, end_date=end_date, keywords=keywords, themes=themes
    )

    # Analyze results
    analyze_gkg_data(gkg_data)

    # Save to CSV if needed
    if gkg_data is not None and not gkg_data.empty:
        output_file = f"gdelt_gkg_{start_date}_{end_date}.csv"
        gkg_data.to_csv(output_file, index=False)
        print(f"\nData saved to {output_file}")
