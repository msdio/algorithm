#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <string>
#include <iomanip>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

int n;
int box[26][4];
int puzzle[6][6]; //각 배열에 들어있는 상자 번호
int rot[6][6]; //각 상자가 회전한 횟수
bool vis[26];
bool isSolved{ false };

void solve(int x, int y)
{
	if (x > n)
	{
		for (int i{ 1 }; i <= n; i++)
		{
			for (int j{ 1 }; j <= n; j++)
			{
				cout << puzzle[i][j] << " ";
			}
			cout << "\n";
		}
		for (int i{ 1 }; i <= n; i++)
		{
			for (int j{ 1 }; j <= n; j++)
			{
				cout << rot[i][j] << " ";
			}
			cout << "\n";
		}
		isSolved = true;
		return;
	}

	int match[4] = { -1, -1, -1, -1 }; //북, 동, 남, 서 방향으로 상자와 매칭되야 하는 수
	if (x == 1) match[0] = 0;
	else
	{
		if(2 - rot[x - 1][y] >= 0) match[0] = box[puzzle[x - 1][y]][2 - rot[x - 1][y]];
		else match[0] = box[puzzle[x - 1][y]][6 - rot[x - 1][y]];
	}
	if (y == 1) match[3] = 0;
	else
	{
		if (1 - rot[x][y - 1] >= 0) match[3] = box[puzzle[x][y - 1]][1 - rot[x][y - 1]];
		else match[3] = box[puzzle[x][y - 1]][5 - rot[x][y - 1]];
	}
	if (x == n) match[2] = 0;
	if (y == n) match[1] = 0;

	for (int idx{ 1 }; idx <= n * n; idx++) //상자 전부 조사
	{
		if (vis[idx]) continue;

		for (int r{ 0 }; r < 4; r++) //회전 수
		{
			bool isMatch{ true };
			for (int i{ 0 }; i < 4; i++)
			{
				if (match[i] == -1) continue;
				if (i >= r && match[i] == box[idx][i - r]) continue;
				if (i < r && match[i] == box[idx][4 + i - r]) continue;

				isMatch = false;
				break;
			}

			if (isMatch)
			{
				puzzle[x][y] = idx;
				rot[x][y] = r;
				vis[idx] = true;
				
				if (y == n) solve(x + 1, 1);
				else solve(x, y + 1);

				vis[idx] = false;

				if (isSolved) return;
			}
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	for (int i{ 1 }; i <= n * n; i++)
	{
		int u; cin >> u;
		cin >> box[u][0] >> box[u][1] 
			>> box[u][2] >> box[u][3];
	}

	solve(1, 1);
}