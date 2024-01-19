#include<iostream>
#include <climits>
using namespace std;
struct NODE{
    int data; 
    NODE* next;
};

NODE* makeNode(int data){
    NODE* temp = new NODE;
    temp -> data = data;
    temp -> next = nullptr;    
    return temp;
}

void pushBack(int data, NODE*& head){
    if (head == nullptr) {
        head = makeNode(data);
    }

    else {
        NODE* temp = makeNode(data);
        NODE* T = head;
        while(T -> next != nullptr) {
            if (T -> data == data) return;
            T = T -> next;
        }
        
        if (T -> data == data) return;
        T -> next = temp;
    }
}

void removeValue(int val, NODE*& head){
    while(head -> data == val) {
        head = head -> next;
    }
    NODE* T = head;

    while (T -> next != nullptr) {
        if (T -> next -> data == val){
            T -> next = T -> next -> next;
        }
        else {
            T = T -> next;
        }
    }
}

void printList(NODE* head) {
    while(head -> next != nullptr) {
        cout << head -> data << " ";
        head = head -> next;
    }
}

int main(){   
    int n; cin >> n;
    NODE* head = nullptr;

    for(int i = 0; i < n; i++) {
        int val;cin >> val;
        pushBack(val, head);
    }

    pushBack(INT_MIN, head);

    printList(head);
}