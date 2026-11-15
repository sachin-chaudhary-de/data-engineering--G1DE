

#                                   # Python Assignment – Data Engineering Foundation

                                      # ## Section A – Variables and Data Types

# ### Q1. Source Configuration
#
# **Question**
#
# A data pipeline receives this configuration:
#
# - Source name: `Upstox`
# - Batch ID: `BATCH_001`
# - Number of records: `1500`
# - Pipeline active: `True`
# - Average processing time: `12.75`
#
# Create Python variables for each value. Print each variable and its data type.
#
# **Explanation / Main Logic**
#
#  1. Store each configuration value in a separate variable.
#  2. Use print() to display the value.
#  3. Use type() to display Variables data type.

# code

# Store source configuration
source_name = "Upstox"
batch_id = "BATCH_001"
number_of_records = 1500
pipeline_active = True
average_processing_time = 12.75

# Print values and their data types
print(source_name, type(source_name))
print(batch_id, type(batch_id))
print(number_of_records, type(number_of_records))
print(pipeline_active, type(pipeline_active))
print(average_processing_time, type(average_processing_time))

                                                   # ### Q2. Ingestion Metadata
#
# **Question**
#
# An ingestion process generates this metadata:
#
# ```python
# source = "customer_api"
# record_count = 2500
# file_size_mb = 45.6
# is_processed = False
# ```
#
# Write Python code to:
# 1. Print all metadata values.
# 2. Print the data type of each variable.
# 3. Identify which variables contain numerical values.
#
# **Explanation / Main Logic**
#
# - 1. Print the four metadata values and their types.
# - 2. `record_count` is an integer and `file_size_mb` is a float.
# - 3. These two variables contain numerical values.

# code

# Store the ingestion metadata
source = "customer_api"
record_count = 2500
file_size_mb = 45.6
is_processed = False

# Print values and data types
print(source, type(source))
print(record_count, type(record_count))
print(file_size_mb, type(file_size_mb))
print(is_processed, type(is_processed))

# Print the numerical values
print("Numerical values:", record_count, file_size_mb)

                                                      # ### Q3. Data Type Investigation
#
# **Question**
#
# A source system provides these values:
#
# ```python
# customer_id = "10245"
# order_amount = "4500.50"
# quantity = "5"
# is_active = "True"
# ```
#
# Identify the current data type of each variable. Then convert them into appropriate Python data types for processing.
#
# **Explanation / Main Logic**
#
# 1. All four starting values are strings.
# 2. Convert the ID and quantity to integers.
# 3. Convert the amount to a float and the active flag to a Boolean.
# 4. Print the converted values and their types.

# code

# Values received as strings
customer_id = "10245"
order_amount = "4500.50"
quantity = "5"
is_active = "True"

# Show the original data types
print("Original types:")
print(type(customer_id), type(order_amount), type(quantity), type(is_active))

# Convert strings to suitable data types
customer_id = int(customer_id)
order_amount = float(order_amount)
quantity = int(quantity)
is_active = is_active == "True"

# Show converted values and types
print("Converted values:")
print(customer_id, type(customer_id))
print(order_amount, type(order_amount))
print(quantity, type(quantity))
print(is_active, type(is_active))

                                                     # ### Q4. Pipeline Configuration
#
# **Question**
#
# A pipeline has these configuration parameters:
#
# ```python
# max_records = 10000
# batch_size = 500
# retry_count = 3
# ```
#
# Calculate how many batches are required to process all records. Print the result.
#
# **Explanation / Main Logic**
#
# - 1. Divide the total records by the batch size.
# - 2. Use ceiling-style integer division so any partly filled batch is also counted.
# - 3. `retry_count` is configuration data and is not needed for this calculation.

# code

# Store pipeline settings
max_records = 10000
batch_size = 500
retry_count = 3

# Count full and partly filled batches
total_batches = (max_records + batch_size - 1) // batch_size

print("Total batches required:", total_batches)

# Additional code cell from the original notebook (preserved in sequence).

# Store pipeline settings
max_records = 10000
batch_size = 500
retry_count = 3

