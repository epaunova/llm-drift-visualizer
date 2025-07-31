def is_hallucinated(response, source_doc):
    """Compares response to source_doc and returns True if hallucinated."""
    return response not in source_doc  # simplistic check
