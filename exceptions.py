class BaseException(Exception):
    '''
    this is the base class of all exceptions.

    members:
        - message:
            this is the message which will be printed.
    '''

    message = None

    def __str__(self):
        return self.__class__.__name__ + \
            ': ' + \
            self.message.format(
                **{key: value for key, value in self.__dict__.items() if not key == 'message'}
            )

class InvalidValueError(BaseException):
    file_name     = None
    arguments     = None
    line_number   = None
    verb          = None
    function_name = None

    message = '{arguments} {verb} invalid, please see the definition of the function <{function_name}> in the file {file_name}, line {line_number}'

    def __init__(self, invalid_argument_name_list, function):
        invalid_argument_list = ['<' + item + '>' for item in invalid_argument_name_list]
        if len(invalid_argument_name_list) == 1:
            self.verb = 'is'
            self.arguments = 'the value of ' + invalid_argument_name_list[0]
        else:
            self.verb = 'are'
            self.arguments = 'the value of ' + ', '.join(invalid_argument_name_list[:-1]) + ' and ' + invalid_argument_name_list[-1]
        self.file_name = function.__code__.co_filename
        self.line_number = function.__code__.co_firstlineno
        self.function_name = function.__name__

class InvalidCheckerError(BaseException):
    name          = None
    file_name     = None
    line_number   = None
    function_name = None

    message = 'che checker of <{name}> is invalid, plaease see the definition of the function <{function_name}> in the file, line number {line_number}'

    def __init__(self, name, function):
        self.name = name
        self.file_name = function.__code__.co_filename
        self.line_number = function.__code__.co_firstlineno
        self.function_name = function.__name__
