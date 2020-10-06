import argparse
from argparse import RawTextHelpFormatter, RawDescriptionHelpFormatter

if __name__ == "__main__":
    d = """Train or predict the features based on protein-ligand complexes.
    Examples:
    python CNN_model_keras.py -fn1 docked_training_features_12ksamples_rmsd_lessthan3a.csv 
           -fn2 training_pka_features.csv -history hist.csv -pKa_col pKa_mimic pKa -train 1
    """

    parser = argparse.ArgumentParser(description=d, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("-fn_train", type=str, default=["features_1.csv", ], nargs="+",
                        help="Input. The docked cplx feature training set.")