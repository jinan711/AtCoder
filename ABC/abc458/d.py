import heapq
X = int(input())
Q = int(input())
med = X
l = []
r = []
for _ in range(Q):
    A, B = map(int,input().split())
    if A == med:
        heapq.heappush(r,A)
        if B == med:
            heapq.heappush(r,B)
        elif A > med:
            heapq.heappush(r,B)
            heapq.heappush(l,med *(-1))
            med = heapq.heappop(r)
        else:
            heapq.heappush(l,B *(-1))
    elif A > med:
        heapq.heappush(r,A)
        if B == med:
            heapq.heappush(r,B)
            heapq.heappush(l,med *(-1))
            med = heapq.heappop(r)
        elif B > med:
            heapq.heappush(r,B)
            heapq.heappush(l,med *(-1))
            # print(l,r)
            med = heapq.heappop(r)
        else:
            heapq.heappush(l,B *(-1))
    else:
        heapq.heappush(l,A *(-1))
        if B == med:
            heapq.heappush(r,B)
        elif B > med:
            heapq.heappush(r,B)
        else:
            heapq.heappush(l,B *(-1))
            heapq.heappush(r,med)
            # print(l,r)
            med = heapq.heappop(l) *(-1)
    # print(l,r)
    print(med)