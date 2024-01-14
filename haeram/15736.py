from sys import stdin
import math

'''
약수 개수가 홀수면 뒤집힘, 아니면 그대로
제곱 수는 약수 개수가 홀수, 아니면 짝수

즉 n까지 중 제곱 수가 몇 개인지 구하면 된다.
'''
n = int(stdin.readline())

print(math.floor(n**0.5))