# Count full and partly filled batches
total_batches = (max_records // batch_size)

print("Total batches required:", total_batches)

                                          # ## Section B – User Input and Operators

                                            # ### Q5. File Ingestion Calculator
#
# **Question**
#
# A pipeline receives files from an external source. Ask the user to enter:
# - Number of files received.
# - Average file size in MB.
#
# Calculate and display the total data volume in MB.
#
# **Explanation / Main Logic**
#
# - 1. Read both values using `input()`.
# - 2. Convert them to numbers.
# - 3. Multiply file count by average file size to get total data volume.

# code

# Get file details from the user
file_count = int(input("Enter number of files: "))
average_file_size = float(input("Enter average file size in MB: "))

# Calculate total data volume
total_Data_volume = file_count * average_file_size

# Display the result
print("Total data volume:", total_Data_volume,"MB")

                                                 # ### Q6. Batch Processing
#
# **Question**
#
# A data ingestion job receives 1,275 records. The pipeline processes 100 records per batch. Calculate:
# 1. Number of complete batches.
# 2. Remaining records.
# 3. Total batches required.
#
# **Explanation / Main Logic**
#
# - 1. Use floor division (`//`) to find complete batches.
# - 2. Use modulo (`%`) to find remaining records.
# - 3. Add one batch if some records remain.

# code

# Store record and batch details
total_records = 1275
batch_size = 100

# Calculate complete batches and remaining records
complete_batches = total_records // batch_size
remaining_records = total_records % batch_size

# Include one more batch if records are left
total_batches = complete_batches
if remaining_records > 0:
    total_batches = total_batches + 1

print("Complete batches:", complete_batches)
print("Remaining records:", remaining_records)
print("Total batches required:", total_batches)

                                                    # ### Q7. Data Processing Cost
#
# **Question**
#
# A cloud processing job charges ₹2.50 per processing unit. Ask the user to enter the number of processing units consumed. Calculate the total processing cost.
#
# **Explanation / Main Logic**
#
# - 1. Read the number of processing units.
# - 2. Convert the input to a number.
# - 3. Multiply units by ₹2.50 to calculate the cost.

# code

# Get processing units from the user
processing_units = float(input("Enter processing units consumed: "))

# Calculate the total cost
cost_per_unit = 2.50
total_cost = processing_units * cost_per_unit

print("Total processing cost: Rs.", total_cost)

                                                 # ### Q8. Storage Calculation
#
# **Question**
#
# A data lake contains:
# - Bronze layer: 250 GB
# - Silver layer: 120 GB
# - Gold layer: 30 GB
#
# Calculate:
# 1. Total storage consumption.
# 2. Percentage of storage occupied by each layer.
#
# **Explanation / Main Logic**
#
# - 1. Add the three layer sizes to get total storage.
# - 2. Divide each layer size by total storage and multiply by 100.
# - 3. Print each percentage with two decimal places.

# code

# Store the size of each layer
bronze = 250
silver = 120
gold = 30

# Calculate total storage
total_storage = bronze + silver + gold

# Calculate the percentage used by each layer
bronze_percent = (bronze / total_storage) * 100
silver_percent = (silver / total_storage) * 100
gold_percent = (gold / total_storage) * 100

print("Total storage:", total_storage, "GB")
print("Bronze:", round(bronze_percent, 2), "%")
print("Silver:", round(silver_percent, 2), "%")
print("Gold:", round(gold_percent, 2), "%")

                                             # ## Section C – Conditional Statements and Data Validation

                                                # ### Q9. Mandatory Field Validation
#
# **Question**
#
# An API provides this customer record:
#
# ```python
# record = {
#     "customer_id": None,
#     "customer_name": "Rahul",
#     "city": "Bangalore"
# }
# ```
#
# Write a program to check whether `customer_id` is available.
# - If available, print `Record accepted`.
# - Otherwise, print `Record rejected: Missing customer ID.`
#
# **Explanation / Main Logic**
#
# - 1. Read the `customer_id` value from the dictionary.
# - 2. Check whether it is not `None`.
# - 3. Print the correct result using `if` and `else`.

# code

# Store the customer record
record = {
    "customer_id": None,
    "customer_name": "Rahul",
    "city": "Bangalore"
}

# Check whether the customer ID is available
if record["customer_id"] is not None:
    print("Record accepted")
else:
    print("Record rejected: Missing customer ID.")

                                                       # ### Q10. API Response Handling
#
# **Question**
#
# An ingestion pipeline receives an HTTP response status code. Ask the user to enter the response status code and apply these rules:
#
# - 200: Process API response
# - 400: Bad request — check request parameters
# - 401: Authentication failed
# - 404: Source endpoint not found
# - 429: Rate limit exceeded
# - Any other code: Handle unexpected API error
#
# Write a program to implement this logic.
#
# **Explanation / Main Logic**
#
# - 1. Read the status code and convert it to an integer.
# - 2. Use `if` / `elif` to check each given code.
# - 3. Use `else` for all other codes.

# code

# Get the HTTP response code
status_code = int(input("Enter HTTP status code: "))

# Choose the action for the response code
if status_code == 200:
    print("Process API response")
elif status_code == 400:
    print("Bad request - check request parameters")
elif status_code == 401:
    print("Authentication failed")
elif status_code == 404:
    print("Source endpoint not found")
elif status_code == 429:
    print("Rate limit exceeded")
else:
    print("Handle unexpected API error")

                                             # ### Q11. Data Quality Check
#
# **Question**
#
# A pipeline receives this transaction record:
#
# ```python
# transaction = {
#     "transaction_id": 101,
#     "amount": -500,
#     "status": "SUCCESS"
# }
# ```
#
# A valid transaction must satisfy both conditions:
# - Amount must be greater than zero.
# - Status must be `SUCCESS`.
#
# Write a program to validate the transaction and print whether it is valid or invalid.
#
# **Explanation / Main Logic**
#
# - 1. Check that the amount is greater than zero.
# - 2. Check that the status is `SUCCESS`.
# - 3. Use `and` because both conditions must be true.

# code

# Store the transaction
transaction = {
    "transaction_id": 101,
    "amount": -500,
    "status": "SUCCESS"
}

# Both conditions must be true
if transaction["amount"] > 0 and transaction["status"] == "SUCCESS":
    print("Transaction is valid")
else:
    print("Transaction is invalid")

                                               # ### Q12. Pipeline Execution Mode
#
# **Question**
#
# A data pipeline supports three execution modes:
# - FULL: Load all historical records.
# - INCREMENTAL: Load new records.
# - BACKFILL: Reload historical data for a specified period.
#
# Accept the execution mode from the user and print the corresponding pipeline action. If the user enters an unsupported mode, print `Invalid execution mode`.
#
# **Explanation / Main Logic**
#
# - 1. Read the mode and convert it to uppercase.
# - 2. Compare it with the three supported modes.
# - 3. Print the matching action, or an invalid-mode message.

# code

# Get the execution mode
mode = input("Enter execution mode (FULL/INCREMENTAL/BACKFILL): ").upper()

# Check the selected mode
if mode == "FULL":
    print("Load all historical records")
elif mode == "INCREMENTAL":
    print("Load new records")
elif mode == "BACKFILL":
    print("Reload historical data for a specified period")
else:
    print("Invalid execution mode")

                                                     # ### Q13. Data Quality Scoring
#
# **Question**
#
# A data quality monitoring process generates a quality score between 0 and 100. Apply these rules:
#
# - 90–100: Excellent
# - 75–89: Good
# - 50–74: Needs improvement
# - Below 50: Critical — investigate pipeline
#
# Accept the score from the user and classify the result. Also reject scores outside the range of 0–100.
#
# **Explanation / Main Logic**
#
# - 1. Read the score as a number.
# - 2. First check whether it is between 0 and 100.
# - 3. If it is in range, use `if` / `elif` to classify it.

# code

# Get the quality score
score = float(input("Enter quality score (0 to 100): "))

# Check the valid score range first
if score < 0 or score > 100:
    print("Invalid score: Enter a value from 0 to 100")
elif score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 50:
    print("Needs improvement")
else:
    print("Critical - investigate pipeline")

# ## Section D – Loops and Record Processing

                                                    # ### Q14. Batch Record Processing
#
# **Question**
#
# A pipeline receives this list of customer IDs:
#
# ```python
# customer_ids = [101, 102, 103, 104, 105]
# ```
#
# Use a loop to process each customer ID. For every ID, print `Processing customer: <ID>`.
#
# **Explanation / Main Logic**
#
# - 1. Use a `for` loop to visit each ID in the list.
# - 2. Print the current ID during each loop run.

# code

# List of customer IDs
customer_ids = [101, 102, 103, 104, 105]

# Process each customer ID
for customer_id in customer_ids:
    print("Processing customer:", customer_id)

                                                 # ### Q15. Failed Record Identification
#
# **Question**
#
# A source system sends these transaction amounts:
#
# ```python
# amounts = [500, 1200, -100, 800, -50, 2000]
# ```
#
# Write a program to:
# 1. Iterate through all amounts.
# 2. Identify negative transaction amounts.
# 3. Print invalid amounts.
# 4. Count the total number of invalid records.
#
# **Explanation / Main Logic**
#
# - 1. Start an invalid-record counter at zero.
# - 2. Use a `for` loop to check every amount.
# - 3. If an amount is negative, print it and increase the counter.
# - 4. Print the final count.

# code

# List of transaction amounts
amounts = [500, 1200, -100, 800, -50, 2000]
invalid_count = 0

# Find negative amounts
for amount in amounts:
    if amount < 0:
        print("Invalid amount:", amount)
        invalid_count = invalid_count + 1

print("Total invalid records:", invalid_count)

                                                    # ### Q16. API Retry Simulation
#
# **Question**
#
# An API ingestion process can fail temporarily. You are given:
#
# ```python
# attempts = 0
# max_retries = 3
# ```
#
# Use a `while` loop to simulate API attempts:
# - Increment the attempt counter on every attempt.
# - Print the attempt number.
# - Stop when three attempts have been completed.
# - Print `Maximum retries reached` after the third attempt.
#
# **Explanation / Main Logic**
#
# - 1. Continue the loop while attempts are less than three.
# - 2. Increase the counter by one on every attempt.
# - 3. Print the attempt number.
# - 4. Print the final message after the loop ends.

# code

# Set the starting attempt and retry limit
attempts = 0
max_retries = 3

# Run attempts until the limit is reached
while attempts < max_retries:
    attempts = attempts + 1
    print("Attempt number:", attempts)

print("Maximum retries reached")

                                              # ### Q17. Daily Ingestion Summary
#
# **Question**
#
# A pipeline processes these records:
#
# ```python
# records = [
#     {"id": 1, "status": "SUCCESS"},
#     {"id": 2, "status": "FAILED"},
#     {"id": 3, "status": "SUCCESS"},
#     {"id": 4, "status": "SUCCESS"},
#     {"id": 5, "status": "FAILED"}
# ]
# ```
#
# Write a program to:
# 1. Iterate through all records.
# 2. Count successful records.
# 3. Count failed records.
# 4. Print the final ingestion summary.
#
# **Explanation / Main Logic**
#
# - 1. Start success and failure counters at zero.
# - 2. Loop through every record.
# - 3. Increase the matching counter based on its status.
# - 4. Print the total and both counts.

# code

# Store the ingestion records
records = [
    {"id": 1, "status": "SUCCESS"},
    {"id": 2, "status": "FAILED"},
    {"id": 3, "status": "SUCCESS"},
    {"id": 4, "status": "SUCCESS"},
    {"id": 5, "status": "FAILED"}
]

successful_count = 0
failed_count = 0

# Count records by their status
for record in records:
    if record["status"] == "SUCCESS":
        successful_count = successful_count + 1
    elif record["status"] == "FAILED":
        failed_count = failed_count + 1

print("Total records:", len(records))
print("Successful records:", successful_count)
print("Failed records:", failed_count)

                                             # ## Section E – Combined Data Engineering Scenarios

                                                     # ### Q18. Customer Data Ingestion Validator
#
# **Question**
#
# A source API sends these customer records:
#
# ```python
# customers = [
#     {"id": 101, "name": "Rahul", "age": 25},
#     {"id": None, "name": "Priya", "age": 30},
#     {"id": 103, "name": "Amit", "age": -5},
#     {"id": 104, "name": "Neha", "age": 28},
#     {"id": None, "name": "John", "age": 22}
# ]
# ```
#
# Write a Python program that:
# 1. Iterates through every customer record.
# 2. Checks whether the customer ID is available.
# 3. Checks whether the age is greater than zero.
# 4. Prints valid and invalid records separately.
# 5. Counts the total valid and invalid records.
#
# **Explanation / Main Logic**
#
# - 1. Create separate counters for valid and invalid records.
# - 2. Loop through every customer.
# - 3. A customer is valid only when the ID is not `None` and age is greater than zero.
# - 4. Print each record in the correct group and update its counter.

# code

# Store customer records
customers = [
    {"id": 101, "name": "Rahul", "age": 25},
    {"id": None, "name": "Priya", "age": 30},
    {"id": 103, "name": "Amit", "age": -5},
    {"id": 104, "name": "Neha", "age": 28},
    {"id": None, "name": "John", "age": 22}
]

valid_count = 0
invalid_count = 0

# Check every customer record
for customer in customers:
    if customer["id"] is not None and customer["age"] > 0:
        print("Valid record:", customer)
        valid_count = valid_count + 1
    else:
        print("Invalid record:", customer)
        invalid_count = invalid_count + 1

print("Valid records:", valid_count)
print("Invalid records:", invalid_count)

                                             # ### Q19. Data Pipeline Monitoring
#
# **Question**
#
# Your team monitors a batch ingestion pipeline with these metrics:
#
# ```python
# total_records = 10000
# processed_records = 8500
# failed_records = 1500
# ```
#
# Write a program to:
# 1. Calculate the processing percentage.
# 2. Calculate the failure percentage.
# 3. Classify pipeline execution:
#    - 95 or above: Healthy
#    - 80–94.99: Warning
#    - Below 80: Critical
# 4. Print a pipeline monitoring report.
#
# **Explanation / Main Logic**
#
# - 1. Divide processed and failed records by total records, then multiply by 100.
# - 2. Use the processing percentage to choose the pipeline status.
# - 3. Print both percentages and the status as a report.

# code

# Store pipeline metrics
total_records = 10000
processed_records = 8500
failed_records = 1500

# Calculate percentages
processing_percentage = (processed_records / total_records) * 100
failure_percentage = (failed_records / total_records) * 100

# Classify the pipeline
if processing_percentage >= 95:
    pipeline_status = "Healthy"
elif processing_percentage >= 80:
    pipeline_status = "Warning"
else:
    pipeline_status = "Critical"

# Print the monitoring report
print("===== PIPELINE MONITORING REPORT =====")
print("Processing percentage:", round(processing_percentage, 2), "%")
print("Failure percentage:", round(failure_percentage, 2), "%")
print("Pipeline status:", pipeline_status)
print("======================================")

                                               # ### Q20. Mini Ingestion Pipeline
#
# **Question**
#
# Build a simple Python-based ingestion process for these e-commerce orders:
#
# ```python
# orders = [
#     {"order_id": 1, "amount": 500, "status": "SUCCESS"},
#     {"order_id": 2, "amount": 1200, "status": "FAILED"},
#     {"order_id": 3, "amount": 800, "status": "SUCCESS"},
#     {"order_id": 4, "amount": -200, "status": "SUCCESS"},
#     {"order_id": 5, "amount": 1500, "status": "SUCCESS"}
# ]
# ```
#
# Perform these stages:
# 1. Read source records by iterating through every order.
# 2. Validate records. An order is valid only if `order_id` is available, `amount` is greater than zero, and `status` is `SUCCESS`.
# 3. Collect valid orders separately, calculate their total revenue, and count them.
# 4. Collect invalid orders separately and count rejected orders.
# 5. Print the ingestion summary.
#
# **Explanation / Main Logic**
#
# - 1. Create separate lists for valid and invalid orders.
# - 2. Loop through all orders and check all three required conditions.
# - 3. Add valid orders to the valid list and add their amount to revenue.
# - 4. Add all other orders to the rejected list.
# - 5. Print the counts and total revenue.



# code 

# Store the source orders
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

# Read and validate each order
for order in orders:
    if (order["order_id"] is not None
            and order["amount"] > 0
            and order["status"] == "SUCCESS"):
        valid_orders.append(order)
        total_revenue = total_revenue + order["amount"]
    else:
        invalid_orders.append(order)

# Print the final ingestion report
print("========== INGESTION REPORT ==========")
print("Total records received:", len(orders))
print("Valid records:", len(valid_orders))
print("Rejected records:", len(invalid_orders))
print("Total revenue:", total_revenue)
print("======================================")
