class AppConfig:
    def __init__(self):
        self._settings = {}

    def __getitem__(self, key):
        if key in self._settings:
            return self._settings[key]
        raise KeyError(f'{key} is missing')

    def __setitem__(self, key, value):
        if isinstance(key, str):
            self._settings[key] = value
        else:
            raise TypeError('Invalid Key. it must be a string')

    def __delitem__(self, key):
        if key not in self._settings:
            raise KeyError(f'Invalid key. {key} is missing')
        del self._settings[key]


config = AppConfig()

# 1. success writing and reading
config['host'] = '127.0.0.1'
config['port'] = 8080
print(f"Host: {config['host']}")
print(f"Port: {config['port']}")

# 2. successfully deleting
del config['port']

# 3. test validate
try:
    config[123] = "database_password"
except TypeError as e:
    print(f"TypeError: {e}")

# 4. inevitable access to key
try:
    print(config['port'])
except KeyError as e:
    print(f"Key access error: {e}")

# 5. test deleting invalid key
try:
    del config['api_key']
except KeyError as e:
    print(f"Error of deleting: {e}")
\