#!/usr/bin/env python3
#These are my comprehensive notes for my Data Structures and Algorithms course.
import math as m
def assignment_one_notes():
    '''
    Assignment One Notes::
    # Complexity Analysis:
        - The ability to predict the time and space complexity of an algorithm
        - T(n) = the number of operations executed in worst case for processing input of size n
        - To determine this, count the number of basic operations in the algorithm, Ex:
            - addition = 1 operation
            - calling a method or returning from a method = 1 operation
            - index in an array = 1 operation
            - comparison = 1 operation
        - remove multipliers and non-dominant terms

        - if we have 3log(n) + log(log(n)), its complexity is O(log(n)), so log(n) grows faster than log(log(n)).

        - Relatives of Big-Oh::
            - Big-Omega (Ω): lower bound (Best case)
            - Big-Theta (Θ): tight bound (Average case)
            - Big-O (O): obviously upper bound (Worst case)
            - Little-o (o): strict upper bound (not a tight bound) - Basically, Little-o cannot share the same growth rate as the function it is bounding.
            - Little-omega (ω): strict lower bound (not a tight bound) - Bsically, the same but for a lower bound.

        - Divide and Conquer Algorithms:
            - Divide: break the problem into subproblems
            - Conquer: solve the subproblems recursively
            - Combine: combine the solutions of the subproblems to solve the original problem
            - To find the complexity of a DAC Algorithm, you must use a Recurrence Relation
                - 3 Main methods: Substitution, Recursion Tree, and the main one, the Master Theorem
                - For sake of time, I'm only going to be studying the Master Theorem for the Final
                    - Master Theorem:
                        Let a>=1 and b>1 be const, let f(n) be a function, and let T(n) be defined on +/0 ints by recurrence:
                            T(n) = aT(n/b) + f(n) || Here n/b is either floor or ceiling of n/b, then T can have the following bounds:
                                if f(n) = O(n^log_ba - ε) for some ε>0, then T(n) = Θ(n^log_ba)
                                if f(n) = Θ(n^log_ba), then T(n) = Θ(n^log_ba * log n)
                                if f(n) = Ω(n^log_ba + ε) for some ε>0, and if af(n/b) <= cf(n) for some c<1 and sufficiently large n, then T(n) = Θ(f(n))
                                - All of this is a fancy way to say: COMPARE A AND B^D where f(n) = Θ(n^d)
                                    - if a < b^d, then T(n) = Θ(n^d)
                                    - if a = b^d, then T(n) = Θ(n^d log n)
                                    - if a > b^d, then T(n) = Θ(n^log_ba)
                                - We are checking to see whether the recursive part or the non-recursive part of an algorithm is heavier.
    '''
    return None

def assignment_two_notes():
    '''
    Assignment Two Notes::
    - Maximum-Subsequence Problem:
        - given an array of numbers, find the contiguous subarray with the largest sum.
    '''
    return None

