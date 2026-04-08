# 🐍 Python Date & Time Modules (Complete Guide)
This README covers all major Python date and time modules in one place, including:

* `datetime`
* `time`
* `calendar`
* `timedelta`

---

# 📌 1. datetime Module

The `datetime` module provides classes for working with date and time.

## 🔹 Import

```python
import datetime
```

## 🔹 Current Date & Time

```python
now = datetime.datetime.now()
print(now)
```

## 🔹 Current Date

```python
today = datetime.date.today()
print(today)
```

## 🔹 Current Time

```python
current_time = datetime.datetime.now().time()
print(current_time)
```

## 🔹 Custom Date & Time

```python
d = datetime.date(2026, 3, 30)
dt = datetime.datetime(2026, 3, 30, 10, 30, 0)
```

## 🔹 Formatting (`strftime`)

```python
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)
```

## 🔹 String to Date (`strptime`)

```python
date_str = "30-03-2026"
date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
```

---

# 📌 2. time Module

The `time` module is used for simple time-related operations.

## 🔹 Import

```python
import time
```

## 🔹 Timestamp

```python
print(time.time())
```

## 🔹 Delay Execution

```python
time.sleep(2)
```

## 🔹 Readable Time

```python
print(time.ctime())
```

## 🔹 Local Time

```python
print(time.localtime())
```

---

# 📌 3. calendar Module

Used to display and manage calendars.

## 🔹 Import

```python
import calendar
```

## 🔹 Display Month

```python
print(calendar.month(2026, 3))
```

## 🔹 Display Year

```python
print(calendar.calendar(2026))
```

## 🔹 Leap Year Check

```python
print(calendar.isleap(2024))
```

---

# 📌 4. timedelta (from datetime)

Used for date calculations.

## 🔹 Import

```python
from datetime import timedelta, date
```

## 🔹 Add Days

```python
today = date.today()
future = today + timedelta(days=5)
```

## 🔹 Date Difference

```python
d1 = date(2026, 3, 30)
d2 = date(2026, 4, 5)

print((d2 - d1).days)
```

# END FILE