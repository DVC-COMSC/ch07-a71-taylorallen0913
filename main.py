
numbers = list(map(int, input().split()))

avg = sum(numbers) / len(numbers)
for num in numbers:
    print (f'{abs(avg - num):.2f}', end=' ')

