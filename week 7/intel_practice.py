import time
import urllib.request from concurrent.futures import ThreadPoolExecutorurls = [
  'http://www.python.org',
  'https://docs.python.org/3/',
  'https://docs.python.org/3/whatsnew/3.7.html',
  'https://docs.python.org/3/tutorial/index.html',
  'https://docs.python.org/3/library/index.html',
  'https://docs.python.org/3/reference/index.html',
  'https://docs.python.org/3/using/index.html',
  'https://docs.python.org/3/howto/index.html',
  'https://docs.python.org/3/installing/index.html',
  'https://docs.python.org/3/distributing/index.html',
  'https://docs.python.org/3/extending/index.html',
  'https://docs.python.org/3/c-api/index.html',
  'https://docs.python.org/3/faq/index.html'  ]
results = []
for url in urls:
    with urllib.request.urlopen(url) as src:
        results.append(src)

print(time.time() - start)



def if_prime(x):
    if x <= 1:
        return 0    elif x <= 3:
        return x    elif x % 2 == 0 or x % 3 == 0:
        return 0    i = 5    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0        i += 6    return xanswer = 0for i in range(1000000):
    answer += if_prime(i)
