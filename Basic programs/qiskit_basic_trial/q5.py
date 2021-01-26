from qiskit import QuantumRegister, QuantumCircuit, ClassicalRegister, Aer, execute

n=2
q=QuantumRegister(n)
c=ClassicalRegister(n)

ckt=QuantumCircuit(q,c)

ckt.cx(q[0],q[1])
ckt.cx(q[1],q[0])
ckt.cx(q[0],q[1])

backend=Aer.get_backend('statevector_simulator')
res=execute(ckt,backend).result()
before_coll=res.get_statevector(ckt)

print('before collapse	',before_coll)
