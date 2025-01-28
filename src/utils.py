import numpy as np
from typing import List, Union

def calculate_error_rate(key1: np.ndarray, key2: np.ndarray) -> float:
    """
    Calculate the error rate between two bit strings.
    
    Args:
        key1: First bit string
        key2: Second bit string
        
    Returns:
        float: Error rate between 0 and 1
    """
    if len(key1) != len(key2):
        raise ValueError("Keys must have the same length")
    
    differences = np.sum(key1 != key2)
    return differences / len(key1)

def privacy_amplification(key: np.ndarray) -> np.ndarray:
    """
    Perform privacy amplification on the shared key to reduce
    potential information leakage to an eavesdropper.
    
    Args:
        key: Input key to be amplified
        
    Returns:
        np.ndarray: Amplified key
    """
    # Use a simple universal hash function
    # In practice, more sophisticated methods would be used
    key_len = len(key)
    reduced_len = key_len // 2  # Reduce key length by half
    
    # Generate random matrix for universal hashing
    hash_matrix = np.random.randint(2, size=(reduced_len, key_len))
    
    # Perform matrix multiplication modulo 2
    amplified_key = np.dot(hash_matrix, key) % 2
    
    return amplified_key

def verify_key_quality(error_rate: float, key_length: int, security_parameter: float = 0.01) -> bool:
    """
    Verify if the generated key meets security requirements.
    
    Args:
        error_rate: Observed error rate
        key_length: Length of the generated key
        security_parameter: Desired security level (default: 0.01)
        
    Returns:
        bool: True if key meets security requirements
    """
    # Theoretical threshold for BB84
    max_error_rate = 0.11
    
    # Check if error rate is below threshold
    if error_rate >= max_error_rate:
        return False
    
    # Check if key length is sufficient for security parameter
    min_length = -np.log2(security_parameter) / (1 - 2 * error_rate)
    return key_length >= min_length
