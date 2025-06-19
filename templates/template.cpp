#include <bits/stdc++.h>
using namespace std;

// 👇 필요한 경우 typedef나 매크로 사용
typedef long long ll;
typedef pair<int, int> pii;
#define all(v) v.begin(), v.end()

// 👇 입출력 최적화
void fast_io() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

// 👇 테스트 케이스마다 실행될 함수
void solve() {
    // 예시 입력
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int &x : arr) cin >> x;

    sort(all(arr));

    for (int x : arr) cout << x << " ";
    cout << '\n';
}

int main() {
    fast_io();

    int T = 1;
    // cin >> T; // 테스트 케이스 여러 개인 경우 사용

    while (T--) {
        solve();
    }

    return 0;
}
