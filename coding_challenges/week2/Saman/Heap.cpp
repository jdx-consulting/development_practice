﻿// Heap.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <vector>
#include <chrono>

using namespace std::chrono;

//heap sort array
void Heapify(std::vector<int> &HeapList, int parent, int listLength) {

	int maxChild;
	int temp;

	// get children indexes. Each parent  has 2 children, left & right
	int lChild = 2 * parent + 1;
	int rChild = 2 * parent + 2;

	// set largest child to maxChild
	if (rChild < listLength && HeapList[rChild] > HeapList[lChild])
		maxChild = rChild;
	else if (lChild < listLength)
		maxChild = lChild;
	else return;

	// swap child with parent
	if (HeapList[maxChild] > HeapList[parent])
	{
		temp = HeapList[maxChild];
		HeapList[maxChild] = HeapList[parent];
		HeapList[parent] = temp;

		// re heap list
		Heapify(HeapList, maxChild, listLength);
	}
}

// return random array
std::vector<int> BuildRandList(const int maxLength, const int maxValue = INT32_MAX)
{
	std::vector<int> randVec(maxLength);

	for (int i = 0; i < maxLength; ++i)
		randVec[i] = rand() % maxValue;

	return randVec;
}


int main()
{
	srand(time(NULL));

	int testRuns = 10;
	std::vector<double> timings;
	std::vector<int> randomList;

	int ListLengths = 10000000;

	std::cout << "Starting heap sorts. Running " << testRuns << " tests.\n";
	std::cout << "list sizes: " << ListLengths << std::endl;

	for (int j = 0; j < testRuns; j++)
	{
		int temp;
		int ListLength = ListLengths;

		randomList = BuildRandList(ListLength, ListLength);

		high_resolution_clock::time_point startTime = high_resolution_clock::now();

		for (int i = ListLength / 2 - 1; i >= 0; i--)
			Heapify(randomList, i, ListLength);

		//swap the last index with the first (i.e. put largest item to the end of the list)
		while (ListLength > 0)
		{
			temp = randomList[0];
			randomList[0] = randomList[ListLength - 1];
			randomList[ListLength - 1] = temp;

			ListLength--;

			// re heap list
			Heapify(randomList, 0, ListLength);
		}

		high_resolution_clock::time_point endTime = high_resolution_clock::now();

		duration<double, std::milli> timeTaken = endTime - startTime;

		std::cout << "time taken: " << timeTaken.count() / 1000 << "s\n";
		timings.push_back(timeTaken.count()/1000);
	}

	double sum = 0;
	double average;

	for(double value : timings)
		sum += value;

	average = sum / testRuns;

	std::cout << "average time: " << average << std::endl;
	std::cin.get();

	return 0;
}
