<div align="center">

# Parth Danve

**Quantum software engineer building algorithms, tooling, and the infrastructure that runs them.**

![Qiskit Advocate](https://img.shields.io/badge/Qiskit_Advocate-6929C4?style=flat-square&logo=qiskit&logoColor=white)
![IBM](https://img.shields.io/badge/Quantum_SWE_Intern_'26-IBM-054ADA?style=flat-square&logo=ibm&logoColor=white)
![UConn](https://img.shields.io/badge/CS_Honors-UConn_'27-E4002B?style=flat-square)

</div>

- ⚛️ Build **quantum software tooling**: reusable functions, serverless workflows, and templates that run on real hardware
- 🔬 Research **hybrid quantum algorithms** for optimization and simulation, spanning QAOA, ADMM, quantum annealing, and N-body methods
- 🧠 Apply **quantum-inspired methods to classical ML**: physics-informed networks and evolutionary optimizers that drop into PyTorch
- 🛠️ Contribute **upstream to Qiskit** and the IBM Quantum Platform documentation
- 🏆 Compete in **quantum hackathons**, with 3 podium finishes at Yale, MIT, and UConn in 2025

---

## Shipped upstream

<details open>
<summary><b>⚛️ AQC + Trotter Hamiltonian dynamics template</b> &nbsp;·&nbsp; <code>+3,673</code> lines &nbsp;·&nbsp; <b>100×</b> less peak memory</summary>
<br>

Reusable 1-D Hamiltonian dynamics simulation that runs across local, simulated, and IBM Quantum hardware backends, combining Trotterization with Approximate Quantum Compilation.

**`+3,673` lines across 22 files** · **100×** lower peak memory at 50 qubits (10× at 30 to 40) · **≥0.999** AQC fidelity against IBM's simulation benchmark

→ [qiskit-community/qiskit-function-templates#41](https://github.com/qiskit-community/qiskit-function-templates/pull/41)

</details>

<details>
<summary><b>📖 Neutron scattering tutorial + AQC template</b> &nbsp;·&nbsp; <code>+1,641</code> lines &nbsp;·&nbsp; <sup>in review</sup></summary>
<br>

Tutorial function and AQC function template written for `quantum.cloud.ibm.com/docs`, the IBM Quantum Platform learning catalog.

**`+1,641` lines across 14 files** · co-authored, **13 of 24 commits** · currently in review

→ [Qiskit/documentation#5510](https://github.com/Qiskit/documentation/pull/5510)

</details>

## Research

<details>
<summary><b>🛰️ Satellite orbital propagation</b> &nbsp;·&nbsp; <b>200×</b> faster than Orekit</summary>
<br>

Quantum-assisted physics-informed neural networks (QA-PINN) for satellite orbit propagation, benchmarked against Orekit, a leading astrodynamics package, at comparable accuracy.

<sub>BosonQ Psi</sub>

</details>

<details>
<summary><b>📉 Quantum-inspired optimization</b> &nbsp;·&nbsp; sparse recovery + PyTorch optimizers</summary>
<br>

Applied quantum-inspired evolutionary optimization (QIEO) to non-convex sparse recovery, reconstructing high-dimensional signals from limited measurements. Built PyTorch-compatible optimizer wrappers so QIEO drops into standard training loops the way ADAM does.

<sub>BosonQ Psi</sub>

</details>

<details>
<summary><b>🌌 Hybrid quantum algorithms</b> &nbsp;·&nbsp; <b>90%</b> runtime speedup</summary>
<br>

Hybrid quantum algorithms for close-neighbor search in N-body simulations, asymptotically faster than current heuristics, optimized to a **90%** runtime speedup over the original implementation. Separately, combined ADMM with QAOA to solve mixed binary optimization problems, benchmarked in Qiskit.

<sub>UConn School of Computing · mentors: Dr. Sanguthevar Rajasekaran, Dr. Bing Wang</sub>

</details>

## Hackathons

<details>
<summary><b>🥇 Yale Quantum 2025</b> &nbsp;·&nbsp; 1st, BlueQubit Challenge &nbsp;·&nbsp; <b>500%</b> speedup</summary>
<br>

Hunted hidden peaked bitstrings in circuits too entangled and too deep for classical CPU/GPU simulators, and in some cases for quantum hardware. Tuned matrix product state bond dimensions across BlueQubit, Qiskit-Aer, and Quimb.

**500%** speedup on a 44-qubit circuit

→ [pdd23001/YQuantum2025-Last-Minute](https://github.com/pdd23001/YQuantum2025-Last-Minute)

</details>

<details>
<summary><b>🥇 HackUConn 2025</b> &nbsp;·&nbsp; 1st place overall</summary>
<br>

University finals scheduling as a constrained quadratic model on D-Wave's annealers, with simulated annealing via variational quantum algorithms in Qiskit. Fine-tuned GPT-2 to prototype AI-assisted academic advising.

→ [pdd23001/QuantumAdvisors](https://github.com/pdd23001/QuantumAdvisors)

</details>

<details>
<summary><b>🥉 MIT iQuHack 2025</b> &nbsp;·&nbsp; 3rd, D-Wave Challenge &nbsp;·&nbsp; <b>50%</b> better minimization</summary>
<br>

Hospital logistics, with patient rooms and supply closets whose flow varies over time, formulated as quadratic assignment problems in both constrained quadratic and non-linear form, then solved on D-Wave's hybrid annealers.

**50%** better minimization accuracy than SciPy's non-linear baselines

→ [Hackers-of-Tomorrow/5-idiots-MIT](https://github.com/Hackers-of-Tomorrow/5-idiots-MIT)

</details>

## Recent contributions

<sub>Updated daily by a GitHub Action.</sub>

<!-- RECENT:START -->
| Pull request | Repository | Merged |
| :-- | :-- | :-- |
| [Add AQC+Trotter Hamiltonian dynamics template](https://github.com/qiskit-community/qiskit-function-templates/pull/41) | `qiskit-community/qiskit-function-templates` | 2026-08-10 |
| [Update AQC Tensor Addon Version](https://github.com/Qiskit/qiskit-serverless/pull/2355) | `Qiskit/qiskit-serverless` | 2026-07-21 |
| [Update Cotengrust Dependency](https://github.com/Qiskit/qiskit-serverless/pull/2335) | `Qiskit/qiskit-serverless` | 2026-07-13 |
| [Add input validation for negative errors in SynthesizeRZRotations](https://github.com/Qiskit/qiskit/pull/16389) | `Qiskit/qiskit` | 2026-06-29 |
<!-- RECENT:END -->

## Toolkit

<table>
<tr>
<td><b>Quantum</b></td>
<td>
<img src="https://img.shields.io/badge/Qiskit-6929C4?style=flat-square&logo=qiskit&logoColor=white">
<img src="https://img.shields.io/badge/Qiskit_Serverless-6929C4?style=flat-square">
<img src="https://img.shields.io/badge/Qiskit_Aer-6929C4?style=flat-square">
<img src="https://img.shields.io/badge/Cirq-2C8EBB?style=flat-square">
<img src="https://img.shields.io/badge/D--Wave_Ocean-008CBA?style=flat-square">
<img src="https://img.shields.io/badge/Quimb-4B8BBE?style=flat-square">
</td>
</tr>
<tr>
<td><b>Languages</b></td>
<td>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white">
<img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black">
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white">
</td>
</tr>
<tr>
<td><b>ML</b></td>
<td>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white">
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white">
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white">
</td>
</tr>
<tr>
<td><b>Tools</b></td>
<td>
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white">
<img src="https://img.shields.io/badge/AWS_EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white">
</td>
</tr>
</table>

<div align="center">

[LinkedIn](https://linkedin.com/in/parthdanve39) · [parthdanve39@gmail.com](mailto:parthdanve39@gmail.com)

</div>