def assignment_three_notes():
    '''
    Assignment Three Notes::
        Sorting Algorithms:
            - Basic Sorting Algorithms: Bubble Sort, Insertion Sort, Selection Sort
            - Advanced Sorting Algorithms: Shell Sort, Heap Sort, Quick Sort, Merge Sort, Counting Sort, Radix Sort, Bucket Sort
            - Inversions:
                - An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j]
                - An array with few inversions is almost sorted, an array with many is far from sorted
                - Maximum number of inversions in an array of size n is n(n-1)/2, average number of inversions is n(n-1)/4
            - Sensitive Algorithms: these perform differently based on how sorted the array is, AKA, how many inversions the array has.
                - Examples: Insertion Sort, Bubble Sort
            - Important Note: ANY algorithm that sorts by exchanging adjacent elements REQUIRES theta(n^2) time to exeute
            - ALSO: ANY algorithm that compares elements REQUIRES theta(n log n) time to execute
            - INSERTION SORT::
                - Array is divided into sorted and unsorted parts, and elements from the unsorted part are picked out and placed correctly into the sorted part.
                - Best case: O(n) time (when array is already sorted)
                - Average case: O(n^2) time
                - Worst case: O(n^2) time (when array is sorted in reverse order)
                - Summary: VERY simple, but highly inefficient on even moderately large lists. VERY sensitive
            - BUBBLE SORT::
                - Compares adjacent elements, swapping them if needed, then moves to the next pair, ad infinitum until end of array.
                - Very easy to reverse sort
                - Best case: O(n) time (when array is already sorted)
                - Average case: O(n^2) time
                - Worst case: O(n^2) time (when array is sorted in reverse order)
                - Summary: Simple, but highly inefficient on even moderately large lists. Not very sensitive if using basic version as it always runs n^2 time if list isn't sorted.
            - SELECTION SORT::
                - Divides array, like past 2, but casts find min or find max and shoves them to the right part of the array.
                - Best case: O(n^2) time
                - Average case: O(n^2) time
                - Worst case: O(n^2) time
                - Summary: Simple, but highly inefficient on even moderately large lists. Not sensitive at all
            - SHELL SORT::
                - An optimization of Insertion Sort that allows the exchange of items that are far apart.
                - It compares non-consecutive elements, reducing the gap between elements to be compared as the algorithm progresses.
                    - basically, it "x" sorts the array for gap size x, then reduces x and repeats until x=1, which is insertion sort.
                    - You could 5-sort an array, then 3-sort it, then 1-sort it.  An h_k sorted file that is then h_k-1 sorted stays h_k sorted.
                - Shell sort is, in theory, not any more efficient, but in practice is usually much faster than insertion sort.  It is sensitive.
                - In fact, if elements sorted are relatively prime to each other, shell sort can be run in O(n^3/2)
                - Best case: O(n log n)
                - Average case: O(n^2) (but a little faster)
                - Worst case: O(n^2)
                - Summary: More efficient than basic sorts, but sensitive.
            - DAC Algorithms::
                - MERGE SORT::
                    - Divides the array into 2 lists of equal elements, then divide them again, until they are lists of only one element, then recombines them
                    - ALWAYS O(n log n) complexity
                    - Merge sort MUST BE RECURSIVE
                - QUICK SORT::
                    - A pivot is chosen, then elements less than or equal to pivot are placed before the pivot and greater than after
                    - Those two halves are then sorted, but splitting the list is enough to make the algorithm much faster
                    - Quick sort MUST BE RECURSIVE
                    - Best case: O(n log n)
                    - Average case: O(n log n)
                    - Worst case: O(n^2) *if you pick the pivot horribly, you are just sorting rudimentarily
            - TIM SORT::
                - The default standard sorting algorithm in all recent Python/Java versions
                - Tim sort uses different sorting algorithms based on the number of elements in the list and any sorted sub-lists
                - Best case: O(n)
                - Average case: O(n log n)
                - Worst case: O(n log n)
            - Non-Comparative Algorithms::
                - COUNTING SORT::
                    - Assumes that each of the n input elements is an integer in the range 0 to k, when k = O(n), it runs O(n)
                    - It counts elements given a range of values the elements can fall in and counts occurances of each element, then lists them.
                - RADIX SORT::
                    - When each option is of the same 10^x, you can sort by digit (100s, 10s, 1s, done)
                    - Possible linear time (O(n))
                - BUCKET SORT::
                    - Assumes elements are uniformly distributed, meaning the amount of elements in a bucket would be small and the buckets could be sorted quickly.
                    - Possible linear time (O(n))
    '''
    return None

