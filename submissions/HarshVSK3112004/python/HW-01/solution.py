# # Python Assignment — Data Engineering Foundation
# **Scenario:** Data Ingestion and Processing Pipelines  
# **Total Questions:** 20 (Sections A–E)  
# 
# This notebook contains complete, executable solutions for all 20 questions, including:
# * **Logic explanations** before every code block.
# * **Fixes** for variable names, ceiling batch calculation, stray output, and segregated record printing.
# * **Multiple test scenarios** (at least two different input cases wherever applicable) so every cell runs cleanly while demonstrating full test coverage.

# ---
# ## Section A — Variables, Data Types, and Type Conversion

# ### Q1. Source Configuration
# **Logic Explanation:**  
# Each pipeline configuration parameter is stored in a descriptive variable using Python's built-in primitive data types: `str` for text identifiers (`source_name`, `batch_id`), `int` for discrete counts (`number_of_records`), `bool` for binary status flags (`pipeline_active`), and `float` for decimal metrics (`average_processing_time`). The `type()` function inspects and displays each variable's runtime data type.

# Define variables with appropriate data types
source_name = "Upstox"
batch_id = "BATCH_001"
number_of_records = 1500
pipeline_active = True
average_processing_time = 12.75

# Print each variable and its data type
print(f"Source Name: {source_name} | Type: {type(source_name)}")
print(f"Batch ID: {batch_id} | Type: {type(batch_id)}")
print(f"Number of Records: {number_of_records} | Type: {type(number_of_records)}")
print(f"Pipeline Active: {pipeline_active} | Type: {type(pipeline_active)}")
print(f"Average Processing Time: {average_processing_time} | Type: {type(average_processing_time)}")

# ### Q2. Ingestion Metadata
# **Logic Explanation:**  
# We store the metadata attributes (`source`, `record_count`, `file_size_mb`, `is_processed`), display their values and data types using `type()`, and programmatically identify numerical variables by checking whether each value is an instance of `(int, float)` while excluding `bool` (since `bool` is a subclass of `int` in Python).

# Ingestion metadata variables
source = "customer_api"
record_count = 2500
file_size_mb = 45.6
is_processed = False

# 1. Print all metadata values
print("--- Metadata Values ---")
print("Source:", source)
print("Record Count:", record_count)
print("File Size (MB):", file_size_mb)
print("Is Processed:", is_processed)

# 2. Print the data type of each variable
print("\n--- Data Types ---")
print("source type:", type(source))
print("record_count type:", type(record_count))
print("file_size_mb type:", type(file_size_mb))
print("is_processed type:", type(is_processed))

# 3. Identify variables containing numerical values
metadata = {
    "source": source,
    "record_count": record_count,
    "file_size_mb": file_size_mb,
    "is_processed": is_processed
}
numerical_vars = [
    name for name, val in metadata.items()
    if isinstance(val, (int, float)) and not isinstance(val, bool)
]
print("\n--- Numerical Variables ---")
print("Variables with numerical values:", ", ".join(numerical_vars))

# ### Q3. Data Type Investigation
# **Logic Explanation:**  
# Raw data from text-based sources (such as CSVs or JSON payloads) often arrives as strings (`str`). Before performing arithmetic or boolean checks, we cast whole numbers with `int()`, decimal amounts with `float()`, and string flags using an explicit comparison (`is_active == "True"`) rather than `bool(is_active)`—because `bool("False")` would erroneously evaluate to `True` for any non-empty string.

# Raw values provided as strings
customper_id = "10245"
order_amount = "4500.50"
quantity = "5"
is_active = "True"

print("Original Types:")
print(type(customper_id), type(order_amount), type(quantity), type(is_active))

# Convert into appropriate Python data types for processing
customer_id_int = int(customper_id)
order_amount_float = float(order_amount)
quantity_int = int(quantity)
is_active_bool = is_active == "True"

