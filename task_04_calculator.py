def calculate_operations(a: float, b: float) -> dict:
    try:
        result = dict()
        if isinstance(a, (int, float)) and isinstance(a, (int, float)):
            result['sum'] = a + b
            result['difference'] = a - b
            result['product'] = a * b
            result['quotient'] = a / b
            return result
        else:
            raise ValueError("Error: Both inputs must be numbers (int or float) ->")
    except Exception as e:
        print(e, end=" ")
        return {}
