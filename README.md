

# 🗂️ Log Parser

A simple and efficient **Bash-based log parsing tool** for reading, filtering, and analyzing server log files.  
Designed for quick data extraction, formatted output, and automated testing.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Usage](#usage)
- [Docker Setup](#docker-setup)
- [Testing](#testing)
- [Sample Output](#sample-output)
- [Author](#author)

---

## 📖 Overview
The **Log Parser** reads `.log` files from a specified directory, processes them, and outputs cleaned, formatted results.  
This is useful for:
- Extracting key information from large log files
- Filtering based on specific patterns
- Generating summaries for quick analysis

---

## 📂 Project Structure
```

.
├── solution.sh           # Main Bash script for parsing logs
├── data/                 # Input log files (sample/test data)
├── tests/                # Test cases for verification
├── run-tests.sh          # Script to run all tests
├── Dockerfile            # Container environment setup
├── docker-compose.yaml   # Optional container orchestration
└── README.md             # Documentation



---

## ⚙️ Requirements
- **Bash** (v4.0 or later)
- **Docker** (optional, for containerized runs)
- Execution permission for `.sh` files

---

## 🚀 Usage

### 1️⃣ Run Locally
```bash
# Give execution permission
chmod +x solution.sh

# Run the parser
./solution.sh
````

### 2️⃣ Run Tests

```bash
chmod +x run-tests.sh
./run-tests.sh
```

---

## 🐳 Docker Setup

If you prefer running in a container:

```bash
# Build the Docker image
docker build -t log-parser .

# Run the parser inside the container
docker run --rm -v $(pwd):/app log-parser
```

---

## 🧪 Testing

Run:

```bash
./run-tests.sh
```

This will execute all test cases in `tests/` and display pass/fail status.

---

## 📊 Sample Output

**Example input (data/sample.log):**

```
2025-08-13 12:01:45 INFO User 'admin' logged in
2025-08-13 12:03:10 ERROR Failed to connect to database
```

**Example output:**

```
[INFO] 2025-08-13 12:01:45 - User 'admin' logged in
[ERROR] 2025-08-13 12:03:10 - Failed to connect to database
```

---

## 👤 Author

**Name:** frostbeast *(submitted for assessment)*
**Email:** *(anonymous)*

---

## ⚠️ Notes

* All IP addresses, log entries, and data in this project are **dummy** for demonstration purposes.
* No real system information is exposed.

