
```python
    print(f'employee id: {info[modify_num]['id']}, name: {info[modify_num]['name']}, tel: {info[modify_num]['tel']}')
            
    # Unterminated expression in f-string; missing close brace
```

solution:

```python
    print(f'employee id: {info[modify_num]["id"]}, name: {info[modify_num]["name"]}, tel: {info[modify_num]["tel"]}')
```