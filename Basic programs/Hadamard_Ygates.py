import qiskit as q
from qiskit import Aer,execute
from qiskit import IBMQ
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
qr=q.QuantumRegister(2)
cr=q.ClassicalRegister(2)
circuit=q.QuantumCircuit(qr,cr)
circuit.h(qr[0])
circuit.h(qr[1])
circuit.y(qr[1])
circuit.measure([qr[0],qr[1]],[cr[0],cr[1]])
simulator=Aer.get_backend('qasm_simulator')
Result=execute(circuit,backend=simulator).result()
plot_histogram(Result.get_counts(circuit)).show()
print(circuit)
