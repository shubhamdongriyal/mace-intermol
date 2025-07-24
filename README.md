# mace-intermol

# ⚛️ Intermolecular Loss Extension for MACE

This repository contains modifications to `mace/modules/loss.py` for incorporating **intermolecular force loss** during training of MACE models. These changes are useful when modeling weak, non-covalent interactions (e.g., van der Waals) in molecular systems.

---

## ✨ What's New?

Three key functions have been added/modified:

### 🔧 `WeightedEnergyForceIntermolForceLoss`

- Computes a **total weighted loss** combining:
  - Force loss
  - Energy loss
  - Intermolecular force loss (optional)
- Customizable weights: `w_forces : w_intermol_forces : w_energy`
- Enables fine-tuning of the model's sensitivity to specific interactions.

---

### 🧩 `compute_mol_forces`

- Computes **intermolecular forces** between molecular fragments.
- Requires a `mol.idx` file:
  - Each line specifies atom indices belonging to a single fragment.
  - Used to compute the net force on each fragment and subtract internal forces.

---

### 📉 `mean_square_intermol_error`

- Calculates **mean squared error (MSE)** between predicted and reference intermolecular forces.
- Passed into `WeightedEnergyForceIntermolForceLoss` to contribute to the overall training loss.

---

## 📁 Input Requirement

- A `mol.idx` file must be included in the dataset.
  - Example:
    ```
    0 1 2 3 4
    5 6 7 8 9
    ```
  - This defines two molecular fragments (e.g., for a dimer).

---

## 🧪 Motivation

By explicitly penalizing the model for errors in **intermolecular forces**, we improve its accuracy on:
- Weak interactions (e.g., π–π stacking, hydrogen bonding)
- Systems dominated by non-covalent physics

---

## 🛠️ Compatibility

These changes are designed to be **drop-in compatible** with the official [MACE](https://github.com/ACEsuit/mace) repository.

---

## 📬 Questions?

Feel free to open an [Issue](https://github.com/YOUR_USERNAME/YOUR_REPO/issues) or contact us for clarifications and contributions.
