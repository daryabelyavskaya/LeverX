from concurrent.futures.thread import ThreadPoolExecutor


def function(args):
    a = 0
    for _ in range(args):
        a += 1
    return a


def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        var = executor.map(function, [1000000] * 5)
        print("----------------------", sum(var))


main()
