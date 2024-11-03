from pathlib import Path

import pandas as pd
from crawl4ai import AsyncWebCrawler


async def scrape_documents(csv_path: str, output_dir: str, batch_size: int = 10):
    # Read the CSV file
    df = pd.read_csv(csv_path, sep="\t")

    # Create output directory if it doesn't exist
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    async with AsyncWebCrawler(verbose=True) as crawler:
        for i in range(0, len(df), batch_size):
            batch = df.iloc[i : i + batch_size]

            for _, row in batch.iterrows():
                doc_id = row["DocumentIdentifier"]

                # Skip if already processed
                output_file = output_dir / f"{i}_{doc_id.replace('/', '_')}.md"
                if output_file.exists():
                    continue

                try:
                    result = await crawler.arun(
                        url=doc_id,
                        word_count_threshold=10,
                        exclude_external_links=True,
                        remove_overlay_elements=True,
                        process_iframes=True,
                        bypass_cache=False,
                    )

                    if result.success:
                        # Save the content
                        output_file.write_text(
                            f"# Original URL: {doc_id}\n\n{result.markdown}"
                        )
                    else:
                        print(f"Failed to crawl {doc_id}: {result.error_message}")

                except Exception as e:
                    print(f"Error processing {doc_id}: {str(e)}")

            print(f"Processed batch {i//batch_size + 1}")
