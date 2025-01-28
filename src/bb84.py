import numpy as np
from .quantum_channel import QuantumChannel
from .utils import calculate_error_rate, privacy_amplification

class BB84Protocol:
    def __init__(self, num_qubits=1000, noise_level=0.0):
        """
        Initialize the BB84 protocol.
        
        Args:
            num_qubits (int): Number of qubits to use in the protocol
            noise_level (float): Amount of noise in the quantum channel
        """
        self.num_qubits = num_qubits
        self.quantum_channel = QuantumChannel(noise_level)
        self.alice_bits = None
        self.alice_bases = None
        self.bob_bases = None
        self.bob_measurements = None
        self.shared_key = None
        self.error_rate = None
        
    def _generate_random_bits(self, size):
        """Generate random classical bits."""
        return np.random.randint(2, size=size)
    
    def _generate_random_bases(self, size):
        """Generate random bases ('Z' or 'X')."""
        return np.random.choice(['Z', 'X'], size=size)
    
    def _sift_key(self):
        """
        Perform key sifting by keeping only the bits where Alice and Bob
        used the same basis for encoding and measurement.
        """
        matching_bases = self.alice_bases == self.bob_bases
        self.shared_key = self.alice_bits[matching_bases]
        self.bob_measurements = self.bob_measurements[matching_bases]
        
    def generate_key(self):
        """
        Execute the complete BB84 protocol.
        
        Returns:
            tuple: (shared_key, error_rate)
        """
        # Step 1: Alice generates random bits and bases
        self.alice_bits = self._generate_random_bits(self.num_qubits)
        self.alice_bases = self._generate_random_bases(self.num_qubits)
        
        # Step 2: Bob generates random bases for measurement
        self.bob_bases = self._generate_random_bases(self.num_qubits)
        
        # Step 3: Quantum transmission
        self.bob_measurements = np.array(
            self.quantum_channel.transmit(self.alice_bits, self.alice_bases)
        )
        
        # Step 4: Key sifting
        self._sift_key()
        
        # Step 5: Error estimation
        self.error_rate = calculate_error_rate(
            self.shared_key, 
            self.bob_measurements
        )
        
        # Step 6: Privacy amplification if error rate is acceptable
        if self.error_rate < 0.11:  # Theoretical threshold for BB84
            final_key = privacy_amplification(self.shared_key)
            return final_key
        else:
            return None
    
    def check_error_rate(self):
        """Return the calculated error rate."""
        return self.error_rate
    
    def verify_security(self):
        """
        Verify if the protocol execution was secure.
        
        Returns:
            bool: True if the error rate is below the security threshold
        """
        if self.error_rate is None:
            return False
        return self.error_rate < 0.11  # Theoretical threshold for BB84
