# itertools
> from itertools

## 중복조합
combinations_with_replacement(iter, r) : A~E 5명의 후보가 있다. 중복을 허용해 2명의 대표를 뽑는 방법
```python
from itertools import combinations_with_replacement

list(itertools.combinations_with_replacement('ABC', 2)) #결과 : 'AA' 'AB' 'AC' 'BB' 'BC' 'CC' 
```

## 중복순열
product(iter, r) : 1~5 숫자카드가 있다. 중복을 허용해 2자리수를 만드는 방법.
```python
from itertools import product

list(itertools.product('ABC', 2)) #결과 : 'AA' 'AB' 'AC' 'BA' 'BB' 'BC' 'CA' 'CB' 'CC'
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
