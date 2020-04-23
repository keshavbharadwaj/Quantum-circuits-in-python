from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute

n=3

q=QuantumRegister(n)
c=ClassicalRegister(n)

ckt=QuantumCircuit(q,c)
ckt.x(q[1])
ckt.h(q[0])
ckt.h(q[1])
#ckt.cswap(q[0],q[1],q[2])
ckt.cx(q[0],q[1])


backend=Aer.get_backend('statevector_simulator')
initial=execute(ckt,backend).result()
before_coll=initial.get_statevector(ckt)


ckt.measure(q,c)
backend=Aer.get_backend('qasm_simulator')
mes=execute(ckt,backend).result()



backend=Aer.get_backend('statevector_simulator')
final=execute(ckt,backend).result()
after_coll=final.get_statevector(ckt)



print(initial.get_counts(ckt))
print('before collapse	',before_coll)

print(mes.get_counts(ckt))

print('after collapse	',after_coll)
print(final.get_counts(ckt))

print(ckt)