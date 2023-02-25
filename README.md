# DynamoDB-Wrapper
DynamoDB Wrapper in Python

How to Use it

dynamodb_wrapper = DynamoDBWrapper('my-table')

# Query the table for items with a specific partition key value
query_params = QueryParams(
    key_condition_expression='pk = :pk',
    expression_attribute_values={':pk': 'my-partition-key-value'}
)
items = dynamodb_wrapper.query(query_params)

# Scan the table for all items with a specific attribute value
scan_params = ScanParams(
    filter_expression='attribute_name = :attribute_value',
    expression_attribute_values={':attribute_value': 'my-attribute-value'}
)
items = dynamodb_wrapper.scan(scan_params)
