#include <iostream>     // std::cout
#include <queue>        // std::queue
#include <stddef.h>     // size_t

/*
    given a tree you need to return the sum of all numbers each of which 
    is formed by a unique path from root to leaf
*/

struct Node
{
public:
    Node()
    {
        left = NULL;
        right = NULL;
    }

    int data;
    Node *right;
    Node *left;
};

struct Tree
{
    Node *root;
};

size_t SumRec(Node *node, size_t multiplyer, std::queue<int> queue);

size_t Sum(Tree *tree)
{
    std::queue<int> queue;

    return (SumRec(tree->root, 1, queue));
}

size_t SumRec(Node *node, size_t multiplyer, std::queue<int> queue)
{
    if (NULL == node)
    {
        return 0;
    }
    if (NULL == node->left && 
        NULL == node->right)
    {
        size_t sum = 0;
        queue.push(node->data);

        while (!queue.empty())
        {
            sum += multiplyer * queue.front();
            multiplyer /= 10;
            queue.pop();
        }

        return sum;
    }
    else
    {
        queue.push(node->data);
        multiplyer *= 10;

        return (SumRec(node->left, multiplyer, queue) + 
                SumRec(node->right, multiplyer, queue));
    }   
}

int main()
{
    Tree tree;
    Node rootNode;
    Node node1;
    Node node2;
    Node node3;
    Node node4;

    tree.root = &rootNode;
    tree.root->left = &node1;
    tree.root->right = &node2;
    node1.left = &node3;
    node1.right = &node4;

    tree.root->data = 4;
    node1.data = 9;
    node2.data = 0;
    node3.data = 5;
    node4.data = 1;

    std::cout << Sum(&tree) << "\n";

    return 0;
}