class LoggableList(Loggable, list):
    def append(self, obj):
        super(LoggableList, self).append(obj)
        super(LoggableList, self).log(obj)
       