def assignment_four_notes():
    '''
    Assignment Four Notes::
        - Lists, Stacks, and Queues: (First Data Structures *Yaaaay!*)
            - ADTs First:
                - Abstract Data Types - specify data stored, operations on said data, and error conditions associated with operations
            - Lists are ADTs that describes a linear collection of data items in some order, in that each element occupies a specific position in the list
                - So, a list of elements with a linearly increasing index (from 0 to n)
                - Static arrays are a fixed size and memory is allocated contiguously at the compile time, so you must be careful adding to them
                - Linked lists are dynamic but have to use pointers to access items in memory
                    - Singly Linked Lists (SLLs)::
                        - consist of a sequence of nodes, starting from a head pointer
                        - each node stores: an element, and a link to the next node
                        - appending and iterating can be a pain unless you initialize the class and object with a tail
                    - Doubly Linked Lists (DLLs)::
                        - consist of a sequence of nodes, starting from a head pointer
                        - each node stores: an element, a link to the next node, and a link to the previous node
                        - this makes traversal possible in the positive or negative direction in terms of index
            - Stacks::
                - Stacks store arbitrary objects.  They are Last-In-First-Out
                - Main Operations: 
                    - push(obj): inserts an element to top of stack
                    - obj pop(): removes and returns the last inserted element
                - So we only have access to the top of the stack
                - Python recognizes stacks, so it's super easy to implement and use them within the language
                - Infix / Postfix Notation::
                    - Infix:: (4.99 * 1.06 + 6.99 * 1.06 = 19.05 (if just read from L to R))
                    - Postfix:: (4.99 1.06 * 5.99 + 6.99 1.06 * + = 18.69 (correct, read as numbers followed by their operations))
                    - Infix to Postfix::
                        - 1. when a number is seen, it is pushed onto the stack;
                        - 2. when an operator is seen: the operator is applied to the two numbers that are popped from the stack, and the result is pushed onto the stack
                        - Ex. || 6 * (5 - (2 + 3) * 8 + 3) || Postfix: 6 5 2 3 + 8 * - 3 + *
                            - Detailed Steps:
                                1. Create an empty stack
                                2. start scanning the infix expression from L to R
                                3. If current character is an operand, append it to the result string
                                4. If current character is (, push it onto the stack
                                5. If current char is ), pop operators from the stack and append them to the result string until you reach a left parentheses, then discard ( and )
                                6. if char is an operator, push it onto the stack if empty, otherwise compare it to the operator on top.  Push current op if it has higher priority, 
                                else pop the high priority operator before pushing the current one
                                7. repeat steps 2 through 6 until you have scanned the entire expression
                                8. Pop remaining operators from the stack and append them to the result
                            - Detailed Example:
                                current     stack       postfix string
                                1. A                    A
                                2. *        *           A
                                3. (        *(          A
                                4. B        *(          A B
                                5. +        *(+         A B
                                6. C        *(+         A B C
                                7. )        *           A B C +
                                8.                      A B C + *
                            - MOOOOORRRRRE::
                                - a*b+c --> ab * c + 
                                - 6*(5 + (2 + 3) * 8 + 3) --> 6523 + 8 *+ 3 +*
                                - (a + b)*(c - d)/(e + f) --> ab + cd -* ef +/
            - Queues::
                - Informally, a queue is a data structure where you can only access items in the order they were added to the structure
                - First-In-First_Out
                - enqueue: inserts an item at the rear end of a queue
                - dequeue: removes an item from the front of a queue
                - When a queue is full, we cannot enqueue, when it is empty, we cannot dequeue
                - Circular Queues:
                    - Without circular queues, queues can fill up, even if items are dequeued, they will only be allowed total n items EVER
                    - with a circular queue, you can continue to enqueue and dequeue as long as the queue doesn't get too full
                - Possibly the biggest application of Queues in the real world is scheduling.
            - TIP:: Be careful to align your DS with your task!
    '''
    return None

