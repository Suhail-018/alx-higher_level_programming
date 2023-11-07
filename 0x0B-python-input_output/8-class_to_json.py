def class_to_json(obj):
    """
    Returns a dictiion of a class instance for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the class instance.
    """
    # Initialize an empty dictionary to store the attributes
    json_dict = {}
