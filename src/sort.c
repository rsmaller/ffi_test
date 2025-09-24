#include <stdlib.h>
#include <string.h>

// Merge Sort
static void merge(int *array1, int *array2, int size1, int size2) { // shuffles array2 into array1. array1 should have everything
    int *internalArray = (int *)malloc((size1 + size2) * sizeof(int));
    int array1Index = 0; 
    int array2Index = 0;
    int totalSize = size1 + size2;
    while ((array1Index < size1) && (array2Index < size2)) {
        if (array1[array1Index] < array2[array2Index]) {
            internalArray[array1Index + array2Index] = array1[array1Index];
            array1Index++;
        } else {
            internalArray[array1Index + array2Index] = array2[array2Index];
            array2Index++;
        }
    }
    while (array1Index < (size1)) {
        internalArray[array1Index + array2Index] = array1[array1Index];
        array1Index++;
    }
    while (array2Index < (size2)) {
        internalArray[array1Index + array2Index] = array2[array2Index];
        array2Index++;
    }
    memcpy(array1, internalArray, totalSize * sizeof(int));
    free(internalArray);
    return;
}

void mergeSort(int *array1, int sizeTotal) {
    int partition2Index = sizeTotal / 2; // also size of first partition
    int *array2 = array1 + partition2Index;
    int size1 = partition2Index;
    int size2 = sizeTotal - partition2Index;
    if (sizeTotal <=1) return;
    mergeSort(array1, size1);
    mergeSort(array2, size2);
    merge(array1, array2, size1, size2);
    return;
}