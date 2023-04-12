import argparse
from os.path import *
from conllu import *
from random_split import write_conllu

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Filter CoNNL-U sentences with certain SweLL " +
        "error labels"
        )
    parser.add_argument(
        'l1', 
        metavar='L1_TREEBANK', 
        type=str, 
        help='''path to the treebank of corrections'''
        )
    parser.add_argument(
        'l2', 
        metavar='L2_TREEBANK', 
        type=str, 
        help='''path to the treebank of original learner sentences'''
        )
    parser.add_argument(
        'labels', 
        metavar='LABELS', 
        nargs='+',
        type=str, 
        help='''space-separated list of labels'''
        )
    
    args = parser.parse_args()

    if not exists(args.l1) and exists(args.l2):
        print("Invalid treebank path(s)")
        exit(-1)

    with open(args.l1) as l1:
        l1_txt = l1.read()
    l1_ss = parse(l1_txt)

    with open(args.l2) as l2:
        l2_txt = l2.read()
    l2_ss = parse(l2_txt)

    ss = list(zip(l1_ss, l2_ss))
    
    top_labels = list(filter(lambda label: len(label) == 1, args.labels))
    full_labels = set(args.labels) - set(top_labels)

    s1s = []
    s2s = []
    for (s1,s2) in ss:
        # assuming each sentence only has one label because so is DaLAJ
        slabel = s2.metadata["error_labels"] 
        if slabel in full_labels or slabel[0] in top_labels: 
            s1s.append(s1)
            s2s.append(s2)
    
    write_conllu(join(dirname(args.l1), "filtered_L1.conllu"), s1s)
    write_conllu(join(dirname(args.l2), "filtered_L2.conllu"), s2s)