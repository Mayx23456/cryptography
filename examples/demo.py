from src.bb84 import BB84Protocol
import numpy as np

def main():
    # Initialize the BB84 protocol with 1000 qubits
    print("Initializing BB84 protocol with 1000 qubits...")
    bb84 = BB84Protocol(num_qubits=1000, noise_level=0.01)
    
    # Generate the key
    print("\nGenerating quantum key...")
    final_key = bb84.generate_key()
    
    # Check results
    error_rate = bb84.check_error_rate()
    is_secure = bb84.verify_security()
    
    print(f"\nResults:")
    print(f"Error Rate: {error_rate:.3f}")
    print(f"Protocol Security: {'Secure' if is_secure else 'Not Secure'}")
    
    if final_key is not None:
        print(f"Final Key Length: {len(final_key)} bits")
        print(f"Sample of Final Key: {final_key[:20]}...")
    else:
        print("Key generation failed due to high error rate")

if __name__ == "__main__":
    main()