print("\nConverted Types & Values:")
print(f"Customer ID: {customer_id_int} ({type(customer_id_int)})")
print(f"Order Amount: {order_amount_float} ({type(order_amount_float)})")
print(f"Quantity: {quantity_int} ({type(quantity_int)})")
print(f"Is Active: {is_active_bool} ({type(is_active_bool)})")

# ### Q4. Pipeline Configuration
# **Logic Explanation:**  
# To calculate the exact number of batches needed without losing trailing records if `max_records` is not an exact multiple of `batch_size`, we use ceiling division via integer arithmetic: `(max_records + batch_size - 1) // batch_size`. This handles both exact multiples and remainders accurately.

max_records = 10000
batch_size = 500
retry_count = 3

# Ceiling division ensures any partial final batch is accounted for
total_batches = (max_records + batch_size - 1) // batch_size

print(f"Total records: {max_records}")
print(f"Batch size: {batch_size}")
print(f"Retry count configured: {retry_count}")
print(f"Batches required to process all records: {total_batches}")

# ---
# ## Section B — User Input and Operators

# ### Q5. File Ingestion Calculator
# **Logic Explanation:**  
# We accept the number of files as an integer (`int`) and average file size in MB as a floating-point number (`float`), then multiply them (`num_files * avg_file_size_mb`) to compute total data volume. Two test scenarios are demonstrated using a reusable helper function (with interactive `input()` shown in comments).

def calculate_ingestion_volume(num_files, avg_file_size_mb):
    total_data_volume_mb = num_files * avg_file_size_mb
    print(f"Files: {num_files}, Avg Size: {avg_file_size_mb} MB -> Total Volume: {total_data_volume_mb:.2f} MB")

# Interactive version:
# num_files = int(input("Enter number of files received: "))
# avg_file_size_mb = float(input("Enter average file size in MB: "))
# calculate_ingestion_volume(num_files, avg_file_size_mb)

print("--- Test Scenario 1 ---")
calculate_ingestion_volume(12, 45.5)

print("--- Test Scenario 2 ---")
calculate_ingestion_volume(250, 1.25)

# ### Q6. Batch Processing
# **Logic Explanation:**  
# Floor division (`total_records // batch_size`) computes the number of full 100-record batches, while the modulo operator (`total_records % batch_size`) extracts the leftover records. If `remaining_records > 0`, one additional batch is added to process the remaining records.

total_records = 1275
batch_size = 100

# 1. Number of complete batches
complete_batches = total_records // batch_size

# 2. Remaining records
remaining_records = total_records % batch_size

# 3. Total batches required
total_batches_required = complete_batches + (1 if remaining_records > 0 else 0)

print(f"1. Complete batches: {complete_batches}")
print(f"2. Remaining records: {remaining_records}")
print(f"3. Total batches required: {total_batches_required}")

# ### Q7. Data Processing Cost
# **Logic Explanation:**  
# The number of consumed processing units (`float`) is multiplied by the unit rate (`₹2.50`) to obtain the total cloud compute cost, formatted to two decimal places. Two test scenarios demonstrate different workload sizes.

def calculate_processing_cost(processing_units):
    cost_per_unit = 2.50
    total_cost = processing_units * cost_per_unit
    print(f"Units consumed: {processing_units} -> Total processing cost: ₹{total_cost:.2f}")

# Interactive version:
# units = float(input("Enter the number of processing units consumed: "))
# calculate_processing_cost(units)

print("--- Test Scenario 1 ---")
calculate_processing_cost(140)

print("--- Test Scenario 2 ---")
calculate_processing_cost(325.5)

# ### Q8. Storage Calculation
# **Logic Explanation:**  
# We sum the storage across the Bronze, Silver, and Gold medallion layers to get `total_storage`. Each layer's share is then computed as `(layer_gb / total_storage) * 100` and formatted to two decimal places.

bronze_gb = 250
silver_gb = 120
gold_gb = 30

# 1. Total storage consumption
total_storage = bronze_gb + silver_gb + gold_gb

