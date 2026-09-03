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
## Order Items

| Column | Description |
|---|---|
| order_id | Identifier of the order |
| order_item_id | Sequential item number within an order |
| product_id | Identifier of the purchased product |
| seller_id | Identifier of the seller |
| shipping_limit_date | Deadline for shipping the item |
| price | Price of the item |
| freight_value | Freight/shipping cost |

## Payments

| Column | Description |
|---|---|
| order_id | Identifier of the order |
| payment_sequential | Sequence number of the payment |
| payment_type | Payment method |
| payment_installments | Number of installments |
| payment_value | Payment amount |

## Reviews

| Column | Description |
|---|---|
| review_id | Identifier of the review |
| order_id | Identifier of the reviewed order |
| review_score | Customer review score |
| review_comment_title | Review title |
| review_comment_message | Review message |
| review_creation_date | Date the review was created |
| review_answer_timestamp | Timestamp of the review answer |