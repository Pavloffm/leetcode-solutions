    return pd.merge(person, address, on='personId', how='left')[['firstName', 'lastName', 'city', 'state']]
