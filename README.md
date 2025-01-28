# BB84 Quantum Key Distribution Implementation

This project implements the BB84 quantum key distribution protocol, which is the first quantum cryptography protocol developed by Charles Bennett and Gilles Brassard in 1984.

## Overview

BB84 is a quantum key distribution scheme that allows two parties (traditionally called Alice and Bob) to create a shared random secret key that can be used for encrypting messages. The protocol's security is based on the principles of quantum mechanics, specifically:

1. The impossibility of perfectly distinguishing between non-orthogonal quantum states
2. The no-cloning theorem
3. The observer effect in quantum mechanics

## Project Structure

```
cryptography/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── quantum_channel.py
│   ├── bb84.py
│   └── utils.py
└── examples/
    └── demo.py
```

## Dependencies

The project requires the following Python packages:
- numpy: For numerical computations and random number generation
- qiskit: For quantum circuit simulation
- matplotlib: For visualization (optional)

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Implementation Details

The implementation consists of several key components:

1. **Quantum Channel Simulation** (`quantum_channel.py`):
   - Simulates the quantum communication channel
   - Handles quantum state preparation and measurement
   - Implements noise and eavesdropping detection

2. **BB84 Protocol** (`bb84.py`):
   - Implements the core BB84 protocol
   - Handles basis selection and bit encoding
   - Performs key sifting and error detection

3. **Utilities** (`utils.py`):
   - Helper functions for quantum state manipulation
   - Error rate calculation
   - Security parameter estimation

## Protocol Steps

1. **Quantum State Preparation (Alice)**
   - Generate random bits
   - Randomly choose between rectilinear (+) and diagonal (×) bases
   - Encode bits into quantum states

2. **Quantum Transmission**
   - Send quantum states through the quantum channel
   - Handle potential eavesdropping and noise

3. **Measurement (Bob)**
   - Randomly choose measurement bases
   - Measure received quantum states

4. **Classical Communication**
   - Exchange basis information
   - Perform key sifting
   - Error rate estimation
   - Privacy amplification

5. **Final Key Generation**
   - Generate the final secure key
   - Verify key security parameters

## Usage Example

```python
from src.bb84 import BB84Protocol

# Initialize the protocol
bb84 = BB84Protocol(num_qubits=1000)

# Generate and exchange quantum states
shared_key = bb84.generate_key()

# Check error rate and security
error_rate = bb84.check_error_rate()
is_secure = bb84.verify_security()
```

## Security Considerations

The implementation includes:
- Eavesdropping detection
- Error rate estimation
- Privacy amplification
- Security parameter verification

## References

1. Bennett, C. H., & Brassard, G. (1984). Quantum cryptography: Public key distribution and coin tossing.
2. Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information.
