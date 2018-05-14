# Software Delivery Practice

## [Heap Sort](https://en.wikipedia.org/wiki/Heapsort)

The objective of the challenge this week is to deliver a sorted array of integer values using an in-place [maxHeap](http://btechsmartclass.com/DS/U3_T7.html) sorting algorithm.

You should:
* Build a maxHeap from an input of 100,000 `SIZE` random integers, using _heapify_ so that it has the largest integer as the root and all child nodes conform to the principles of a maxHeap. You will need to use an integer array to hold the maxHeap, see notes below for guidance on how this can be implemented.
* Set the end position of the sort range: `POS = SIZE - 1`
* Repeat the following until the array is sorted in ascending order:
  * Swap the root node (largest integer) with the end node (ie the node at position `POS`).
  * Decrement the range under sort `POS--`.
  * Trickle the _new_ root node down to its correct position in the maxHeap, ie where its parent node is larger and both its child nodes are smaller.
  * This will result in the root node again being the largest integer in the sort range (remember that the previous largest was moved to the end of the array, and the sort range `POS` reduced by 1).
* Once the `POS` value is zero the array will be sorted.


### Notes

In this [sort](https://en.wikipedia.org/wiki/Heapsort) you essentially start with a maxHeap held in the full length of the array, as the sort progresses the array is split between a maxHeap in the botton section, and a sorted list of integers in the top section. Each iteration the bottom section is reduced in size, and the top section increased commensurately, until ultimately the entire array is a sorted list of integers and the maxHeap has been reduced down to nothing.

Heap Sort overview @ https://en.wikipedia.org/wiki/Heapsort

Max Heap overview @ http://btechsmartclass.com/DS/U3_T7.html

A maxHeap can be held in an array using the following indexing rules:

Let n be the number of elements in the heap and i be an arbitrary valid index of the array storing the heap. If the tree root is at index 0, with valid indices 0 through n − 1, then each element a at index __i__ has:

Left child index = `2i + 1`
Right child index = `2i + 2`
Parent index = `floor((i − 1) ∕ 2)`
