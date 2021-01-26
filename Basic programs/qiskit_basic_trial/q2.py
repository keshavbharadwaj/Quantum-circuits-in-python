
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer, execute
from qiskit.quantum_info import Pauli



q0 = QuantumRegister(2, 'q0')
c0 = ClassicalRegister(2, 'c0')
q1 = QuantumRegister(2, 'q1')
c1 = ClassicalRegister(2, 'c1')

circ = QuantumCircuit(q0, q1)
circ.x(q0[1])
circ.x(q1[0])
print(circ)
