from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# Create a Quantum Circuit acting on a quantum register of two qubits
circ = QuantumCircuit(2, 2)

# Add a H gate on qubit 0, putting this qubit in superposition.
circ.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, creating an entanglement between them.
circ.cx(0, 1)

# Map the quantum measurement to the classical bits
circ.measure([0,1], [0,1])

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator
job = execute(circ, simulator, shots=1000)

# Grab the results from the job
result = job.result()

# Get the counts (how many times each possible outcome was obtained)
counts = result.get_counts(circ)

# Plot a histogram of the results
plot_histogram(counts).show()


# Add this line to explicitly show the plot.
plt.show()
