import boto3

class DynamoDBWrapper:
    def __init__(self, table_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def query(self, query_params):
        """
        Query the DynamoDB table with the given query parameters.

        :param query_params: An object representing the query parameters.
        :return: A list of items matching the query.
        """
        key_condition_expression = query_params.key_condition_expression
        expression_attribute_values = query_params.expression_attribute_values
        filter_expression = query_params.filter_expression

        kwargs = {
            'KeyConditionExpression': key_condition_expression,
        }
        if expression_attribute_values is not None:
            kwargs['ExpressionAttributeValues'] = expression_attribute_values
        if filter_expression is not None:
            kwargs['FilterExpression'] = filter_expression

        response = self.table.query(**kwargs)
        return response['Items']

    def scan(self, scan_params):
        """
        Scan the DynamoDB table with the given scan parameters.

        :param scan_params: An object representing the scan parameters.
        :return: A list of items matching the scan.
        """
        filter_expression = scan_params.filter_expression
        expression_attribute_values = scan_params.expression_attribute_values

        kwargs = {}
        if filter_expression is not None:
            kwargs['FilterExpression'] = filter_expression
        if expression_attribute_values is not None:
            kwargs['ExpressionAttributeValues'] = expression_attribute_values

        response = self.table.scan(**kwargs)
        items = response['Items']
        while response.get('LastEvaluatedKey'):
            response = self.table.scan(ExclusiveStartKey=response['LastEvaluatedKey'], **kwargs)
            items.extend(response['Items'])
        return items

class QueryParams:
    def __init__(self, key_condition_expression, expression_attribute_values=None, filter_expression=None):
        self.key_condition_expression = key_condition_expression
        self.expression_attribute_values = expression_attribute_values
        self.filter_expression = filter_expression

class ScanParams:
    def __init__(self, filter_expression=None, expression_attribute_values=None):
        self.filter_expression = filter_expression
        self.expression_attribute_values = expression_attribute_values
