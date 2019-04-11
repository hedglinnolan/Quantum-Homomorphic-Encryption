''' This is just a small demo to see if we can create bell states and access an actual QC like in the video.

For more info on the basics of qiskit, check out the jupyter notebooks on their github. https://github.com/Qiskit

I only imported the visulatization tools I thought were sufficient/cool, but there are plenty more.
'''

import qiskit as qk
from qiskit.tools.visualization import plot_histogram, plot_state_qsphere, plot_bloch_vector, plot_bloch_multivector, circuit_drawer
import Qconfig
import quantumFunctions as qf

#Create blank variables for the quantum register, classical register, and the resulting quantum circuit. Will change when we call createQC function
qr = 0
cr = 0
qc = 0

#Store values for number of qubits and the qubits being addressed 
gateDepth = 2
qubitI = 0
qubitJ = 1

#Creating a circuit to prepare the bell state. All functions can be found in quantumFunctions.py
qf.createQC(gateDepth)
qf.bellState(qubitI,qubitJ,qc,qr)

#Initialize blank circuits to perform measurments. Will change when we call basisMeasure and hadamardMeasure
measure_Z = 0
measure_X = 0

qf.basisMeasure(qr,cr)
qf.hadamardMeasure(qr,cr)

#Split the original circuit to perform Z measurment and X measurement
#Append circuits using the addition operator
test_Z = qc + measure_Z
test_X = qc + measure_X

#Draw the quantum circuit
qc.draw()

#Running the circuits on a quantum simulator with 1000 trials
job_1 = qk.execute([test_Z,test_X], backend = 'local_qasm_simulator',shots = 1000)
result_1 = job_1.result()

result_1.get_counts(test_Z)
result_1.get_counts(test_X)

#psi = result_1.get_statevector(test_Z) #Should return the equation for a bell state
#plot_state_qsphere(psi) #plotting it on the bloch sphere!

#Running the circuits on an actual IBM quantum computer (refer to quantumFunctions.py for name of backend)
job_2 = qk.execute([test_Z,test_X], backend = 'ibmqxf', shots = 1000)
result_2 = job_2.result()

result_2.get_counts(test_Z)
result_2.get_counts(test_X)

#Plot the results. There are a ton of different ways to plot using qiskit
legend = ['QASM Simulator','Melbourne QC (16 qubits)']
plot_histogram([result_1.get_counts(test_Z), result_2.get_counts(test_Z)], legend = legend, title='Entanglement Generation Fidelity (computational basis)')
plot_histogram([result_1.get_counts(test_X), result_2.get_counts(test_X)], legend=legend, title= 'Entanglement Generation Fidelity (Hadamard basis)')