def assignment_five_notes():
    '''
    Trees and Binary Search Trees
        - technically, trees are a type of graph, which we will learn about later
        - traversals are much more difficult with trees
        - A TREE is a collection of nodes
            - the collection can be empty, otherwise, it consists of a distinguished node r, called the rood, and 0 or more nonempty subtrees, each of whose
            roots are connected by a directed edge from r
            - ROOT is the only node without a parent (visually at the top of a tree)
            - DEPTH is the distance from the root
            - HEIGHT is the distance from the farthest leaf (longest path from the visual bottom)
        - BINARY TREES are a tree in which each node has at MOSt 2 children
            - a PROPER BINARY TREE has exactly 2 children per parent
            - Binary trees can have a single node also
            - trees have special traversal rules since they have a lack of linearity.
        - TRAVERSALS::
            - Preorder: parent, left, right
            - Postorder: left, right, parent
            - Inorder: left, parent, right
        - BINARY SEARCH TREES::
            - let u, v, and w be three nodes such that u is in the left subtree of v and w is in the right, we have key(u) <= key(v) <= key(w)
            - basically, a root must be greater than (or =) the left leaf and lesser than (or =) the right leaf
            - an inorder traversal should print the nodes sorted
            - Insertion gets tricky with BSTs
                - we need to compare the value of the new node with the root, if it is lesser than, we go left, else right.  We continue this to the end of the tree
            - Deletion is very difficult
                - leaf nodes can just be deleted immediately with no adjustments
                - parents with one child are removed and replaced with their only child
                - parents with two children are replaced with the largest element in their left subtree or the least element in their right subtree
            - why would the max nmber of nodes in a BT of height h be 2^(h+1) - 1?
                - each tier (layer of height) increases the number of nodes by 2^(h+1) after the root node, then we take one away since the root has no partner node.
                - 2 possibilities added to every leaf every time you expand the tree.
            - short and wide BSTs are good, whereas skinny, tall BSTs lead to inefficiency - BST height is always between O(n) and O(log n)
        - AVL TREES:: (Adelson-Velskii and Landis)
            - these are binary search trees that are either nearly or perfectly balanced (every parent has 2 children = perf. balanced)
            - the height of the left and right subtrees can differ by at most 1 <-- THIS IS THE MAIN QUALIFIER!!!
            - empty trees are determined to be height of -1
            - All of this means the height of an avl tree is at MOST log n, meaning most tree operations can be performed in O(log n)
            - This comes with the price, also, of needing to maintain these extra rules when deleting from / adding to an AVL Tree
                - Inserting
                    - let's call the first unbalanced node a, from the insertion point back to the root.  A height imbalance requires that a's 22 subtrees' height differ by two
                    - a violation could happen four ways:
                        1. An insertion into the left subtree of the left child of a (single rotation)
                        2. An ins. into right subtree of the left child of a (double rotation)
                        3. An ins. into left subtree of the right child of a (double rotation)
                        4. an ins. into right subtree of the right child of a (single rotation)
                    - This might be the HARDEST concept in the course, but once it clicks, it clicks.  I recommend YouTube Videos and not lecture material to be honest. My professor
                    seemed too disorganized to explain this concept clearly and effectively.
                - Deleting
                    - first, search for the node that is to be deleted in the tree, then delete the contents of the node
                    - finally, we check the balancing factor of the nodes of the tree, rotating if necessary
        - B-TREES::
            - first, M-ARY SEARCH TREES: BSTs without the restriction of having only 2 children per parent node
                - a perfect MST has the same depth for every leaf
                - this means while a binary tree with 31 nodes has 5 levels, a 5-ary tree of 31 nodes has 3 levels
                - M-1 keys are needed to decide which branch to take, and MSTs should be balanced in some way and maintain a bounded height
            - B-Trees are self-balancing search trees designed to work well on external storage devices
                - data items are stored at leaves
                - non-leaf nodes store up to M-1 keys to guide the searching; key i represents the smallest key in subtree i+1
                - the root is either a leaf or has between 2 and M children
                - all non-leaf nodes (save for the root) have between ceil(M/2) and M children
                - all leaves are at the same depth and have between ceil(L/2) and L children
            - each node of a B-Tree represents a disk block
            - a 228-ary B-Tree, leaves would be on just level 4.  That's extremely efficient.  Disk reads could be restricted to levels 3 and 4 also,
            since the upper 2 are small enough to be cached in memory.
            - Insertion:
                - if empty, we create one node that is a root node and insert there
                - else: find the node the key belongs in, insert it if there is enough room, and split the node in half, and insert new key in parent recursively
                - Splitting nodes:
                    - take existing node, shove inserted number where it goes, then split the node after the inserted number
                    - then take the least out of the right leaf and push it up into the parent node, adjusting parent data as needed
            - Deletion:
                - if in a leaf and free, delete, move on
                - if a leaf has the minimum number of items, combine/merge with a neighbor to form a full leaf
                - this means the parent looses a child, which means if the parent falls below it's minimum, it must also be merged.
    '''
    return None

