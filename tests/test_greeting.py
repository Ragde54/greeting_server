from greeting_mcp.tools.greeting import say_hello

def test_say_hello_with_name():
    assert say_hello("John") == "Hello, John!"

def test_say_hello_without_name():
    assert say_hello("") == "Hello, !"