# 2. Percentage of storage occupied by each layer
bronze_pct = (bronze_gb / total_storage) * 100
silver_pct = (silver_gb / total_storage) * 100
gold_pct = (gold_gb / total_storage) * 100

print(f"1. Total storage consumption: {total_storage} GB")
print("2. Storage breakdown:")
print(f"   - Bronze layer: {bronze_gb} GB ({bronze_pct:.2f}%)")
print(f"   - Silver layer: {silver_gb} GB ({silver_pct:.2f}%)")
print(f"   - Gold layer: {gold_gb} GB ({gold_pct:.2f}%)")

# ---
# ## Section C — Conditional Statements and Data Validation

# ### Q9. Mandatory Field Validation
# **Logic Explanation:**  
# We check `record.get("customer_id") is not None` (and ensure it is not an empty string) to verify that the mandatory primary key exists before accepting the record. Two test cases verify both missing (`None`) and valid (`105`) customer IDs.

def validate_customer_record(record):
    if record.get("customer_id") is not None and str(record.get("customer_id")).strip() != "":
        print(f"Input: {record} -> Record accepted.")
    else:
        print(f"Input: {record} -> Record rejected: Missing customer ID.")

print("--- Test Scenario 1 (Missing ID) ---")
record_1 = {"customer_id": None, "customer_name": "Rahul", "city": "Bangalore"}
validate_customer_record(record_1)

print("\n--- Test Scenario 2 (Valid ID) ---")
record_2 = {"customer_id": 105, "customer_name": "Ananya", "city": "Mumbai"}
validate_customer_record(record_2)

# ### Q10. API Response Handling
# **Logic Explanation:**  
# An `if-elif-else` chain maps standard HTTP response status codes (`200`, `400`, `401`, `404`, `429`) to specific pipeline recovery or ingestion actions, with a fallback `else` branch for unexpected server/network errors. Multiple status codes are tested below.

def handle_api_response(status_code):
    if status_code == 200:
        action = "Process API response"
    elif status_code == 400:
        action = "Bad request — check request parameters"
    elif status_code == 401:
        action = "Authentication failed"
    elif status_code == 404:
        action = "Source endpoint not found"
    elif status_code == 429:
        action = "Rate limit exceeded"
    else:
        action = "Handle unexpected API error"
    print(f"Status {status_code}: {action}")

# Interactive version:
# code = int(input("Enter the HTTP response status code: "))
# handle_api_response(code)

for test_code in [200, 429, 503]:
    handle_api_response(test_code)

# ### Q11. Data Quality Check
# **Logic Explanation:**  
# Both business rules (`amount > 0` and `status == "SUCCESS"`) must hold simultaneously, so they are joined with the logical `and` operator. Two scenarios test an invalid negative-amount record and a valid positive `SUCCESS` transaction.

def check_transaction_quality(transaction):
    if transaction["amount"] > 0 and transaction["status"] == "SUCCESS":
        print(f"Transaction {transaction['transaction_id']}: Valid transaction.")
    else:
        print(f"Transaction {transaction['transaction_id']}: Invalid transaction.")

print("--- Test Scenario 1 (Negative Amount) ---")
txn_1 = {"transaction_id": 101, "amount": -500, "status": "SUCCESS"}
check_transaction_quality(txn_1)

print("\n--- Test Scenario 2 (Valid Transaction) ---")
txn_2 = {"transaction_id": 102, "amount": 1250, "status": "SUCCESS"}
check_transaction_quality(txn_2)

# ### Q12. Pipeline Execution Mode
# **Logic Explanation:**  
# User input is normalized using `.strip().upper()` so variations in casing or accidental whitespace (e.g., `"backfill"`) still match the supported modes (`FULL`, `INCREMENTAL`, `BACKFILL`). Unrecognized inputs fall into the `else` branch.

