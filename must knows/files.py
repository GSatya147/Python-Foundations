# FILES

# r - read, w - write, a - append, r+ - read and write
f = open('test.txt', 'r')

print(f.name) # file name
print(f.mode) # file mode
print(f.closed) # boolean returns False

f.close() # always close 

# Context keyword 'with' - no need to close explicitly
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# READ MODE
with open('test.txt', 'r') as f:
    """
    1. f.readlines() - returns a list of all lines with newline char
    2. f.readline() - reads one line at a time (can use loops to iterate over lines)
    3. f.read() - by default reads all the contents as it is
    4. f.read(chunk_size) - reads till chunk size is reached and can use another time to continue from left off
    """
    f_contents = f.read() # loads exact file contents

    # Use Cases:
    # 1: Iterating each line for safe memory
    for line in f:
        print(line, end = '') # end here avoids auto new line by print st
    
    # 2: Iterating through readline()
    for line in f:
        pass

    # 3: Hard coded chunking
    f_contents = f.read(100) # reads till 100 chars
    f_contents1 = f.read(100) # continues to read another 100 chars from previous left off
    
    # 4: Chunking intuition
    size_to_read = 10
    
    f_contents = f.read(size_to_read) # reads first 10 chars
    f.tell() # returns our present position i.e. 10

    while len(f_contents) > 0: # loop to print all file contents
        print(f_contents, end = '*') # prints first 10 chars i.e 1 to 10 which were read outside loop.

        # To end the infinite loop, consider updating f_contents, and it's size
        f_contents = f.read(size_to_read) # Here f_contents gets updated from 1 to 10, 11 to 20, 21 to 30, till the f_contents gets en empty string

    # 5: To set position, use f.seek(position)
    f_contents = f.read(10) # reads first 10 chars
    wanna_read_again = True

    if wanna_read_again:
        f.seek(0) # sets pointer to 0th pos
        f_contents = f.read(10) # reads first 10 chars again
    else:
        f.contents = f.read(10) # reads next 10, i.e. 11 to 20

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# WRITE MODE - creates if not present
with open('test.txt', 'w') as wf:
    wf.write('hello')
    wf.write(', world!') # file will have hello, world!

    # Seek playing
    wf.write('Test')
    wf.seek(0)
    wf.write('R') # file will have Rest, haha

    # Use cases:
    # 1: Copying test.txt to test2.txt
    with open('test.txt', 'r') as rf:
        with open('test2.txt', 'w') as wf:
            for line in rf:
                wf.write(line)

    # 2: Copying picture files needs file pointer to be open in binary mode, i.e we will need to work with bytes of file instead of characters, with 'rb', 'wb'
    with open('test.jpg', 'rb') as rf:
        with open('test2.jpg', 'wb') as wf:
            for line in rf:
                wf.write(line)

    #3: Since some files can be large when opened in binary modes - use safe file copying with actual chunk sizes instead of chars, bytes
    with open('test.jpg', 'rb') as rf:
        with open('test2.jpg', 'wb') as wf:

            chunk_size = 4096 # 4KBs
            rf_chunk = rf.read(chunk_size) # reads 4KBs of test.jpg

            while len(rf.chunk) > 0:
                wf.write(rf) # writes 4KBs to test2.jpg
                rf_chunk = rf.read(chunk_size) # to read next chunk, else while is gonna be an infinite loop checking same size 