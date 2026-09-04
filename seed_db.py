from backend.database import get_db_connection

connection = get_db_connection()
cursor = connection.cursor()

# Customer
cursor.execute("""
INSERT INTO customers (name, email, phone)
VALUES (%s, %s, %s)
""", ("Ravi", "ravi@recoverai.test", "9876543210"))

customer_id = cursor.lastrowid

# Failed transaction
cursor.execute("""
INSERT INTO transactions
(customer_id, amount, payment_method, status, failure_reason)
VALUES (%s, %s, %s, %s, %s)
""", (
    customer_id,
    500,
    "UPI",
    "FAILED",
    "Insufficient balance"
))

transaction_id = cursor.lastrowid

# AI decision
cursor.execute("""
INSERT INTO ai_decisions
(transaction_id, recoverable, priority, reason,
 recommended_action, expected_recovery)
VALUES (%s, %s, %s, %s, %s, %s)
""", (
    transaction_id,
    True,
    "HIGH",
    "Payment failed due to insufficient balance",
    "PAYMENT_LINK",
    500
))

connection.commit()

print("SUCCESS: Demo data created!")
print("Customer ID:", customer_id)
print("Transaction ID:", transaction_id)

cursor.close()
connection.close()