"""Utils module."""

import random


def random_n_digits(n):
    """Generate a random n digits number."""
    # Disable standard pseudo random usage warning
    return f"{random.randrange(1, 10**n):0{n}}"  # noqa
