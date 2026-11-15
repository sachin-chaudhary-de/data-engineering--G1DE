"""
                                                                                              ASSIGNMENT : 1
                                                                                              
                                                                                 DATA ENGINEERING FOUNDATION  USING PYTHON

                                                                                             SUBMITTED BY
                                                                                             
                                                                                        STUDENT ID: STU-5E348D
                                                                                          SHAIK CHARAN - G1 DE

           
                                                                                              SUBMITTED TO
                                                                                             
                                                                                          Sri. Sachin Chaudhary
                                                                                         
                                                                                            DATE : 15/11/2026
"""


# ======================================================================================================================================================================================================

# ======================================================================================================================================================================================================
# # Section A – Variables and Data Types
#
# ## Q1. Source Configuration
#
# A data pipeline receives the following configuration:
#
# | Configuration | Value |
# |---|---|
# | Source name | Upstox |
# | Batch ID | BATCH_001 |
# | Number of records | 1500 |
# | Pipeline active | True |
# | Average processing time | 12.75 |
#
#  Create Python variables for each configuration value. Print each variable and its data type.
# ==============================================================================

print("\n" + "="*70)
print("Q1. Source Configuration")
print("="*70)
# %%
source_name = "Upstox"
batch_id = "BATCH_001"
number_of_records = 1500
pipeline_active = True
avg_processing_time = 12.75

print("source_name:", source_name,"| Data type:", type(source_name))
print("batch_id:", batch_id,"| Data type:", type(batch_id))
print("number_of_records:", number_of_records, "| Data type:", type(number_of_records))
print("pipeline_active:", pipeline_active, "| Data type:", type(pipeline_active))
print("avg_processing_time:", avg_processing_time, "| Data type:", type(avg_processing_time))




# logic / my approach:
# - created variables for all pipeline configuration values.
# - used appropriate data types: str, int, bool, and float.
# - used print() to display the values.
# - used type() to identify each variable's data type.

# ==============================================================================
# ## Q2. Ingestion Metadata
#
# An ingestion process generates the following metadata:
#
# ```python
# source = "customer_api"
# record_count = 2500
# file_size_mb = 45.6
# is_processed = False
#
# Write Python code to:
#
# 1. Print all metadata values.
# 2. Print the data type of each variable.
# 3. Identify which variables contain numerical values.
# ==============================================================================

print("\n" + "="*70)
print("Q2. Ingestion Metadata")
print("="*70)
# %%
source = "customer_api"
record_count = 2500
file_size_mb = 45.6
is_processed = False

print("1.ALL META DATA VALUES")
print(source)
print(record_count)
print(file_size_mb)
print(is_processed)
print()

print("2.DATA TYPE OF EACH VARIBLE")
print("source:",source ,"|" ,type(source))
print("record_count:", record_count, "|", type(record_count))
print("file_size_mb:", file_size_mb, "|", type(file_size_mb))
print("is_processed:" , is_processed, "|", type(is_processed))
print()

print("Numerical variables: record_count, file_size_mb")



# logic / my approach:
# - created variables to store the ingestion metadata.
# - printed all metadata values.
# - used type() to identify the data type of each variable.
# - identified record_count and file_size_mb as numerical variables.


# ==============================================================================
#
#
# ## Q3. Data Type Investigation
#
# A source system provides these values:
#
# ```python
# customer_id = "10245"
# order_amount = "4500.50"
# quantity = "5"
# is_active = "True"
#
# Identify the current data type of each variable.
# Then convert them into appropriate Python data types for processing.
# ==============================================================================

print("\n" + "="*70)
print("Q3. Data Type Investigation")
print("="*70)
# %%
customer_id = "10245"
order_amount = "4500.50"
quantity = "5"
is_active = "True"

print("DATA TYPE OF EACH VARIABLE")
print("customer_id:", customer_id , " - ", type(customer_id))
print("order_amount:", order_amount , " - ", type(order_amount))
print("quantity:", quantity, " - ", type(quantity))
print("is_active:", is_active, " - ", type(is_active))
print()
 
 #converting into appropriate python data types for processing
