# Software Delivery Practice

## Heap Sort

The objective of the challenge this week is to deliver a sorted array of integer values using a minHeap as the sorting algorithm.

You should:
1. Build an unsorted array of random integers. This source array should be 100,000 elements in size.
2. Create an empty target array of the same size.
3. Build a minHeap from the source array, using _heapify_ so that it has the smallest integer as the root.
4. Remove the root (minimum) element from the minHeap and place it in position 0 in the target array.
5. Run _heapify_ on the minHeap, so that the next smallest value becomes the root element.
6. Remove the root (minimum) element from the minHeap and place it in (next) position 1 in the target array.
7. Run _heapify_ on the minHeap, so that the next smallest value becomes the root element.
8. Repeat 6 and 7 until the minHeap is empty, and the target array is fully populated and in order.



