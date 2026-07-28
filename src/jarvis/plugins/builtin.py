"""
Built-in JARVIS tools.
"""



def calculator(
    expression: str,
) -> str:
    """
    Simple calculator.
    """


    try:

        result = eval(
            expression
        )


        return str(result)


    except Exception:

        return "Invalid expression"