customer_id = int(customer_id)
order_amount = float(order_amount)
quantity = int(quantity)
is_active = is_active == "True"
 
# Verify converted values and data types
print("CONVERTED VALUES AND DATA TYPES")
print("customer_id:", customer_id, "-", type(customer_id))
print("order_amount:", order_amount, "-", type(order_amount))
print("quantity:", quantity, "-", type(quantity))
print("is_active:", is_active, "-", type(is_active))


# logic / my approach:
# - created variables with string values.
# - used type() to identify their original data types.
# - converted customer_id and quantity into int.
# - converted order_amount into float.
# - converted is_active into bool.
# - printed the converted values and their data types.


# ==============================================================================
# ## Q4. Pipeline Configuration
#
# A pipeline has these configuration parameters:
#
# ```python
# max_records = 10000
# batch_size = 500
# retry_count = 3
#
#
# Calculate how many batches are required to process all records.
#
# Print the result.
# ==============================================================================

print("\n" + "="*70)
print("Q4. Pipeline Configuration")
print("="*70)
# %%
#given input
max_records = 10000
batch_size = 500
retry_count = 3

#calc
total_batches = max_records // batch_size
print("total_batches:", total_batches)


# logic / my approach:
# - assigned values to max_records, batch_size, and retry_count.
# - used // (floor division) to calculate the number of batches.
# - printed the total number of batches required.


# ==============================================================================
# ## Section B – User Input and Operators
#
# ### Q5. File Ingestion Calculator
#
# A pipeline receives files from an external source.
#
# Ask the user to enter:
#
# - Number of files received.
# - Average file size in MB.
#
# Calculate and display the total data volume in MB.
# ==============================================================================

print("\n" + "="*70)
print("Q5. File Ingestion Calculator")
print("="*70)
# %%
# user input
number_of_files = int(input("enter number files recieved:"))
avg_file_size = float(input("enter avg file recieved in MB:"))

#calc
total_data_volume = number_of_files * avg_file_size
print(total_data_volume, "MB")



# logic / my approach:
# - used input() to get the number of files and average file size.
# - converted the inputs into int and float.
# - multiplied both values to calculate total data volume.
# - printed the total data volume in MB.

# ==============================================================================
#
# ### Q6. Batch Processing Calculation
#
# A data pipeline needs to process 1275 records. Each batch can process 100 records.
#
# Calculate and display:                                                                           
# 1 .Number of complete batches.                                                                 
# 2 .Number of remaining records.                                                               
# 3 .Total number of batches required.
# ==============================================================================

print("\n" + "="*70)
print("Q6. Batch Processing Calculation")
print("="*70)
# %%
#given input
total_records = 1275
each_batch_size = 100

#calc
complete_batches = total_records // each_batch_size # cacl how many full batches can be created
remaining_records = total_records % each_batch_size # calc and tells remaining records , after creating full batches
total_batches_required = complete_batches
if remaining_records > 0:
    total_batches_required = total_batches_required + 1
    
    
print("complete_batches:", complete_batches)
print("remaining_records:", remaining_records)
print("total_batches_required:", total_batches_required)


# logic / my approach:
# - assigned the total number of records and batch size.
# - used // to calculate complete batches.
# - used % to find the remaining records.
# - used an if condition to add one extra batch if records remain.
# - printed complete batches, remaining records, and total batches required.


# ==============================================================================
# ### Q7. Data Processing Cost
#
# A cloud processing job charges ₹2.50 per processing unit.
#
# Ask the user to enter the number of processing units consumed.
#
# Calculate the total processing cost.
# ==============================================================================

print("\n" + "="*70)
print("Q7. Data Processing Cost")
print("="*70)
# %%
# given input 
per_processing_unit = 2.50

#calc
consumed_units =float(input("enter total no of processing units consumed:"))

