## A. Python
### 1. Beyond mutability, how do a list and a tuple differ? When would you choose each?

**Answer:** 
the list store data in order and use index to look up for data or loop in.
tuple use kay and vaule to store data, and it's faster than list if you want to look up for data

we choose list if order is matter 
and use tuple if we don't care about order but we care about faster look up.

---

### 2. What does this print, and why?
```
def add(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add(1))
print(add(2))
```
**Answer:** 

first print well return [1], and the second print well return [2]

since the add function is add item to the bucket list and then return this list.

---

### 3. Explain is vs ==. Give an example where they give different results.

**Answer:** 

all "is" and "==" return True or False 
but "==" is for equlity, for example: 
```
a = [5, 6]
if [5] == a:
  return "a = [5]"
return " a not equle to [5]"
```

"is" is to mmm i don't know how to explain but it's like yes or no, is this varible in this list? True if yes, False if no, for example:
```
a = [5,6]
is 5 in [5, 6]:
```

---

### 4. What is a generator? Write one that yields Fibonacci numbers forever.

**Answer:** 
i don't know

---

### 5. a = [[1, 2], [3, 4]], b = a.copy(), then b[0].append(99). What is a now? Why? How do you avoid it?

**Answer:** 
now a is the same [[1, 2], [3, 4]]

---

### 6. What is a decorator? Write one that prints how long a function took to run.

**Answer:** 
i don't know

---

### 7. What is the GIL? For CPU-heavy work, would you use threads or processes in Python, and why?

**Answer:** 
i don't know

---

### 8. How do *args and **kwargs work? Write a function signature that uses both.

**Answer:** 
i don't know

---

## B. Data structures & complexity

### 9. Define Big-O formally. Is 3n² + 100n in O(n²)? In O(n³)? In Θ(n³)? Justify.

**Answer:** 
i don't know

---

### 10. Give the time complexity (average and worst) of: list.append(x), list.insert(0, x), x in list, x in set, d[key].

**Answer:** 
i don't know

---

### 11. How does a hash table work internally? What is a collision? Name two ways to handle it.

**Answer:** 
i don't know

---

### 12. Array vs linked list: list three tradeoffs.

**Answer:** 
i don't know

---

### 13. Stack vs queue. How do you implement an efficient queue in Python, and why not just use a list?

**Answer:** 
i don't know

---

### 14. What is a binary search tree? Search complexity when balanced vs unbalanced?

**Answer:** 
i don't know

---

### 15. BFS vs DFS: how does each work, what data structure does each use, and when would you choose each?

**Answer:**
i don't know

---

### 16. What is a heap? What is it good for? Complexity of push and pop?

**Answer:** 
i don't know

---

### 17. What is dynamic programming? Name a problem it solves and explain the subproblem.

**Answer:** 
i don't know

---

## C. How computers work

### 18. Process vs thread.

**Answer:** 
i don't Know

---

### 19. Stack memory vs heap memory.

**Answer:** 
i don't know

---

### 20. What happens, step by step, when you type ./program in a shell and press Enter?

**Answer:**
i don't know 

---

### 21. What is a race condition? How do you prevent one?

**Answer:** 
i don't know

---

### 22. What is a deadlock? What conditions cause it?

**Answer:** 
i don't know

---

### 23. What is virtual memory, and why does it exist? 

**Answer:**
i don't know

---

### D. Networking & the web

1. What happens when you type `https://example.com` in a browser and press Enter? Go as deep as you can.

**Answer:**
i don't know

---

2. TCP vs UDP. Give a use case for each.

**Answer:**
i don't know

---

3. What does DNS do?

**Answer:**
i don't know

---

4. PUT vs PATCH. What does “idempotent” mean, and which HTTP methods are idempotent?

**Answer:**
i don't know

---

5. Explain: 401 vs 403, 400 vs 422, 500 vs 503.

**Answer:**
i don't know

---

6. What does HTTPS (TLS) add on top of HTTP?

**Answer:**
i don't know

---

7. Server-side sessions with cookies vs JWTs: tradeoffs.

**Answer:**
i don't know

---

### E. Databases

1. What is an index? How does it speed up reads, and what does it cost?

**Answer:**
i don't know

---

2. Explain each letter of ACID.

**Answer:**
i don't know

---

3. Tables: `users(id, name)` and `orders(id, user_id, amount, created_at)`. Write a query that returns every user’s name and total amount spent in 2026, including users with no orders (show 0), sorted from highest to lowest.

**Answer:**
i don't know

---

4. What is the N+1 query problem? How do you fix it?

**Answer:**
i don't know

---

5. What is normalization? When and why would you denormalize?

**Answer:**
i don't know

---

### F. Git & Linux

1. `git merge` vs `git rebase`.

**Answer:**
i don't know

---

2. You pushed a bad commit to a shared branch. How do you undo it safely?

**Answer:**
i don't know 

---

3. Write one shell command that counts all lines containing `ERROR` across every `.log` file in a directory and its subdirectories.

**Answer:**
i don't know 

---

4. What do the permissions `755` mean?

**Answer:**
i don't know
