"""
BB84 Quantum Key Distribution Protocol Implementation
"""

from .bb84 import BB84Protocol
from .quantum_channel import QuantumChannel
from .utils import calculate_error_rate, privacy_amplification, verify_key_quality

__version__ = "1.0.0"
