data = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

sorted_data = sorted(data, key=lambda x: (x['First Name'], x['Last Name']))

for item in sorted_data:
    print(item)

import time
import random

def sorting_algorithm(data):
    # الگوریتم مرتب‌سازی
    return sorted(data, key=lambda x: (x['First Name'], x['Last Name']))

# ساخت داده‌های تصادفی با اندازه‌های مختلف
data_sizes = list(range(10, 1001, 10))
execution_times = []

for size in data_sizes:
    # ساخت داده تصادفی
    random_data = [
        {'First Name': f'First_{random.randint(1, 100)}', 'Last Name': f'Last_{random.randint(1, 100)}'}
        for _ in range(size)
    ]

    # زمان شروع اجرا
    start_time = time.time()

    # اجرای الگوریتم مرتب‌سازی
    sorting_algorithm(random_data)

    # زمان پایان اجرا
    end_time = time.time()

    # محاسبه زمان اجرا
    execution_time = end_time - start_time
    execution_times.append(execution_time)

# چاپ زمان‌های اجرا
for size, time_taken in zip(data_sizes, execution_times):
    print(f"Data Size: {size}, Execution Time: {time_taken} seconds")

