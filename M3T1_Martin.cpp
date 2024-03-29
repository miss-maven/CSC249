#include <iostream>
using namespace std; 
#include <string>

// CSC-249 M3T1
// Jane Martin
// 2/10/2023

// debug the toggle switch
static const bool DEBUG = true;
// Forward declaration of a method defined later
string ArrayToString(int* array, int arraySize);

void SelectionSort(int* numbers, int numbersSize) {
   for (int i = 0; i < numbersSize - 1; i++) {
      // Find index of smallest remaining element
      int indexSmallest = i;
      for (int j = i + 1; j < numbersSize; j++) {
         if (numbers[j] < numbers[indexSmallest]) {
            indexSmallest = j;
           if (DEBUG) {
             cout << "\tsmallest: " << numbers[j];
             cout << " @ " << j << endl;
           }
         }
      }

      // Swap numbers[i] and numbers[indexSmallest]
      if (DEBUG) {
        cout << "\t\t" << "swap positions " << i;
        cout << " and " << indexSmallest << endl; 
      }
     
      int temp = numbers[i];
      numbers[i] = numbers[indexSmallest];
      numbers[indexSmallest] = temp;
     // show partially sorted array
     if (DEBUG) {
       cout << "\tPART_SORTED: " << ArrayToString(numbers, numbersSize) << endl;
     }
   }
}

string ArrayToString(int* array, int arraySize) {
   // Special case for empty array
   if (0 == arraySize) {
      return string("[]");
   }

   // Start the string with the opening '[' and element 0
   string result = "[" + to_string(array[0]);

   // For each remaining element, append comma, space, and element
   for (int i = 1; i < arraySize; i++) {
      result += ", ";
      result += to_string(array[i]);
   }

   // Add closing ']' and return result
   result += "]";
   return result;
}

int main() {
   // Create an array of numbers to sort
   int numbers[] = { 10, 2, 78, 4, 45, 32, 7, 11 };
   int numbersSize = sizeof(numbers) / sizeof(numbers[0]);

   // Display the contents of the array
   cout << "UNSORTED: " << ArrayToString(numbers, numbersSize) << endl;

   // Call the SelectionSort function
   SelectionSort(numbers, numbersSize);

   // Display the sorted contents of the array
   cout << "SORTED:   " << ArrayToString(numbers, numbersSize) << endl;
}