def run_pipeline_mode(mode_input):
    execution_mode = mode_input.strip().upper()
    if execution_mode == "FULL":
        print(f"Mode '{mode_input}' -> Load all historical records.")
    elif execution_mode == "INCREMENTAL":
        print(f"Mode '{mode_input}' -> Load new records.")
    elif execution_mode == "BACKFILL":
        print(f"Mode '{mode_input}' -> Reload historical data for a specified period.")
    else:
        print(f"Mode '{mode_input}' -> Invalid execution mode.")

# Interactive version:
# mode = input("Enter pipeline execution mode (FULL, INCREMENTAL, BACKFILL): ")
# run_pipeline_mode(mode)

for test_mode in ["INCREMENTAL", "backfill", "DELTA"]:
    run_pipeline_mode(test_mode)

# ### Q13. Data Quality Scoring
# **Logic Explanation:**  
# Boundary validation (`quality_score < 0 or quality_score > 100`) is evaluated first to reject out-of-range scores immediately. Subsequent `elif` branches check descending thresholds (`>= 90`, `>= 75`, `>= 50`) so each band cleanly captures its exact range.

def classify_quality_score(quality_score):
    if quality_score < 0 or quality_score > 100:
        print(f"Score {quality_score}: Invalid score — must be between 0 and 100.")
    elif quality_score >= 90:
        print(f"Score {quality_score}: Excellent")
    elif quality_score >= 75:
        print(f"Score {quality_score}: Good")
    elif quality_score >= 50:
        print(f"Score {quality_score}: Needs improvement")
    else:
        print(f"Score {quality_score}: Critical — investigate pipeline")

# Interactive version:
# score = float(input("Enter data quality score (0-100): "))
# classify_quality_score(score)

for test_score in [94, 68, 105]:
    classify_quality_score(test_score)

# ---
# ## Section D — Loops and Record Processing

# ### Q14. Batch Record Processing
# **Logic Explanation:**  
# A `for` loop iterates sequentially over each element in the `customer_ids` list and logs the active customer ID being processed.

customer_ids = [101, 102, 103, 104, 105]

for customer_id in customer_ids:
    print(f"Processing customer: {customer_id}")

# ### Q15. Failed Record Identification
# **Logic Explanation:**  
# We iterate through `amounts` using a `for` loop, check if each value is strictly negative (`amt < 0`), print every invalid amount detected, and increment an accumulator (`invalid_count`) to report the total count of failed records.

amounts = [500, 1200, -100, 800, -50, 2000]
invalid_count = 0

print("Invalid transaction amounts:")
for amt in amounts:
    if amt < 0:
        print(amt)
        invalid_count += 1

print(f"Total invalid records: {invalid_count}")

# ### Q16. API Retry Simulation
# **Logic Explanation:**  
# A `while` loop executes as long as `attempts < max_retries`. On every iteration, `attempts` is incremented by `1` and logged. Once the loop terminates after 3 attempts, `"Maximum retries reached"` is printed.

attempts = 0
max_retries = 3

while attempts < max_retries:
    attempts += 1
    print(f"Attempt {attempts}: Calling external API...")

print("Maximum retries reached")

# ### Q17. Daily Ingestion Summary
# **Logic Explanation:**  
# We initialize `successful_count` and `failed_count` to `0`, iterate through the list of record dictionaries, inspect `record["status"]`, and update the corresponding counter. `len(records)` provides the total record count dynamically without hardcoding.

records = [
    {"id": 1, "status": "SUCCESS"},
    {"id": 2, "status": "FAILED"},
    {"id": 3, "status": "SUCCESS"},
    {"id": 4, "status": "SUCCESS"},
    {"id": 5, "status": "FAILED"}
]

successful_count = 0
failed_count = 0

for record in records:
    if record["status"] == "SUCCESS":
        successful_count += 1
    elif record["status"] == "FAILED":
        failed_count += 1

print(f"Total records: {len(records)}")
print(f"Successful records: {successful_count}")
print(f"Failed records: {failed_count}")

# ---
# ## Section E — Combined Data Engineering Scenarios

