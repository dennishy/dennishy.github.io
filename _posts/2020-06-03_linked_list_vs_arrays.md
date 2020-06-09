---
layout: post
title: "Linked Lists vs Arrays"
date: 2020-06-03 12:00:00 -0000
categories: PYTHON 
---
## Linked Lists
A Linked List is a collection of nodes. Linked Lists can be used to create queues, stacks, and graphs (among other structures). Each node has two fields: **Data** and **Next**. The **Data** field contains the data to be stored and **Next** points to the next **Node** in the Linked List. 

The first node in a Linked List is the **head**. The last node has a **Next** value of **None**. 



See this excellent write up at [realpython](https://realpython.com/linked-lists-python/). 

Linked Lists allow data to be stored anywhere in memory (See 'grokking algorithms' by Aditya Y. Bhargava) and are faster for **inserts** (O(1)) as a result. Conversely, they are slower for **reads** because you would have to traverse each node if the data you're looking for is near the end of the Linked List (O(n)). 

## Arrays

Unlike Linked Lists, Arrays store all values contiguously in memory. This makes Arrays more efficient for **reads** (O(1)) as each data element is in a fixed position in memory. However, Arrays have a challenge with **inserts**. The size of the Array has to be large enough to contain all the data elements needed of it or it has to rewrite the entirety of the existing array along with the new data element into a new position in memory. Alternatively the array has to be large enough when instantiated to hold all the elements it may need, leading to unused blocks. For this reason it is slower for inserts at O(n). 
