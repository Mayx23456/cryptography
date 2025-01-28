from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import Aer
from qiskit.primitives import Sampler
import numpy as np

class QuantumChannel:
    def __init__(self, noise_level=0.0):
        """
        Initialize the quantum channel with optional noise.
        
        Args:
            noise_level (float): Amount of noise in the channel (0.0 to 1.0)
        """
        self.noise_level = noise_level
        self.simulator = Aer.get_backend('qasm_simulator')
    
    def prepare_state(self, bit: int, basis: str) -> QuantumCircuit:
        """
        Prepare a quantum state based on the input bit and basis.
        
        Args:
            bit (int): The classical bit to encode (0 or 1)
            basis (str): The basis to use ('Z' for rectilinear or 'X' for diagonal)
            
        Returns:
            QuantumCircuit: The prepared quantum circuit
        """
        qr = QuantumRegister(1)
        cr = ClassicalRegister(1)
        qc = QuantumCircuit(qr, cr)
        
        # Prepare state based on bit value
        if bit == 1:
            qc.x(qr[0])
            
        # Apply basis transformation if needed
        if basis == 'X':
            qc.h(qr[0])
            
        return qc
    
    def measure_state(self, circuit: QuantumCircuit, basis: str) -> int:
        """
        Measure a quantum state in the specified basis.
        
        Args:
            circuit (QuantumCircuit): The quantum circuit to measure
            basis (str): The basis to measure in ('Z' or 'X')
            
        Returns:
            int: The measurement result (0 or 1)
        """
        qr = circuit.qregs[0]
        cr = circuit.cregs[0]
        
        # Transform basis if needed
        if basis == 'X':
            circuit.h(qr[0])
            
        # Add noise if specified
        if self.noise_level > 0:
            if np.random.random() < self.noise_level:
                circuit.x(qr[0])
                
        # Measure
        circuit.measure(qr, cr)
        
        # Execute using Sampler primitive
        sampler = Sampler()
        job = sampler.run(circuit, shots=1)
        result = job.result()
        counts = result.quasi_dists[0]
        
        # Get the most frequent measurement outcome
        measured_bit = max(counts.items(), key=lambda x: x[1])[0]
        return measured_bit
    
    def transmit(self, sender_bits, sender_bases):
        """
        Transmit quantum states through the channel.
        
        Args:
            sender_bits (list): List of classical bits to encode
            sender_bases (list): List of bases to use for encoding
            
        Returns:
            list: List of received bits after measurement
        """
        received_bits = []
        
        for bit, basis in zip(sender_bits, sender_bases):
            # Prepare the quantum state
            circuit = self.prepare_state(bit, basis)
            
            # Simulate transmission and measurement
            received_bit = self.measure_state(circuit, basis)
            received_bits.append(received_bit)
            
        return received_bits