def assignment_six_notes():
    '''
    Assignment Six Notes::
        - PRIORITY QUEUES::
            - A queue for a collection of prioritized elements that allows arbitrary element insertion and allows the removal of the element that has highest priority
            - Each item is a pair (key, value)
            - These are basically a sorted Python dictionary that act like stacks.
            - elements are added with their priorities, but you remove the highest priority item, similar to popping a stack
            - Implementations:
                - unsorted list:
                    - takes O(1) time to add an element
                    - takes O(n) time to find the smallest key
                - sorted list:
                    - takes O(n) time to add an element
                    - takes O(1) time to find the smallest key
                - AVL Tree:
                    - everything takes O(log n), but this is obviously difficult
                - Heaps (still not defined):
                    - takes O(1) time to find the smallest key
                    - insert takes O(1) time on avg and O(log n) worst case
                    - remove_min takes O(log n)
        - HEAPS::
            - A MIN HEAP is a binary tree storing keys at its nodes while satisfying some properties:
                - Heap-Order or the value property:
                    - for every internal node v other than the root :: key(v) >= key(parent(v))
                - Structure property:
                    - heaps are complete binary trees (NOT binary SEARCH trees, JUST BTs)!
                    - let h be the height of the heap:
                        - for i = 0, ..., h-1, there are 2^i nodes of depth i
                        - at depth h-1, the internal nodes are to the left of the external nodes
            - The last node of a heap is the rightmost node of maximum depth
            - The max heap s defined similarly to the min heap
            - Heaps are filled as a book is read, not from the top branching downwards.
            - A MAX HEAP is a binary tree the same as a min heap except that the properties are slightly different:
                - for every internal node v other than the root :: key(v) <= key(parent(v))
            - Array-Based Heap Implementation:
                - We can represent a heap with n keys by means of an array of length n
                - links between nodes are not explicitly stores
                - funnily enough, array-based heaps are actually one-dimensional data structures, despite the fact they are still trees
            - inserting new elements into a min heap, you still need to insert an element into the next spot reading-wise, then shift it up to it's correct position priority-wise
            - it is possible, also, to merge two heaps given a new key.  Take the new key, make it the new root, and then heapify or uphead to reorganize the heap based 
            on the minheap rules
            - building a heap from an array of elements (bottom up) runs in O(n) time
        - D HEAPS::
            - D Heaps are exactly like binary heaps except that all nodes have d children
            - This means that you will end up with more time per level for down heap, but you have much fewer levels
            - Upheap won't change too much since you still have one parent per leaf
        - Can we use Heaps to sort items??
        - HEAP SORT::
            - first, you build a heap out of the elements that needs sorting, then you run delete_min n times
            - record the elements deleted at the end of the list, which will end up forming your sorted list
            - this is much faster than basic sorting algorithms at O(n log n) time
        - GOOD QUESTIONS TO LEARN::
            - how would you find the minimum element in a max heap?
            - how would you conver a max heap into a min heap?
        - MAPS::
            - A MAP is a searchable collection of items that consists of key-value pairs
            - keys are unique and multiple items with the same key are not allowed!
                - This doesn't mean that values are necessarily unique, though
            - The main operations of a map are for searching for, inserting, and deleting items
        - DICTIONARIES::
            - Everyone's favorite Python DS, this is actually a unique part of Python as a language and they are an abstraction
        - MAPS and DICTS in Python can be used semi-interchangeably
            - This means all the same Python methods for manipulating and creating dictionaries work on MAPS as well
        - HASH TABLES::
            - These are one of the most practical data structures for implementing a map (Python uses these to make dictionaries!)
            - we have to use a hash function to map each key k to an integer in the range [0, N-1], where N is the capacity of the bucket array for a hash table
                - basically we have a function that, given an element, will tell us exactly where that element is, "mapping" the element to that location given the hashing function
            - hashing can make the expected case of deleting and searching O(1) time
            - A HASH TABLE or HASH MAP is a data structure that uses a hash function to efficiently translate certain keys into associated values.  The hash function is used to
            transform the key into the index of an array element, where the corresponding value is to be sought.
            - HASHING IS GENIUS
            - Ideal hash table structure is just a list of some fixed size containing items, these items containing a key that will return the stored data when ran through the
            hash function
            - A Hashing Collision is when one key houses more than one data point.
            - You want hash functions to be simple to compute and MUST attempt to distribute the keys evenly among cells
            - If we know which keys will occur in advance we can write perfect hash functions, but we usually don't
            - If your input keys are integers, then simply key mod tablesize is an okay general strategy, though it isn't perfect
            - So how do we tackle all of these challenges while still being practical?
                - to decide a size for a hash table, keep this in mind:
                    - small tables are likely to produce many collisions
                    - large tables are likely to waste valuable space
                - generalizing things a bit:
                    - A hash function could be specified as the composition of two functions:
                        - hash code:
                            h_1: keys -> integers
                        - compression function:
                            h_2: integers -> [0, N-1]
                - Resolving collisions:
                    - Chaining
                        - When collision exists, we just put elements and their keys in a linked list at the hashed location 
                        - This does leave that if your hashing funciton is not chosen well, you will end up with an extremely large chain
                        - So, if implemented poorly, your searching can creep towards order n time
                        - SEPARATE CHAINING is when your hash function yields a pointer that points to a linked list of collision elements
                        - delta is the load factor of a hash table defined as the number of elements in the hash table / the table size
                            - given this, we want to make the table size as large as the number of elements expected
                            - it is also good to keep the table size PRIME!
                    - Linear Probing
                        - all elements are still stored in the table, but collisions are placed in the next place storage-wise (circularly)
                        - Collided elements are going to clump together
                        - If you end up with elements that collide and the next position is NOT available, the element finds the next available element and goes there
                        - in terms of searching, you may end up having to look at a few elements, but the hash function yields a good starting place most of the time
                        - this also creates a problem when it comes to deleting elemnts, since empty cells could mislead the search algorithm
                            - to solve this, we introduce a special object called AVAILABLE, which replaces deleted elements, but still allows the search to move on
                        - Primary Clustering is the tendency for linear probing hash tables collision resolution schemes to create long sequences of filled slots
                    - Quadratic Probing
                        - does the same thing as linear probing, but iterates in squares of 1, 2, 3, ..., n to find an empty bucket instead of linearly
                        - this still creates Secondary Clustering, though, but it is much less of an issue since things that originally mapped to the same location will follow
                        the same pattern
                    - Double Hashing
                        - double hashing uses a secondary hash function d(k) and handles collisions by iterating in d(1, 2, 3, ..., n) to find an empty cell
                    - Rehashing
                        - if the table gets too full, you can just stop and rehash the whole table as a new table that is around twice as big with probably a different hash function
                - So, in general, hashing is great but is complicated to effectively implement.  In a very rare worst case, hashing will run O(n), but most of the time it will run O(1)
    '''
    return None

