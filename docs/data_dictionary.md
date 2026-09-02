# Data Dictionary

## Customers

| Column | Description |
|---|---|
| customer_id | Unique identifier for an order customer |
| customer_unique_id | Identifier representing the unique customer |
| customer_zip_code_prefix | Customer ZIP code prefix |
| customer_city | Customer city |
| customer_state | Customer state |

## Orders

| Column | Description |
|---|---|
| order_id | Unique order identifier |
| customer_id | Customer associated with the order |
| order_status | Current order status |
| order_purchase_timestamp | Timestamp when the order was placed |
| order_delivered_customer_date | Actual customer delivery date |
| order_estimated_delivery_date | Estimated delivery date |