from sys import stdin

"""
시작좌표 start, 끝 좌표 end

1. 만약에 꽉 찬 용기라면 고려하지 않아도 된다. (end--)
2. 두 용기를 합쳤을 때 양이 절반 이상이라면 하나가 완성된다. (start++, end--)
3. 만약 절반보다 적으면? 어떡하지
  3-1. 두 개를 합치면 무조건 절반 이상은 찬다. 절반은 서비스로 주니까
  3-2. 그니까 하나 더 합치면 무조건 1개가 된다.(또 절반은 서비스로 주니까)
  3-3. 그래서 먼저 2개를 합쳐서 1병을 만들 수 있는 경우를 모두 고르고
  3-4. 남은 애들은 3병씩 아무렇게나 묶어서 넘기면 된다.
  3-5. 3-4는 3으로 나눈 몫이라는 말이다.
"""

n, x = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

arr.sort()

start = 0
end = n - 1

ans = 0
remain = 0
while start <= end:
    # x인 애들은 온전한 1병이다.
    if arr[end] == x:
        ans += 1
        end -= 1
        continue

    if start == end:
        remain += 1
        break

    # 두 개를 합쳤을 때 절반 이상이라면
    if 2 * (arr[start] + arr[end]) >= x:
        ans += 1
        start += 1
        end -= 1
    else:  # 절반 이하라면 미뤄놓는다
        remain += 1
        start += 1

print(ans + remain // 3)  # 남은 애들은 3개당 하나씩 온전한 병을 만들 수 있다.