total_processing_units = consumed_units * per_processing_unit

print("total processing cost:", total_processing_units)


# logic / my approach:
# - assigned the processing cost per unit.
# - used input() to get the consumed processing units.
# - converted the input into float.
# - multiplied consumed units by the cost per unit.
# - printed the total processing cost.

# ==============================================================================
# ### Q8. Storage Calculation
#
# A data lake contains:
#
# ● Bronze layer: 250 GB                  
#
# ● Silver layer: 120 GB
#
# ● Gold layer: 30 GB
#
#
# Calculate:
# 1. Total storage consumption.
# 2. Percentage of storage occupied by each layer.
# ==============================================================================

print("\n" + "="*70)
print("Q8. Storage Calculation")
print("="*70)
# %%
#given input
bronze_layer = 250
silver_layer = 120 
gold_layer = 30 

#calc total storage
total_storage = bronze_layer + silver_layer + gold_layer

#calc %
bronze_storage =(bronze_layer / total_storage) * 100
silver_storage =(silver_layer / total_storage) * 100
gold_storage = (gold_layer / total_storage) * 100

print(total_storage, "gb")
print("bronze_storage:", bronze_storage, "%")
print("silver_storage:", silver_storage, "%")
print("gold_storage:", gold_storage, "%")


# logic / my approach:
# - assigned storage values for bronze, silver, and gold layers.
# - added all three values to calculate total storage.
# - calculated the storage percentage of each layer.
# - used print() to display total storage and individual percentages.

# ==============================================================================
# ## Section C – Conditional Statements and Data Validation
#
# ### Q9. Mandatory Field Validation
#
# An API provides customer records.
#
# ```python
# record = {
#     "customer_id": None,
#     "customer_name": "Rahul",
#     "city": "Bangalore"
# }
#
# Write a program to check whether customer_id is available.
# - If available, print Record accepted.
# - Otherwise, print Record rejected: Missing customer ID.
# ==============================================================================

print("\n" + "="*70)
print("Q9. Mandatory Field Validation")
print("="*70)
# %%
#given input:
record = {
    "customer_id": None,
    "customer_name": "Rahul",
    "city": "Bangalore"
}

if record["customer_id"] is not None:
    print("record accepted")
else: 
    print("Record rejected: Missing customer ID")
    
    
# logic / my approach:
# - created a dictionary to store customer details.
# - used an if condition to check whether customer_id is not None.
# - if the customer_id is available, accepted the record.
# - otherwise, rejected the record with a missing customer ID message.
    


# ==============================================================================
#
# ### Q10. API Response Handling
#
# An ingestion pipeline receives an HTTP response status code.
#
# Ask the user to enter the response status code.
#
# Apply these rules:
#
# | Status code | Pipeline action |
# |---|---|
# | 200 | Process API response |
# | 400 | Bad request — check request parameters |
# | 401 | Authentication failed |
# | 404 | Source endpoint not found |
# | 429 | Rate limit exceeded |
# | Any other | Handle unexpected API error |
#
# Write a program to implement this logic.
# ==============================================================================

print("\n" + "="*70)
print("Q10. API Response Handling")
print("="*70)
# %%
#user input
status_code =int(input("enter response status code:"))

#verify status code
if status_code == 200:
    print("process api response")

elif status_code == 400:
    print("bad request -- check request parameter")

elif status_code == 401:
    print("authentication failed")

elif status_code == 404:
    print("source endpoint not found")
    
elif status_code == 429:
    print("rate limit exceeded")
    
else:
    print("handle unexpected API error")
    
    
    
# logic / my approach:
# - used input() to accept the HTTP response status code.
# - converted the input into an integer.
# - used if, elif, and else conditions to check the status code.
# - displayed the corresponding pipeline action for each status code.
# - handled unexpected status codes using else.

