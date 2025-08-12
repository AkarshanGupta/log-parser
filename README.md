
# Log Parser

A Bash-based utility to process and analyze log files.  
It reads logs from a given directory, filters and formats the data, and outputs structured results for further use.

---

## 📂 Project Structure

. ├── solution.sh           # Main Bash script for parsing logs ├── data/                 # Input log files ├── tests/                # Test cases ├── run-tests.sh          # Automated test runner ├── Dockerfile            # Container environment setup ├── docker-compose.yaml   # For local container runs └── README.md             # Documentation

---

## 🚀 How to Run

### Prerequisites
- **Bash** (v4+)
- **Docker** (optional, for container runs)
- Execution permissions for shell scripts

### Run Locally
```bash
chmod +x solution.sh
./solution.sh

Run Tests

chmod +x run-tests.sh
./run-tests.sh


---

🐳 Run with Docker

docker build -t log-parser .
docker run --rm -v $(pwd):/app log-parser


---

📜 Features

Reads and parses .log files

Filters and formats output

Includes automated tests

Runs on Linux/MacOS or via Docker



---

🧪 Testing

./run-tests.sh

Runs all test cases in tests/ and shows pass/fail results.


---

📝 Author

frostbeast
Email: (anonymous)


---

⚠️ Notes

For assessment purposes only

Sample log data is dummy and not from real systems


If you paste that into a file called `README.md` in your project root, it’s done.  

Do you want me to **add sample input and output logs** so it looks better for submission? That would make it look more professional.

