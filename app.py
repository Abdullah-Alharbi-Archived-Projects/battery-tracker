from functions import start


print('Started battery tracker.')
print('note: each hour you will recieve toast notification or')
print('if the battery is less than or equal to 15% also if battery is greater than 90%.')

SECS = 60 * 60  # 1 hour

start(SECS)
