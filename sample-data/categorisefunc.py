"""Associated with original simple tests."""
def categorise(fname):
    """Categorise documents for training."""
    if "cryptid" in fname:
        category = "crypto"
    else:
        category = "dino"
    return category
