#https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four
def gridChallenge(grid):
    # Write your code here
    result = "YES"
    new_grid = []
    for i in grid:
        new_grid.append(sorted(i))
    for i, item in enumerate(new_grid):
        if i > 0:
            word = new_grid[i]
            previous_word= new_grid[i-1]
            if (not check_columns(word, previous_word)):
                result = "NO"
                break;
    return result

def check_columns(word, previous_word):
    for j, letter in enumerate(word):
        if word[j] < previous_word[j]:
            return False
    return True

if __name__ == '__main__':
    grid = ["mpxz", "abcd", "wlmf"]
    print(gridChallenge(grid))
    grid = ["abc", "lmp", "qrt"]
    print(gridChallenge(grid))
    grid = ["abc", "hjk", "mpq", "rtv"]
    print(gridChallenge(grid))





