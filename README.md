# SDNeqCHECK
SDN (Software-Defined Networking) Equivalence Checker

aSTEAM Project https://asteam.korea.ac.kr

## Introduction

**SDNeqCHECK** is a program for checking the equivalence of two SDN infrastructures based on their forwarding behaviors.

This takes the resulting forwarding rules for each SDN switch and a (ordered) topology of the SDN infrastructures. The program produces the equivalence of SDNs as True / False.

## Requirements and Dependencies
- Python 3.6 or newer, Numpy 1.13 or newer
- Z3 4.6.0 or newer (Z3py must be available for corresponding system architecture, e.g., 32bit/64bit)

## Instructions
1. Each switch is represented as a function (Edit the rules in the function)
2. Composite the (topologically ordered) order of the switches
3. **Run** the program ```python3 sdn_equiv-pub.py```

## Reference of installing Z3
https://github.com/Z3Prover/z3
