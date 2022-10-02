# Name
# Time: Minutes since last transaction
person = ''

transactions = {
    person: {}
}


def fraudulent_transaction(name: str, amount: float, time: int, location: str):

    person = name
    transactions[person] = {"amount": amount,
                            "time": time, "location": location}
    print(transactions[person])
    if time - transaction['time'] <= 60 and location != transaction['location']:
        return (name, amount, time, location)
    if amount > 1000:
        return (name, amount, time, location)
    transaction = transactions[person]


fraudulent_transaction("Isaac", 650.00, 200, 'Boston')
fraudulent_transaction("Alexis", 1200.00, 4, 'London')
fraudulent_transaction("Alexis", 3200.00, 4.30, 'Stockholm')
fraudulent_transaction("Isaac", 6500.00, 7, 'New York')
