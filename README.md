# SemanticSoftSegmentation
Python Implementation of Semantic Soft Segmentation


Current update:

Yes, I have stopped it midway as you have to calculate eigenvalues of a huge sparse matrix, python is taking hours to calculate that. Matlab is doing the same in a few minutes. You can find my interaction with a former scipy contributor on Twitter : https://twitter.com/Combalgorythm/status/1129787645679218693 .

Also, if you want to have the Laplacian sparse .npz file it's here: https://drive.google.com/file/d/1RU0kH3rVf6TMILI4Z6Y0E-E_cFHFRrYo/view

Anyway, if you want to use the current technique for production, it's terribly slow. Lots of optimisation needs to be done in order to use the technique outlined in the paper. I am really busy with work till August. Then, I'll again have a look at how to optimize it.


