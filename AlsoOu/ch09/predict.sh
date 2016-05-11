#!/bin/bash
./svm-scale -r range1 test.data > test.scale
./svm-train train.scale
./svm-predict test.scale train.scale.model test.predict
