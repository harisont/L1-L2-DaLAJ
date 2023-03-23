# L1-L2-DaLAJ
The [DaLAJ Dataset for Linguistic Acceptability Judgments for Swedish](https://arxiv.org/abs/2105.06681) as an [L1-L2 parallel UD treebank](https://aclanthology.org/W17-6306/).

## Processing
Learner sentences, correction hypotheses and error labels were extracted from the original DaLAJ TSV files and processed as follows: 

1. __missing token markers (`@`) were removed__ from the L2 sentences
2. both in the L1 and L2 sentences, __anonymization labels were replaced__ by the following pseudonyms[^1]:
   - `x-land-gen` -> `Sveriges`
   - `x-stad-gen` -> `Göteborgs`
   - `x-land` -> `Sverige`
   - `x-skola` -> `Martinaskolan`
   - `x-svensk-stad` -> `Göteborg`
   - `x-institution` -> `Chalmers`
   - `x-region` -> `Värmland`
   - `x-geoplats` -> `Kviberg`
   - `x-stad` -> `Göteborg`
   - `x-hemland` -> `Italien`
3. the resulting __sentences were automatically annotated in UD__ with [UDPipe 1](https://ufal.mff.cuni.cz/udpipe/1) using the [`swedish-talbanken-ud-2.5-191206`](https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-3131/swedish-talbanken-ud-2.5-191206.udpipe?sequence=96&isAllowed=y) model. The results of the UD annotation are NOT manually validated.
4. the resulting CoNNL-U sentences were shuffled
5. DaLAJ error labels were added as sentence metadata to the L2 CoNNL-U file (e.g. `# error_labels = L-Der`)

## Citation
If you use this data, you are welcome to cite

```
@inproceedings{
masciolini2023a,
title={A query engine for L1-L2 parallel dependency treebanks},
author={Arianna Masciolini},
booktitle={The 24rd Nordic Conference on Computational Linguistics},
year={2023},
url={https://openreview.net/forum?id=ngh-uZ2ivH}
}
```

[^1]: the reason for this is that the anonymization labels are likely to be wrongly lemmatized and POS-labelled. This pseudonymization strategy is obviously naïve, but acceptable in cases where semantics is not crucial, i.e. for automatic UD annotation.