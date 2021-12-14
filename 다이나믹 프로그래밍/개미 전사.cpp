#include <bits/stdc++.h>

using namespace std;

// 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
int d[100];
int n;
vector<int> arr;

int main(void) {
    // 정수 N을 입력받기
    cin >> n;
    // 모든 식량 정보 입력받기
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        arr.push_back(x); //현재의 마지막 원소 뒤에 새로운 원소를 추가하며, 그 원소의 값은 x 의 복사본으로 초기화 된다. e.g. 1 3 1 5 이라면 1 -> 3 -> 1 -> 5 -> 가 입력되는 순서를 맞출 수 있다. 
    }

    // 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
    d[0] = arr[0];
    d[1] = max(arr[0], arr[1]);
    for (int i = 2; i < n; i++) {
        d[i] = max(d[i - 1], d[i - 2] + arr[i]);
    }

    // 계산된 결과 출력
    cout << d[n - 1] << '\n';
}