# ==============================================================================
# ### Q11. Data Quality Check
#
# A pipeline receives a transaction record:
#
# ```python
# transaction = {
#     "transaction_id": 101,
#     "amount": -500,
#     "status": "SUCCESS"
# }
#
#
# A valid transaction must satisfy both conditions:
# - Amount must be greater than zero.
# - Status must be SUCCESS.
# Write a program to validate the transaction.
#
# Print whether it is valid or invalid.
# ==============================================================================

print("\n" + "="*70)
print("Q11. Data Quality Check")
print("="*70)
# %%
#given input
transaction = {
    "transaction_id": 101,
    "amount": -500,
    "status": "SUCESS"
}

if transaction["amount"]  > 0 and transaction["status"] == "SUCESS":
    print("valid transaction")

else:
    print("invalid transaction")


# logic / my approach:
# - created a dictionary to store transaction details.
# - used an if condition with and operator to check both conditions.
# - checked whether the amount is greater than zero.
# - checked whether the status is SUCCESS.
# - printed valid or invalid transaction based on the conditions.

# ==============================================================================
# ### Q12. Pipeline Execution Mode
#
# A data pipeline supports three execution modes:
#
# - FULL: Load all historical records.
# - INCREMENTAL: Load new records.
# - BACKFILL: Reload historical data for a specified period.
#
# Accept the execution mode from the user and print the corresponding pipeline action.
#
# If the user enters an unsupported mode, print Invalid execution mode.
# ==============================================================================

print("\n" + "="*70)
print("Q12. Pipeline Execution Mode")
print("="*70)
# %%
execution_mode = input(" to accept enter execution mode:")
if execution_mode == "FULL":
    print("load all historical records")
elif execution_mode == "INCREMENTAL":
    print(" load new records")
elif execution_mode == "BACKFILL":
    print("reload historical data for a specified period.")
else :
    print("invalid execution mode")
    
    
# logic / my approach:
# - used input() to accept the execution mode.
# - used if, elif, and else conditions to check the entered mode.
# - displayed the corresponding pipeline action for FULL, INCREMENTAL, and BACKFILL.
# - used else to handle unsupported execution modes.

# ==============================================================================
# ### Q13. Data Quality Scoring
#
# A data quality monitoring process generates a quality score between 0 and 100.
#
# Apply these rules:
#
# | Quality score | Classification |
# |---|---|
# | 90–100 | Excellent |
# | 75–89 | Good |
# | 50–74 | Needs improvement |
# | Below 50 | Critical — investigate pipeline |
#
# Accept the score from the user and classify the result.
#
# Also reject scores outside the range of 0–100.
# ==============================================================================

print("\n" + "="*70)
print("Q13. Data Quality Scoring")
print("="*70)
# %%
#user input:
score = int(input("enter your score to accept:"))

#quality of score and classifications
if score > 100 or score < 0:
    print("outside the range: rejected")
elif score >= 90:
    print("excellent")
elif score >= 75:
    print("good")
elif score >= 50:
    print("needs improvement")
else:
    print("critical --- investigate pipeline")
    
    
# logic / my approach:
# - used input() to accept the quality score.
# - converted the input into an integer.
# - checked whether the score is outside the range of 0 to 100.
# - used if, elif, and else conditions to classify the score.
# - displayed the appropriate quality classification.


# ==============================================================================
# ## Section D – Loops and Record Processing
#
# ### Q14. Batch Record Processing
#
# A pipeline receives the following list of customer IDs:
#
# ```python
# customer_ids = [101, 102, 103, 104, 105]
#
#
# Use a loop to process each customer ID.
#
# For every ID, print:
# Processing customer: 101
# Processing customer: 102
# - - -
# ==============================================================================

print("\n" + "="*70)
print("Q14. Batch Record Processing")
print("="*70)
# %%
# given input 
customer_ids = [101, 102, 103, 104, 105]

for  customer_id in customer_ids:
    print("processing customer:", customer_id)


# logic / my approach:
# - created a list containing customer IDs.
# - used a for loop to iterate through each customer ID.
# - printed a processing message for every customer.

