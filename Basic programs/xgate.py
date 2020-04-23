import qiskit as q
import matplotlib
qr=q.QuantumRegister(2)
cr=q.ClassicalRegister(2)
#circuit=q.QuantumCircuit(2,2)# 2 quibits,2 classical bits
circuit=q.QuantumCircuit(2,2)
circuit.h(0)
#####print(circuit)
####circuit.x(0)
####circuit.cx(0,1)
####circuit.measure([0,1],[0,1])#value for qubit should be in classical bit 0 s
#currently
print(circuit)
circuit.draw(output = 'mpl',filename='ckt.png')
