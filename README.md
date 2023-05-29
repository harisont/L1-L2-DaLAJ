# L1-L2-DaLAJ
The [DaLAJ Dataset for Linguistic Acceptability Judgments for Swedish](https://arxiv.org/abs/2105.06681) as an [L1-L2 parallel UD treebank](https://aclanthology.org/W17-6306/).

## Data
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
3. the resulting __sentences were automatically annotated in UD__ with [UDPipe 1](https://ufal.mff.cuni.cz/udpipe/1) using the [`swedish-talbanken-ud-2.5-191206`](https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-3131/swedish-talbanken-ud-2.5-191206.udpipe?sequence=96&isAllowed=y) model. The results of the UD annotation are NOT manually validated
4. DaLAJ __error labels were added__ as sentence metadata to the L2 CoNNL-U file (e.g. `# error_labels = L-Der`)
5. __the treebank was filtered__ with the [`filter_swell_labels.py`](filter_swell_labels.py) to only keep M- and S- labelled sentences, i.e. sentences containing morphosyntactical errors (see [M+S](M+S) folder)
6. for evaluating the pattern extraction system presented at the [2023 BEA workshop](sig-edu.org/bea/2023), the resulting __CoNNL-U sentences were shuffled and split__ into two subsets, found in [M+S/bea](M+S/bea), with the [`random_split.py`](random_split.py) script. The `ex` ("examples") set contains the 100 sentences to extract patterns from. The `tb` ("treebank") set contains all other sentences patterns are matched against in the example retrieval task
7. during preliminary experiments, it was noted that many errors were due to incorrect UD annotation. All parts of the treebank (both the splits and the full treebank) were therefore re-annotated using the [UDPipe 2 REST API](https://lindat.mff.cuni.cz/services/udpipe/api-reference.php) with the default Swedish model. For instance, for the L2 half of the `ex` set:
   
   ```
   curl -F data=@ex_L2.conllu -F model=swedish -F tagger= -F parser= http://lindat.mff.cuni.cz/services/udpipe/api/process | PYTHONIOENCODING=utf-8 python -c "import sys,json; sys.stdout.write(json.load(sys.stdin)['result'])" > ex_L2_udpipe2.conllu
   ```
   This round of annotation was also NOT manually checked, but a superficial comparison revealed that using UDPipe 2 gives significant improvements wrt UDPipe 1.

## Citation
If you use this data, you are welcome to cite

```
TBA
```

[^1]: the reason for this is that the anonymization labels are likely to be wrongly lemmatized and POS-labelled. This pseudonymization strategy is obviously naïve, but acceptable in cases where semantics is not crucial, i.e. for automatic UD annotation.