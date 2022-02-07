# Logger template for python

Log the message to the file and terminal simultaneously.

## Usage
```python
from logger import Logger

logger = Logger('/path/to/log_file', __name__).get_logger()
logger.info('hello world')
```

More details about Logger can be found in the `Logger.__init__`.

## Example
Run the following command:
```bash
python test/a.py
```

You can see the following output in the test.log file and terminal:
> [INFO] [02/07 15:25:12] b.py:6 - this is b  
> [INFO] [02/07 15:25:12] b.py:7 - b hello  
> [INFO] [02/07 15:25:12] a.py:7 - this is a  
> [INFO] [02/07 15:25:12] a.py:8 - a hello  