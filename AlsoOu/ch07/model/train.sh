#!/bin/bash
./svm-train ./train.data.real
./svm-predict ./test.data train.data.real.model predict.data
