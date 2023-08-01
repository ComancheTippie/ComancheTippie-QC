from qiskit import BasicAer
from qiskit.utils import QuantumInstance
from qiskit.circuit import QuantumCircuit, ParameterVector
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit_machine_learning.algorithms import QSVC
from sklearn import datasets
from sklearn.model_selection import train_test_split


# Load Iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

# Create a 2-qubit quantum circuit
params = ParameterVector('theta', length=2)
qc = QuantumCircuit(2)
qc.h([0,1])
qc.rz(params[0], 0)
qc.rx(params[1], 1)
qc.cx(0, 1)

# Create quantum kernel
kernel = QuantumKernel(feature_map=qc, quantum_instance=QuantumInstance(BasicAer.get_backend('statevector_simulator')))

# Split into test and training datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train QSVC
qsvc = QSVC(quantum_kernel=kernel)
qsvc.fit(X_train, y_train)

# Test QSVC
score = qsvc.score(X_test, y_test)
print(f'Test Score: {score}')
