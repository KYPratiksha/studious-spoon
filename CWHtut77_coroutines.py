def searcher():
    import time
    time.sleep(4)
    book = "this is a book which contains huge data"
    while True:
        text = yield
        if text in book:
            print("text is in book")
        else:
            print("text is not in the book")

coroutine = searcher()
next(coroutine)
coroutine.send("book")
coroutine.send("hello")
coroutine.close()