def assignment_seven_notes():
    '''
    Assignment Seven Notes::
        - GRAPHS::
            - Every element in a graph is represented by a node, every relationship is represented by an edge
            - Graphs and graph algorithms can help you model and find a solution respectively
            - "Networks" are really just graphs - networks are graphs dressed with an abstraction
            - Graphs = (Verticies, Edges)
                - V = vertex set (n = |V| = total verticies)
                - E = edge set (m = |E| = total edges)
                - G_size = n + m
            - A Cycle in a graph - A path <v_0, v_1, ..., v_k> in an undirected graph forma s cycle if v_0 = v_k and k>=3
                - in an directed graph, <v_0, v_1, ..., v_k> where v_0 = v_k and k >= 2
            - Acyclic Graphs - graphs with no cycles at all
                - DAG (Directed A.G.) - what it sounds like...
            - Strongly connected components are pieces of a graph were every node is reachable from every other node
                - to find these, call DFS to compute finishing times, then find the reverse of the edges of the graph (G^T), then call DFS on that graph using the 
                order of the first DFS ordering, grouping the new DFS items together
        - GRAPH ALGORITHMS::
            - Graph Searches:
                - BFS::
                    - discovers all vertices at diestance k from s before discovering any vertices at distance k+1
                    - from one node to all its neighbors, then to the neighbors' neighbors, and so on
                    - time complexity: O(n + m), each vertex is enqueued O(1) at most once, then every each adjacency list is scanned at most once
                - DFS::
                    - from one node to a neighbor, then to another neighbor, until you can't find a neighbor anymore, then start exploring
                    - time complexity: O(n + m), again, for the same reason
            - TOPOLOGICAL SORT::
                - A linear ordering of all a graph's vertices such that if G contains an edge u-->v, u appears before v in the ordering
                - if the graph is not acyclic, then no linear ordering is possible
                - So this is different than a typical "sort", it kind of sorts edges
                - It works by:
                    1. call DFS to compute finishing times for each vertex
                    2. as each vertex is finished, insert it onto the front of a linked list
                    3. return the list of vertexes
            - SPANNING TREES::
                - A subgraph of G that is also a tree and includes every node of G
                - This means connecting every node as efficiently as possible with N-1 edges
                - The MIN COST SPANNING TREE is a min spanning tree, but with edge weights in mind to find the cheapest, and thus shortest, way to connect every node
                    - Kruskal's Algorithm::
                        - Sort the edges from small to large
                        - Go in order from heaviest to lightest edge, adding them to the min. spanning tree if adding them DOES NOT CREATE A CYCLE
                        - output the tree
                        - running time is O(m log m) = O(m log n)
                        - this algorithm is GREEDY, meaning it accepts a LOCALLY OPTIMAL CHOICE in hopes it will eventually yield a GLOBALLY OPTIMAL SOLUTION
                            - This means if a graph is sparse, Kruskal's might not even yield a connected MST
                            - greedy algorithms are simple to design and implement and fast, also
                    - Prim's Algorithm::
                        - Instead of starting with n nodes and hoping things end up connected, Prim's starts somewhere and then picks the cheapest edge forward
                        - Still checks for cycles
                        - running time is O(m log m) = O(m log n)
                    - So... Kruskal's starts with a forest and merges into a tree, whereas Prim's stays a tree always
            - SHORTEST PATH PROBLEMS:
                - Dijkstra's Algorithm
                    - single-source shrotest path problem
                    - It cannot be done with negative-weight edges
                    - Done by "Relaxing" an edge (u, v), or testing whetehr we can improve the shortes path to v found so far by going through u
                        - verticies in V - S reside in a min-priority queue
                            - keys in q are estimates of shortest-path weights d[u]
                        - repeatedly select a vertex u in V-s, with the minimum shortest-path estimate d[u]
                        - relax all edges leaving u
                    - Running time: O(m log n)
    '''
    return None

