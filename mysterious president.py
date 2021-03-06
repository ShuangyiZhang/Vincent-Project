import sys

INF = 1000000


def build(p, a, dp):
    if (dp[p] == 1):
        return [p]
    i = p - 1
    while not (a[i] < a[p] and dp[i] + 1 == dp[p]):
        i = i - 1
    r = build(i, a, dp)
    r.append(p)
    return r


def lis(a):
    n = len(a)
    if n == 0:
        return []
    b = [INF] * (n + 1)
    b[0] = -INF
    dp = [0] * n
    ix, maxLo = -1, -1
    for i in range(0, n):
        lo, hi = 0, n + 1
        while lo < hi:
            mid = (lo + hi) / 2
            if b[mid] >= a[i]:
                hi = mid
            else:
                lo = mid + 1
        b[lo] = a[i]
        if lo > maxLo:
            maxLo = lo
            ix = i
        dp[i] = lo
    r = build(ix, a, dp)
    return r


def main():
    sys.setrecursionlimit(10000)
    # print lis(range(1, 1000))
    # return
    (n, w, h) = sys.stdin.readline().split(" ")
    (n, w, h) = (int(n), int(w), int(h))
    l = []
    for i in range(n):
        (x, y) = sys.stdin.readline().split(" ")
        (x, y) = (int(x), int(y))
        if x > w and y > h:
            l.append((x, -y, i + 1))
    l.sort()
    nl = len(l)
    a = [0] * nl
    for i in range(0, nl):
        a[i] = -l[i][1]
    # l[i] = (l[i][0], -l[i][1], l[i][2])

    positions = lis(a)
    print len(positions)
    for p in positions:
        print l[p][2],

    return
    # dp = [1] * nl
    # prev = [-1] * nl
    # ix = -1
    # for i in range(0, nl):
    #	jx = -1
    #	for j in range(0, i):
    #		if l[j][1] < l[i][1] and (jx == -1 or dp[j] > dp[jx]):
    #			jx = j
    #	if jx != -1:
    #		dp[i] = dp[jx] + 1
    #		prev[i] = jx
    #	if ix == -1 or dp[ix] < dp[i]:
    #		ix = i

    if ix == -1:
        print "0"
        return

    print dp[ix]
    ans = []
    while ix != -1:
        ans.append(l[ix][2] + 1)
        ix = prev[ix]
    ans.reverse()
    for x in ans:
        print x,


main()
