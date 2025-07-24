# Intermolecular Loss Extension for MACE

This repository contains modifications to `mace/modules/loss.py` for incorporating **intermolecular force loss** during training of MACE models. 

---

## What's New?

Three key functions have been added/modified:

### `WeightedEnergyForceIntermolForceLoss`

- Computes a **total weighted loss** combining:
  - Force loss
  - Energy loss
  - Intermolecular force loss 
- Customizable weights: `w_forces : w_intermol_forces : w_energy`

---

### `compute_mol_forces`

- Computes **intermolecular forces** between molecular fragments.
- Requires a `mol.idx` file:
  - it contain the indexes of atom for the fragments 

---

### `mean_square_intermol_error`

- Calculates **mean squared error (MSE)** between predicted and reference intermolecular forces.
- Passed into `WeightedEnergyForceIntermolForceLoss`

---

