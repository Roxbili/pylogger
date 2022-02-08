# Logger template for python

Log the message to the file and terminal simultaneously.

## Usage
Init log_path the first time
```python
from logger import Logger
logger = Logger(__name__ ,'/path/to/log_file').get_logger()

logger.info('hello world')
```

Then you can save log message to the log file same as above
```python
from logger import Logger
logger = Logger(__name__).get_logger()

logger.info('hello world')
```

Or save log message to the new log file
```python
from logger import Logger
logger = Logger(__name__, '/new/path/to/new_log_file').get_logger()

logger.info('hello world')
```

More details about Logger can be found in the `Logger.__init__`.

## Example
Run the following command:
```bash
python test/a.py
```

You can see the following output in the test.log file and terminal:
> [INFO] [02/07 16:52:31] a.py:7 - this is a  
> [INFO] [02/07 16:52:31] a.py:8 - a hello  
> [INFO] [02/07 16:52:31] b.py:7 - this is b  
> [INFO] [02/07 16:52:31] b.py:8 - b hello  
> [INFO] [02/07 16:52:31] b.py:7 - this is b  
> [INFO] [02/07 16:52:31] b.py:8 - b hello  

(call b.msg() twice in a.py)