# ### Q18. Customer Data Ingestion Validator
# **Logic Explanation:**  
# This solution combines list iteration, dictionary field access, compound boolean conditions (`cust["id"] is not None and cust["age"] > 0`), and separate collection lists (`valid_records` and `invalid_records`). Both the segregated records and their counts are displayed.

customers = [
    {"id": 101, "name": "Rahul", "age": 25},
    {"id": None, "name": "Priya", "age": 30},
    {"id": 103, "name": "Amit", "age": -5},
    {"id": 104, "name": "Neha", "age": 28},
    {"id": None, "name": "John", "age": 22}
]

valid_records = []
invalid_records = []

for cust in customers:
    if cust["id"] is not None and cust["age"] > 0:
        valid_records.append(cust)
    else:
        invalid_records.append(cust)

print("--- Valid Customer Records ---")
for rec in valid_records:
    print(rec)

print("\n--- Invalid Customer Records ---")
for rec in invalid_records:
    print(rec)

print(f"\nValid records: {len(valid_records)}")
print(f"Invalid records: {len(invalid_records)}")

# ### Q19. Data Pipeline Monitoring
# **Logic Explanation:**  
# Processing and failure rates are computed as percentages of `total_records`. An `if-elif-else` classifier evaluates `processing_percentage` against SLA thresholds (`>= 95` Healthy, `80–94.99` Warning, `< 80` Critical) and outputs a structured monitoring report. Two test scenarios verify both Warning and Healthy states.

def generate_monitoring_report(total_records, processed_records, failed_records):
    processing_percentage = (processed_records / total_records) * 100
    failure_percentage = (failed_records / total_records) * 100

    if processing_percentage >= 95:
        status = "Healthy"
    elif processing_percentage >= 80:
        status = "Warning"
    else:
        status = "Critical"

    print("========== PIPELINE MONITORING REPORT ==========")
    print(f"Total Records       : {total_records}")
    print(f"Processed Records   : {processed_records} ({processing_percentage:.2f}%)")
    print(f"Failed Records      : {failed_records} ({failure_percentage:.2f}%)")
    print(f"Pipeline Status     : {status}")
    print("================================================\n")

print("--- Test Scenario 1 (Assignment Metrics) ---")
generate_monitoring_report(10000, 8500, 1500)

print("--- Test Scenario 2 (Healthy Run) ---")
generate_monitoring_report(10000, 9750, 250)

# ### Q20. Mini Ingestion Pipeline Capstone
# **Logic Explanation:**  
# This end-to-end ingestion pipeline integrates iteration, multi-condition record validation (`order_id` present, `amount > 0`, and `status == "SUCCESS"`), routing valid vs. rejected records into separate lists, aggregating revenue exclusively from valid orders, and formatting a dynamic summary report.

orders = [
    {"order_id": 1, "amount": 500, "status": "SUCCESS"},
    {"order_id": 2, "amount": 1200, "status": "FAILED"},
    {"order_id": 3, "amount": 800, "status": "SUCCESS"},
    {"order_id": 4, "amount": -200, "status": "SUCCESS"},
    {"order_id": 5, "amount": 1500, "status": "SUCCESS"}
]

valid_orders = []
invalid_orders = []
total_revenue = 0

# Stage 1 & 2: Read and validate source records
for order in orders:
    is_id_valid = order.get("order_id") is not None
    is_amount_valid = order["amount"] > 0
    is_status_valid = order["status"] == "SUCCESS"

    # Stage 3 & 4: Route valid and invalid records
    if is_id_valid and is_amount_valid and is_status_valid:
        valid_orders.append(order)
        total_revenue += order["amount"]
    else:
        invalid_orders.append(order)

# Stage 5: Generate ingestion summary
print("========== INGESTION REPORT ==========")
print(f"Total records received: {len(orders)}")
print(f"Valid records: {len(valid_orders)}")
print(f"Rejected records: {len(invalid_orders)}")
print(f"Total revenue: {total_revenue}")
print("======================================")
