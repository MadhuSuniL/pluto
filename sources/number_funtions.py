from num2words import num2words
from .name_patterns import number_patterns
import random

def digits(num):
    return len(str(num))

def reverse(num):
    return str(num)[::-1]

def even(num):
    return 'Yes' if num % 2 == 0 else 'No'

def odd(num):
    return 'Yes' if num % 2 != 0 else 'No'

def prime(num):
    c = 0
    for i in range(1,num+1):
        if num % i == 0:
            c+=1
    return 'Yes' if c == 2 else 'No'

def armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return 'Yes' if num == sum_of_powers else 'No' 

# print(armstrong(100))

def magic(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in num_str)
    
    # Check if the digit sum is equal to the product of digits
    return 'Yes' if digit_sum * digit_sum == num else 'No'


def perfect(num):
    if num <= 0:
        return False
    divisors = [divisor for divisor in range(1, num) if num % divisor == 0]
    divisors_sum = sum(divisors)
    return 'Yes' if num == divisors_sum else 'No'

# def sum(num):
#     return sum(divisor for divisor in range(1, num) if num % divisor == 0)

def collatz(num):
    sequence = [num]
    while num != 1:
        if num % 2 == 0:
            num = numr // 2
        else:
            num = num * 3 + 1
        sequence.append(num)
    return sequence

def binary(num):
    return bin(num)[2:]

def octal(num):
    return oct(num)[2:]

def hexadecimal(num):
    return hex(numr)[2:]

def word(num):
    word = num2words(num)
    return word.replace('-',' ').title()

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def palindrome(num):
    return 'Yes' if str(num) == str(num)[::-1] else 'No'

def fibonacci(num):
    if num < 0:
        return False

    a, b = 0, 1
    while b < num:
        a, b = b, a + b

    return 'Yes' if b == num else 'No'



def prime_factorization(num):
    factors = []
    for i in range(2,num+1):
        if num % i == 0:
            factors.append(i)
    factors.remove(num)
    return factors

def table(num):
    table_string = ''
    table_patterns = (
    f"Here is the <b>{num}</b>th math table:",
    f"I have the <b>{num}</b>th math table for you:",
    f"Let's look at the <b>{num}</b>th math table:",
    f"The <b>{num}</b>th math table is as follows:",
    f"Here's the table for <b>{num}</b>:",
    f"Behold the <b>{num}</b>th math table:",
    f"Prepare to witness the <b>{num}</b>th math table:",
    f"Unlocking the secrets of the <b>{num}</b>th math table:",
    f"The <b>{num}</b>th math table holds valuable information:",
    f"Exploring the depths of the <b>{num}</b>th math table:",
    f"Unveiling the mysteries of the <b>{num}</b>th math table:",
    f"Discovering the patterns in the <b>{num}</b>th math table:",
    f"Behold, the majestic <b>{num}</b>th math table:",
    f"Embark on a journey through the <b>{num}</b>th math table:",
    f"Prepare to be amazed by the <b>{num}</b>th math table:",
    f"Let's delve into the <b>{num}</b>th math table:",
    f"The <b>{num}</b>th math table awaits your attention:",
    f"Unlocking the power of the <b>{num}</b>th math table:",
    f"Behold the beauty of the <b>{num}</b>th math table:",
    f"Delving into the wonders of the <b>{num}</b>th math table:"    )

    for i in range(1,11):
        table_string+= f"<h1 class='text-center text-xl'>{num} X {i} = {num*i}</h1><br>"
    return random.choice(table_patterns)+'<br><br>'+table_string 

def even_numbers(from_,to_):
    even_numbers_list = []
    for i in range(from_,to_+1):
        if i % 2 == 0:
            even_numbers_list.append(str(i))
    return random.choice(number_patterns).replace('{number_category}', '<b>Even</b>').replace('{start}', str(from_)).replace('{end}', str(to_)) +'<br><b class="text-xl">&nbsp;&nbsp;&nbsp;&nbsp;'+', '.join(even_numbers_list)+'</b>'
            
def odd_numbers(from_,to_):
    even_numbers_list = []
    for i in range(from_,to_+1):
        if i % 2 != 0:
            even_numbers_list.append(str(i))
    return random.choice(number_patterns).replace('{number_category}', '<b>Odd</b>').replace('{start}', str(from_)).replace('{end}', str(to_)) +'<br><b class="text-xl">&nbsp;&nbsp;&nbsp;&nbsp;'+', '.join(even_numbers_list)+'</b>'
            
def prime_numbers(from_,to_):
    prime_numbers_list = []
    for num in range(from_,to_+1):
        c = 0
        for i in range(1,num+1):
            if num % i == 0 :
                c += 1
        prime_numbers_list.append(str(num)) if c == 2 else 0
    return random.choice(number_patterns).replace('{number_category}', '<b>Prime</b>').replace('{start}', str(from_)).replace('{end}', str(to_)) +'<br><b class="text-xl">&nbsp;&nbsp;&nbsp;&nbsp;'+', '.join(prime_numbers_list)+'</b>'

def fibonacci_numbers(from_,to_):
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] < to_:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    fibonacci_numbers = [str(num) for num in fibonacci_numbers if from_ <= num <= to_]
    return random.choice(number_patterns).replace('{number_category}', '<b>Fibonacci</b>').replace('{start}', str(from_)).replace('{end}', str(to_)) +'<br><b class="text-xl">&nbsp;&nbsp;&nbsp;&nbsp;'+', '.join(fibonacci_numbers)+'</b>'



def explain_number(num):
    num = int(num)
    value = f"""
        <h1 class='text-3xl m-4 text-center text-cyan-400'>{num}</h1>
        
        <p class='p-2'>
        {'&nbsp;'*4}The given number is <b>{num}({word(num)})</b>. It is {'<b>an Even</b>' if even(num) == 'Yes' else '<b>not an Even</b>'} number. It is {'<b>an Odd</b>' if odd(num) == 'Yes' else '<b>not an Odd</b>'} number. It is {'<b>a Prime</b>' if prime(num) == 'Yes' else '<b>not a Prime</b>'} number. It is {'<b>a Perfect</b>' if perfect(num) == 'Yes' else '<b>not a Perfect</b>'} number. It is {'<b>Armstrong</b>' if armstrong(num) == 'Yes' else '<b>not an Armstrong</b>'} number. It is {'<b>a Magic</b>' if magic(num) == 'Yes' else '<b>not a Magic</b>'} number. It is {'<b>a Fibonacci</b>' if fibonacci(num) == 'Yes' else '<b>not a</b>'} Fibonacci number.
        </p>
        <p class='text-center'>
        No of digits : <b class='text-xl'>{digits(num)}</b><br>
        Even Number : <b class='text-xl'>{even(int(num))}</b><br>
        Odd Number : <b class='text-xl'>{odd(int(num))}</b><br>
        Prime Number : <b class='text-xl'>{prime(int(num))}</b><br>
        Perfect Number : <b class='text-xl'>{perfect(int(num))}</b><br>
        Armstrong Number : <b class='text-xl'>{armstrong(int(num))}</b><br>
        Magic Number : <b class='text-xl'>{magic(int(num))}</b><br>
        Fibonacci Number : <b class='text-xl'>{fibonacci(int(num))}</b><br>
    </p>"""
    return value

