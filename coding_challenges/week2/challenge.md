# Software Delivery Practice

## [Heap Sort](https://en.wikipedia.org/wiki/Heapsort)

The objective of the challenge this week is to deliver a sorted array of integer values using a __Heap Sort__ ([maxHeap](http://btechsmartclass.com/DS/U3_T7.html)) algorithm. 

You should:
* Build a maxHeap of 100,000 random integers, using _heapify_ so that it has the largest integer as the root and all child nodes conform to the principles of a maxHeap. 
* You will need to use an integer array to hold the maxHeap, see notes below for guidance on how this can be implemented. The length of the array, ie 100,000, is the initial `SIZE`
* Set the end position of the sort range: `POS = SIZE - 1`
* Repeat the following until the array is sorted in ascending order:
  * Swap the root node (largest integer) with the end node (ie the node at position `POS`).
  * Trickle the _new_ root node down to its correct position in the maxHeap, ie where its parent node is larger and both its child nodes are smaller.
  * Decrement the range under sort `POS--`.
  * This will result in the root node again being the largest integer in the sort range (remember that the previous largest was moved to the end of the array, and the sort range `POS` reduced by 1).
* Once the `POS` value is zero the array will be sorted.


### Notes

In this [sort](https://en.wikipedia.org/wiki/Heapsort) you essentially start with a maxHeap held in the full length of the array, as the sort progresses the array is split between a maxHeap in the first section, and a sorted list of integers in the second section. Each iteration the first section is reduced in size, and the second section increased commensurately as the current max value in the heap is picked off and moved across, until ultimately the entire array is a sorted list of integers and the maxHeap has been reduced down to nothing.

__This is a very efficient sort, and with 100,000 elements should complete in < 1sec.__

__This is an _in place_ sorting algorithm, ie the sort takes place within the source array (memory efficient).__

Heap Sort overview @ https://en.wikipedia.org/wiki/Heapsort

Max Heap overview @ http://btechsmartclass.com/DS/U3_T7.html

A maxHeap can be held in an array using the following indexing rules:

Let n be the number of elements in the heap and i be an arbitrary valid index of the array storing the heap. If the tree root is at index 0, with valid indices 0 through n − 1, then each element a at index __i__ has:

Left child index = `2i + 1`
Right child index = `2i + 2`
Parent index = `floor((i − 1) ∕ 2)`
