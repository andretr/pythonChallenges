# https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

def superDigit(n, k):
    # Write your code here
    result = super_digit(sumDigits(int(n)) * k)
    print(result)
    return result

def super_digit(no):
    if no < 10:
        return no
    else:
        sum_digits = sumDigits(no)
        return super_digit(sum_digits)

def sumDigits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s




if __name__ == '__main__':
    superDigit(148, 3)