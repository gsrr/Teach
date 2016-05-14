#!/bin/bash
#!/bin/bash
./svm-scale -l -1 -u 1 -s range1 train.data > train.scale
./svm-scale -r range1 test.data > test.scale
./svm-train train.scale
./svm-predict test.scale train.scale.model test.predict
