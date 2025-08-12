import os
import csv

# This gets the directory where this test file is located
TEST_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct absolute path to the report file relative to test file
REPORT_PATH = os.path.abspath(os.path.join(TEST_DIR, '../reports/error_summary.csv'))

def test_report_file_exists():
    """Test 1: Checks that the 'error_summary.csv' file was actually created."""
    assert os.path.exists(REPORT_PATH), "The output file error_summary.csv was not found."

def test_report_is_not_empty():
    """Test 2: Checks that the generated report contains more than just a header line."""
    assert os.path.getsize(REPORT_PATH) > 0, "The report file is empty."
    with open(REPORT_PATH, 'r') as f:
        # Expecting a header and 3 data rows, so more than 1 line total.
        assert len(f.readlines()) > 1, "The report file only contains a header."

def test_report_header():
    """Test 3: Validates the header row of the CSV file is exactly correct."""
    with open(REPORT_PATH, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ['ip_address', 'error_count'], f"Header row is incorrect: {header}"

def test_report_content_and_order():
    """Test 4: Checks the full content and descending sort order of the data."""
    expected_data = [
        ['88.201.54.12', '3'],
        ['10.0.0.5', '1'],
        ['203.0.113.45', '1']
    ]
    with open(REPORT_PATH, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        data = list(reader)
        assert data == expected_data, f"Report content/order incorrect: {data}"

def test_number_of_unique_ips():
    """Test 5: Ensures the correct number of unique IP addresses with errors were found."""
    with open(REPORT_PATH, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        unique_ips = {row[0] for row in reader}
        assert len(unique_ips) == 3, f"Unexpected number of unique IPs: {len(unique_ips)}"

def test_highest_count_ip():
    """Test 6: Confirms the IP with the most errors is the first data row."""
    with open(REPORT_PATH, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        first_row = next(reader)
        assert first_row[0] == '88.201.54.12', f"IP with highest errors should be first row: {first_row[0]}"
