# mace-intermol

Changes are in mace/modules/loss.py , It contains 3 major function for intermol loss.
WeightedEnergyForceIntermolForceLoss -> computed the weighted loss
compute_mol_forces  -> computes the interfragment force by using mol.idx provided as a saperate file which contain the indexes of fragments.
mean_square_intermol_error  -> compute mean square error only on intermol forces which later passed to WeightedEnergyForceIntermolForceLoss
