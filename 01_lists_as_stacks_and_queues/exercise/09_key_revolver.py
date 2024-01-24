from collections import deque

# Input collection
bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())

total_cost_of_bullets = 0
shots_fired = 0

# Main loop to process bullets and locks
while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    # Accounting for the bullet cost
    total_cost_of_bullets += bullet_price
    shots_fired += 1

    # Bullet and lock interaction
    if current_bullet <= current_lock:
        # The lock is destroyed
        print("Bang!")
    else:
        # The lock is not destroyed
        print("Ping!")
        locks.appendleft(current_lock)  # Lock remains if not destroyed

    # Reloading logic
    if shots_fired % gun_barrel_size == 0 and bullets:
        print("Reloading!")

# Outcome determination and printing
if locks:
    # Locks are not destroyed. Objective failed.
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    # Locks are destroyed. Mission succeeded.
    money_earned = intelligence_value - total_cost_of_bullets
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
