from qiskit.circuit.library.standard_gates import MCXGate


def xor_circuit(qc, num_qbitsetx, num_qbitsety):

    num_qbit_index = num_qbitsetx + num_qbitsety
    mcxg_xor = MCXGate(2, None, '00')
    qc.append(mcxg_xor, [num_qbit_index+2, num_qbit_index+3, num_qbit_index+4])
    qc.barrier()

    return qc
