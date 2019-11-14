import asyncio

groups_dict = {}


def join(group_name, writer):
    if groups_dict.get(group_name) is None:
        groups_dict[group_name] = [writer]
    else:
        groups_dict[group_name].append(writer)


def send(group_name, message):
    for wr in groups_dict[group_name]:
        wr.write(message.encode())


def leave(group_name, writer):
    groups_dict[group_name].remove(writer)


async def handle_echo(reader, writer):
    # Read up to n bytes. If n is not provided, or set to -1, read until EOF and return all read bytes.
    data = await reader.read(1024)
    message = data.decode()  # Return a string decoded from the given bytes.
    # socket:
    # 'peername': the remote address to which the socket is connected,
    # result of socket.socket.getpeername() (None on error)
    addr = writer.get_extra_info('peername')

    # {..!r} Calls repr() on the argument first
    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    command = message.split()[0]
    gp_name = message.split()[1]
    if command == "join":
        join(group_name=gp_name, writer=writer)
    elif command == "send":
        input_message = message.split()[2]
        send(group_name=gp_name, message=input_message)
    elif command == "leave":
        leave(group_name=gp_name, writer=writer)
    else:
        writer.write("Boro gom shooo!".encode())
    # writer.write(data)
    await writer.drain()

    print("Close the connection")
    # writer.close()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print('Bye Bye')
        loop.close()
