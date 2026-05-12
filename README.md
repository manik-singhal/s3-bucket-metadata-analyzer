# Advanced S3 Bucket Metadata Manipulation

A Python-based DevOps automation project for analyzing, optimizing, and managing AWS S3 bucket metadata using a local JSON dataset.

Built as part of the **DevOps + SRE Daily Challenge Series**.

---

## What This Does

This tool reads S3 bucket metadata from a JSON file and runs a suite of analysis functions — surfacing unused buckets, estimating storage costs, recommending cleanups, and flagging candidates for Glacier archival. No AWS credentials needed; everything runs on a local dataset.

---

## Project Structure

```
.
├── buckets.json              # S3 bucket metadata dataset
├── s3_metadata_analysis.py   # Main analysis script
├── README.md
└── screenshot.png
```

---

## Features

### 1. Bucket Summary
Prints a clean overview of each bucket including name, region, size, and versioning status.

### 2. Unused Large Bucket Detection
Flags buckets that are larger than 80 GB and haven't been accessed in over 90 days — prime candidates for cost savings.

### 3. Cost Report
Estimates S3 storage costs grouped by:
- Region
- Department / Team

### 4. Cleanup Recommendations
Highlights buckets that meet cleanup criteria:
- Larger than 50 GB
- Larger than 100 GB and idle for 20+ days

### 5. Deletion Queue and Glacier Recommendations
- Builds a deletion queue for stale, low-value buckets
- Suggests Glacier archival for cold storage candidates to cut storage costs

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/manik-singhal/s3-bucket-metadata-analyzer.git
cd s3-bucket-metadata-analyzer
```

Run the script:

```bash
python3 s3_metadata_analysis.py
```

No external dependencies required. Uses Python 3 standard library only.

---

## Tech Stack

| Tool | Usage |
|---|---|
| Python 3 | Core scripting |
| JSON | Metadata storage and parsing |
| `datetime` | Staleness and age calculations |

---

## Challenges and Learnings

**What was tricky:**
- Navigating deeply nested JSON structures
- Accurate datetime parsing for staleness logic
- Keeping cleanup and deletion logic readable and maintainable
- Structuring everything cleanly with `if __name__ == "__main__"`

**What this project strengthened:**
- Cloud storage lifecycle thinking
- Cost analysis and infrastructure governance
- Writing modular, reusable Python for DevOps workflows
