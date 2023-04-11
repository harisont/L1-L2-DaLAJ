import argparse
from os.path import *
from conllu import *
from random import shuffle

def write_conllu(path,ss):
    with open(path,"w") as outfile:
        outfile.write("".join([s.serialize() for s in ss]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Shuffle and split parallel (L1-L2) CoNNL-U treebanks " +
        "into a train, dev and test set"
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
        'train', 
        metavar='N_TRAIN', 
        type=int, 
        help='number of sentences to reserve for the training set'
        )
    parser.add_argument(
        'dev', 
        metavar='N_DEV', 
        type=int, 
        help='number of sentences to reserve for the development set'
        )
    parser.add_argument(
        "-l",
        "--labels",
        type=str,
        help="path to the error labels"
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

    if args.labels:
        if not exists(args.labels):
            print("Invalid labels path")
            exit(-1)
        with open(args.labels) as l:
            labels = l.readlines()

    if args.labels:
        ss = list(zip(l1_ss, l2_ss, labels))
    else:    
        ss = list(zip(l1_ss, l2_ss))

    if args.train + args.dev > len(ss):
        print("Train + dev sets too big")
        exit(-1)

    shuffle(ss)

    train_ss = ss[:args.train]
    dev_ss = ss[args.train:args.dev]
    test_ss = ss[args.dev:]

    if args.labels:
        for set in [train_ss, dev_ss, test_ss]:
            for (l1,l2,e) in set:
                l2.metadata["error_labels"] = e

    for (name,set) in [("train",train_ss), ("dev",dev_ss), ("test",test_ss)]:
        if set:
            if args.labels:
                [l1_ss, l2_ss, _] = list(zip(*set))
            else:
                [l1_ss, l2_ss] = list(zip(*set))
            write_conllu(join(dirname(args.l1), name + "_L1.conllu"), l1_ss)
            write_conllu(join(dirname(args.l2), name + "_L2.conllu"), l2_ss)
    
