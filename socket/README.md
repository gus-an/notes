# 1. Tips

- There is one socket used for listening with `s.listen()`. And there is another socket when a connection is accepted with `s.accept()`. That can be saved into a variable `conn`

- `conn.recv()` receives whatever sent from client with `s.sendall()`

- At the end of `with` statement, `s.close()` is authomatically called, and returns an empty bytes object `b''`.

- Use `HOST = ''` instead of `HOST = '127.0.0.1'`, all available host interfaces that support the address family will be used to accept incoming connections. Client with `127.0.0.1` works!

# 3. Concepts

- `lo0` : loopback interface
- `eth0` : ethernet interface

# 2. Commands

- check the server running on localhost

```
netstat -an | grep 127.0.0.1
```

- list of open files with IPv[46] and no host names

```
lsof -i -n
```

### accept()
- blocks and waits for incoming connection

### send()
- Applications are responsible for checking that all data has been sent; if only some of the data was transmitted, the application needs to attempt delivery of the remaining data.

- `sendall()` continues to send until all data is sent.

### concurrency

1. Use Asynchronous I/O: `asyncio`: uses single-thread cooperative multitasking and a event loop to manage tasks.
2. Use threads
3. Use `select()`: more traditional than threads, allows you to check for I/O completion on more than one socket. Check which socket has I/O ready for read/write. This is not running concurrently. 

### sel.select(timeout=None)
- blocks until there are sockets ready for I/O.
- returns [(key, events) ...]
- `key.fileobj`: socket object
- mask: event mask of the operations that are ready
- if `key.data is None`: this event is from `listen`, we need to `accept`
- if `key.data is not None`: socket that is accepted, we need to service it.


