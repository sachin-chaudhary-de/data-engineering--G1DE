# ==============================================================================
# Python Assignment - Data Engineering Foundation (HW-01)
# Name: Soham Jagtap
# Course / Batch: G1 - Data Engineering
# ==============================================================================


# ==============================================================================
# SECTION A - Variables and Data Types
# ==============================================================================

# --- Q1: Source Configuration ---
# Setting up basic configuration parameters for Upstox source stream
source_name = "Upstox"
batch_id = "BATCH_001"
record_count = 1500
is_pipeline_active = True
avg_processing_time = 12.75

print("--- Q1: Source Configuration ---")
print("Source Name:", source_name, "| Type:", type(source_name))
print("Batch ID:", batch_id, "| Type:", type(batch_id))
print("Record Count:", record_count, "| Type:", type(record_count))
print("Pipeline Active:", is_pipeline_active, "| Type:", type(is_pipeline_active))
print("Avg Processing Time:", avg_processing_time, "| Type:", type(avg_processing_time))


# --- Q2: Ingestion Metadata ---
# Inspecting metadata values, types, and identifying numeric metrics
source = "customer_api"
record_count = 2500
file_size_mb = 45.6
is_processed = False

metadata = {
    "source": source,
    "record_count": record_count,
    "file_size_mb": file_size_mb,
    "is_processed": is_processed
}

print("\n--- Q2: Ingestion Metadata ---")
for key, val in metadata.items():
    print(f"{key}: {val} (Type: {type(val).__name__})")

print("\nNumerical variables:")
for key, val in metadata.items():
    # In python, bool inherits from int, so we check not bool
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        print(f"- {key}: {val}")


# --- Q3: Data Type Investigation ---
# Raw values coming in as text strings; converting to proper data types
customer_id = "10245"
order_amount = "4500.50"
quantity = "5"
is_active = "True"

print("\n--- Q3: Data Type Investigation ---")
print("Before casting:")
print("customer_id:", type(customer_id), "order_amount:", type(order_amount))

# Type casting
customer_id_clean = int(customer_id)
order_amount_clean = float(order_amount)
quantity_clean = int(quantity)
is_active_clean = (is_active == "True")

print("\nAfter casting:")
print(f"customer_id: {customer_id_clean} ({type(customer_id_clean).__name__})")
print(f"order_amount: {order_amount_clean} ({type(order_amount_clean).__name__})")
print(f"quantity: {quantity_clean} ({type(quantity_clean).__name__})")
print(f"is_active: {is_active_clean} ({type(is_active_clean).__name__})")


# --- Q4: Pipeline Configuration ---
# Calculating total batches needed based on record count and batch size
max_records = 10000
batch_size = 500
retry_count = 3

total_batches = max_records // batch_size
print("\n--- Q4: Pipeline Configuration ---")
print(f"Total records: {max_records}, Batch size: {batch_size}")
print(f"Total batches required: {total_batches}")

# Test with odd number of records
test_records = 10250
extra_batches = (test_records + batch_size - 1) // batch_size
print(f"Test scenario: {test_records} records requires {extra_batches} batches.")


# ==============================================================================
# SECTION B - User Input and Operators
# ==============================================================================

# --- Q5: File Ingestion Calculator ---
print("\n--- Q5: File Ingestion Calculator ---")
# Calculating total MB from file count and average size
num_files = 12
avg_size_mb = 25.5
total_volume = num_files * avg_size_mb
print(f"Files: {num_files}, Avg Size: {avg_size_mb} MB -> Total Volume: {total_volume:.2f} MB")

# Test scenario 2
test_files, test_avg = 50, 4.2
print(f"Test scenario: {test_files} files * {test_avg} MB = {test_files * test_avg:.2f} MB")


# --- Q6: Batch Processing ---
print("\n--- Q6: Batch Processing ---")
total_records = 1275
batch_capacity = 100

complete_batches = total_records // batch_capacity
remaining_records = total_records % batch_capacity
total_batches_needed = complete_batches + (1 if remaining_records > 0 else 0)

print(f"Total records: {total_records}")
print(f"1. Complete batches: {complete_batches}")
print(f"2. Remaining records: {remaining_records}")
print(f"3. Total batches required: {total_batches_needed}")


# --- Q7: Data Processing Cost ---
print("\n--- Q7: Data Processing Cost ---")
rate_per_unit = 2.50
units_consumed = 450
total_cost = units_consumed * rate_per_unit

