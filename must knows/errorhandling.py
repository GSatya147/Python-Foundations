# ERROR HANDLING
# always place generic exception names at bottom and specific ones at top

try:
    f = open('test.txt')
    # var = bad_var # undeclared bad_var

except FileNotFoundError as e: # specific exception at top
    print(e)

except Exception as e: # more generic exceotion at bottom
    print(e)

else: # runs only if try doesn't raise any excepitons
    print(f.read())
    f.close()

finally: # runs no matter what happens in try and except
    print("Executing finally")

# -----------------------------------------------------------------------------------
# instead of letting python catch default exceptions, we can raise custom exceptions

try:
    f = open('test.txt')
    if f.name == 'test.txt':
        raise Exception # raises custom exception

except FileNotFoundError as e: # specific exception at top
    print(e)

except Exception as e:
    print('Custom error!') # custom message

finally: # runs no matter what happens in try and except
    print("Executing finally")