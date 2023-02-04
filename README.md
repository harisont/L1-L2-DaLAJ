# L1-L2-DaLAJ
The [DaLAJ Dataset for Linguistic Acceptability Judgments for Swedish](https://arxiv.org/abs/2105.06681) as an [L1-L2 parallel UD treebank](https://aclanthology.org/W17-6306/).

---

Learner sentences, correction hypotheses and error labels were extracted from the original DaLAJ TSV files and processed as follows: 

1. missing token markers `@` were removed from the L2 sentences
2. both in the L1 and L2 sentences, anonymization labels were replaced by the following pseudonyms[^1]:
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
3. the resulting sentences were parsed with [UDPipe 1](https://ufal.mff.cuni.cz/udpipe/1) using the [`swedish-talbanken-ud-2.5-191206`](https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-3131/swedish-talbanken-ud-2.5-191206.udpipe?sequence=96&isAllowed=y) model
4. the resulting CoNNL-U sentences were shuffled
5. error labels were added to the L2 CoNNL-U file

[^1]: this was done as the anonymization labels are likely to be wrongly lemmatized and POS-labelled. The pseudonymization strategy is admittedly naïve. However, since UD parsers are not concerned with the semantics of the sentences, it is not important for them to make sense.