print(f"Units: {units_consumed}, Rate: Rs.{rate_per_unit}")
print(f"Total processing cost: Rs.{total_cost:.2f}")

# Test scenario 2
test_units = 1000
print(f"Test scenario: {test_units} units cost Rs.{test_units * rate_per_unit:.2f}")


# --- Q8: Storage Calculation ---
print("\n--- Q8: Storage Calculation ---")
bronze = 250
silver = 120
gold = 30

total_storage = bronze + silver + gold
print(f"1. Total storage consumption: {total_storage} GB")
print(f"2. Bronze: {bronze} GB ({(bronze / total_storage) * 100:.1f}%)")
print(f"   Silver: {silver} GB ({(silver / total_storage) * 100:.1f}%)")
print(f"   Gold:   {gold} GB ({(gold / total_storage) * 100:.1f}%)")


# ==============================================================================
# SECTION C - Conditional Statements and Data Validation
# ==============================================================================

# --- Q9: Mandatory Field Validation ---
print("\n--- Q9: Mandatory Field Validation ---")
record = {
    "customer_id": None,
    "customer_name": "Rahul",
    "city": "Bangalore"
}

if record.get("customer_id") is not None:
    print("Record accepted.")
else:
    print("Record rejected: Missing customer ID.")

# Test scenario with valid customer_id
record_valid = {"customer_id": 101, "customer_name": "Priya", "city": "Pune"}
if record_valid.get("customer_id") is not None:
    print("Test scenario (with ID): Record accepted.")


# --- Q10: API Response Handling ---
print("\n--- Q10: API Response Handling ---")
def check_status(code):
    if code == 200:
        return "Process API response"
    elif code == 400:
        return "Bad request — check request parameters"
    elif code == 401:
        return "Authentication failed"
    elif code == 404:
        return "Source endpoint not found"
    elif code == 429:
        return "Rate limit exceeded"
    else:
        return "Handle unexpected API error"

# Checking sample status codes
for sc in [200, 401, 429, 500]:
    print(f"Status {sc}: {check_status(sc)}")


# --- Q11: Data Quality Check ---
print("\n--- Q11: Data Quality Check ---")
transaction = {
    "transaction_id": 101,
    "amount": -500,
    "status": "SUCCESS"
}

if transaction.get("amount", 0) > 0 and transaction.get("status") == "SUCCESS":
    print("Transaction is valid.")
else:
    print("Transaction is invalid.")

# Test scenario with positive amount
txn_valid = {"transaction_id": 102, "amount": 1500, "status": "SUCCESS"}
if txn_valid.get("amount", 0) > 0 and txn_valid.get("status") == "SUCCESS":
    print("Test scenario (positive amount): Transaction is valid.")


# --- Q12: Pipeline Execution Mode ---
print("\n--- Q12: Pipeline Execution Mode ---")
def run_pipeline_mode(mode):
    clean_mode = mode.strip().upper()
    if clean_mode == "FULL":
        return "Load all historical records."
    elif clean_mode == "INCREMENTAL":
        return "Load new records."
    elif clean_mode == "BACKFILL":
        return "Reload historical data for a specified period."
    else:
        return "Invalid execution mode"

print("Mode FULL:", run_pipeline_mode("FULL"))
print("Mode INCREMENTAL:", run_pipeline_mode("INCREMENTAL"))
print("Mode BACKFILL:", run_pipeline_mode("BACKFILL"))
print("Mode UNKNOWN:", run_pipeline_mode("UNKNOWN"))


# --- Q13: Data Quality Scoring ---
print("\n--- Q13: Data Quality Scoring ---")
def score_quality(score):
    if score < 0 or score > 100:
        return "Invalid score: Must be between 0 and 100"
    elif score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Needs improvement"
    else:
        return "Critical — investigate pipeline"

for s in [95, 82, 65, 40, 105]:
    print(f"Score {s}: {score_quality(s)}")


# ==============================================================================
# SECTION D - Loops and Record Processing
# ==============================================================================

# --- Q14: Batch Record Processing ---
print("\n--- Q14: Batch Record Processing ---")
customer_ids = [101, 102, 103, 104, 105]

for cid in customer_ids:
    print(f"Processing customer: {cid}")


# --- Q15: Failed Record Identification ---
print("\n--- Q15: Failed Record Identification ---")
amounts = [500, 1200, -100, 800, -50, 2000]

