This directory contain a data set prepared for the use of participants
for the 1994 AAAI Spring Symposium on Artificial Intelligence in Medicine.

* diabetes-data.tar.Z contains the distribution for 70 sets of data recorded
on diabetes patients (several weeks' to months' worth of glucose, insulin,
and lifestyle data per patient + a description of the problem domain).
Archived using tar and compressed.

Extract the data files from the archive.  On a Unix system, type
'tar xvf icu-data.tar'.  This will create a new directory named  ICU-Data
and extract all data files into that directory.  Very occasionally
this may not work; in that case try 'tar xvof' instead of 'tar xvf'.

## License

This dataset is adapted from the
[Diabetes dataset from the UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/diabetes)
under the terms of the
Creative Commons Attribution 4.0 International (CC BY 4.0) license.

### Statement of Changes

- The `Diabetes-Data` directory has similar structure to the unzipped
  version from the UCI repository.
- Fixes "*corrupted data*" where multiple files (`data-20`,
  `data-22`, `data-27`) contained lines that did not match the
  "day, time, type, quantity" structure. Some of these involved
  Alexander Hayes's judgements for what the correct value should be,
  many of which are documented in `hayesall-notes`.
- Adds some quality-of-life improvements to make the data easier
  to analyze. This work is ongoing.

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
