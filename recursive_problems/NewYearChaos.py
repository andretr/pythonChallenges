#https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four&h_r=next-challenge&h_v=zen

def minimumBribes(q):
    # Write your code here
    bribes = 0
    for i in range(len(q)):
        if (q[i] > i + 3):
            print("Too chaotic")
            return;
        for j in range(max(0, q[i] - 2), i):
            if (q[i] < q[j]):
                bribes += 1
    print(bribes)


if __name__ == '__main__':
    ticket_list = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(ticket_list)
