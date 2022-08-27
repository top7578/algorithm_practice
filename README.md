# itertools
> from itertools

## 중복조합
combinations_with_replacement(iter, r) : A~E 5명의 후보가 있다. 중복을 허용해 2명의 대표를 뽑는 방법
```python
from itertools import combinations_with_replacement

list(combinations_with_replacement('ABC', 2)) #결과 : 'AA' 'AB' 'AC' 'BB' 'BC' 'CC' 
```

## 중복순열
product(iter, r) : 1~5 숫자카드가 있다. 중복을 허용해 2자리수를 만드는 방법.
```python
from itertools import product

list(product('ABC', repeat=2)) #결과 : 'AA' 'AB' 'AC' 'BA' 'BB' 'BC' 'CA' 'CB' 'CC'
```


# heap
> import heapq

## 기존 리스트를 힙으로 변환
heapq.heapify( 리스트 )

```python
a = [4,1,3,10]
heapq.heapify(a)  //결과: a는 [1, 4, 3, 10]
```
-> 힙에서 인덱스 0이 최솟값이라고 해서, 인덱스 1에 두 번째, 인덱스 2에 세 번째로 작은 원소가 있는 것이 아니다.
두 번째로 작은 원소를 얻으려면 heappop()을 통해 최솟값을 삭제한 후 heap[0]로 접근하는 방법을 사용하거나, 인덱스 1을 인덱스 2와 비교하는 방법을 사용해야 한다. (최소값만 보장)


# hash
> from collections import defaultdict </br>
 ```python
defaultdict(int)
defaultdict(list)
```
딕셔너리에 items() 메서드를 사용해주면 {"key" : value}의 형태를 [(key, value)]의 형태로 만들어 준다.
## key를 기준으로 딕셔너리 정렬
```python
sorted(d)
```

## value를 기준으로 딕셔너리 정렬
```python
sorted(d.items(), key=lambda x : x[1])
```
### value가 list인 경우
```python
for key in d:
    d[key].sort()
```

# Math
> import math

## 최대공약수
math.gcd( 숫자들 )

```python
math.gcd(12,8)  //결과: 4
```

# Counter
요소가 딕셔너리 키로 저장되고 개수가 딕셔너리 값으로 저장되는 컬렉션
> from collections import Counter

## 데이터 개수가 많은 순으로 정렬된 배열을 리턴
Counter( [리스트] or [문자열] ).most_common( 출력갯수 )

# 문자열
## 문자열 정렬
문자열을 정렬하고 싶을 땐 sort한 다음에 join으로 묶어줘야 한다. (sort하면 리스트를 반환한다)
```python
orders[i] = "".join(sorted(orders[i]))
```

## 문자열 수정
문자열 값을 변경하고 싶을땐 list로 변환 후 idx에 해당하는 값을 수정하고 join으로 묶어준다.

## 찾기
find() 함수는 왼쪽부터 찾고, rfind() 함수는 오른쪽부터 찾는다.
```python
"별똥별".find("별") #결과: 0
"별똥별".rfind("별") #결과: 2
```

# 진수 변환
## 10진수 -> n진수
```python
#1. bin(x)[2:]): 내장함수 bin 사용
#2. 
def change_10to2(n):
    tmp = []
    while n > 0:
        tmp.append(str(n%2))
        n //= 2
    tmp = tmp[::-1]
    return tmp
```

## n진수 -> 10진수
```python
int(문자열 값, n)
```

# zip 함수
각 iterables 의 요소들을 모으는 이터레이터를 만듭니다.
튜플의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.
## 사용 예 #1 - 여러 개의 Iterable 동시에 순회할 때 사용
```python
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for number1, number2, number3 in zip(list1, list2, list3):
   print(number1 + number2 + number3)
```
## 사용 예 #2 - Key 리스트와 Value 리스트로 딕셔너리 생성하기
```python
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```
