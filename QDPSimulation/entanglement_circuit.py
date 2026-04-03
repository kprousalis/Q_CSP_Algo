from qiskit import QuantumCircuit
from qiskit.circuit.library.standard_gates import XGate


def entanglement_circuit_dagger(NoQubits):
    qc = QuantumCircuit(NoQubits+1)
    qc.name = "   Entanglement   "

    qc.h(0)
    for q in range(NoQubits):
        qc.cx(q, q+1)
    return qc


def entanglement_circuit(qc, num_qbitsetx, num_qbitsety):

    num_qbit_index = num_qbitsetx + num_qbitsety

    qc.cx(num_qbit_index, num_qbit_index + 2)
    qc.cx(num_qbit_index+1, num_qbit_index + 3)
    qc.barrier()

    return qc
