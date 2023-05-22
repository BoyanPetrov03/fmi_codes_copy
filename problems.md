
```cpp
void selection_sort(vector<int> &A) {
    for (int i = 0; i < A.size(); ++i) {
        int min_index = i;
        for (int j = min_index+1; j < A.size(); ++j) {
            if (A[j] < A[min_index]) {
                j = min_index;
            }
        }

        swap(A[i], A[min_index]);
    }
}
```

