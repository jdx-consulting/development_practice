using System;
using System.Collections.Generic;


/*
 * Code to Heap sort a list of random integers
 * 
 * RandomList is used to create a list of random numbers of any size
 * 
 * The main function then uses Heapify to heap sort the list
 * 
 * 1. Following this the largest element (the root, index 0) is swapped with the last element and the list size is reduced by 1
 * 2. The list (1 element smaller) is heap sorted again
 * 
 * Steps 1 and 2 are reapeated until the list size is 0 and all the elements are sorted with the largest at the end
 */

namespace HeapSortCode
{
    static class HeapSort
    {

        static void Main(string[] args)
        {
            int temp;

            int listLength = 100000;
            List<int> someList = RandomList(listLength, 0, listLength);

            Console.WriteLine("Random list of {0} integers created", listLength);

            //create variables for tracking time taken
            double timeTaken = 0;
            DateTime endTime;
            DateTime heapTime;
            DateTime startTime = DateTime.Now;

            someList.Sort();

            /*
            //sort the list into a max heap
            for (int i = listLength / 2 - 1; i >= 0; --i)
                Heapify(ref someList, i, listLength);

            heapTime = DateTime.Now;
            timeTaken = (heapTime - startTime).TotalSeconds;
            Console.WriteLine("time taken to heapify list: {0:#.###}{1}", timeTaken, "s");

            //swap the last index with the first (i.e. put larest item to the end of the list)
            while (listLength > 0)
            {
                temp = someList[0];
                someList[0] = someList[listLength - 1];
                someList[listLength - 1] = temp;

                listLength--;

                //re-heap list
                Heapify(ref someList, 0, listLength);
            }
            */

            endTime = DateTime.Now;
            timeTaken = (endTime - startTime).TotalSeconds;
            Console.WriteLine("time taken to sort list: {0:#.###}{1}", timeTaken, "s");

            Console.Write("Heap sort complete");
            Console.ReadLine();
        }

        //heap function
        static void Heapify(ref List<int> integerList, int parent, int listLength)
        {
            int lChild;
            int rChild;
            int maxChild;
            int temp;

            // each parent node has two children as its a binary tree
            lChild = 2 * parent + 1;
            rChild = 2 * parent + 2;

            // the largest child is taken as maxChild
            if (rChild < listLength && integerList[rChild] > integerList[lChild])
                maxChild = rChild;
            else if (lChild < listLength)
                maxChild = lChild;
            else return;

            // the largest value is swapped with the parent
            if (integerList[maxChild] > integerList[parent])
            {
                temp = integerList[maxChild];
                integerList[maxChild] = integerList[parent];
                integerList[parent] = temp;

                //Swap(ref integerList, maxChild, parent); //<-using this function increases run time by ~20-30% !!!!

                // the list is heap sorted again
                Heapify(ref integerList, maxChild, listLength);
            }
                
        }


        //swap parent and child
        static void Swap(ref List<int> fullList, int indexA, int indexB)
        {
            //temp store
            int valParent = fullList[indexA];

            //swap parent and child
            fullList[indexA] = fullList[indexB];
            fullList[indexB] = valParent;
        }

        //builds a list of random numbers
        static List<int> RandomList(int length, int min = 0, int max = int.MaxValue)
        {
            List<int> sortedList = new List<int>();
            Random randNb = new Random();
           
            for (int i = 0; i < length; ++i)
                sortedList.Add(randNb.Next(min, max));

            return sortedList;
        }


    }



}