invalid_count = 0
for amt in amounts:
    if amt < 0:
        print(f"Invalid negative amount found: {amt}")
        invalid_count += 1

print(f"Total invalid records: {invalid_count}")


# --- Q16: API Retry Simulation ---
print("\n--- Q16: API Retry Simulation ---")
attempts = 0
max_retries = 3

while attempts < max_retries:
    attempts += 1
    print(f"Attempt number: {attempts}")

print("Maximum retries reached")


# --- Q17: Daily Ingestion Summary ---
print("\n--- Q17: Daily Ingestion Summary ---")
records = [
    {"id": 1, "status": "SUCCESS"},
    {"id": 2, "status": "FAILED"},
    {"id": 3, "status": "SUCCESS"},
    {"id": 4, "status": "SUCCESS"},
    {"id": 5, "status": "FAILED"}
]

success_count = 0
failed_count = 0

for rec in records:
    if rec["status"] == "SUCCESS":
        success_count += 1
    elif rec["status"] == "FAILED":
        failed_count += 1

print(f"Total records: {len(records)}")
print(f"Successful records: {success_count}")
print(f"Failed records: {failed_count}")


# ==============================================================================
# SECTION E - Combined Data Engineering Scenarios
# ==============================================================================

# --- Q18: Customer Data Ingestion Validator ---
print("\n--- Q18: Customer Data Ingestion Validator ---")
customers = [
    {"id": 101, "name": "Rahul", "age": 25},
    {"id": None, "name": "Priya", "age": 30},
    {"id": 103, "name": "Amit", "age": -5},
    {"id": 104, "name": "Neha", "age": 28},
    {"id": None, "name": "John", "age": 22}
]

valid_customers = []
invalid_customers = []

for cust in customers:
    # Rule: id must not be None and age must be positive
    if cust.get("id") is not None and cust.get("age", 0) > 0:
        valid_customers.append(cust)
    else:
        invalid_customers.append(cust)

print("Valid records:")
for v in valid_customers:
    print(" ", v)

print("Invalid records:")
for inv in invalid_customers:
    print(" ", inv)

print(f"\nValid records: {len(valid_customers)}")
print(f"Invalid records: {len(invalid_customers)}")


# --- Q19: Data Pipeline Monitoring ---
print("\n--- Q19: Data Pipeline Monitoring ---")
total_records = 10000
processed_records = 8500
failed_records = 1500

proc_pct = (processed_records / total_records) * 100
fail_pct = (failed_records / total_records) * 100

if proc_pct >= 95:
    health_status = "Healthy"
elif proc_pct >= 80:
    health_status = "Warning"
else:
    health_status = "Critical"

print("========== PIPELINE MONITORING REPORT ==========")
print(f"Total Records:      {total_records}")
print(f"Processed Records:  {processed_records} ({proc_pct:.2f}%)")
print(f"Failed Records:     {failed_records} ({fail_pct:.2f}%)")
print(f"Pipeline Status:    {health_status}")
print("================================================")


# --- Q20: Mini Ingestion Pipeline (Capstone) ---
print("\n--- Q20: Mini Ingestion Pipeline ---")
orders = [
    {"order_id": 1, "amount": 500, "status": "SUCCESS"},
    {"order_id": 2, "amount": 1200, "status": "FAILED"},
    {"order_id": 3, "amount": 800, "status": "SUCCESS"},
    {"order_id": 4, "amount": -200, "status": "SUCCESS"},
    {"order_id": 5, "amount": 1500, "status": "SUCCESS"}
]

valid_orders = []
rejected_orders = []
revenue = 0

# Stage 1: Read source records
for order in orders:
    # Stage 2: Validate records
    valid_id = order.get("order_id") is not None
    valid_amt = order.get("amount", 0) > 0
    valid_status = order.get("status") == "SUCCESS"

    if valid_id and valid_amt and valid_status:
        # Stage 3: Process valid records
        valid_orders.append(order)
        revenue += order["amount"]
    else:
        # Stage 4: Handle invalid records
        rejected_orders.append(order)

# Stage 5: Ingestion summary
print("========== INGESTION REPORT ==========")
print(f"Total records received: {len(orders)}")
print(f"Valid records: {len(valid_orders)}")
print(f"Rejected records: {len(rejected_orders)}")
print(f"Total revenue: {revenue}")
print("======================================")
