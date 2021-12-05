// ���� ���̺귯���� �׻� �־��� ��쿡�� �ð� ���⵵ O(NlogN)�� �����Ѵ�.
#include <bits/stdc++.h>

using namespace std;

class Fruit {
public:
    string name;
    int score;
    Fruit(string name, int score) {
        this->name = name;
        this->score = score;
    }
    // ���� ������ '������ ���� ����'
    bool operator <(Fruit& other) {
        return this->score < other.score;
    }
};

int n = 10;
int arr[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

int main(void) {

    // ���� ���̺귯���� ����Ͽ���
    sort(arr, arr + n);
    for (int i = 0; i < n; i++) {
        cout << arr[i] << ' ';
    }

    // ���� ���̺귯������ ��ųʸ� key�� ����� �ڵ�
    int n = 3;
    Fruit fruits[] = {
        Fruit("�ٳ���", 2),
        Fruit("���", 5),
        Fruit("���", 3)
    };
    sort(fruits, fruits + n);
    for (int i = 0; i < n; i++) {
        cout << '(' << fruits[i].name << ',' << fruits[i].score << ')' << ' ';
    }

}