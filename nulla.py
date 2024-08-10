def unwrap_function(optional_value, default=None):
    """Unwraps an optional value, returning a default if None."""
    if optional_value is None:
        return default
    return optional_value

# Example usage:
value = None
default_value = 42
print(unwrap_function(value, default_value))  # Output: 42