#Assignment One Functions::
def binary_search (arr, start, end, key):   
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return None
def binary_search_recursive(arr, start, end, key):
    if start > end:
        return None
    mid = start + (end - start) // 2
    if arr[mid] < key:
        return binary_search_recursive(arr, mid + 1, end, key)
    elif arr[mid] > key:
        return binary_search_recursive(arr, start, mid - 1, key)
    else:
        return mid
#End Assingment One Functions

#Assignment Three Functions::
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)
    return arr
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
        print(arr)
    return arr
def selection_sort(arr):
    n = len(arr)
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j    
        print(arr)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def shell_sort(arr):
    interval = len(arr) // 2
    while interval > 0:
        for i in range(interval, len(arr)):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2
        print(arr)
    return arr
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            print(L, R, arr)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            print(L, R, arr)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            print(L, R, arr)
    return arr
#No Code provided for some sorting algorithms - "too complex" for him to test us with
#End Assignment Three Functions 

#Assignment Four Functions/Classes::
class Node2: #For DLL
    def __init__ (self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.count = 0
    '''Doubly Linked lists have very similar methods to a singly linked list, so code is not included for that'''
class Node: #For SLL
    def __init__ (self, data=None):
        self.data = data #initializing a Linked List
        self.next = None
class SinglyLinkedList:
    def __init__ (self):
        self.head = None #initializing a Singly Linked List
        self.size = 0
        self.tail = None

    def search(self, data): #To look for an element
        for node in self.iter():
            if data == node:
                return True
        return False

    def iter(self): #To traverse the List
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def append_using_tail(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def append(self, data): #To add a new element to the end of the list
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node #Here you may see an issue... We have to traverse the whole thing to add an item.  You can add a tail upon initialization if you want to make this easier

    def append_at_a_location(self, new_data, before_data): #To insert an element
        current = self.head
        prev = self.head
        node = Node(new_data)
        while current:
            if current.data == before_data:
                node.next = current
                prev.next = node
            prev = current
            current = current.next

    def append_at_a_location(self, data, index): #To insert an item given an index
        if self.size < index:
            print("The list has less number of elemnents")
            return
        node = Node(data)
        if index == 1:
            node.next = self.head
            self.head = node
            return
        current = self.head.next
        prev = self.head
        count = 2
        while current:
            if count == index:
                node.next = current
                prev.next = node
                return
            count += 1
            prev = current
            current = current.next
        '''Deleting nodes is extremely similar to finding nodes, so code for that isn't included.'''
#End Assignment Four Classes/Functions

#Assignment Five Classes/Functions
def preorder(node):
    if node is None:
        return
    print(node.data)
    preorder(node.left_child)
    preorder(node.right_child) #recursively explores, starting with the parent, then the left leaf, then the right
def postorder(node):
    if node is None:
        return
    postorder(node.left_child)
    postorder(node.right_child)
    print(node.data) #recursively explores, starting with the left leaf, then right, then parent
def inorder(node):
    if node is None:
        return
    inorder(node.left_child)
    print(node.data)
    inorder(node.right_child) #recursively explores, starting with the left leaf, then parent, then right
def count_nodes(t): #To count nodes in any tree
    if (t==None):
        return 0
    return 1 + count_nodes(t.left) + count_nodes(t.right)
def search(self, data): #To look for an element in a BST
    current = self.root_node
    while True:
        if current is None:
            print("Item not found")
            return None
        elif current.data is data:
            print("Item found", data)
            return data
        elif current.data > data:
            current = current.left_child
        else:
            current = current.right_child
def find_min_binary(self): #To find the minimum element in a BST, goes all the way to the left of the tree
    current = self.root_node
    while current.left_child:
        current = current.left_child
    return current.data
def insert_binary(self, data): #To insert an element into a BST
    node = Node(data)
    if self.root_node is None:
        self.root_node = node
        return self.root_node
    else:
        current = self.root_node
        parent = None
        while True:
            parent = current
            if node.data < parent.data:
                current = current.lefft_child
                if current is None:
                    parent.left_child = node
                    return self.root_node
            else:
                current = current.right_child
                if current is None:
                    parent.right_child = node
                    return self.root_node
def delete_node_binary(root, key): #To delete a node from a BST
    if root is None:
        return root
    if key < root.key:
        root.left = delete_node_binary(root.left, key)
    elif key > root.key:
        root.right = delete_node_binary(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = find_min_binary(root.right)
        root.key = temp.key
        root.right = delete_node_binary(root.right, temp.key)
    return root
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
class AVL_Tree(object):
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
#No code for AVL Tree Rotations, I'm way to tired to type all that
#End Assignment Five Classes/Functions

def main():# Examples with code go here!
    
    print("\nAssignment One Examples::")
    #Binary Search Example (with an already sorted array as input)
    arr = [2, 3, 4, 10, 40]
    arr2 = [1, 5, 8, 12, 20, 25, 30]
    key = 10
    key2 = 20
    result = binary_search(arr, 0, len(arr)-1, key)
    result_recursive = binary_search_recursive(arr2, 0, len(arr)-1, key2)
    print("Non-Recursive Array and Key: ", arr, key, "\n", "Non-Recursive Results: ", result)
    print("Recursive Array and Key: ", arr2, key2,  "\n", "Recursive Results: ", result_recursive)
    print("End of Assignment One Examples\n")

    print("Assignment Three Examples::")
    arr_ins = [12, 500, 3, 4, 6, -10]
    sorted_arr_ins = insertion_sort(arr_ins)
    print("Insertion Sort Result: ", sorted_arr_ins)
    arr_bub = [64, 34, -5, 25, 12, 22, 11, -5, 90, -10]
    sorted_arr_bub = bubble_sort(arr_bub)
    print("Bubble Sort Result: ", sorted_arr_bub)
    arr_sel = [29, 10, 14, -500, 37, 13, -10]
    sorted_arr_sel = selection_sort(arr_sel)
    print("Selection Sort Result: ", sorted_arr_sel)
    arr_shell = [35, 67, -20, 35, -1, -2, 5, 7, 10]
    sorted_arr_shell = selection_sort(arr_shell)
    print("Shell Sort Result: ", sorted_arr_shell)
    arr_merge = [12, 33, 4, 6, 7, 1, -23, 5, 6]
    sorted_arr_merge = selection_sort(arr_merge)
    print("Merge Sort Result: ", sorted_arr_merge)
    print("End of Assignment Three Examples\n")


if __name__ == "__main__":
    main()