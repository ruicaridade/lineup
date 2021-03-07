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


class Serializable:
    def to_dict(self, as_camel_case=False):
        """
        Rudimentary function to serialise a Python object to a dictionary. It's not a recursive function, thus won't
        work for deeply nested objects (i.e. non-primitive fields, nested dicts, etc). Also doesn't account for parent
        classes.

        Args:
            as_camel_case: If True, transforms snake_case keys to camelCase.

        Returns:
            The current object represented as a Python dictionary.
        """
        dict_repr = {}
        for k, v in self.__dict__.items():
            if k.startswith('__'):
                continue

            if as_camel_case:
                tokens = k.split('_')
                k = tokens[0] + ''.join([x.title() for x in tokens[1:]])

            dict_repr[k] = v
        return dict_repr
