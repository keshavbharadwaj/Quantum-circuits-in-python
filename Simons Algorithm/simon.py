import qiskit as q
from qiskit.visualization import plot_histogram,plot_bloch_multivector
import matplotlib
import math
qasm_sim=q.Aer.get_backend("qasm_simulator")
statevec_sim=q.Aer.get_backend("statevector_simulator")
def oracle_function(c):#oracle function 
    n_qubits=int(c.num_qubits)
    n=int(n_qubits/2)
    for i in range(n):
        c.cx(i,[j for j in range(n,2*n)])
    return c

def hadamard(c):#This function is used to apply hadamard to n/2 qubiits
    n_qubits=int(circuit.num_qubits)
    print(n_qubits/2)
    for i in range(int(n_qubits/2)):
        c.h(i)
    return c

def sdotz(a, b):
    accum = 0
    for i in range(len(a)):
        accum += int(a[i]) * int(b[i])
    return (accum % 2)

n=2
circuit=q.QuantumCircuit(2*n)#quantumbits = 2*n =4
circuit=hadamard(circuit)
circuit.barrier()
circuit=oracle_function(circuit)
circuit.barrier()
circuit=hadamard(circuit)
print(circuit)
circuit.draw(output='mpl',filename='simonsckt')
circuit.measure_all()
results = q.execute(circuit, backend=qasm_sim).result().get_counts()
#print(results)
answer_plot = {}

for measresult in results.keys():
    measresult_input = measresult[n:]
    if measresult_input in answer_plot:
        answer_plot[measresult_input] += results[measresult]
    else:
        answer_plot[measresult_input] = results[measresult]
#print(answer_plot)
plot_histogram(answer_plot).show()
s="1"*n
print('s, z, s.z (mod 2)')
for z_rev in answer_plot:
    z = z_rev[::-1]
    print( '{}, {}, {}.{}={}'.format(s, z, s,z,sdotz(s,z)) )
