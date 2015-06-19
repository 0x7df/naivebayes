"""Goes with test09."""
def categorise(fname):
    """Categorise documents for training."""
    for category in ["Linear_algebra", "Numerical_integration",
                     "Radiation_transport", "Reactor_physics"]:
        if category in fname:
            return category