# ==============================================================================
# ### Q15. Invalid Transaction Detection
#
# A pipeline receives the following transaction amounts:
#
# ```python
# amounts = [500, 1200, -100, 800, -50, 2000]
#
#
# Use a loop to identify negative transaction amounts.
#
# Print all negative amounts and count the number of invalid transactions.
# ==============================================================================

print("\n" + "="*70)
print("Q15. Invalid Transaction Detection")
print("="*70)
# %%
transaction_amounts = [500, 1200, -100, 800, -50, 2000]

count = 0
for amount in transaction_amounts:
    if amount < 0:
        print(amount)
        count = count + 1
print("invalid transactions:", count)



# logic / my approach:
# - created a list containing transaction amounts.
# - initialized a counter to track invalid records.
# - used a for loop to check each transaction amount.
# - used an if condition to identify negative amounts.
# - printed negative amounts and increased the counter.
# - displayed the total number of invalid transactions.

# ==============================================================================
#
# ### Q16. API Retry Simulation
#
# An API ingestion process can fail temporarily.
#
# You are given:
#
# ```python
# attempts = 0
# max_retries = 3
# ```
#
# Use a while loop to simulate API attempts.
#
# For this exercise:
# - Increment the attempt counter on every attempt.
# - Print the attempt number.
# - Stop when three attempts have been completed.
# - Print Maximum retries reached after the third attempt.
# ==============================================================================

print("\n" + "="*70)
print("Q16. API Retry Simulation")
print("="*70)
# %%
attempts = 0
max_retries = 3

while attempts < max_retries:
    attempts = attempts + 1
    print("attempt:", attempts)

print("maximum retries reached")


# logic / my approach:
# - initialized attempts to 0 and set maximum retries to 3.
# - used a while loop to repeat attempts until the limit is reached.
# - incremented the attempt counter after each attempt.
# - printed each attempt number.
# - displayed the maximum retries message after three attempts.

# ==============================================================================
# ### Q17. Daily Ingestion Summary
#
# A pipeline processes the following records:
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
# Expected summary:
#
# ```text
# Total records: 5
# Successful records: 3
# Failed records: 2
# ```
# ==============================================================================

print("\n" + "="*70)
print("Q17. Daily Ingestion Summary")
print("="*70)
# %%
records = [
    {"id": 1, "status": "SUCCESS"},
    {"id": 2, "status": "FAILED"},
    {"id": 3, "status": "SUCCESS"},
    {"id": 4, "status": "SUCCESS"},
    {"id": 5, "status": "FAILED"}
]

success = 0
failed = 0

for record in records:
    if record["status"] == "SUCCESS":
        success = success + 1
    elif record["status"] == "FAILED":
        failed = failed + 1
        
print("total records:", len(records))
print("successful records:", success)
print("failed records:", failed)



# logic / my approach:
# - created a list of records containing id and status.
# - initialized counters for successful and failed records.
# - used a for loop to iterate through each record.
# - used if and elif conditions to check the record status.
# - increased the respective counters.
# - used len() to calculate the total number of records.
# - printed the final ingestion summary.

# ==============================================================================
# ## Section E – Combined Data Engineering Scenarios
#
# These questions require students to combine multiple Python concepts. They should not approach them as isolated syntax exercises.
#
# ### Q18. Customer Data Ingestion Validator
#
# A source API sends customer records to your ingestion pipeline.
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
# Expected result:
#
# ```text
# Valid records: 2
# Invalid records: 3
# ```
# ==============================================================================

print("\n" + "="*70)
print("Q18. Customer Data Ingestion Validator")
print("="*70)
# %%
customers = [
    {"id": 101, "name": "Rahul", "age": 25},
    {"id": None, "name": "Priya", "age": 30},
    {"id": 103, "name": "Amit", "age": -5},
    {"id": 104, "name": "Neha", "age": 28},
    {"id": None, "name": "John", "age": 22}
]

