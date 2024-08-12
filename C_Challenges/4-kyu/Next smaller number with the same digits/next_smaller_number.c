#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// A utility function to swap two characters
void swap(char* a, char* b) {
    char temp = *a;
    *a = *b;
    *b = temp;
}

// Comparator function to sort in descending order
int desc(const void* a, const void* b) {
    return (*(char*)b - *(char*)a);
}

long long next_smaller_number(unsigned long long n) {
    // Convert the number to a string
    char numStr[21]; // enough to store a long long number
    sprintf(numStr, "%llu", n);
    int len = strlen(numStr);

    // Traverse the number from right to left
    for (int i = len - 1; i > 0; i--) {
        // Find the first digit that is larger than the digit next to it
        if (numStr[i] < numStr[i - 1]) {
            // Find the largest digit to the right of numStr[i-1] and smaller than numStr[i-1]
            int maxIndex = i;
            for (int j = i + 1; j < len; j++) {
                if (numStr[j] < numStr[i - 1] && numStr[j] > numStr[maxIndex]) {
                    maxIndex = j;
                }
            }

            // Swap the found digits
            swap(&numStr[i - 1], &numStr[maxIndex]);

            // Sort the digits after (i-1) in descending order
            qsort(numStr + i, len - i, sizeof(char), desc);

            // Convert back to long long
            long long result = atoll(numStr);

            // Ensure the result is valid (i.e., no leading zeros)
            if (numStr[0] == '0') {
                return -1;
            }
            return result;
        }
    }
    return -1; // Return -1 if no smaller number is possible
}