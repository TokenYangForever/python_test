import time
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('invoke')
def now():
	print(time.ctime(time.time()))
if __name__ == '__main__':
	now()