valid = []
invalid = []

for customer in customers:
    if customer["id"] is not None and customer["age"] > 0:
        valid.append(customer)
    else:
        invalid.append(customer)

print("valid records:", valid)
print("invalid records:", invalid)
print("total valid records:", len(valid))
print("total invalid records:", len(invalid))


# logic / my approach:
# - created a list of customer records.
# - created separate lists to store valid and invalid records.
# - used a for loop to check each customer.
# - used and operator to check whether customer id is available and age is greater than zero.
# - used append() to store records in the respective lists.
# - used len() to count valid and invalid records.

# ==============================================================================
# ### Q19. Data Pipeline Monitoring
#
# Your team monitors a batch ingestion pipeline.
#
# The pipeline receives these metrics:
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
#
# | Processing percentage | Status |
# |---|---|
# | 95 or above | Healthy |
# | 80–94.99 | Warning |
# | Below 80 | Critical |
#
# 4. Print a pipeline monitoring report.
# ==============================================================================

print("\n" + "="*70)
print("Q19. Data Pipeline Monitoring")
print("="*70)
# %%
total_records = 10000
processed_records = 8500
failed_records = 1500

processing_percentage = (processed_records / total_records) * 100
failure_percentage = (failed_records / total_records) * 100

if processing_percentage >= 95:
    status = "Healthy"
elif processing_percentage >= 80:
    status = "Warning"
else:
    status = "critical"

print("processing percentage:", processing_percentage)
print("failure percentage:", failure_percentage)
print("pipeline status:", status)



# logic / my approach:
# - assigned values for total, processed, and failed records.
# - calculated processing and failure percentages using division and multiplication.
# - used if, elif, and else conditions to classify pipeline execution.
# - stored the classification in the status variable.
# - printed the percentages and final pipeline status.

# ==============================================================================
# ### Q20. Mini Ingestion Pipeline
#
# **Capstone question:** You are building a simple Python-based ingestion process for an e-commerce platform.
#
# The source provides the following records:
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
# Build a program that performs the following operations:
#
# **Stage 1 — Read source records**
#
# Iterate through every order.
#
# **Stage 2 — Validate records**
#
# An order is valid only if:
# - order_id is available.
# - amount is greater than zero.
# - status is SUCCESS.
#
# **Stage 3 — Process valid records**
#
# - Collect valid orders in a separate list.
# - Calculate the total revenue from valid orders.
# - Count the number of valid orders.
#
# **Stage 4 — Handle invalid records**
#
# - Collect invalid orders separately.
# - Count the number of rejected orders.
#
# **Stage 5 — Generate ingestion summary**
#
# Print:
#
# ```text
# ========== INGESTION REPORT ==========
# Total records received: 5
# Valid records: 3
# Rejected records: 2
# Total revenue: 2800
# ======================================
# ```
# ==============================================================================

print("\n" + "="*70)
print("Q20. Mini Ingestion Pipeline")
print("="*70)
# %%
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
valid_count = 0
rejected_count = 0

for order in orders:
    if order["order_id"] is not None and order["amount"] > 0 and order["status"] == "SUCCESS":
        valid_orders.append(order)
        total_revenue = total_revenue + order["amount"]
        valid_count = valid_count + 1
    else:
        invalid_orders.append(order)
        rejected_count = rejected_count + 1

print("====== INGESTION REPORT ==========")
print("total records received:", len(orders))
print("valid records:", valid_count)
print("rejected records:", rejected_count)
print("total revenue:", total_revenue)
print("======================================")


# logic / my approach:
# - created a list of e-commerce order records.
# - created separate lists for valid and invalid orders.
# - initialized variables to calculate total revenue and count records.
# - used a for loop to check each order.
# - used and operator to validate order id, amount, and status.
# - used append() to store valid and invalid orders separately.
# - calculated total revenue and counted valid and rejected orders.
# - printed the final ingestion report.

