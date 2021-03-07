from importlib import import_module


def import_class(class_path):
    """
    Quick and dirty wrapper around Python's `import_module` to dynamically import a class.

    Args:
        class_path: A python path to a class, such as `example.foobar.MyClass`

    Raises:
        ImportError: Invalid class path, or class not found.

    Returns:
        If path is valid, returns an instance of a Python class.
    """
    try:
        tokens = class_path.split('.')
        mod_path = tokens[:-1]
        if not mod_path:
            raise ImportError()
        mod = import_module('.'.join(mod_path))
        return getattr(mod, tokens[-1])
    except (ImportError, AttributeError):
        raise ImportError(class_path)
