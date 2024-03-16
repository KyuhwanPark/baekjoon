# import sys

# def min_comparisons(cards):
#     cards.sort()  # 입력된 카드 묶음을 오름차순으로 정렬

#     comparisons = 0

#     for i in range(len(cards) - 1):
#         current_card = cards[i]
#         next_card = cards[i + 1]

#         comparisons += current_card + next_card
#         cards[i + 1] = current_card + next_card

#         # 디버깅 출력
#         print(f"Current Card: {current_card}, Next Card: {next_card}, Updated Cards: {cards}, Comparisons: {comparisons}")

#     return comparisons

# # 카드 묶음의 개수를 입력 받음
# n = int(input("카드 묶음의 개수를 입력하세요: "))

# # 각 카드 묶음의 크기를 입력받음
# card_sizes = [int(sys.stdin.readline().strip()) for _ in range(n)]

# result = min_comparisons(card_sizes)
# print(result)
import sys
import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards,int(sys.stdin.readline()))

total_cost = 0
while len(cards)>1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum = a+b

    total_cost += sum
    heapq.heappush(cards,sum)

print(total_cost)